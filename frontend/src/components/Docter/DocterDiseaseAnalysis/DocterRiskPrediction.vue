<template>
    <el-container>
      <el-header class="header" style="background: #00ffff">
          <div class="heading_left">
            <i class="el-icon-s-platform">精神疾病诊断平台</i>
          </div>
          <div class="heading_right">
            <div class="change-icon" style="font-size:30px;">
            <i class="el-icon-user-solid"></i>
            </div>
            <el-dropdown @command="handleCommand"><span class="el-dropdown-link">{{ nickName }}<i
              class="el-icon-arrow-down el-icon--right"></i></span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="goToHelloWorld">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </el-header>

      <el-container class="background">
      <el-aside width="250px">
        <DocterMenu></DocterMenu>
      </el-aside>
        <el-main style="padding-left: 5%; padding-right: 10%" class="main">
          <el-row>
            <el-col :span="24">
              <el-row>
                <el-col :span="16">
                  <el-input
                    placeholder="任务名称"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span="8">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: left; margin-right: 10px;margin-left: 20px"
                    @click="searchDiscuss(inputSearch)"
                    circle>
                  </el-button>
                  <el-button
                    type="primary"
                    icon="el-icon-plus"
                    @click="buildThemeVisible = true">创建风险预测任务</el-button>

                  <el-dialog title="新建风险预测任务" :visible.sync = "buildThemeVisible" >
                    <el-form ref="form" :model="form" label-width="120px">
                      <el-form-item label="任务名称">
                        <el-input placeholder="根据疾病场景、数据集、模型自动生成名称" v-model="form.name" :disabled="true"></el-input>
                      </el-form-item>
                      <el-form-item label="任务简介">
                        <el-input placeholder="请输入" v-model="form.introduction"></el-input>
                      </el-form-item>
<!--                      <el-form-item label="疾病场景">-->
<!--                        <el-select v-model="form.scenes" placeholder="请选择诊断疾病">-->
<!--                          <el-option key="AD" label="AD" value="AD">-->
<!--                          </el-option>-->
<!--                          <el-option key="抑郁症" label="抑郁症" value="抑郁症">-->
<!--                          </el-option>-->
<!--                        </el-select>-->
<!--                      </el-form-item>-->
                      <el-form-item label="数据集">
                        <el-select v-model="form.data" placeholder="选择数据集">
                          <el-option label="默认数据集" value="默认数据集"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="诊断病人">
                        <el-select v-model="form.patient" placeholder="选择患者"  :style="{ width: '60%' }">
                          <el-option
                            v-for="item in patients"
                            :key="item.id"
                            :label="item.name"
                            :value="item.id">
                          </el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="模型">
                        <el-select v-model="form.model" placeholder="选择风险预测模型">
                          <el-option label="默认模型辅助诊断模型" value="默认模型"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="TaskSubmit">立即创建</el-button>
                        <el-button @click="buildThemeVisible=false">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog id = 'aa' title="查看结果" :visible.sync = "showDataContent" >
                  </el-dialog>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
          <el-divider></el-divider>
          <el-table
            :data="tasks"
            :header-cell-style="{'text-align':'center'}"
            :cell-style="{'text-align':'center'}"
            style="width: 100%">
            <el-table-column
              label="任务名称"
              prop="name"
              width="180">
            </el-table-column>
            <el-table-column
              label="患者"
              prop="patientName"
              width="180">
            </el-table-column>
            <el-table-column
              label="状态"
              width="180">
              <template slot-scope="scope">
                  <div slot="reference" class="name-wrapper">
                    <el-tag size="medium">{{ scope.row.finishState }}</el-tag>
                  </div>
              </template>
            </el-table-column>
             <el-table-column label="完成时间">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span >{{ scope.row.time }}</span>
              </template>
            </el-table-column>
            <el-table-column label="是否通知患者">
              <template slot-scope="scope">
                <el-switch v-model="scope.row.notifyPredictState" active-color="#13ce66" inactive-color="#ff4949" @change="updatePredictState(scope.row)">
                </el-switch>
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template v-slot="scope">
              <el-dropdown size="mini" split-button @command="handleCommand2">
                <span class="el-dropdown-link">
                  详情
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item :command="beforeHandleCommand(scope.$index,'a')">查看结果</el-dropdown-item>
                  <el-dropdown-item :command="beforeHandleCommand(scope.$index,'b')" divided>删除</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
                </template>
            </el-table-column>
          </el-table>
          <el-dialog
            :visible.sync="deleteDialogVisible"
            title="确认删除"
            width="30%">
            <span>您确定要删除吗？</span>
            <span slot="footer" class="dialog-footer">
              <el-button type="primary" @click="confirmDelete">确认</el-button>
              <el-button @click="deleteDialogVisible=false">取消</el-button>
            </span>
          </el-dialog>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import DocterMenu from '../DocterMenu'
export default {
  name: 'DocterRiskPrediction',
  components: {DocterMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      nickName: '',
      inputSearch: '',
      input: {
        title: '',
        content: ''
      },
      patients: [
        {id: 1, name: '王二'}, {id: 2, name: '张三'}
      ],
      diagnosises: [{id: 1, name: '抑郁症-默认数据集-默认辅助诊断模型'}, {id: 2, name: '阿尔兹海默症-默认数据集-默认辅助诊断模型'}],
      tasks: [{
        id: '1',
        name: '抑郁症-默认数据集-默认辅助诊断模型',
        finishState: '未完成',
        patientID: 1,
        patientName: '张三',
        notifyResultState: true,
        notifyPredictState: false,
        time: '2001-2-26 01:01:01',
        introduction: '为患者进行抑郁症辅助诊断',
        scene: '抑郁症',
        data: '默认数据集',
        model: '默认模型',
        risk: '又进入阿尔兹海默症中期的风险'
      }, {
        id: '2',
        name: '阿尔兹海默症-默认数据集-默认辅助诊断模型',
        finishState: '已完成',
        patientID: 2,
        patientName: '李四',
        notifyResultState: false,
        notifyPredictState: false,
        time: '2001-2-26 01:01:01',
        introduction: '为患者进行阿尔兹海默症辅助诊断',
        scene: '阿尔兹海默症',
        data: '默认数据集',
        model: '默认模型',
        risk: '又进入阿尔兹海默症中期的风险'
      }],
      form: {
        name: '',
        introduction: '',
        scenes: '',
        data: '',
        diagnosis: 1,
        patient: '',
        model: ''
      },
      detail: {
        id: '2',
        name: 'AD Diagnasdosis',
        finishState: '未完成',
        notifyResultState: false,
        notifyPredictState: false,
        time: '2001-2-26 01:01:01',
        introduction: 'asdwa',
        scene: 'AD',
        data: 'asd',
        model: 'VGG16',
        risk: ''
      },
      buildThemeVisible: false,
      showDataContent: false,
      deleteDialogVisible: false,
      curIndex: 0
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getDoctorPredictTaskList()
    this.getPatients()
  },
  methods: {
    getPatients: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getPatientList/',
        method: 'get'
      }).then(function (response) {
        that.patients = response.data
      })
    },
    getDoctorPredictTaskList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getDoctorPredictTaskList/',
        method: 'get'
      }).then(function (response) {
        that.tasks = response.data
      })
    },
    TaskSubmit () {
      this.buildThemeVisible = false
      let that = this
      this.$http.request({
        url: that.$url + 'DocterEstablishPredictTask/',
        method: 'get',
        params: {
          taskName: '风险预测-' + that.form.patient + '-' + that.form.model,
          taskIntroduction: that.form.introduction,
          taskScene: '阿尔兹海默症',
          taskDataset: that.form.data,
          taskModel: that.form.model,
          patientID: that.form.patient
        }
      }).then(function (response) {
        console.log(response.data)
        that.getDoctorPredictTaskList()
      })
    },
    onSubmit () {
      this.showDataContent = false
    },
    beforeHandleCommand (rowIndex, ope) {
      return {
        row: rowIndex,
        ope: ope
      }
    },
    handleCommand2: function (command) {
      if (command.ope === 'a') {
        this.showDetail(command.row)
      } else {
        this.curIndex = command.row
        this.deleteDialogVisible = true
        console.log(this.curIndex)
      }
    },
    confirmDelete () {
      this.deleteDialogVisible = false
      let that = this
      console.log(that.curIndex)
      that.$http.request({
        url: that.$url + 'DeletePredictTask/',
        method: 'get',
        params: {
          taskID: that.tasks[that.curIndex].id
        }
      }).then(function (response) {
        that.getDoctorPredictTaskList()
      })
    },
    showDetail: function (row) {
    // 将当前行的内容传递给修改的数据对象
      let that = this
      console.log(that.tasks[row])
      this.$router.push({
        name: 'DocterRiskPredictionGraph',
        query: {
          detail: that.tasks[row]
        }
      })
      console.log(this.$route.query.detail)
    },
    updatePredictState (task) {
      let that = this
      const index = that.tasks.indexOf(task)
      console.log(index)
      that.tasks[index].notifyPredictState = !task.notifyPredictState
      task.notifyPredictState = !task.notifyPredictState
      console.log(task.notifyPredictState)
      this.$http.request({
        url: that.$url + 'updatePredictState/',
        method: 'get',
        params: {
          taskID: task.id,
          notifyPredictState: task.notifyPredictState ? '是' : '否'
        }
      }).then(function (response) {
        console.log(response.data)
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('nickName')
      this.$router.replace('/')
    },
    handleCommand: function (command) {
      this.goToHelloWorld()
    }
  }
}
</script>

<style scoped>
@import "../../../assets/css/back.css";
</style>
<style scoped>
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
</style>
<style scoped>

.todo-app {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.todo-input {
  width: 200px;
  margin-bottom: 10px;
}

.todo-select {
  width: 200px;
  margin-bottom: 10px;
}

/* 调整日期选择器样式 */
.todo-datepicker {
  width: 200px;
  margin-bottom: 10px;
}
.todo-button {
  margin-bottom: 10px;
}
.todo-table {
  margin-top: 10px;
  width: 400px;
}
.todo-table th {
  background-color: #f5f7fa;
  color: #909399;
  font-weight: bold;
  text-align: left;
}
.todo-table tr:nth-child(odd) {
  background-color: #f9fafc;
}
.custom-table {
  /* 添加自定义样式 */
}

.custom-table::before {
  content: "";
}
</style>
<style scoped>
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }
</style>

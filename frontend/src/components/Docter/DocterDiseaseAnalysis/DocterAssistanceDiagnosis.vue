<template>
    <el-container>
      <el-header class="header" style="background: #00ffff">
          <div class="heading_left" style="font-family: fontFestival;">
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
                    @click="buildTaskVisible = true">创建辅助诊断任务</el-button>

                  <el-dialog title="新建辅助诊断任务" :visible.sync = "buildTaskVisible" >
                    <el-form ref="form" :model="establishDiagnosisForm" label-width="120px">
                      <el-form-item label="任务名称">
                        <el-input placeholder="根据疾病场景、数据集、模型自动生成名称" v-model="establishDiagnosisForm.name" :disabled="true"></el-input>
                      </el-form-item>
                      <el-form-item label="任务简介">
                        <el-input placeholder="请输入" v-model="establishDiagnosisForm.introduction"></el-input>
                      </el-form-item>
                      <el-form-item label="疾病场景">
                        <el-select v-model="establishDiagnosisForm.scenes" placeholder="请选择诊断疾病">
                          <el-option key="阿尔兹海默症" label="阿尔兹海默症" value="阿尔兹海默症">
                          </el-option>
                          <el-option key="抑郁症" label="抑郁症" value="抑郁症">
                          </el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="数据集">
                        <el-select v-model="establishDiagnosisForm.data" placeholder="请选择数据集">
                          <el-option label="默认数据集" value="默认数据集"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="模型">
                        <el-select v-model="establishDiagnosisForm.model" placeholder="请选择模型">
                          <el-option label="默认模型" value="默认模型"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="患者">
                        <el-select v-model="establishDiagnosisForm.patient" filterable placeholder="请选择诊断患者">
                          <el-option
                            v-for="item in patients"
                            :key="item.id"
                            :label="item.name"
                            :value="item.id">
                          </el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="TaskSubmit">立即创建</el-button>
                        <el-button @click="buildTaskVisible=false">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog title="查看结果" :visible.sync = "showTaskDetail" >
                    <el-form ref="form" :model="taskDetail" label-width="120px">
                      <el-form-item label="任务名称:">
                        {{ taskDetail.name }}
                      </el-form-item>
                      <el-form-item label="任务简介:">
                        {{ taskDetail.introduction }}
                      </el-form-item>
                      <el-form-item label="疾病场景:">
                        {{ taskDetail.scene }}
                      </el-form-item>
                      <el-form-item label="数据集:">
                        {{ taskDetail.data }}
                      </el-form-item>
                      <el-form-item label="辅助诊断模型:">
                        {{ taskDetail.model }}
                      </el-form-item>
                      <el-form-item label="诊断结果:">
                        <el-card class="box-card">
                          <el-form>
                            <el-form-item label="患病种类：">
<!--                              {{ taskDetail.resultDisease }}-->
                              <el-input @input="startSave"  v-model="taskDetail.resultDisease" placeholder="请输入内容"></el-input>
                            </el-form-item>
                            <el-form-item label="疾病阶段：">
<!--                              {{ taskDetail.resultStage }}-->
                               <el-input @input="startSave"  v-model="taskDetail.resultStage" placeholder="请输入内容"></el-input>
                            </el-form-item>
                          </el-form>
                        </el-card>
                      </el-form-item>
                      <el-form-item>
                        <el-button v-if="showSave" type="success" @click="saveEditAssistanceResult">保存</el-button>
                        <el-button type="primary" @click="onSubmit">返回</el-button>
                      </el-form-item>
                    </el-form>
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
                <el-switch v-model="scope.row.notifyResultState" active-color="#13ce66" inactive-color="#ff4949" @change="updateNotifyState(scope.row)">
                </el-switch>
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template v-slot="scope">
                <el-dropdown size="mini" split-button @command="handleDropdownCommand">
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
            <span>确定要删除吗？</span>
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
import '../../../assets/font/fontFestival.css'
export default {
  name: 'DocterAssistanceDiagnosis',
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
      tasks: [{
        id: '1',
        name: '抑郁症-默认数据集-默认辅助诊断模型',
        patientID: 1,
        patientName: '张三',
        finishState: '未完成',
        notifyResultState: true,
        time: '2020-1-26 01:01:01',
        introduction: '为患者进行抑郁症辅助诊断',
        scene: '抑郁症',
        data: '默认数据集',
        model: '默认模型',
        resultDisease: '阿尔兹海默症',
        resultStage: '中期'
      }, {
        id: '2',
        name: '阿尔兹海默症-默认数据集-默认辅助诊断模型',
        patientID: 2,
        patientName: '李四',
        finishState: '未完成',
        notifyResultState: false,
        time: '2021-2-26 01:01:01',
        introduction: '为患者进行阿尔兹海默症辅助诊断',
        scene: '阿尔兹海默症',
        data: '默认数据集',
        model: '默认模型',
        resultDisease: '阿尔兹海默症',
        resultStage: '中期'
      }],
      establishDiagnosisForm: {
        name: '',
        introduction: '',
        scenes: '',
        data: '',
        patient: '',
        model: ''
      },
      taskDetail: {
        id: '2',
        name: 'AD Diagnasdosis',
        state: '未完成',
        time: '2001-2-26 01:01:01',
        introduction: 'asdwa',
        scene: 'AD',
        data: 'asd',
        model: 'VGG16',
        resultDisease: '阿尔兹海默症',
        resultStage: '中期'
      },
      buildTaskVisible: false,
      showTaskDetail: false,
      deleteDialogVisible: false,
      showSave: false,
      curIndex: 0
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getDiagnosisTaskList()
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
    getDiagnosisTaskList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getDoctorDiagnosisTaskList/',
        method: 'get'
      }).then(function (response) {
        that.tasks = response.data
      })
    },
    TaskSubmit () {
      this.buildTaskVisible = false
      let that = this
      this.$http.request({
        url: that.$url + 'DocterEstablishDiagnosisTask/',
        method: 'get',
        params: {
          taskName: '辅助诊断-' + that.establishDiagnosisForm.patient + '-' + that.establishDiagnosisForm.scenes,
          taskIntroduction: that.establishDiagnosisForm.introduction,
          taskScene: that.establishDiagnosisForm.scenes,
          taskDataset: that.establishDiagnosisForm.data,
          taskModel: that.establishDiagnosisForm.model,
          patientID: that.establishDiagnosisForm.patient
        }
      }).then(function (response) {
        console.log(response.data)
        that.getDiagnosisTaskList()
      })
    },
    onSubmit () {
      this.showTaskDetail = false
    },
    startSave () {
      this.showSave = true
    },
    saveEditAssistanceResult () {
      this.showSave = false
      this.showTaskDetail = false
      let that = this
      this.tasks[this.curIndex].resultDisease = this.taskDetail.resultDisease
      this.tasks[this.curIndex].resultStage = this.taskDetail.resultStage
      this.$http.request({
        url: that.$url + 'saveEditAssistanceResult/',
        method: 'get',
        params: {
          taskID: that.tasks[that.curIndex].id,
          resultDisease: that.taskDetail.resultDisease,
          resultStage: that.taskDetail.resultStage
        }
      }).then(function (response) {
        console.log(response.data)
      })
    },
    beforeHandleCommand (rowIndex, ope) {
      return {
        row: rowIndex,
        ope: ope
      }
    },
    handleDropdownCommand: function (command) {
      if (command.ope === 'a') {
        this.showDetail(command.row)
      } else if (command.ope === 'b') {
        this.curIndex = command.row
        this.deleteDialogVisible = true
        console.log(this.curIndex)
      }
    },
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.taskDetail = this.tasks[row]
      this.curIndex = row
      this.showTaskDetail = true
    },
    showAddHomeworkDialog () {
      this.addHomeworkDialogVisible = true
    },
    confirmDelete () {
      this.deleteDialogVisible = false
      let that = this
      console.log(that.curIndex)
      that.$http.request({
        url: that.$url + 'DeleteDiagnosisTask/',
        method: 'get',
        params: {
          taskID: that.tasks[that.curIndex].id
        }
      }).then(function (response) {
        that.getDiagnosisTaskList()
      })
    },
    updateNotifyState (task) {
      let that = this
      const index = that.tasks.indexOf(task)
      console.log(index)
      that.tasks[index].notifyResultState = !task.notifyResultState
      task.notifyResultState = !task.notifyResultState
      console.log(task.notifyResultState)
      this.$http.request({
        url: that.$url + 'updateAssistantNotifyState/',
        method: 'get',
        params: {
          taskID: task.id,
          notifyResultState: task.notifyResultState ? '是' : '否'
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

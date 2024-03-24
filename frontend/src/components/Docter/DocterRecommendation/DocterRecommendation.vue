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
                    @click="buildThemeVisible = true">创建方案推荐任务</el-button>
                  <el-dialog title="新建方案推荐任务" :visible.sync = "buildThemeVisible" >
                    <el-form ref="form" :model="form" label-width="120px">
                      <el-form-item label="任务名称">
                        <el-input placeholder="根据疾病场景、数据集、模型自动生成名称" v-model="form.name" :disabled="true"></el-input>
                      </el-form-item>
                      <el-form-item label="任务简介">
                        <el-input placeholder="请输入" v-model="form.introduction"></el-input>
                      </el-form-item>
                      <el-form-item label="患者">
                        <el-select v-model="form.patient" filterable placeholder="请选择诊断患者">
                          <el-option
                            v-for="item in patients"
                            :key="item.id"
                            :label="item.name"
                            :value="item.id">
                          </el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="数据集">
                        <el-select v-model="form.data" placeholder="请选择数据集">
                          <el-option label="默认数据集" value="默认数据集"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="辅助诊断结果">
                        <el-input disabled placeholder="结果已与患者绑定"></el-input>
                      </el-form-item>
                      <el-form-item label="风险预测结果">
                        <el-input disabled placeholder="结果已与患者绑定"></el-input>
                      </el-form-item>
                      <el-form-item label="模型">
                        <el-select v-model="form.model" placeholder="请选择方案模型">
                          <el-option label="默认模型" value="默认模型"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="医生建议">
                        <el-input placeholder="在此输入您的建议" v-model="form.recommendation"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="TaskSubmit">立即创建</el-button>
                        <el-button @click="buildThemeVisible=false">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
<!--                  <el-dialog title="查看结果" :visible.sync = "showDataContent" >-->
<!--                    <el-form ref="form" :model="detail" label-width="150px" >-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="任务名称:" >-->
<!--                        {{detail.name}}-->
<!--                      </el-form-item>-->
<!--                        </el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="任务简介:">-->
<!--                        {{detail.introduction}}-->
<!--                      </el-form-item>-->
<!--                      </el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="患者基础信息:">-->
<!--                        {{detail.patientName}}-->
<!--                      </el-form-item>-->
<!--                        </el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="数据集:">-->
<!--                        {{detail.data}}-->
<!--                      </el-form-item>-->
<!--                        </el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="辅助诊断模型:">-->
<!--                        默认辅助诊断模型-->
<!--                      </el-form-item>-->
<!--                        </el-col>-->
<!--&lt;!&ndash;                        <el-col span=12>&ndash;&gt;-->
<!--&lt;!&ndash;                      <el-form-item label="辅助诊断结果:">&ndash;&gt;-->
<!--&lt;!&ndash;                        {{detail.diagnosisResult}}&ndash;&gt;-->
<!--&lt;!&ndash;                      </el-form-item>&ndash;&gt;-->
<!--&lt;!&ndash;                          </el-col>&ndash;&gt;-->
<!--&lt;!&ndash;                      <el-col span=12>&ndash;&gt;-->
<!--&lt;!&ndash;                      <el-form-item label="风险诊断结果:">&ndash;&gt;-->
<!--&lt;!&ndash;                        {{detail.predictResult}}&ndash;&gt;-->
<!--&lt;!&ndash;                      </el-form-item>&ndash;&gt;-->
<!--&lt;!&ndash;                        </el-col>&ndash;&gt;-->
<!--&lt;!&ndash;                      <el-col span=12>&ndash;&gt;-->
<!--&lt;!&ndash;                      <el-form-item label="模型:">&ndash;&gt;-->
<!--&lt;!&ndash;                        {{detail.model}}&ndash;&gt;-->
<!--&lt;!&ndash;                      </el-form-item>&ndash;&gt;-->
<!--&lt;!&ndash;                        </el-col>&ndash;&gt;-->
<!--                      <el-form-item label="方案:">-->
<!--                        {{detail.recommendation}}-->
<!--                      </el-form-item>-->
<!--                      <el-form-item>-->
<!--                        <el-button type="primary" @click="onSubmit">返回</el-button>-->
<!--                      </el-form-item>-->
<!--                    </el-form>-->
<!--                  </el-dialog>-->
                  <el-dialog title="修改方案" :visible.sync = "modifySchemeDialog" >
                    <el-form ref="form" :model="detail" label-width="150px" >
<!--                      <el-col span=12>-->
                      <el-form-item label="任务名称:" >
                        {{detail.name}}
                      </el-form-item>
<!--                        </el-col>-->
<!--                      <el-col span=12>-->
                      <el-form-item label="任务简介:">
                        {{detail.introduction}}
                      </el-form-item>
<!--                      </el-col>-->
<!--                      <el-col span=12>-->
                      <el-form-item label="患者基础信息:">
                        {{detail.patientName}}
                      </el-form-item>
<!--                        </el-col>-->
                      <el-col span=12>
                      <el-form-item label="数据集:">
                        默认数据集
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="辅助诊断模型:">
                        默认辅助诊断模型
                      </el-form-item>
                        </el-col>
<!--                        <el-col span=12>-->
<!--                      <el-form-item label="辅助诊断结果:">-->
<!--                        {{detail.diagnosisResult}}-->
<!--                      </el-form-item>-->
<!--                          </el-col>-->
<!--                      <el-col span=24>-->
<!--                      <el-form-item label="风险诊断结果:">-->
<!--                        {{detail.predictResult}}-->
<!--                      </el-form-item>-->
<!--                        </el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="模型:">-->
<!--                        {{detail.model}}-->
<!--                      </el-form-item>-->
<!--                        </el-col>-->
                      <el-form-item label="方案:">
<!--                        {{detail.recommendation}}-->
                        <el-input
                          type="textarea"
                          autosize
                          placeholder="请输入您的方案"
                          v-model="detail.recommendation">
                        </el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="success" @click="saveModifyScheme">保存修改</el-button>
                        <el-button type="warning" @click="modifySchemeDialog=false">取消修改</el-button>
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
                <el-switch v-model="scope.row.notifySchemeState" active-color="#13ce66" inactive-color="#ff4949" @change="updateSchemeState(scope.row)">
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
                  <el-dropdown-item :command="beforeHandleCommand(scope.$index,'b')" divided>修改方案</el-dropdown-item>
                  <el-dropdown-item :command="beforeHandleCommand(scope.$index,'a')">删除</el-dropdown-item>
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
export default {
  name: 'DocterRecommendation',
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
        name: '张三-默认方案推荐模型-1',
        finishState: '未完成',
        notifySchemeState: false,
        time: '2021-2-16 01:01:01',
        introduction: '为张三推荐治疗方案',
        scene: '抑郁症',
        data: '默认数据集',
        model: '默认模型',
        patientName: '张三',
        patientID: 1,
        patientResume: '28、男、无病史',
        diagnosisResult: '抑郁症-初期',
        predictResult: '未来可能进入抑郁者中期',
        recommendation: '加强锻炼，保持充足的睡眠，减少熬夜，规律饮食'
      }, {
        id: '2',
        name: '李四-默认方案推荐模型-1',
        finishState: '完成',
        notifySchemeState: false,
        time: '2022-5-11 12:01:01',
        introduction: '为李四推荐治疗方案',
        scene: '阿尔兹海默症',
        patientResume: '68、女、无病史',
        data: '默认数据集',
        model: '默认模型',
        patientName: '李四',
        patientID: 2,
        diagnosisResult: '阿尔兹海默症-初期',
        predictResult: '未来可能会仍保持初期水准',
        recommendation: '加强锻炼，保持充足的睡眠，减少熬夜，规律饮食'
      }],
      form: {
        name: '',
        introduction: '',
        patient: '',
        data: '',
        assistance: '',
        prediction: '',
        model: '',
        recommendation: ''
      },
      detail: {
        id: '2',
        name: '李四-默认方案推荐模型-1',
        finishState: '完成',
        notifySchemeState: false,
        time: '2022-5-11 12:01:01',
        introduction: '为李四推荐治疗方案',
        scene: '阿尔兹海默症',
        patientResume: '68、女、无病史',
        data: '默认数据集',
        model: '默认模型',
        patientName: '李四',
        patientID: 2,
        diagnosisResult: '阿尔兹海默症-初期',
        predictResult: '未来可能会仍保持初期水准',
        recommendation: '加强锻炼，保持充足的睡眠，减少熬夜，规律饮食'
      },
      buildThemeVisible: false,
      showDataContent: false,
      modifySchemeDialog: false,
      deleteDialogVisible: false,
      curIndex: 0
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getRecommendationTaskList()
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
    getRecommendationTaskList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getRecommendationTaskList/',
        method: 'get'
      }).then(function (response) {
        that.tasks = response.data
      })
    },
    saveModifyScheme: function () {
      this.modifySchemeDialog = false
      let that = this
      this.tasks[this.curIndex].recommendation = this.detail.recommendation
      this.$http.request({
        url: that.$url + 'updateScheme/',
        method: 'get',
        params: {
          taskID: that.tasks[that.curIndex].id,
          scheme: that.detail.recommendation
        }
      }).then(function (response) {
        console.log(response.data)
      })
    },
    updateSchemeState (task) {
      let that = this
      const index = that.tasks.indexOf(task)
      console.log(index)
      that.tasks[index].notifySchemeState = !task.notifySchemeState
      task.notifySchemeState = !task.notifySchemeState
      console.log(task.notifySchemeState)
      this.$http.request({
        url: that.$url + 'updateSchemeState/',
        method: 'get',
        params: {
          taskID: task.id,
          notifySchemeState: task.notifySchemeState ? '是' : '否'
        }
      }).then(function (response) {
        console.log(response.data)
      })
    },
    TaskSubmit () {
      this.buildThemeVisible = false
      let that = this
      this.$http.request({
        url: that.$url + 'DoctorEstablishSchemeTask/',
        method: 'get',
        params: {
          taskName: '方案推荐-' + that.form.patient + '-阿尔兹海默症',
          taskIntroduction: that.form.introduction,
          taskScene: '阿尔兹海默症',
          taskDataset: that.form.data,
          taskModel: that.form.model,
          taskPlan: that.form.recommendation,
          patientID: that.form.patient
        }
      }).then(function (response) {
        console.log(response.data)
        that.getRecommendationTaskList()
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
        this.curIndex = command.row
        this.deleteDialogVisible = true
      } else {
        this.modifyScheme(command.row)
      }
    },
    confirmDelete () {
      this.deleteDialogVisible = false
      let that = this
      console.log(that.curIndex)
      that.$http.request({
        url: that.$url + 'DeleteRecommendationTask/',
        method: 'get',
        params: {
          taskID: that.tasks[that.curIndex].id
        }
      }).then(function (response) {
        that.getRecommendationTaskList()
      })
    },
    // showDetail (row) {
    // // 将当前行的内容传递给修改的数据对象
    //   console.log(row)
    //   this.detail = this.tasks[row]
    //   this.showDataContent = true
    // },
    modifyScheme (row) {
      this.curIndex = row
      this.modifySchemeDialog = true
      this.detail = this.tasks[this.curIndex]
    },
    showAddHomeworkDialog () {
      this.addHomeworkDialogVisible = true
    },
    clearAddHomeworkForm () {
      this.$refs.addHomeworkForm.resetFields()
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

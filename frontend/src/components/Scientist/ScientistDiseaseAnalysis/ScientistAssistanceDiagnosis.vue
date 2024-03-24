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
        <ScientistMenu></ScientistMenu>
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
                          <el-option key="AD" label="阿尔兹海默症" value="AD">
                          </el-option>
                          <el-option key="抑郁症" label="抑郁症" value="抑郁症">
                          </el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="数据集">
                        <el-select v-model="establishDiagnosisForm.data" placeholder="请选择数据集">
                          <el-option label="ADNI dataset" value="ADNI dataset"></el-option>
                          <el-option label="FFAIR dataset" value="FFAIR dataset"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="模型">
                        <el-select v-model="establishDiagnosisForm.model" placeholder="请选择模型" :style="{ width: '50%' }">
                          <el-option label="Multi-modality Fusion Model" value="MMFM"></el-option>
                          <el-option label="LSTM" value="LSTM"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="TaskSubmit">立即创建</el-button>
                        <el-button @click="buildTaskVisible=false">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog title="模型性能" :visible.sync = "showTaskDetail">
                    <el-form ref="form" :model="taskDetail" label-width="120px">
<!--                      <el-form-item label="任务名称:">-->
<!--                        {{ taskDetail.name }}-->
<!--                      </el-form-item>-->
<!--                      <el-form-item label="任务简介:">-->
<!--                        {{ taskDetail.introduction }}-->
<!--                      </el-form-item>-->
                      <el-col span="12">
                      <el-form-item label="疾病场景:">
                        {{ taskDetail.scene }}
                      </el-form-item>
                        </el-col>
                      <el-col span="12">
                      <el-form-item label="数据集:">
                        {{ taskDetail.data }}
                      </el-form-item>
                      </el-col>
                      <el-form-item label="辅助诊断模型:">
                        {{ taskDetail.model }}
                      </el-form-item>
                      <el-form-item label="模型效率:">MAE:smaller=better wR:larger=better</el-form-item>
                      <el-card class="box-card" :style="{ width: '600px'}" style="margin-left: 40px">
                          <el-col span="12">
                          <div style="font-weight: bold; font-size: 17px; margin-bottom: 20px">MAE (平均绝对误差)</div>
                          <el-form>
                            <el-form-item label="MMSE：">
                              {{ taskDetail.MAE_MMSE }}
                            </el-form-item>
                            <el-form-item label="CDR-Global：">
                              {{ taskDetail.MAE_CDRG }}
                            </el-form-item>
                            <el-form-item label="CDR-SOB：">
                              {{ taskDetail.MAE_CDRS }}
                            </el-form-item>
                            <el-form-item label="ADAS-Cog：">
                              {{ taskDetail.MAE_ADAS }}
                            </el-form-item>
                          </el-form>
                            </el-col>
                          <el-col span="12">
                          <div style="font-weight: bold; font-size: 17px; margin-bottom: 20px">wR (加权相关系数)</div>
                          <el-form>
                            <el-form-item label="MMSE：">
                              {{ taskDetail.wR_MMSE }}
                            </el-form-item>
                            <el-form-item label="CDR-Global：">
                              {{ taskDetail.wR_CDRG }}
                            </el-form-item>
                            <el-form-item label="CDR-SOB：">
                              {{ taskDetail.wR_CDRS }}
                            </el-form-item>
                            <el-form-item label="ADAS-Cog：">
                              {{ taskDetail.wR_ADAS }}
                            </el-form-item>
                          </el-form>
                            </el-col>
                        </el-card>
                      <el-form-item style="text-align: right; margin-bottom: -8px; margin-top: 10px">
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
import ScientistMenu from '../ScientistMenu'
import '../../../assets/font/fontFestival.css'
export default {
  name: 'ScientistAssistanceDiagnosis',
  components: {ScientistMenu},
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
        data: 'ANDI dataset',
        model: 'Multi-modality Fusion Model',
        MAE_MMSE: '2.1373 ± 0.0442',
        MAE_CDRG: '0.2753 ± 0.0029',
        MAE_CDRS: '1.3560 ± 0.0190',
        MAE_ADAS: '5.8689 ± 0.0623',
        wR_MMSE: '0.7620 ± 0.0132',
        wR_CDRG: '0.7415 ± 0.0050',
        wR_CDRS: '0.7979 ± 0.0083',
        wR_ADAS: '0.7249 ± 0.0165'
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
        MAE_MMSE: '2.1373 ± 0.0442',
        MAE_CDRG: '0.2753 ± 0.0029',
        MAE_CDRS: '1.3560 ± 0.0190',
        MAE_ADAS: '5.8689 ± 0.0623',
        wR_MMSE: '0.7620 ± 0.0132',
        wR_CDRG: '0.7415 ± 0.0050',
        wR_CDRS: '0.7979 ± 0.0083',
        wR_ADAS: '0.7249 ± 0.0165'
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
        MAE_MMSE: '2.1373 ± 0.0442',
        MAE_CDRG: '0.2753 ± 0.0029',
        MAE_CDRS: '1.3560 ± 0.0190',
        MAE_ADAS: '5.8689 ± 0.0623',
        wR_MMSE: '0.7620 ± 0.0132',
        wR_CDRG: '0.7415 ± 0.0050',
        wR_CDRS: '0.7979 ± 0.0083',
        wR_ADAS: '0.7249 ± 0.0165'
      },
      buildTaskVisible: false,
      showTaskDetail: false,
      deleteDialogVisible: false,
      curIndex: 0
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getScientistDiagnosisTaskList()
  },
  methods: {
    getScientistDiagnosisTaskList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getScientistDiagnosisTaskList/',
        method: 'get'
      }).then(function (response) {
        that.tasks = response.data
      })
    },
    TaskSubmit () {
      this.buildTaskVisible = false
      let that = this
      this.$http.request({
        url: that.$url + 'establishScientistDiagnosisTask/',
        method: 'get',
        params: {
          patientID: 1,
          taskName: '辅助诊断性能评估-' + that.establishDiagnosisForm.model + '-' + that.establishDiagnosisForm.data,
          taskIntroduction: that.establishDiagnosisForm.introduction,
          taskScene: that.establishDiagnosisForm.scenes,
          taskDataset: that.establishDiagnosisForm.data,
          taskModel: that.establishDiagnosisForm.model
        }
      }).then(function (response) {
        console.log(response.data)
        that.getScientistDiagnosisTaskList()
      })
    },
    onSubmit () {
      this.showTaskDetail = false
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
      // this.showTaskDetail = true
      let that = this
      console.log(that.tasks[row])
      this.$router.push({
        name: 'ScientistAssistanceDiagnosisGraph',
        query: {
          detail: that.tasks[row]
        }
      })
    },
    showAddHomeworkDialog () {
      this.addHomeworkDialogVisible = true
    },
    confirmDelete () {
      this.deleteDialogVisible = false
      let that = this
      console.log(that.curIndex)
      that.$http.request({
        url: that.$url + 'DeleteScientistDiagnosisTask/',
        method: 'get',
        params: {
          taskID: that.tasks[that.curIndex].id
        }
      }).then(function (response) {
        that.getScientistDiagnosisTaskList()
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

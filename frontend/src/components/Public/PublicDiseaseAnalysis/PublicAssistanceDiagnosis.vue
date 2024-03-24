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
        <PublicMenu></PublicMenu>
      </el-aside>
        <el-main style="padding-left: 5%; padding-right: 10%" class="main">
          <div class="todo-app">
            <el-table :border="true" class="custom-table" :row-class-name="tableRowClassName" :data="diagnoses" style="width: 100%;margin-bottom: 20px;" :header-row-class-name="headerRowClassName" :header-cell-style="{
            background:'#f0f9eb'}">
              <el-table-column :align="'center'" label="诊断ID" prop="id"></el-table-column>
              <el-table-column :align="'center'" label="诊断任务" prop="name"></el-table-column>
              <el-table-column :align="'center'" label="诊断时间" prop="startTime"></el-table-column>
              <el-table-column :align="'center'" label="结束时间" prop="endTime"></el-table-column>
              <el-table-column :align="'center'" label="诊断结果">
              <template slot-scope="scope">
                    {{ scope.row.notifyState === '是' ? scope.row.content : '经医生审查后方可查看' }}
                </template>
            </el-table-column>
            </el-table>
            <el-button round type="success" style="box-shadow: 0 12px 16px rgba(0, 0, 0, 0.1);font-size: 16px"  @click="showAddHomeworkDialog">发起诊断</el-button>
            <el-dialog
              title="发起诊断"
              :visible.sync="establishDiagnosis"
              width="30%"
              @close="clearAddHomeworkForm">
              <el-form :model="addDiagnosisForm" ref="addHomeworkForm" :rules="addDiagnosisRules">
                <el-form-item label="任务名称" prop="course">
                  <el-input v-model="addDiagnosisForm.taskName" placeholder="根据疾病场景、数据集、模型自动生成" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="任务简介" prop="course">
                  <el-input v-model="addDiagnosisForm.describe" type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入任务描述" ></el-input>
                </el-form-item>
                <el-form-item label="疾病场景" prop="course">
                  <el-select v-model="addDiagnosisForm.disorder" placeholder="请选择疾病场景">
                    <el-option v-for="disorder in disorders" :key="disorder.id" :label="disorder.name" :value="disorder.id" />
                  </el-select>
                </el-form-item>
        <!--        <el-form-item label="数据集" prop="course">-->
        <!--          <el-select v-model="addTaskForm.data" placeholder="请选择数据集">-->
        <!--            <el-option v-for="course in datas" :key="course.id" :label="course.name" :value="course.id" />-->
        <!--          </el-select>-->
        <!--        </el-form-item>-->
                <el-form-item label="模型" prop="course">
                  <el-select v-model="addDiagnosisForm.model" placeholder="请选择模型">
                    <el-option v-for="course in models" :key="course.id" :label="course.name" :value="course.id" />
                  </el-select>
                </el-form-item>
              </el-form>

              <div slot="footer" class="dialog-footer">
                <el-button @click="establishOk" type="primary">发起诊断</el-button>
                <el-button @click="establishDiagnosis = false">取消</el-button>
              </div>
            </el-dialog>
          </div>
        </el-main>
      </el-container>
    </el-container>
</template>

<script>
import PublicMenu from '../PublicMenu'
export default {
  name: 'PublicAssistanceDiagnosis',
  components: {PublicMenu},
  data: function () {
    return {
      circleUrl: '',
      userName: '',
      nickName: '',
      show: false,
      diagnoses: [
        {id: 1, name: '抑郁症-默认数据集-默认辅助诊断模型', startTime: '2023-12-31', endTime: '2023-12-31', content: '玉玉症二期', finishState: false, notifyState: false},
        {id: 2, name: '阿尔兹海默症-默认数据集-默认辅助诊断模型', startTime: '2023-12-31', endTime: '2023-12-31', content: '恢复健康', finishState: true, notifyState: false}
      ],
      disorders: [{id: 1, name: '阿尔兹海默症'}],
      datas: [{id: 1, name: '数据集1'}, {id: 2, name: '数据集2'}],
      models: [{id: 1, name: '默认辅助诊断模型'}],
      addDiagnosisForm: {
        model: '',
        data: null,
        describe: '',
        disorder: null,
        taskName: ''
      },
      establishDiagnosis: false,
      addDiagnosisRules: {
        model: [{ required: true, message: '请选择模型', trigger: 'change' }],
        // data: [{ required: true, message: '请选择数据集', trigger: 'blur' }],
        disorder: [{ required: true, message: '请选择场景', trigger: 'change' }]
      }
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getPublicDiagnosisList()
  },
  methods: {
    getPublicDiagnosisList: function () {
      let that = this
      that.$http.request({
        url: that.$url + 'getPublicDiagnosisList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.diagnoses = response.data
      })
    },
    showAddHomeworkDialog () {
      this.establishDiagnosis = true
    },
    clearAddHomeworkForm () {
      this.$refs.addHomeworkForm.resetFields()
    },
    establishOk () {
      this.establishDiagnosis = false
      this.$refs.addHomeworkForm.validate((valid) => {
        if (valid) {
          let that = this
          this.$http.request({
            url: that.$url + 'PublicEstablishDiagnosis/',
            method: 'get',
            params: {
              userName: that.userName,
              // model: that.addDiagnosisForm.model,
              describe: that.addDiagnosisForm.describe,
              disorder: that.addDiagnosisForm.disorder,
              state: false,
              taskName: that.userName + '-' + that.addDiagnosisForm.disorder + '-默认辅助诊断模型'
            }
          }).then(function (response) {
            console.log(response.data)
            that.getPublicDiagnosisList()
          })
          that.addHomeworkDialogVisible = false
          that.clearAddHomeworkForm()
        } else {
          // 验证失败，不执行任何操作
        }
      })
    },
    tableRowClassName ({row, rowIndex}) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    headerRowClassName () {
      // 返回自定义表头的样式类名
      return 'custom-header-row'
    },
    rowStyle ({ row, rowIndex }) {
      // 自定义每一行的样式
      return {
        background: rowIndex % 2 === 0 ? '#a4e4fd' : 'rgba(164,228,253,0.93)', // 行的背景颜色交替
        color: '#333'
      }
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

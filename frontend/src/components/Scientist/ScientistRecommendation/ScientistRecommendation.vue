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
                    @click="buildThemeVisible = true">创建方案推荐任务</el-button>
                  <el-dialog title="新建方案推荐任务" :visible.sync = "buildThemeVisible" >
                    <el-form ref="form" :model="form" label-width="120px">
                      <el-form-item label="任务名称">
                        <el-input placeholder="根据疾病场景、数据集、模型自动生成名称" v-model="form.name" :disabled="true"></el-input>
                      </el-form-item>
                      <el-form-item label="任务简介">
                        <el-input placeholder="请输入" v-model="form.introduction"></el-input>
                      </el-form-item>
                      <el-form-item label="数据集">
                        <el-select v-model="form.data" placeholder="请选择数据集">
                          <el-option label="ADNI dataset" value="ADNI dataset"></el-option>
                          <el-option label="FFAIR dataset" value="FFAIR dataset"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="模型">
                        <el-select v-model="form.model" placeholder="请选择方案模型">
                          <el-option label="VGG16" value="VGG16"></el-option>
                          <el-option label="RESNET50" value="RESNET50"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="TaskSubmit">立即创建</el-button>
                        <el-button @click="buildThemeVisible=false">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog title="查看结果" :visible.sync = "showDataContent" >
                    <el-form ref="form" :model="detail" label-width="150px" >
                      <el-col span=12>
                      <el-form-item label="任务名称:" >
                        {{detail.name}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="任务简介:">
                        {{detail.introduction}}
                      </el-form-item>
                      </el-col>
                      <el-col span=12>
                      <el-form-item label="患者基础信息:">
                        {{detail.patient}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="数据集:">
                        {{detail.data}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="辅助诊断模型:">
                        {{detail.model}}
                      </el-form-item>
                        </el-col>
                        <el-col span=12>
                      <el-form-item label="辅助诊断结果:">
                        {{detail.assistance}}
                      </el-form-item>
                          </el-col>
                      <el-col span=12>
                      <el-form-item label="风险诊断结果:">
                        {{detail.prediction}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="模型:">
                        {{detail.model}}
                      </el-form-item>
                        </el-col>
                      <el-form-item label="方案:">
                        {{detail.recommendation}}
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="onSubmit">返回</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog title="查看结果" :visible.sync = "modifySchemeDialog" >
                    <el-form ref="form" :model="detail" label-width="150px" >
                      <el-col span=12>
                      <el-form-item label="任务名称:" >
                        {{detail.name}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="任务简介:">
                        {{detail.introduction}}
                      </el-form-item>
                      </el-col>
                      <el-col span=12>
                      <el-form-item label="患者基础信息:">
                        {{detail.patient}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="数据集:">
                        {{detail.data}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="辅助诊断模型:">
                        {{detail.model}}
                      </el-form-item>
                        </el-col>
                        <el-col span=12>
                      <el-form-item label="辅助诊断结果:">
                        {{detail.assistance}}
                      </el-form-item>
                          </el-col>
                      <el-col span=12>
                      <el-form-item label="风险诊断结果:">
                        {{detail.prediction}}
                      </el-form-item>
                        </el-col>
                      <el-col span=12>
                      <el-form-item label="模型:">
                        {{detail.model}}
                      </el-form-item>
                        </el-col>
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
                        <el-button type="primary" @click="saveModifyScheme">保存修改</el-button>
                        <el-button type="primary" @click="modifySchemeDialog=false">取消修改</el-button>
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
              <el-dropdown size="mini" split-button @command="handleCommand2">
                <span class="el-dropdown-link">
                  详情
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item :command="beforeHandleCommand(scope.$index,'a')">查看结果</el-dropdown-item>
<!--                  <el-dropdown-item :command="beforeHandleCommand(scope.$index,'b')" divided>修改方案</el-dropdown-item>-->
                </el-dropdown-menu>
              </el-dropdown>
                </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
</template>

<script>
import ScientistMenu from '../ScientistMenu'
export default {
  name: 'ScientistRecommendation',
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
      tasks: [{
        id: '1',
        name: 'AD Diagnosis',
        finishState: '未完成',
        notifyResultState: true,
        notifySchemeState: false,
        time: '2001-2-26 01:01:01',
        introduction: 'asdwa',
        scene: 'AD',
        data: 'asd',
        model: 'VGG16',
        patient: 'asd',
        recommendation: '多喝热水'
      }, {
        id: '2',
        name: 'AD Diagnasdosis',
        finishState: '未完成',
        notifyResultState: false,
        notifySchemeState: false,
        time: '2001-2-26 01:01:01',
        introduction: 'asdwa',
        scene: 'AD',
        data: 'asd',
        model: 'VGG16',
        patient: 'asd',
        recommendation: '多喝热水'
      }],
      form: {
        name: '',
        introduction: '',
        patient: '',
        data: '',
        assistance: '',
        prediction: '',
        model: '',
        docterRecommendation: ''
      },
      detail: {
        id: '2',
        name: 'AD Diagasdnosis',
        state: '未完成',
        time: '2001-2-26 01:01:01',
        introduction: 'asasddwa',
        patient: 'ADsd',
        data: 'assdad',
        assistance: 'ADtasdaskName1',
        prediction: 'RPtasasdkName2',
        model: 'VGG16',
        recommendation: '多喝热水'
      },
      buildThemeVisible: false,
      showDataContent: false,
      modifySchemeDialog: false,
      curIndex: 0
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getScientistRecommendationTaskList()
  },
  methods: {
    getScientistRecommendationTaskList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getScientistRecommendationTaskList/',
        method: 'get'
      }).then(function (response) {
        that.tasks = response.data
      })
    },
    TaskSubmit () {
      this.buildThemeVisible = false
      let that = this
      this.$http.request({
        url: that.$url + 'ScientistEstablishSchemeTask/',
        method: 'get',
        params: {
          taskName: '方案推荐性能评估-' + that.form.model + '-' + that.form.data,
          taskIntroduction: that.form.introduction,
          taskScene: that.form.scenes,
          taskDataset: that.form.data,
          patientID: 1,
          taskModel: that.form.model
        }
      }).then(function (response) {
        console.log(response.data)
        that.getScientistRecommendationTaskList()
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
        this.modifyScheme(command.row)
      }
    },
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.tasks[row]
      this.showDataContent = true
    },
    modifyScheme (row) {
      this.curIndex = row
      this.modifySchemeDialog = true
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

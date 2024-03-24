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
                <el-col :span="18">
                  <el-input
                    placeholder="患者id"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span="6">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: left; margin-right: 10px;margin-left: 20px"
                    @click="searchDiscuss(inputSearch)"
                    circle>
                  </el-button>
                </el-col>
              </el-row>
<!--              <el-row type="flex" alig="middle" justify="center">-->
<!--               <el-col span="18">数据集信息</el-col>-->
<!--                <el-col span="3">-->
<!--                  疾病场景</el-col>-->
<!--                <el-col span="3">操作</el-col>-->
<!--                </el-row>-->
<!--              <el-divider></el-divider>-->
<!--              <el-card v-for="(data, index) in showDatasList" :key="index"-->
<!--                       style="margin-bottom: 2%">-->
<!--                <el-col span="18">-->
<!--                  <el-row class="clearfix" style="font-size: 20px; margin-bottom: 15px">-->
<!--                    {{data.name}}-->
<!--                  </el-row>-->
<!--                  <el-row style="margin-bottom: 20px;">-->
<!--                    <i class="el-icon-user" style="margin-right: 20px">{{data.owner}}</i>-->
<!--                    <i class="el-icon-time" style="margin-right: 20px">{{data.time}}</i>-->
<!--                    <i class="el-icon-folder" style="margin-right: 20px">{{data.size}}</i>-->
<!--                  </el-row>-->
<!--                  <el-row style="margin-bottom: 20px;">{{data.introduction}}</el-row>-->
<!--                </el-col>-->
<!--                <el-col span="3" justify-content="center" >-->
<!--                  <div style="margin-top: 25px">{{data.scenes}}</div>-->
<!--                </el-col>-->
<!--                <el-col span="3">-->
<!--                  <el-row>-->
<!--          <el-button @click="showDetail(index)" size="small" type="success" style="margin-top: 10px">详情</el-button>-->
<!--                  </el-row>-->
<!--                   <el-row>-->
<!--                    <el-button @click="confirmDelete(index)" size="small" type="danger" style="margin-top: 10px">删除</el-button>-->
<!--                  </el-row>-->
<!--                </el-col>-->
<!--              </el-card>-->
            </el-col>
          </el-row>
<!--          <div style="display: flex; align-items: center; justify-content: center;">-->
                  <el-table
                    :data="patients"
                    :header-cell-style="{'text-align':'center'}"
                    :cell-style="{'text-align':'center'}"
                    stripe
                    style="width: 100%">
                    <el-table-column
                      prop="id"
                      label="患者id"
                      width="180">
                    </el-table-column>
                    <el-table-column
                      prop="name"
                      label="患者姓名"
                      width="180">
                    </el-table-column>
            <el-table-column
              prop="age"
              label="年龄"
              width="180">
            </el-table-column>
            <el-table-column
              prop="gender"
              label="性别">
            </el-table-column>
            <el-table-column
              prop="history"
              label="病史">
            </el-table-column>
            <el-table-column
              label="关联数据集名称">默认数据集
            </el-table-column>
             <el-table-column
              label="关联的指标分析任务">
               <template slot-scope="scope">
                 <el-link type="primary" @click="handleClick(scope.$index)">信息详情</el-link>
               </template>
            </el-table-column>
          </el-table>
<!--            </div>-->
          <el-dialog title="指标分析任务" :visible.sync = "showDataContent" >
            <el-descriptions class="margin-top" title="" :column="3" :size="size" border>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-user"></i>
                姓名
              </template>
              {{ resume.name }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                年龄
              </template>
              {{ resume.age }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-location-outline"></i>
                性别
              </template>
              {{ resume.gender }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-tickets"></i>
                学历
              </template>
              <el-tag size="small">{{ resume.education }}</el-tag>
            </el-descriptions-item>
              <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-tickets"></i>
                病史
              </template>
              <el-tag size="small">{{ resume.history }}</el-tag>
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-office-building"></i>
                联系地址
              </template>
              {{ resume.region }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-date"></i>
                出生日期
              </template>{{ resume.birthdate }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                电话号码
              </template>{{ resume.phone }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-user-solid"></i>
                身份证号
              </template>
              {{ resume.ID }}
            </el-descriptions-item>
<!--            <el-descriptions-item>-->
<!--              <template slot="label">-->
<!--                <i class="el-icon-star-on"></i>-->
<!--                MRI得分-->
<!--              </template>{{ resume.MRI }}-->
<!--            </el-descriptions-item>-->
<!--            <el-descriptions-item>-->
<!--              <template slot="label">-->
<!--                <i class="el-icon-s-help"></i>-->
<!--                PET得分-->
<!--              </template>{{ resume.PET }}-->
<!--            </el-descriptions-item>-->
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-trophy"></i>
                ApoE得分
              </template>{{ resume.ApoE }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-first-aid-kit"></i>
                MMSE得分
              </template>{{ resume.MMSE }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-medal"></i>
                ADAS_Cog得分
              </template>{{ resume.ADAS_Cog }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-s-opportunity"></i>
                CDR_Global得分
              </template>{{ resume.CDR_Global }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-s-check"></i>
                CDR_SOB得分
              </template>{{ resume.CDR_SOB }}
            </el-descriptions-item>
            </el-descriptions>
<!--                    <el-form ref="form" :model="detail" label-width="120px">-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="任务名称:">-->
<!--                        {{detail.taskName}}-->
<!--                      </el-form-item></el-col>-->
<!--                      <el-col span=12>-->
<!--                        <el-form-item label="疾病场景:">-->
<!--                        {{detail.scene}}-->
<!--                      </el-form-item></el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="辅助诊断模型:">-->
<!--                        {{detail.model}}-->
<!--                      </el-form-item></el-col>-->
<!--                      <el-col span=12>-->
<!--                      <el-form-item label="数据集:">-->
<!--                        {{detail.data}}-->
<!--                      </el-form-item></el-col>-->
<!--                      <el-form-item label="任务简介:">-->
<!--                        {{detail.introduction}}-->
<!--                      </el-form-item>-->
<!--                      <el-form-item label="诊断结果:">-->
<!--                        <el-card class="box-card">-->
<!--                          <el-form>-->
<!--                            <el-form-item label="患病种类：">-->
<!--                              {{detail.result.disease}}-->
<!--                            </el-form-item>-->
<!--                            <el-form-item label="疾病阶段：">-->
<!--                              {{detail.result.stage}}-->
<!--                            </el-form-item>-->
<!--                          </el-form>-->
<!--                        </el-card>-->
<!--                      </el-form-item>-->
<!--                      <el-form-item>-->
<!--                        <el-button type="primary" @click="onSubmit">返回</el-button>-->
<!--                      </el-form-item>-->
<!--                    </el-form>-->
                  </el-dialog>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import DocterMenu from '../DocterMenu'
export default {
  name: 'DocterPatientData',
  components: {DocterMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      nickName: '',
      inputSearch: '',
      showDataContent: false,
      resume: {
        name: '冯小如',
        gender: '女',
        age: '22',
        history: '无',
        birthdate: '2003-01-01',
        ID: '110110110110110',
        region: '北京市海淀区',
        education: '本科',
        ApoE: '63',
        MMSE: '769',
        CDR_Global: '805',
        CDR_SOB: '637',
        ADAS_Cog: '450',
        MRI: '50',
        PET: '0',
        phone: '18810001000'
      },
      // detail: {
      //   id: '1',
      //   name: 'AD Diagnasdosis',
      //   state: '未完成',
      //   time: '2001-2-26 01:01:01',
      //   introduction: 'asdwa',
      //   scene: 'AD',
      //   data: 'asd',
      //   model: 'VGG16',
      //   result: {
      //     disease: 'as',
      //     stage: 'stage 2',
      //     accuracy: '85%'
      //   }
      // },
      input: {
        title: '',
        content: ''
      },
      patients: [
        {
          name: '是小谔',
          id: 1,
          gender: '男',
          age: '22',
          birthdate: '2003-01-01',
          ID: '123456789',
          region: '北京市海淀区',
          education: '专科',
          ApoE: '623',
          history: '无',
          MMSE: '2169',
          CDR_Global: '805',
          CDR_SOB: '637',
          ADAS_Cog: '450',
          MRI: '50',
          PET: '0',
          phone: '11234564456'
        },
        {
          name: '冯大如',
          id: 2,
          gender: '女',
          age: '22',
          birthdate: '2003-01-01',
          ID: '110110110110110',
          region: '北京市海淀区',
          education: '本科',
          ApoE: '63',
          MMSE: '769',
          history: '无',
          CDR_Global: '805',
          CDR_SOB: '637',
          ADAS_Cog: '450',
          MRI: '50',
          PET: '0',
          phone: '18810001000'
        }
      ]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getPatientsList()
  },
  methods: {
    getPatientsList: function () {
      let that = this
      that.$http.request({
        url: that.$url + 'getPatientList/',
        method: 'get'
      }).then(function (response) {
        that.patients = response.data
      })
    },
    // getPatientAssistantTask: function (patientID) {
    //   let that = this
    //   that.$http.request({
    //     url: that.$url + 'getPatientAssistantTask',
    //     method: 'get',
    //     params: {
    //       userName: patientID
    //     }
    //   }).then(function (response) {
    //     that.detail = response.data
    //   })
    // },
    handleClick (row) {
      // console.log(row)
      this.detail = this.patients[row]
      // this.getPatientAssistantTask(this.patients[row].id)
      this.resume = this.patients[row]
      this.showDataContent = true
    },
    onSubmit () {
      this.showDataContent = false
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

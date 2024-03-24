<template>
  <div>
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
      </el-container>
      <el-container class="background">
      <el-aside width="250px">
        <PublicMenu></PublicMenu>
      </el-aside>
        <el-main style="padding-left: 10%; padding-right: 10%" class="main">
          <div class="form-container">
            <div class="form-row">
              <label for="student-id">姓名<span class="required">*</span></label>
              <el-input type="text" id="student-id" v-model="resume.name" />
            </div>
            <div class="form-row">
              <label for="student-id">年龄<span class="required">*</span></label>
              <el-input type="text" id="student-id" v-model="resume.age" />
            </div>
            <div class="form-row">
              <label for="gender">性别<span class="required">*</span></label>
              <el-select id="gender" v-model="resume.gender">
                <el-option value="男">男</el-option>
                <el-option value="女">女</el-option>
              </el-select>
            </div>
            <div class="form-row">
              <label for="education">学历<span class="required">*</span></label>
              <el-select id="education" v-model="resume.education">
                <el-option value="小学">小学</el-option>
                <el-option value="初中">初中</el-option>
                <el-option value="高中">高中</el-option>
                <el-option value="专科">专科</el-option>
                <el-option value='本科'>本科</el-option>
                <el-option value="研究生">研究生</el-option>
              </el-select>
            </div>
            <div class="form-row">
              <label for="region">联系地址 <span class="required">*</span></label>
              <el-input type="text" id="region" v-model="resume.region" />
            </div>
            <div class="form-row">
              <label for="id-number">身份证号 <span class="required">*</span></label>
              <el-input type="text" id="id-number" v-model="resume.ID" />
            </div>
            <div class="form-row">
              <label for="birthdate">出生日期 <span class="required">*</span></label>
              <el-input type="date" id="birthdate" v-model="resume.birthdate" />
            </div>
            <div class="form-row">
              <label for="residence-type">电话号码 <span class="required">*</span></label>
              <el-input type="text" id="residence-type" v-model="resume.phone" />
            </div>
            <div class="form-row">
              <label for="ApoE">ApoE得分 <span class="required">*</span></label>
              <el-input type="text" id="ApoE" v-model="resume.ApoE" />
            </div>
            <div class="form-row">
              <label for="MMSE">MMSE得分 <span class="required">*</span></label>
              <el-input type="text" id="MMSE" v-model="resume.MMSE" />
            </div>
            <div class="form-row">
              <label for="ADAS_Cog" style="width: 160px">ADAS_Cog得分<span class="required">*</span></label>
              <el-input type="text" id="ADAS_Cog" v-model="resume.ADAS_Cog" />
            </div>
            <div class="form-row">
              <label for="CDR_Global">CDR_Global <span class="required">*</span></label>
              <el-input type="text" id="CDR_Global" v-model="resume.CDR_Global" />
            </div>
            <div class="form-row">
              <label for="CDR_SOB">CDR_SOB <span class="required">*</span></label>
              <el-input type="text" id="CDR_SOB" v-model="resume.CDR_SOB" />
            </div>
        </div>
          <div class="confirm-button" style=" display: flex;justify-content: flex-end; margin-top: 20px; margin-right: 150px">
      <el-button type="primary" @click="saveResume" >确定</el-button>
    </div>
        </el-main>

    </el-container>
  </div>
</template>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  margin: 0 auto;
}

.form-row {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

label {
  width: 150px;
  font-weight: bold;
}

input,
select {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.required {
  color: red;
}
</style>

<script>
import PublicMenu from '../PublicMenu'
import {quillEditor} from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

export default {
  name: 'PublicResumeEdit',
  components: {PublicMenu, quillEditor},
  data: function () {
    return {
      userName: 'asd',
      nickName: 'asd',
      resume: {
        name: 'asdwad',
        gender: '男',
        age: '22',
        birthdate: '2003-01-01',
        ID: '131311541515',
        region: '北京海淀',
        education: '本科',
        ApoE: 'asd',
        MMSE: '1',
        CDR_Global: 'asd',
        CDR_SOB: 'asd',
        ADAS_Cog: '123',
        MRI: 'a',
        PET: 'asd',
        phone: '100-1010'
      }
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.resume = this.$route.query.resume
  },
  methods: {
    saveResume: function () {
      // 保存到数据库
      let that = this
      this.$http.request({
        url: that.$url + 'PublicSaveResume/',
        method: 'get',
        params: {
          userName: that.userName,
          nickName: that.resume.name,
          userGender: that.resume.gender,
          userAge: that.resume.age,
          userBirthdate: that.resume.birthdate,
          userID: that.resume.ID,
          userRegion: that.resume.region,
          userEducation: that.resume.education,
          userApoE: that.resume.ApoE,
          userMMSE: that.resume.MMSE,
          userCDR_Global: that.resume.CDR_Global,
          userCDR_SOB: that.resume.CDR_SOB,
          userADAS_Cog: that.resume.ADAS_Cog,
          userMRI: that.resume.MRI,
          userPET: that.resume.PET,
          userPhone: that.resume.phone
        }
      }).then(function (response) {
        console.log(response.data)
        that.$router.push({
          name: 'PublicResume'
        })
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('nickName')
      this.$router.replace('/')
    },
    handleCommand (command) {
      this.goToHelloWorld()
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>

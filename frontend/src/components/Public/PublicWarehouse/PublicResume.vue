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
          <div style="text-align: right">
          <el-button type="primary"  size="small" @click="goToEditPage">编辑资料</el-button></div>
<!--          <div style="text-align: right"><el-button type="primary" round style="margin-top: 10px" @click="goToEditPage">上传</el-button></div>-->
          <div style="text-align: right; margin-top: 10px">
                    <el-upload
            class="upload-demo"
            action="https://jsonplaceholder.typicode.com/posts/"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            multiple
            :limit="3"
            :on-exceed="handleExceed"
            :file-list="fileList">
            <el-button size="small" type="primary" >上传MRI图像</el-button>
                      <el-button size="small" type="primary" >上传PET图像</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
          </div>
          <el-descriptions class="margin-top" title="个人信息" :column="3" :size="size" border>
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
                <i class="el-icon-trophy"></i>
                ApoE得分
              </template>{{ resume.ApoE }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-star-on"></i>
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
                <i class="el-icon-s-help"></i>
                CDR_SOB得分
              </template>{{ resume.CDR_SOB }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-user-solid"></i>
                身份证号
              </template>
              {{ resume.ID }}
            </el-descriptions-item>
          </el-descriptions>
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
  name: 'PublicResume',
  components: {PublicMenu, quillEditor},
  data: function () {
    return {
      userName: 'asd',
      nickName: 'asd',
      resume: {
        name: '冯小如',
        gender: '女',
        age: '22',
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
      }
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getPublicResume()
  },
  methods: {
    getPublicResume: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getPublicResume/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.resume = response.data
      })
    },
    goToEditPage: function () {
      let that = this
      this.$router.push({
        name: 'PublicResumeEdit',
        query: {
          userName: that.userName,
          nickName: that.nickName,
          resume: that.resume
        }
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

<template>
  <transition name="head-login-register">
    <div class="background">
      <br>
      <div class="register_block">
        <div class="register_head">
          <p>注册</p>
        </div>
        <el-form rules="rules" style="margin-left: -50px">
          <div id="register-n">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入工号以确认您的科研身份"
                        v-model="userName" clearable></el-input>
            </el-form-item>
          </div>
          <div id="register-name">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入您的昵称"
                        v-model="nickName" clearable></el-input>
            </el-form-item>
          </div>
          <div id="register-password">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入密码"
                        v-model="userPassWord" show-password clearable></el-input>
            </el-form-item>
          </div>
          <div id="confirm-password">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请确认密码"
                        v-model="userPassWord2" show-password clearable></el-input>
            </el-form-item>
          </div>
          <div class="confirm-button">
            <el-button id="button_in_student" type="primary" size="medium" v-on:click="Register">
              确认
            </el-button>
          </div>
          <div class="return-button">
            <el-button id="button_re" type="success" plain="true" size="medium" v-on:click="goToStudentLogin">
              返回
            </el-button>
          </div>
        </el-form>
      </div>
      <div class="register_right_student">
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'ScientistRegister',
  data: function () {
    return {
      status: -1,
      nickName: '',
      userName: '',
      userPassWord: '',
      userPassWord2: ''
    }
  },
  mounted () {
    window.addEventListener('keydown', this.keydown)
  },
  methods: {
    goToStudentLogin: function () {
      this.$router.push({
        name: 'ScientistLogin'
      })
    },
    Register: function () {
      let that = this
      if (that.userPassWord === '') {
        that.$message.error('密码不能为空')
      } else if (that.userName !== 'SCI') {
        that.$message.error('IDKey不合法!!!')
      } else if (that.nickName === '') {
        that.$message.error('请添加您的昵称')
      } else {
        this.$http.request({
          url: that.$url + 'ScientistRegister/',
          method: 'get',
          params: {
            nickName: that.nickName,
            userName: that.userName,
            userPassword: that.userPassWord,
            userPassword2: that.userPassWord2
          }
        }).then(function (response) {
          console.log(response)
          that.status = response.data
          if (that.status === 0) {
            that.$router.push({
              name: 'ScientistLogin',
              params: {
                userName: that.userName
              }
            })
          } else if (that.status === 1) {
            that.$message.error('该用户已存在')
          } else if (that.status === 2) {
            that.$message.error('密码不一致')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    keydown (e) {
      if (e.keyCode === 13) {
        this.Register()
      }
    }
  },
  destroyed () {
    window.removeEventListener('keydown', this.keydown, false)
  }
}
</script>

<style scoped>
@import "../../assets/css/register.css";
@import "../../assets/css/Transition/head-login-register.css";
</style>

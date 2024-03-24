<template>
  <transition name="head-login-register">
    <div class="background">
      <br>
      <div class="register_block">
        <div class="register_head">
          <p>注册</p>
        </div>
        <el-form style="margin-left: -50px">
          <div id="register-name">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入正确的工号以确认您的医生身份" v-model="userName" clearable></el-input>
            </el-form-item>
          </div>
          <div id="register-n">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入您的昵称" v-model="nickName" clearable></el-input>
            </el-form-item>
          </div>
          <div id="register-password">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入密码" v-model="userPassWord" show-password
                        clearable></el-input>
            </el-form-item>
          </div>
          <div id="confirm-password">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请确认密码" v-model="userPassWord2" show-password
                        clearable></el-input>
            </el-form-item>
          </div>
          <div class="confirm-button">
            <el-button id="button_in_teacher" size="medium" v-on:click="Register">
              确认
            </el-button>
          </div>
          <div class="return-button">
            <el-button id="button_re" plain="true" size="medium" v-on:click="goToDocterLogin">
              返回
            </el-button>
          </div>
        </el-form>
      </div>
      <div class="register_right_teacher">
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  data: function () {
    return {
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
    goToDocterLogin: function () {
      this.$router.push({
        name: 'DocterLogin'
      })
    },
    Register: function () {
      let that = this
      if (that.userPassWord === '') {
        that.$message.error('密码不能为空')
      } else if (that.nickName === '') {
        that.$message.error('昵称不能为空')
      } else if (that.userName !== 'BUAA') {
        that.$message.error('医院不存在此工号!!!')
      } else {
        this.$http.request({
          url: that.$url + 'DocterRegister/',
          method: 'get',
          params: {
            userName: that.userName,
            nickName: that.nickName,
            userPassword: that.userPassWord,
            userPassword2: that.userPassWord2
          }
        }).then(function (response) {
          console.log(response)
          that.status = response.data
          if (that.status === 0) {
            that.$router.push({
              name: 'DocterLogin'
            })
          } else if (that.status === 1) {
            that.$message.error('工号已存在')
          } else if (that.status === 2) {
            that.$message.error('两次输入的密码不一致')
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

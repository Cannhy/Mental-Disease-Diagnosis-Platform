<template>
  <transition name="head-login-register">
    <div class="background">
      <br>
      <div class="register_block">
        <div class="register_head">
          <p>登录</p>
        </div>
        <el-form style="margin-left: -50px">
          <div id="register-name">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入IDKey"
                        v-model="userName" clearable></el-input>
            </el-form-item>
          </div>
          <div id="register-password">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入密码"
                        v-model="userPassWord" show-password clearable></el-input>
            </el-form-item>
          </div>
          <div class="confirm-button">
            <el-button id="button_in_teacher" size="medium" v-on:click="goToDocterHead">
              确认
            </el-button>
          </div>
          <div class="register-button">
            <el-button id="button_re" :plain="true" size="medium" v-on:click="goToDocterRegister">
              注册
            </el-button>
          </div>
          <div class="register-button">
            <el-button id="button_re" plain="true" size="medium" v-on:click="goToStart">
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
/* eslint-disable */
export default {
  name: 'TeacherLogin',
  data: function () {
    return {
      nickName: '',
      userName: '',
      userPassWord: '',
      status: -1
    }
  },
  mounted () {
    window.addEventListener('keydown', this.keydown)
  },
  methods: {
    goToDocterHead: function () {
      let that = this
      let debug = false
      if (debug) {
        if (that.userName === '1' && that.userPassWord === '1') {
          let loginInfo = {userName: '1', nickName: '前端测试医生'}
          that.cookie.setCookie(loginInfo)
          that.$router.push({
            name: 'DocterHead',
          })
        } else {
          that.$message.error('!!!')
        }
      } else {
        this.$http.request({
          url: that.$url + 'DocterLogin/',
          method: 'get',
          params: {
            userName: that.userName,
            userPassword: that.userPassWord
          }
        }).then(function (response) {
          console.log(response)
          that.status = response.data.ret
          if (that.status === 0) {
            let loginInfo = {userName: that.userName, nickName: response.data.nickName}
            that.cookie.setCookie(loginInfo)
            that.$router.push({
              name: 'DocterHead',
            })
          } else if (that.status === 1) {
            that.$message.error('密码错误')
          } else if (that.status === 2) {
            that.$message.error('该用户不存在')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    goToDocterRegister: function () {
      this.$router.push({
        name: 'DocterRegister'
      })
    },
    goToStart: function () {
      this.$router.push({
        name: 'HelloWorld'
      })
    },
    keydown (e) {
      if (e.keyCode === 13) {
        this.goToDocterHead()
      }
    }
  },
  destroyed () {
    window.removeEventListener('keydown', this.keydown, false)
  }
}
</script>

<style scoped>
@import "../../assets/css/login.css";
@import "../../assets/css/Transition/head-login-register.css";
</style>

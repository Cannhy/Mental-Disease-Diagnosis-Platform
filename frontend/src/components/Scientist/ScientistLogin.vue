<template>
  <transition name="head-login-register">
    <div class="background">
      <br>
      <div class="register_block">
        <div class="register_head_admin">
          <p>登录</p>
        </div>
        <el-form style="margin-left: -50px">
          <div id="register-name">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入您的IDKey"
                        v-model="userName" clearable></el-input>
            </el-form-item>
          </div>
          <div id="register-password">
            <el-form-item>
              <el-input class="inputs" style="width: 290px" type="text" size="medium" placeholder="请输入您的密码"
                        v-model="userPassWord" show-password clearable></el-input>
            </el-form-item>
          </div>
          <div class="confirm-button">
            <el-button id="button_in_admin" type="success" size="medium" v-on:click="goToScientistHead">
              确认
            </el-button>
          </div>
          <div class="register-button">
            <el-button id="button_re" type="success" :plain="true" size="medium" v-on:click="goToScientistRegister">
              注册
            </el-button>
          </div>
          <div class="register-button">
            <el-button id="button_re" type="success" :plain="true" size="medium" v-on:click="goToStart">
              返回
            </el-button>
          </div>
        </el-form>
      </div>
      <div class="register_right_admin">
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'ScientistLogin',
  data: function () {
    return {
      userName: '',
      userPassWord: '',
      nickName: '',
      status: -1
    }
  },
  mounted () {
    window.addEventListener('keydown', this.keydown)
  },
  methods: {
    goToScientistHead: function () {
      let that = this
      let debug = false
      if (debug) {
        if (that.userName === '1' && that.userPassWord === '1') {
          let loginInfo = {userName: '1', nickName: '科研人员测试'}
          that.cookie.setCookie(loginInfo)
          that.$router.push({
            name: 'ScientistHead'
          })
        } else {
          that.$message.error('!!!')
        }
      } else {
        this.$http.request({
          url: that.$url + 'ScientistLogin/',
          method: 'get',
          params: {
            // userNickName: that.userNickName,
            userName: that.userName,
            userPassword: that.userPassWord
          }
        }).then(function (response) {
          console.log(response.data)
          that.status = response.data.ret
          if (that.status === 0) {
            let loginInfo = {userName: that.userName, nickName: response.data.nickName}
            that.cookie.setCookie(loginInfo)
            that.$router.push({
              name: 'ScientistHead'
            })
          } else if (that.status === 1) {
            that.$message.error('密码错误')
          } else if (that.status === 2) {
            that.$message.error('用户名不存在')
          } else {
            that.$message.info('请输入用户名')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    goToScientistRegister: function () {
      this.$router.push({
        name: 'ScientistRegister'
      })
    },
    goToStart: function () {
      this.$router.push({
        name: 'HelloWorld'
      })
    },
    keydown (e) {
      if (e.keyCode === 13) {
        this.goToScientistHead()
      }
    },
    destroyed () {
      window.removeEventListener('keydown', this.keydown, false)
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/login.css";
@import "../../assets/css/Transition/head-login-register.css";
</style>

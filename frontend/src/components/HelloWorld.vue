<template >
  <transition name="head-login-register">
    <div class="welcome">
      <div class="navigator">
        <div class="navigator-left">
          <i class="el-icon-s-platform"> 精神疾病诊断平台</i>
        </div>
        <div class="cover">
              <span><el-button type="warning" plain round
                               @click="goToStudentLogin">社会大众</el-button></span>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <span><el-button type="warning" plain round
                               @click="goToTeacherLogin">医疗人员</el-button></span>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <span><el-button type="warning" plain round
                               @click="goToAdminLogin">科研人员</el-button></span>
        </div>
        <div class="navigator-right">
          <div class="time-container">
            <div id="time">{{ currentTime }}</div>
          </div>
        </div>
      </div>
      <div class="introduction">
<!--        <el-carousel height="550px">-->
<!--          <el-carousel-item v-for="(item, index) in headImg" :key="index">-->
<!--            <img :src="item.src" style="width: 100%; height: 100%;" alt="">-->
<!--            <div class="cover">-->
<!--&lt;!&ndash;              <span style="font-size: 50px; opacity:1;color: #ff002f;">{{ item.title }}</span><br>&ndash;&gt;-->
<!--&lt;!&ndash;              <span style="font-size: 25px; opacity:1;color: #ff002f;">{{ item.subTitle }}</span><br>&ndash;&gt;-->
<!--              <span><el-button round type="success" class="buttons"-->
<!--                               @click="goToStudentLogin">我是学生</el-button></span>-->
<!--              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>-->
<!--              <span><el-button round type="success" class="buttons"-->
<!--                               @click="goToTeacherLogin">我是老师</el-button></span>-->
<!--              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>-->
<!--              <span><el-button round type="success" class="buttons"-->
<!--                               @click="goToAdminLogin">管理员登录</el-button></span>-->
<!--            </div>-->
<!--          </el-carousel-item>-->
<!--        </el-carousel>-->
        <img :src="headImg[0].src" style="width: 100%; height: 100%;" alt="">
<!--        <div class="cover">-->
<!--              <span style="font-size: 50px; opacity:1;color: #ff002f;"></span><br>-->
<!--              <span style="font-size: 25px; opacity:1;color: #ff002f;"></span><br>-->
<!--          <br><br><br><br><br><br><br><br><br><br><br>-->
<!--              <span><el-button type="danger" plain round-->
<!--                               @click="goToStudentLogin">社会大众</el-button></span>-->
<!--              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>-->
<!--              <span><el-button type="danger" plain round-->
<!--                               @click="goToTeacherLogin">医疗人员</el-button></span>-->
<!--              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>-->
<!--              <span><el-button type="danger" plain round-->
<!--                               @click="goToAdminLogin">科研人员</el-button></span>-->
<!--        </div>-->
      </div>
    </div>
  </transition>
</template>

<script>
import background from '../assets/img/bgn.jpg'
// import background2 from '../assets/img/bg2.png'

export default {
  data: function () {
    return {
      headImg: [
        {
          'title': '精神疾病诊断平台',
          'subTitle': 'Psychiatric Diagnosis Platform',
          'src': background
        }
      ],
      fullscreenLoading: false,
      currentTime: ''
    }
  },
  mounted () {
    setInterval(this.updateTime, 1000)
  },
  methods: {
    updateTime () {
      var now = new Date()
      var timeString = now.toLocaleTimeString()
      this.currentTime = timeString
    },
    goToStudentLogin () {
      this.$router.push({
        name: 'PublicLogin'
      })
    },
    goToTeacherLogin () {
      this.$router.push({
        name: 'DocterLogin'
      })
    },
    goToAdminLogin () {
      this.$router.push({
        name: 'ScientistLogin'
      })
    }
  }
}
</script>

<style scoped>
@import "../assets/css/HelloWorld/block1.css";
@import "../assets/css/HelloWorld/block2.css";
@import "../assets/css/HelloWorld/copyright.css";
@import "../assets/css/HelloWorld/introduction.css";
@import "../assets/css/HelloWorld/navigator.css";
@import "../assets/css/Transition/head-login-register.css";

.welcome {
  margin-left: 0px;
  margin-right: 0px;
  background-image: url('../assets/img/background.png');
  background-size: cover;
}

</style>

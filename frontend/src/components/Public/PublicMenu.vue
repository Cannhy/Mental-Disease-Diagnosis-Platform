<template>
  <div>
    <el-menu default-active="$route.path" class="el-head-menu" router>
      <el-menu-item class="item" index="/PublicHead">
        <i class="el-icon-s-home"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-menu-item index="/PublicWarehouse/PublicResume">
        <i class="el-icon-location" ></i>
        <span slot="title">我的病例</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-setting"></i><span>疾病分析</span></template>
          <el-menu-item index="/PublicDiseaseAnalysis/PublicAssistanceDiagnosis">我的诊断</el-menu-item>
          <el-menu-item index="/PublicDiseaseAnalysis/PublicRiskPrediction">风险预测</el-menu-item>
      </el-submenu>
      <el-menu-item index="/PublicRecommendation">
        <i class="el-icon-document"></i>
        <span slot="title">方案推荐</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<style>
@import "../../assets/css/menu.css";
</style>

<script>
import Utils from '../../assets/js/util.js'
export default {
  name: 'PublicMenu',
  data () {
    return {
      userName: '',
      userNickName: '',
      isCollapsed: this.$root.isCollapsed
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    var that = this
    Utils.$on('toggleCollapse', function (message) {
      console.log(message)
      that.toggleCollapse()
    })
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.isCollapsed = !this.isCollapsed
      this.$root.isCollapsed = this.isCollapsed
    }
  }
}
</script>

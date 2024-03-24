<template>
  <div>
    <el-menu default-active="$route.path" class="el-head-menu" router>
      <el-menu-item class="item" index="/DocterHead">
        <i class="el-icon-s-home"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-submenu index="0">
        <template slot="title"><i class="el-icon-setting"></i><span>仓库</span></template>
          <el-menu-item index="/DocterWarehouse/DocterDataset">数据集</el-menu-item>
          <el-menu-item index="/DocterWarehouse/DocterPatientData">患者数据</el-menu-item>
<!--          <el-menu-item index="/DocterWarehouse/DocterModel">模型</el-menu-item>-->
          <el-menu-item index="/DocterWarehouse/DocterBoard">病例模板</el-menu-item>
      </el-submenu>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-setting"></i><span>疾病分析</span></template>
          <el-menu-item index="/DocterDiseaseAnalysis/DocterAssistanceDiagnosis">辅助诊断</el-menu-item>
          <el-menu-item index="/DocterDiseaseAnalysis/DocterRiskPrediction">风险预测</el-menu-item>
      </el-submenu>
      <el-menu-item index="/DocterRecommendation">
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
  name: 'DocterMenu',
  data () {
    return {
      userName: '',
      nickName: '',
      isCollapsed: this.$root.isCollapsed
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    var that = this
    Utils.$on('toggleCollapse', function (message) {
      console.log(message)
      that.toggleCollapse()
    })
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('nickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.isCollapsed = !this.isCollapsed
      this.$root.isCollapsed = this.isCollapsed
    }
  }
}
</script>

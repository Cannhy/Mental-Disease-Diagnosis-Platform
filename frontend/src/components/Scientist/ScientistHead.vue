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
        <ScientistMenu></ScientistMenu>
      </el-aside>
        <el-main style="padding-left: 5%; padding-right: 10%" class="main">
          <h2>精神疾病诊断平台</h2>
          <h1>简介</h1>
          <p style="line-height: 2;">精神疾病诊断平台(Mental Illness Diagnosis Platform)，是集数据集管理、辅助诊断、风险预测和方案推荐的面向社会大众、医疗人员和科研人员的辅助诊断平台，旨在提高精神类疾病的诊断效率。</p>
          <p>精神疾病诊断平台可以允许医疗人员和科研人员根据疾病类别上传数据集，社会大众可以上传个人病例信息</p>
          <p>平台提供了多种模型和算法，为患者的疾病诊断提供决策支持，使得可以更快速、准确地诊断患者病情。</p>
          <p>平台可以基于患者的多源数据、先进的算法模型，对患者在未来时间点的患病风险进行预测。通过此模块，科研人员可以查看预测的效果，随时调整科研方向或模型参数；医生可以了解患者未来可能面临的健康风险，提前做好预防措施，降低患病风险。</p>
          <p>方案推荐基于疾病分析的结果为患者提供一套全面的、个性化的治疗、护理或健康管理方案。这些方案将充分考虑患者的具体情况、诊断结果和潜在风险，确保患者得到最适合自己的治疗建议。</p>
          <h1>功能说明</h1>
          <ul>
            <li>仓库——进行数据集管理和个人病例上传</li>
            <li>疾病分析——进行辅助诊断和风险预测</li>
            <li>方案推荐——查看你的治疗方案</li>
          </ul>
          <h4>感谢您的使用！</h4>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import ScientistMenu from './ScientistMenu'
export default {
  name: 'ScientistHead',
  components: {ScientistMenu},
  data: function () {
    return {
      circleUrl: '',
      userName: '',
      nickName: '',
      show: false
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
  },
  methods: {
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
@import "../../assets/css/back.css";
</style>

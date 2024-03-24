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
        <PublicMenu></PublicMenu>
      </el-aside>
        <el-main style="padding-left: 5%; padding-right: 10%" class="main">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span style="font-weight: bold">医生建议</span>
          <!--    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
            </div>
<!--            <div v-for="o in 4" :key="o" class="text item">-->
<!--              {{'家人应该持续陪伴，做好患者的清洁卫生工作，关注情绪，注意保暖。' + o }}-->
<!--            </div>-->
            <div class="text item" v-if="show" v-html="scheme"></div>
            <div class="text item" v-else>请等待医生审查后查看</div>
          </el-card>
        </el-main>
</el-container>
    </el-container>

</template>

<style module>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>

<script>
import PublicMenu from '../PublicMenu'
export default {
  name: 'PublicRecommendation',
  components: {PublicMenu},
  data: function () {
    return {
      circleUrl: '',
      userName: '',
      nickName: '',
      show: true,
      scheme: '家人应该持续陪伴，做好患者的清洁卫生工作，关注情绪，注意保暖。\n' +
        '药物治疗：\n' +
        '胆碱酯酶抑制剂（Cholinesterase Inhibitors）： 这类药物包括多巴胺胆碱酯酶抑制剂（如多奈哌齐）、甲氧氯普胺和依非酰胆碱酯酶抑制剂。它们可用于改善大脑中的神经递质水平，帮助提高认知功能和日常生活能力。\n' +
        'NMDA受体拮抗剂： 如美金刚、拉美西头孢等，可用于中度至重度阿尔兹海默症患者，帮助缓解症状和减缓疾病进展。\n' +
        '非药物治疗：\n' +
        '认知训练和康复： 包括记忆训练、注意力练习和问题解决技能训练等，旨在帮助患者维持或提高日常生活功能。\n' +
        '生活方式干预： 促进健康的生活方式，包括规律的锻炼、健康饮食、充足睡眠等，有助于改善患者的整体健康状况。\n' +
        '情绪支持和心理疏导： 提供情绪支持和心理疏导服务，帮助患者和家人应对情绪上的困扰和应对挑战。\n' +
        '支持性护理：\n' +
        '日常生活支持： 提供日常生活活动的帮助，如饮食、洗漱、穿衣等，以维持患者的基本生活功能。\n' +
        '社交支持： 通过参加社交活动和与家人、朋友以及社区联系，提供社交支持和心理支持。\n' +
        '安全保障： 确保患者生活在安全的环境中，防止意外和伤害发生，如安装防跌倒设备、监控用具等。'
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getPublicRecommendation()
  },
  methods: {
    getPublicRecommendation: function () {
      let that = this
      that.$http.request({
        url: that.$url + 'getPublicRecommendation/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        that.show = response.data.state
        that.scheme = response.data.scheme
      })
    },
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
@import "../../../assets/css/back.css";
</style>

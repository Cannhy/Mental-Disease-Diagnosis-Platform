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

<script>
export default {
  name: 'header'
}
</script>

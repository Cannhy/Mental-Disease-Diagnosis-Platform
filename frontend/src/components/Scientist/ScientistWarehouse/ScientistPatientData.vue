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
            <el-dropdown @command="handleCommand"><span class="el-dropdown-link">{{ userNickName }}<i
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
          <el-row>
            <el-col :span="24">
              <el-row>
                <el-col :span="18">
                  <el-input
                    placeholder="患者id"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span="6">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: left; margin-right: 10px;margin-left: 20px"
                    @click="searchDiscuss(inputSearch)"
                    circle>
                  </el-button>
                </el-col>
              </el-row>
<!--              <el-row type="flex" alig="middle" justify="center">-->
<!--               <el-col span="18">数据集信息</el-col>-->
<!--                <el-col span="3">-->
<!--                  疾病场景</el-col>-->
<!--                <el-col span="3">操作</el-col>-->
<!--                </el-row>-->
<!--              <el-divider></el-divider>-->
<!--              <el-card v-for="(data, index) in showDatasList" :key="index"-->
<!--                       style="margin-bottom: 2%">-->
<!--                <el-col span="18">-->
<!--                  <el-row class="clearfix" style="font-size: 20px; margin-bottom: 15px">-->
<!--                    {{data.name}}-->
<!--                  </el-row>-->
<!--                  <el-row style="margin-bottom: 20px;">-->
<!--                    <i class="el-icon-user" style="margin-right: 20px">{{data.owner}}</i>-->
<!--                    <i class="el-icon-time" style="margin-right: 20px">{{data.time}}</i>-->
<!--                    <i class="el-icon-folder" style="margin-right: 20px">{{data.size}}</i>-->
<!--                  </el-row>-->
<!--                  <el-row style="margin-bottom: 20px;">{{data.introduction}}</el-row>-->
<!--                </el-col>-->
<!--                <el-col span="3" justify-content="center" >-->
<!--                  <div style="margin-top: 25px">{{data.scenes}}</div>-->
<!--                </el-col>-->
<!--                <el-col span="3">-->
<!--                  <el-row>-->
<!--          <el-button @click="showDetail(index)" size="small" type="success" style="margin-top: 10px">详情</el-button>-->
<!--                  </el-row>-->
<!--                   <el-row>-->
<!--                    <el-button @click="confirmDelete(index)" size="small" type="danger" style="margin-top: 10px">删除</el-button>-->
<!--                  </el-row>-->
<!--                </el-col>-->
<!--              </el-card>-->
            </el-col>
          </el-row>
                  <el-table
            :data="patients"
            stripe
            style="width: 100%">
            <el-table-column
              prop="id"
              label="患者id"
              width="180">
            </el-table-column>
            <el-table-column
              prop="age"
              label="年龄"
              width="180">
            </el-table-column>
            <el-table-column
              prop="gender"
              label="性别">
            </el-table-column>
            <el-table-column
              prop="history"
              label="病史">
            </el-table-column>
            <el-table-column
              prop="data"
              label="关联数据集名称">
            </el-table-column>
             <el-table-column
              label="关联的指标分析任务">
               <template slot-scope="scope">
                 <el-link type="primary" :href="scope.row.task">任务链接</el-link>
               </template>
            </el-table-column>
          </el-table>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import ScientistMenu from '../ScientistMenu'
// import TeacherImg from '../../../assets/img/teacher.png'
export default {
  name: 'ScientistPatientData',
  components: {ScientistMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      inputSearch: '',
      input: {
        title: '',
        content: ''
      },
      patients: [
        {
          id: '1',
          age: 18,
          gender: 'Man',
          history: '玉玉症',
          data: '数据集1',
          task: 'https://baidu.com'
        },
        {
          id: '2',
          age: 28,
          gender: 'Woman',
          history: '狂躁症',
          data: '数据集2',
          task: 'https://zhihu.com'
        }
      ]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  },
  methods: {
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.datas[row]
      this.showDataContent = true
    },
    showAddHomeworkDialog () {
      this.addHomeworkDialogVisible = true
    },
    clearAddHomeworkForm () {
      this.$refs.addHomeworkForm.resetFields()
    },
    addHomework () {
      this.$refs.addHomeworkForm.validate((valid) => {
        if (valid) {
          let that = this
          this.$http.request({
            url: that.$url + 'StudentAddHomework/',
            method: 'get',
            params: {
              sid: that.userName,
              cid: that.addHomeworkForm.course,
              end_time: that.addHomeworkForm.endTime,
              content: that.addHomeworkForm.content
            }
          }).then(function (response) {
            console.log(response.data)
            that.fetchTodoList()
          })
          that.addHomeworkDialogVisible = false
          that.clearAddHomeworkForm()
        } else {
          // 验证失败，不执行任何操作
        }
      })
    },
    tableRowClassName ({row, rowIndex}) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    headerRowClassName () {
      // 返回自定义表头的样式类名
      return 'custom-header-row'
    },
    rowStyle ({ row, rowIndex }) {
      // 自定义每一行的样式
      return {
        background: rowIndex % 2 === 0 ? '#a4e4fd' : 'rgba(164,228,253,0.93)', // 行的背景颜色交替
        color: '#333'
      }
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
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
<style scoped>

.todo-app {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.todo-input {
  width: 200px;
  margin-bottom: 10px;
}

.todo-select {
  width: 200px;
  margin-bottom: 10px;
}

/* 调整日期选择器样式 */
.todo-datepicker {
  width: 200px;
  margin-bottom: 10px;
}
.todo-button {
  margin-bottom: 10px;
}
.todo-table {
  margin-top: 10px;
  width: 400px;
}
.todo-table th {
  background-color: #f5f7fa;
  color: #909399;
  font-weight: bold;
  text-align: left;
}
.todo-table tr:nth-child(odd) {
  background-color: #f9fafc;
}
.custom-table {
  /* 添加自定义样式 */
}

.custom-table::before {
  content: "";
}
</style>

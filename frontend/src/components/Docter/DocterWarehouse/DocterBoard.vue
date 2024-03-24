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
        <DocterMenu></DocterMenu>
      </el-aside>
        <el-main style="padding-left: 5%; padding-right: 10%" class="main">
          <el-row>
            <el-col :span="24">
              <el-row>
                <el-col :span="18">
                  <el-input
                    placeholder="病例模板名称"
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
                  <el-button
                    type="primary"
                    icon="el-icon-plus"
                    @click="uploadBoardVisible = true">新建病例模板</el-button>
                  <el-dialog title="新建病例模板" :visible.sync = "uploadBoardVisible" >
                    <el-form ref="form" :model="uploadBoardForm" label-width="120px">
                      <el-form-item label="模板名称">
                        <el-input v-model="uploadBoardForm.name"></el-input>
                      </el-form-item>
                      <el-form-item label="疾病场景">
                        <el-input v-model="uploadBoardForm.scene"></el-input>
                      </el-form-item>
                      <el-form-item label="模板内容">
                        <el-input v-model="uploadBoardForm.introduction"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="establishSubmit">立即创建</el-button>
                        <el-button @click="cancelUploadBoard">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog title="病例模板详情" :visible.sync = "showBoardDetail" >
                    <el-form ref="form" :model="detail" label-width="120px">
                      <el-form-item label="模板名称:">
                        {{detail.name}}
                      </el-form-item>
                      <el-form-item label="疾病场景">
                        {{detail.scenes}}
                      </el-form-item>
                      <el-form-item label="创建者">
                        {{detail.doctorName}}
                      </el-form-item>
                      <el-form-item label="更新时间:">
                        {{detail.time}}
                      </el-form-item>
                      <el-form-item label="模板内容">
                        {{detail.introduction}}
                      </el-form-item>
                      <el-form-item style="text-align: right;">
                        <el-button type="primary" @click="showBoardDetail=false">返回</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
          <el-divider></el-divider>
          <el-table
            :data="boards"
            :header-cell-style="{'text-align':'center'}"
            :cell-style="{'text-align':'center'}"
            style="width: 100%">
            <el-table-column
              label="病例模板名称"
              prop="name"
              width="180">
            </el-table-column>
            <el-table-column
              label="疾病场景"
              width="180">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.scenes }}</el-tag>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="创建者">
              <template slot-scope="scope">
                 <el-tag size="medium">{{ scope.row.doctorName }}</el-tag>
              </template>
            </el-table-column>
             <el-table-column label="更新时间">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span >{{ scope.row.time }}</span>
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="success"
                  @click="showDetail(scope.$index)">详情</el-button>
                <el-button
                  v-if="userName===scope.row.doctorID"
                  size="mini"
                  type="danger"
                  @click="confirmDialogDelete(scope.$index)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-dialog
              :visible.sync="deleteDialogVisible"
              title="确认删除"
              width="30%">
              <span>确定要删除吗？</span>
              <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="confirmDelete">确认</el-button>
                <el-button @click="deleteDialogVisible=false">取消</el-button>
              </span>
            </el-dialog>
        </el-main>
</el-container>
    </el-container>
</template>

<script>
import DocterMenu from '../DocterMenu'
export default {
  name: 'DocterBoard',
  components: {DocterMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      nickName: '',
      inputSearch: '',
      input: {
        title: '',
        content: ''
      },
      boards: [{
        id: '1',
        name: '抑郁症特征模板',
        doctorID: '1',
        doctorName: '李四医生',
        time: '2020-3-16 01:01:01',
        scenes: '抑郁症',
        introduction: '为患者进行抑郁症辅助诊断'
      }, {
        id: '2',
        name: '阿尔兹海默症特征模板',
        doctorID: '2',
        doctorName: '张三医生',
        time: '2021-2-26 01:01:01',
        scenes: '阿尔兹海默症',
        introduction: '为患者进行阿尔兹海默症辅助诊断'
      }],
      uploadBoardForm: {
        name: '',
        introduction: '',
        scene: ''
      },
      detail: {
        id: '1',
        name: 'Transformer',
        docterName: '王医生',
        time: '2001-2-26 01:01:01',
        scenes: 'yyz',
        introduction: 'FBRNDataBases is used to Forward'
      },
      uploadBoardVisible: false,
      showBoardDetail: false,
      deleteDialogVisible: false,
      curIndex: 0
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getBoardsList()
  },
  methods: {
    getBoardsList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'getBoardsList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.boards = response.data
      })
    },
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.boards[row]
      this.showBoardDetail = true
    },
    establishSubmit: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'uploadBoard/',
        method: 'get',
        params: {
          userName: that.userName,
          boardName: that.uploadBoardForm.name,
          boardScene: that.uploadBoardForm.scene,
          boardTime: that.getNowTime(),
          boardIntroduction: that.uploadBoardForm.introduction
        }
      }).then(function (response) {
        console.log(response.data)
        that.getBoardsList()
      })
      that.uploadBoardVisible = false
      that.uploadBoardForm.name = ''
      that.uploadBoardForm.introduction = ''
      that.uploadBoardForm.scene = ''
    },
    cancelUploadBoard: function () {
      this.uploadBoardVisible = false
      this.uploadBoardForm.name = ''
      this.uploadBoardForm.introduction = ''
      this.uploadBoardForm.scene = ''
    },
    confirmDialogDelete (row) {
      this.deleteDialogVisible = true
      this.curIndex = row
    },
    confirmDelete () {
      this.deleteDialogVisible = false
      let that = this
      console.log(that.curIndex)
      that.$http.request({
        url: that.$url + 'DeleteBoard/',
        method: 'get',
        params: {
          boardID: that.boards[that.curIndex].id
        }
      }).then(function (response) {
        that.getBoardsList()
      })
      that.getBoardsList()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('nickName')
      this.$router.replace('/')
    },
    handleCommand: function (command) {
      this.goToHelloWorld()
    },
    getNowTime () {
      let now = new Date()
      let year = now.getFullYear() // 获取完整的年份(4位,1970-????)
      let month = now.getMonth() + 1 // 获取当前月份(0-11,0代表1月)
      let today = now.getDate() // 获取当前日(1-31)
      let hour = now.getHours() // 获取当前小时数(0-23)
      let minute = now.getMinutes() // 获取当前分钟数(0-59)
      let second = now.getSeconds() // 获取当前秒数(0-59)
      let nowTime = ''
      // 返回年月日时分秒
      nowTime = year + '-' + this.fillZero(month) + '-' + this.fillZero(today) + ' ' + this.fillZero(hour) + ':' + this.fillZero(minute) + ':' + this.fillZero(second)
      // } else { // 返回年月日
      //   nowTime = year + '-' + this.fillZero(month) + '-' + this.fillZero(today)
      // }
      return nowTime
    },
    // 给时间补零
    fillZero (str) {
      let realNum
      if (str < 10) {
        realNum = '0' + str
      } else {
        realNum = str
      }
      return realNum
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

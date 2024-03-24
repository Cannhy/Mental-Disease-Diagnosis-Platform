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
                    @click="buildThemeVisible = true">新建病例模板</el-button>

                  <el-dialog title="新建病例模板" :visible.sync = "buildThemeVisible" >
                    <el-form ref="form" :model="form" label-width="120px">
              <el-form-item label="模型名称">
                <el-input v-model="form.name"></el-input>
              </el-form-item>
                      <el-form-item label="模型介绍">
                <el-input v-model="form.introduction"></el-input>
              </el-form-item>
                      <el-form-item label="模型类型">
                <el-input v-model="form.type"></el-input>
              </el-form-item>
              <el-form-item label="模型场景">
                <el-select v-model="form.scenes" placeholder="请选择疾病场景">
                  <el-option label="抑郁症" value="抑郁症"></el-option>
                  <el-option label="AD" value="AD"></el-option>
                </el-select>
              </el-form-item>
                                  <el-form-item label="关联数据集">
                <el-select v-model="form.data" placeholder="请选择关联数据集">
                  <el-option label="data1" value="Transformer"></el-option>
                  <el-option label="FFAIR" value="Resnet-50"></el-option>
                  <el-option label="data2" value="VGG16"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="上传模型">
                <el-upload
              class="upload-demo"
              action="https://jsonplaceholder.typicode.com/posts/"
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :before-remove="beforeRemove"
              multiple
              :limit="3"
              :on-exceed="handleExceed"
              :file-list="fileList">
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传zip/rar文件，且不超过50GB</div>
            </el-upload>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onSubmit">立即创建</el-button>
                <el-button>取消</el-button>
              </el-form-item>
            </el-form>
                  </el-dialog>
                  <el-dialog title="病例模板详情" :visible.sync = "showDataContent" >
                    <el-form ref="form" :model="detail" label-width="120px">
                      <el-form-item label="模板名称:">
                        {{detail.name}}
                      </el-form-item>
                      <el-form-item label="疾病场景">
                        {{detail.scenes}}
                      </el-form-item>
                      <el-form-item label="创建者">
                        {{detail.doctor}}
                      </el-form-item>
                      <el-form-item label="更新时间:">
                        {{detail.time}}
                      </el-form-item>
                                          <el-form-item label="模板内容">
                        {{detail.introduction}}
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="onSubmit">返回</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
              <el-divider></el-divider>
          <el-table
    :data="showBoardsList"
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
         <el-tag size="medium">{{ scope.row.doctor }}</el-tag>
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
          @click="showDetail(scope.$index)">详情</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="confirmDelete(scope.$index)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import ScientistMenu from '../ScientistMenu'
import TeacherImg from '../../../assets/img/teacher.png'
export default {
  name: 'ScientistBoard',
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
      teacherImg: TeacherImg,
      boards: [{
        id: '1',
        name: 'Transformer',
        doctor: '王医生',
        time: '2001-2-26 01:01:01',
        scenes: 'yyz',
        introduction: 'FBRNDataBases is used to Forward'
      }, {
        id: '1',
        name: 'Transformer',
        doctor: '王医生',
        time: '2001-2-26 01:01:01',
        scenes: 'yyz',
        introduction: 'FBRNDataBases is used to Forward'
      }],
      showBoardsList: [{
        id: '1',
        name: 'Transformer',
        doctor: '王医生',
        time: '2001-2-26 01:01:01',
        scenes: 'yyz',
        introduction: 'FBRNDataBases is used to Forward'
      }, {
        id: '1',
        name: 'Transformer',
        doctor: '王医生',
        time: '2001-2-26 01:01:01',
        scenes: 'yyz',
        introduction: 'FBRNDataBases is used to Forward'
      }],
      form: {
        name: '',
        introduction: '',
        scenes: '',
        type: '',
        data: ''
      },
      detail: {
        id: '1',
        name: 'Transformer',
        doctor: '王医生',
        time: '2001-2-26 01:01:01',
        scenes: 'yyz',
        introduction: 'FBRNDataBases is used to Forward'
      },
      buildThemeVisible: false,
      showDataContent: false,
      time: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  },
  methods: {
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.showBoardsList[row]
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

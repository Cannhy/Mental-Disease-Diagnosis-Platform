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
          <el-row>
            <el-col :span="24">
              <el-row>
                <el-col :span="18">
                  <el-input
                    placeholder="模型名称"
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
                    @click="buildThemeVisible = true">新建模型信息</el-button>
                  <el-dialog title="新建模型信息" :visible.sync = "buildThemeVisible" >
                    <el-form ref="form" :model="form" label-width="120px">
                      <el-form-item label="模型名称">
                        <el-input v-model="form.name"></el-input>
                      </el-form-item>
                      <el-form-item label="模型介绍">
                        <el-input v-model="form.introduction"></el-input>
                      </el-form-item>
                      <el-form-item label="模型类型">
                        <el-select v-model="form.type" placeholder="请选择疾病场景">
                          <el-option label="辅助诊断" value="辅助诊断"></el-option>
                          <el-option label="风险预测" value="风险预测"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="模型场景">
                        <el-select v-model="form.scenes" placeholder="请选择疾病场景">
                          <el-option label="抑郁症" value="抑郁症"></el-option>
                          <el-option label="阿尔兹海默症" value="阿尔兹海默症"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="关联数据集">
                        <el-select v-model="form.data" placeholder="请选择关联数据集">
                          <el-option label="ANDI dataset" value="ANDI dataset"></el-option>
                          <el-option label="FFAIR dataset" value="FFAIR dataset"></el-option>
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
                        <el-button type="primary" @click="uploadModel">立即创建</el-button>
                        <el-button @click="buildThemeVisible=false">取消</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                  <el-dialog title="模型详情" :visible.sync = "showDataContent" >
                    <el-form ref="form" :model="detail" label-width="120px">
                      <el-form-item label="模型名称:">
                        {{detail.name}}
                      </el-form-item>
                      <el-form-item label="更新时间:">
                        {{detail.time}}
                      </el-form-item>
                      <el-form-item label="模型介绍">
                        {{detail.introduction}}
                      </el-form-item>
                      <el-form-item label="支持场景">
                        {{detail.scenes}}
                      </el-form-item>
                      <el-form-item label="关联的数据集">
                        {{detail.data}}
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="showDataContent=false">返回</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
          <el-divider></el-divider>
          <el-table
            :data="models"
            :header-cell-style="{'text-align':'center'}"
            :cell-style="{'text-align':'center'}"
            style="width: 100%">
            <el-table-column
              label="模型名称"
              prop="name"
              width="180">
            </el-table-column>
            <el-table-column
              label="疾病场景&用途"
              width="180">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.scenes }}</el-tag>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="模型类型">
              <template slot-scope="scope">
                 <el-tag size="medium">{{ scope.row.type }}</el-tag>
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
                  v-if="userName===scope.row.ownerID"
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
import ScientistMenu from '../ScientistMenu'
export default {
  name: 'ScientistModel',
  components: {ScientistMenu},
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
      models: [{
        id: '1',
        name: 'Multi-modality Fusion Model',
        type: '辅助诊断',
        ownerID: '1',
        ownerName: '张三医生',
        time: '2021-12-26 01:01:01',
        scenes: '阿尔兹海默症',
        data: 'ANDI dataset',
        introduction: '深度多模态融合模块旨在自动捕获不完整多模态数据中每个个体的互补信息，LSTM捕捉数据中的长期依赖关系'
      }, {
        id: '2',
        name: 'S-GNN',
        type: '风险预测',
        ownerID: '2',
        ownerName: '李四医生',
        time: '2022-7-13 01:02:01',
        scenes: '抑郁者',
        data: 'ANDI dataset',
        introduction: 'SGNN具有自组织和自适应的能力，能够根据输入数据的统计特性来调整自身的结构和参数，从而实现对复杂数据的建模和处理'
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
        name: 'data1',
        ownerID: '2',
        ownerName: '王sa医生',
        time: '2001-2-26 01:01:01',
        size: '32MB',
        scenes: '抑郁症',
        introduction: 'FBRNDataBases is used to Backward'
      },
      buildThemeVisible: false,
      showDataContent: false,
      deleteDialogVisible: false,
      time: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getModelList()
  },
  methods: {
    uploadModel () {
      this.buildThemeVisible = false
      let that = this
      that.$http.request({
        url: that.$url + 'uploadModel/',
        method: 'get',
        params: {
          ownerID: that.userName,
          ownerName: that.nickName,
          name: that.form.name,
          introduction: that.form.introduction,
          scene: that.form.scenes,
          type: that.form.type,
          data: that.form.data
        }
      }).then(function (response) {
        that.getModelList()
      })
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
        url: that.$url + 'DeleteModel/',
        method: 'get',
        params: {
          modelID: that.models[that.curIndex].id
        }
      }).then(function (response) {
        that.getModelList()
      })
    },
    getModelList: function () {
      let that = this
      that.$http.request({
        url: that.$url + 'getModelList/',
        method: 'get'
      }).then(function (response) {
        that.models = response.data
      })
    },
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.models[row]
      this.showDataContent = true
    },
    showAddHomeworkDialog () {
      this.addHomeworkDialogVisible = true
    },
    clearAddHomeworkForm () {
      this.$refs.addHomeworkForm.resetFields()
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

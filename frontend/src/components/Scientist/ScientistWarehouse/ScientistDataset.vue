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
                <el-col :span=18>
                  <el-input
                    placeholder="查找数据集"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span=6>
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
                    @click="uploadDatasetVisible = true">上传数据集</el-button>
                    <el-dialog title="上传数据集" :visible.sync = "uploadDatasetVisible" >
                      <el-form ref="form" :model="uploadForm" label-width="120px">
                        <el-form-item label="数据集名称">
                          <el-input v-model="uploadForm.name"></el-input>
                        </el-form-item>
                        <el-form-item label="数据集简介">
                          <el-input v-model="uploadForm.introduction"></el-input>
                        </el-form-item>
                        <el-form-item label="疾病场景">
                          <el-select v-model="uploadForm.scenes" placeholder="请选择疾病场景">
                            <el-option label="抑郁症" value="抑郁症"></el-option>
                            <el-option label="阿尔兹海默症" value="阿尔兹海默症"></el-option>
                          </el-select>
                        </el-form-item>
                        <el-form-item label="关联模型">
                          <el-select v-model="uploadForm.model" placeholder="请选择关联模型">
                            <el-option label="Multi-modality Fusion" value="Multi-modality Fusion"></el-option>
                            <el-option label="LSTM" value="LSTM"></el-option>
                            <el-option label="Transformer" value="Transformer"></el-option>
                          </el-select>
                        </el-form-item>
                    <!--  <el-form-item label="活动性质">-->
                    <!--    <el-checkbox-group v-model="form.type">-->
                    <!--      <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>-->
                    <!--      <el-checkbox label="地推活动" name="type"></el-checkbox>-->
                    <!--      <el-checkbox label="线下主题活动" name="type"></el-checkbox>-->
                    <!--      <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>-->
                    <!--    </el-checkbox-group>-->
                    <!--  </el-form-item>-->
                        <el-form-item label="选择数据集文件">
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
                          <el-button type="primary" @click="uploadSubmit">立即创建</el-button>
                          <el-button @click="uploadBack">取消</el-button>
                        </el-form-item>
                      </el-form>
                    </el-dialog>
                  <el-dialog title="数据集详情" :visible.sync = "showDatasetDetail" >
                      <el-form ref="form" :model="detail" label-width="120px">
                        <el-form-item label="数据集名称:">
                          {{detail.name}}
                        </el-form-item>
                        <el-form-item label="发布者:">
                          {{detail.ownerName}}
                        </el-form-item>
                        <el-form-item label="发布时间:">
                          {{detail.time}}
                        </el-form-item>
                        <el-form-item label="数据集简介">
                          {{detail.introduction}}
                        </el-form-item>
                        <el-form-item label="疾病场景">
                          {{detail.scenes}}
                        </el-form-item>
                        <el-form-item label="支持模型">
                          {{detail.scenes}}
                        </el-form-item>
                        <el-form-item>
                          <el-button type="primary" @click="detailBack">返回</el-button>
                        </el-form-item>
                      </el-form>
                  </el-dialog>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
          <el-row type="flex" alig="middle" justify="center">
            <el-col span="18">数据集信息</el-col>
            <el-col span="3" style="text-align: left;">疾病场景</el-col>
            <el-col  span="3" style="text-align: center">操作</el-col>
          </el-row>
          <el-divider></el-divider>
            <el-card v-for="(data, index) in datas" :key="index"
                     style="margin-bottom: 2%">
              <el-col span=18>
                <el-row class="clearfix" style="font-size: 20px; margin-bottom: 15px">
                  {{data.name}}
                </el-row>
                <el-row style="margin-bottom: 20px;">
                  <i class="el-icon-user" style="margin-right: 20px">{{data.ownerName}}</i>
                  <i class="el-icon-time" style="margin-right: 20px">{{data.time}}</i>
                  <i class="el-icon-folder" style="margin-right: 20px">{{data.size}}</i>
                </el-row>
                <el-row style="margin-bottom: 20px;">{{data.introduction}}</el-row>
              </el-col>
              <el-col span=3 justify-content="center" >
                <div style="margin-top: 25px">{{data.scenes}}</div>
              </el-col>
              <el-col span=3>
                <el-row>
                  <el-button @click="showDetail(index)" size="small" type="success" style="margin-top: 10px; margin-left: 40px">详情</el-button>
                </el-row>
                 <el-row>
                  <el-button v-if="userName === data.ownerID" @click="confirmDialogDelete(index)" size="small" type="danger" style="margin-top: 10px; margin-left: 40px">删除</el-button>
                </el-row>
              </el-col>
              <el-dialog
                :visible.sync="deleteDialogVisible"
                title="确认删除"
                width="30%">
                <span>确定要删除吗？</span>
                <span slot="footer" class="dialog-footer">
                  <el-button type="primary" @click="confirmDelete">确认</el-button>
                  <el-button @click="cancelDelete">取消</el-button>
                </span>
              </el-dialog>
            </el-card>
        </el-main>
      </el-container>
    </el-container>
</template>

<script>
import ScientistMenu from '../ScientistMenu'
export default {
  name: 'ScientistDataset',
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
      datas: [{
        id: '1',
        name: 'ANDI dataset',
        ownerName: '数据集拥有者1号',
        ownerID: '1',
        time: '2021-2-26 01:01:01',
        size: '10.15GB',
        scenes: '阿尔兹海默症',
        introduction: '包含MRI，PET，人口统计学数据和四种认知分数'
      }, {
        id: '1',
        name: 'FFAIR dataset',
        ownerName: '数据集拥有者2号',
        ownerID: '1',
        time: '2022-1-23 01:01:01',
        size: '6GB',
        scenes: '抑郁症',
        introduction: '包含4800名健康和患病者的核磁共振图像'
      }],
      uploadForm: {
        name: '',
        introduction: '',
        scenes: '',
        model: ''
      },
      detail: {
        id: '1',
        name: 'data1',
        ownerName: '数据集拥有者1号',
        ownerID: '1',
        time: '2001-2-26 01:01:01',
        size: '32MB',
        scenes: '抑郁症',
        introduction: 'FBRNDataBases is used to Backward'
      },
      uploadDatasetVisible: false,
      showDatasetDetail: false,
      deleteDialogVisible: false,
      curIndex: 0,
      time: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    this.getDatasetList()
  },
  methods: {
    getDatasetList: function () {
      let that = this
      that.$http.request({
        url: that.$url + 'getDatasetList/',
        method: 'get'
      }).then(function (response) {
        that.datas = response.data
      })
    },
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.datas[row]
      this.showDatasetDetail = true
    },
    detailBack () {
      this.showDatasetDetail = false
    },
    confirmDialogDelete (row) {
      this.deleteDialogVisible = true
      this.curIndex = row
    },
    cancelDelete () {
      this.deleteDialogVisible = false
    },
    confirmDelete () {
      this.deleteDialogVisible = false
      let that = this
      console.log(that.curIndex)
      that.$http.request({
        url: that.$url + 'DeleteDataset/',
        method: 'get',
        params: {
          datasetID: that.datas[that.curIndex].id
        }
      }).then(function (response) {
        that.getDatasetList()
      })
    },
    uploadSubmit: function () {
      let that = this
      that.$http.request({
        url: that.$url + 'uploadDataset/',
        method: 'get',
        params: {
          name: that.uploadForm.name,
          introduction: that.uploadForm.introduction,
          scene: that.uploadForm.scenes,
          model: that.uploadForm.model,
          ownerName: that.nickName,
          ownerID: that.userName
        }
      }).then(function (response) {
        that.getDatasetList()
      })
      that.uploadDatasetVisible = false
    },
    uploadBack () {
      this.uploadDatasetVisible = false
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

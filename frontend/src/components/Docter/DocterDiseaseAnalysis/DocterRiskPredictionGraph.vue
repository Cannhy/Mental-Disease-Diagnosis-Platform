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
        <el-main style="" class="main">
          <el-form ref="form" :model="detail" label-width="120px">
            <el-col :span="12">
                      <el-form-item label="任务简介:">
                        {{detail.introduction}}
                      </el-form-item>
              </el-col>
            <el-col :span="12">
                      <el-form-item label="疾病场景:">
                        {{detail.scene}}
                      </el-form-item>
              </el-col>
            <el-form-item style="display: flex; justify-content: flex-end;">
                        <el-button type="primary" @click="onSubmit">返回</el-button>
                      </el-form-item>
<!--            <el-col :span="8">-->
<!--                      <el-form-item label="数据集:">-->
<!--                        {{detail.data}}-->
<!--                      </el-form-item>-->
<!--            </el-col>-->
                      <el-form-item label="风险预测:">
                        {{detail.risk}}
                      </el-form-item>
                    </el-form>
          <el-divider></el-divider>
          <div id="chart" style="width: 1000px; height: 500px; margin-left: 40px"></div>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import DocterMenu from '../DocterMenu'
import * as echarts from 'echarts'
export default {
  name: 'DocterRiskPrediction',
  components: {DocterMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      nickName: '',
      detail: {
        id: '2',
        name: 'AD Diagnasdosis',
        state: '未完成asdsad',
        time: '2001-2-26 01:01:01',
        introduction: 'asdwa',
        scene: 'AD',
        data: 'asd',
        risk: '有进入阿尔兹海默症中期的风险',
        model: 'VGG16'
      }
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.nickName = this.cookie.getCookie('nickName')
    console.log(this.$route.query.detail)
    this.detail = this.$route.query.detail
    console.log(this.detail)
    this.initChart()
  },
  methods: {
    initChart () {
      const chart = echarts.init(document.getElementById('chart'))
      const months = []
      const barColors = ['#fe4f4f', '#fead33', '#feca2b', '#fef728', '#c5ee4a', '#87ee4a', '#46eda9', '#47e4ed', '#4bbbee', '#7646d8',
        '#924ae2', '#C6E579', '#F4E001', '#F0805A', '#26C0C0'
      ]
      for (let i = 1; i <= 15; i++) {
        months.push('未来' + i + '月')
        // barColors.push('#' + (Math.random().toString(16) + '000000').substring(2, 8))
      }
      // 生成柱状图的 y 轴数据，即风险百分比（0-100%之间的随机数）
      const barData = []
      for (let i = 0; i < 15; i++) {
        barData.push(Math.floor(Math.random() * 101)) // 生成 0-100 之间的随机数
      }

      // 生成折线图的 y 轴数据，即另一种风险百分比（0-100%之间的随机数）
      const lineData = []
      for (let i = 0; i < 15; i++) {
        lineData.push(Math.floor(Math.random() * 101)) // 生成 0-100 之间的随机数
      }

      // 配置项
      const option = {
        title: {
          text: '风险预测'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: {
          type: 'category',
          data: months
        },
        yAxis: [
          {
            type: 'value',
            name: 'Predict1',
            position: 'left',
            axisLabel: {
              formatter: '{value}%'
            }
          },
          {
            type: 'value',
            name: 'Predict2',
            position: 'right',
            axisLabel: {
              formatter: '{value}%'
            }
          }
        ],
        series: [
          {
            name: '柱状图',
            type: 'bar',
            data: barData,
            itemStyle: {
              color: function (params) {
                return barColors[params.dataIndex] // 每个柱子的颜色
              }
            }
          },
          {
            name: '折线图',
            type: 'line',
            yAxisIndex: 1,
            data: lineData
          }
        ]
      }
      chart.setOption(option)
    },
    TaskSubmit () {
      this.buildThemeVisible = false
    },
    onSubmit () {
      this.$router.push({
        name: 'DocterRiskPrediction'
      })
    },
    beforeHandleCommand (rowIndex, ope) {
      return {
        row: rowIndex,
        ope: ope
      }
    },
    showDetail (row) {
    // 将当前行的内容传递给修改的数据对象
      this.detail = this.showTasksList[row]
      this.showDataContent = true
      this.initChart()
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
      this.cookie.clearCookie('nickName')
      this.$router.replace('/')
    },
    handleCommand: function (command) {
      this.goToHelloWorld()
    },
    handleCommand2: function (command) {
      if (command.ope === 'a') {
        this.showDetail(command.row)
      } else {
        this.showDetail(command.row)
      }
    }
  }
}
</script>

<style scoped>
@import "../../../assets/css/back.css";
</style>
<style scoped>
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
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
<style scoped>
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }
</style>

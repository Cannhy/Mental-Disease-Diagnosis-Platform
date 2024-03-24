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
        <el-main style="" class="main">
          <el-form ref="form" :model="detail" label-width="120px">
<!--            <el-col :span="12">-->
<!--                      <el-form-item label="任务名称:">-->
<!--                        {{detail.name}}-->
<!--                      </el-form-item>-->
<!--              </el-col>-->
<!--            <el-col :span="12">-->
<!--                      <el-form-item label="任务简介:">-->
<!--                        {{detail.introduction}}-->
<!--                      </el-form-item>-->
<!--              </el-col>-->
<!--            <el-col :span="8">-->
<!--                      <el-form-item label="疾病场景:">-->
<!--                        {{detail.scene}}-->
<!--                      </el-form-item>-->
<!--              </el-col>-->
            <el-col :span="6">
                      <el-form-item label="数据集:">
                        {{detail.data}}
                      </el-form-item>
            </el-col>
            <el-col :span="8">
                      <el-form-item label="风险预测模型:">
                        {{detail.model}}
                      </el-form-item>
            </el-col>
                      <el-form-item style="display: flex; justify-content: flex-end;">
                        <el-button type="primary" @click="onSubmit">返回</el-button>
                      </el-form-item>
                    </el-form>
            <el-divider></el-divider>
          <el-col span="12">
          <div id="chart" style="width: 550px; height: 450px;"></div>
            </el-col>
          <el-col span="12"><div id="chart2" style="width: 550px; height: 450px;"></div></el-col>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import ScientistMenu from '../ScientistMenu'
import * as echarts from 'echarts'
export default {
  name: 'ScientistRiskPredictionGraph',
  components: {ScientistMenu},
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
    this.initPieChart()
  },
  methods: {
    initPieChart () {
      const pieChart = echarts.init(document.getElementById('chart2'))
      const legendData = ['GRU-ModelF', 'LSTM-T', 'MinimalRNN', 'Yours']
      const pieData = [
        {value: 0.0671, name: 'GRU-ModelF', itemStyle: { color: '#ff002f' }},
        {value: 0.0815, name: 'LSTM-T', itemStyle: { color: '#79bce5' }},
        { value: 0.2152, name: 'MinimalRNN', itemStyle: { color: 'rgba(198,229,121,0.72)' } },
        {value: 0.0466, name: 'Yours', itemStyle: {color: '#fead33'}}
      ]
      // '#fe4f4f', '#fead33', '#feca2b', '#fef728', '#c5ee4a', '#87ee4a', '#46eda9', '#47e4ed', '#4bbbee', '#7646d8',
      // '#924ae2', '#C6E579', '#F4E001', '#F0805A', '#26C0C0'
      const option = {
        title: {
          text: 'MAE for MRI',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: legendData
        },
        series: [
          {
            name: 'MAE',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: pieData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      pieChart.setOption(option)
    },
    initChart () {
      const chart = echarts.init(document.getElementById('chart'))
      const months = ['GRU-ModelF', 'LSTM-T', 'MinimalRNN', 'Yours']
      const barColors = ['#fe4f4f', '#fead33', '#feca2b', '#fef728', '#c5ee4a', '#87ee4a', '#46eda9', '#47e4ed', '#4bbbee', '#7646d8',
        '#924ae2', '#C6E579', '#F4E001', '#F0805A', '#26C0C0'
      ]
      // for (let i = 1; i <= 15; i++) {
      //   months.push('未来' + i + '月')
      //   // barColors.push('#' + (Math.random().toString(16) + '000000').substring(2, 8))
      // }
      // 生成柱状图的 y 轴数据，即风险百分比（0-100%之间的随机数）
      const barData = [0.0671, 0.0815, 0.2152, 0.0466]
      // for (let i = 0; i < 15; i++) {
      //   barData.push(Math.floor(Math.random() * 101)) // 生成 0-100 之间的随机数
      // }

      // 生成折线图的 y 轴数据，即另一种风险百分比（0-100%之间的随机数）
      const lineData = [0.0806, 0.0930, 0.3143, 0.0606]
      // for (let i = 0; i < 15; i++) {
      //   lineData.push(Math.floor(Math.random() * 101)) // 生成 0-100 之间的随机数
      // }

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
            name: 'MRI',
            position: 'left',
            axisLabel: {
              formatter: '{value}%'
            }
          },
          {
            type: 'value',
            name: 'PET',
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
            barWidth: '50%',
            itemStyle: {
              color: function (params) {
                return barColors[params.dataIndex + 6] // 每个柱子的颜色
              }
            },
            markPoint: {
              data: [
                { type: 'max', name: '最大值', itemStyle: { color: '#ffa600' } },
                { type: 'min', name: '最小值', itemStyle: { color: '#a4e4fd' } }
              ]
            },
            markLine: {
              data: [
                {type: 'average', name: '平均值', itemStyle: { color: 'rgba(255,255,255,0.87)' }}
              ]
            }
          },
          {
            name: '折线图',
            type: 'line',
            yAxisIndex: 1,
            data: lineData,
            itemStyle: {
              color: function (params) {
                return barColors[params.dataIndex] // 每个柱子的颜色
              }
            },
            lineStyle: {
              color: '#fe4f4f' // 设置线的颜色为红色
            }
          }
        ]
      }
      chart.setOption(option)
    },
    drawManyBar (container, titleName, legendData, xData, seriesDatas, seriess) {
      var ticket = echarts.init(document.getElementById(container))
      var ticketOption = {
      // 标题样式
        title: {
          text: titleName,
          textStyle: {
            color: 'black'
          },
          left: 'left'
        },
        // 提示框
        tooltip: {
          trigger: 'axis',
          backgroundColor: 'gray',
          axisPointer: {
            type: 'shadow'
          },
          // 提示信息格式，支持html样式
          formatter: function (params) {
            var res = '<div style="color:#00C7FF">'
            res += '<strong>' + params[0].name + '</strong>'
            for (var i = 0, l = params.length; i < l; i++) {
              res += '<br/>' + ((i === 4) ? '&nbsp;&nbsp;' : '') +
              params[i].seriesName + ' : ' +
                (params[i].value * 100).toFixed(2) + '%'
            }
            res += '</div>'
            return res
          }
        },
        // 菜单
        legend: [{
        // 菜单字体样式
          textStyle: {
            color: 'black'
          },
          // 菜单位置
          x: 'right', // 将图例水平居中显示
          y: 'top', // 将图例放置在底部
          // 菜单数据
          data: legendData.slice(7, 15)
        }, {
        // 菜单字体样式
          textStyle: {
            color: 'black'
          },
          // 菜单位置
          x: 'right', // 将图例水平居中显示
          y: '6.5%', // 将图例放置在底部
          // 菜单数据
          data: legendData.slice(0, 7)
        }
        ],

        xAxis: [{
          type: 'category',
          axisLine: {
            show: true,
            // x轴线样式
            lineStyle: {
              color: '#17273B',
              width: 1,
              type: 'solid'
            }
          },
          // x轴字体设置
          axisLabel: {
            show: true,
            fontSize: 12,
            color: 'black'
          },
          data: xData
        }],
        yAxis: [{
          type: 'value',
          // y轴字体设置
          axisLabel: {
            show: true,
            color: 'black',
            fontSize: 12,
            formatter: function (value) {
              return value * 100 + '%'
            }
          },
          // y轴线设置不显示
          axisLine: {
            show: true
          },
          // 与x轴平行的线样式
          splitLine: {
            show: true,
            lineStyle: {
              color: '#17273B',
              width: 1,
              type: 'dashd'
            }
          }
        }
        ],
        series: seriess
      }
      ticket.setOption(ticketOption)
    },
    initChart1 () {
      var titleName = '性能比较-MAE'
      var seriess = []
      const barColors = ['#fe4f4f', '#fead33', '#feca2b', '#fef728', '#c5ee4a', '#87ee4a', '#46eda9', '#47e4ed', '#4bbbee', '#7646d8', '#924ae2', '#C6E579', '#F4E001', '#F0805A', '#26C0C0']
      var legendData = ['Lasso-MeanF', 'Lasso-FF', 'Lasso-LF', 'SVR-MeanF', 'SVR-FF', 'SVR-LF', 'GRU-MeanF', 'GRU-FF', 'GRU-LF', 'GRU-ModelF', 'cFSGL', 'LSTM-P', 'LSTM-T', 'MinimalRNN', 'Yours']
      var xData = [ 'MMSE', 'CDRG', 'CDRS', 'ADAS' ]
      var seriesDatas = [[ 2.2171, 0.3223, 1.6372, 6.6206 ], [ 2.9151, 0.3268, 1.6794, 7.0454 ], [ 2.2819, 0.3350, 1.6860, 6.7834 ], [ 3.0900, 0.3724, 2.0465, 7.8284 ], [ 3.0720, 0.3729, 2.0569, 7.8026 ], [ 2.8494, 0.3655, 2.0338, 7.4960 ], [ 2.2153, 0.2882, 1.4917, 6.1111 ], [ 2.2028, 0.2882, 1.4969, 6.1786 ], [ 2.2602, 0.3024, 1.5221, 6.1002 ], [ 2.1786, 0.2848, 1.3929, 6.1422 ], [ 2.7392, 0.3882, 2.1472, 7.6065 ], [ 2.5492, 0.3457, 1.8175, 7.5018 ], [ 4.5031, 0.3576, 1.9734, 17.810 ], [ 4.5600, 0.3556, 2.1074, 9.2416 ], [ 2.1373, 0.2753, 1.3560, 5.8689 ]]
      for (let i = 0; i < 4; i++) {
        let sum = 0
        for (let j = 0; j < 15; j++) {
          sum += seriesDatas[j][i]
        }
        for (let j = 0; j < 15; j++) {
          seriesDatas[j][i] = (seriesDatas[j][i] / sum)
        }
      }
      for (let i = 0; i < 15; i++) {
        seriess.push({
          name: legendData[i],
          type: 'bar',
          barWidth: 8,
          yAxisIndex: 0,
          itemStyle: {
            color: barColors[i],
            barBorderRadius: [30, 30, 0, 0]
          },
          data: seriesDatas[i]
        })
      }
      this.drawManyBar('chart', titleName, legendData, xData, seriesDatas, seriess)
      console.log(seriess)
      // const chart = echarts.init(document.getElementById('chart'))
      // const months = ['Lasso-MeanF', 'Lasso-FF', 'Lasso-LF', 'SVR-MeanF', 'SVR-FF', 'SVR-LF',
      //   'GRU-MeanF', 'GRU-FF', 'GRU-LF', 'GRU-ModelF', 'cFSGL', 'LSTM-P', 'LSTM-T', 'MinimalRNN', 'Yours']
      // const barColors = ['#fe4f4f', '#fead33', '#feca2b', '#fef728', '#c5ee4a', '#87ee4a', '#46eda9', '#47e4ed', '#4bbbee', '#7646d8',
      //   '#924ae2', '#C6E579', '#F4E001', '#F0805A', '#26C0C0'
      // ]
      // // for (let i = 1; i <= 15; i++) {
      // //   months.push('未来' + i + '月')
      // //   // barColors.push('#' + (Math.random().toString(16) + '000000').substring(2, 8))
      // // }
      // // 生成柱状图的 y 轴数据，即风险百分比（0-100%之间的随机数）
      // const barData = []
      // for (let i = 0; i < 15; i++) {
      //   barData.push(Math.floor(Math.random() * 101)) // 生成 0-100 之间的随机数
      // }
      //
      // // 生成折线图的 y 轴数据，即另一种风险百分比（0-100%之间的随机数）
      // const lineData = []
      // for (let i = 0; i < 15; i++) {
      //   lineData.push(Math.floor(Math.random() * 101)) // 生成 0-100 之间的随机数
      // }
      //
      // // 配置项
      // const option = {
      //   tooltip: {
      //     trigger: 'axis',
      //     axisPointer: {
      //       type: 'cross'
      //     }
      //   },
      //   xAxis: {
      //     type: 'category',
      //     data: months,
      //     axisLabel: {
      //       interval: 0, // 强制显示所有刻度标签,
      //       rotate: 30
      //     }
      //   },
      //   yAxis: [
      //     {
      //       type: 'value',
      //       name: 'Predict1',
      //       position: 'left',
      //       axisLabel: {
      //         formatter: '{value}%'
      //       }
      //     },
      //     {
      //       type: 'value',
      //       name: 'Predict2',
      //       position: 'right',
      //       axisLabel: {
      //         formatter: '{value}%'
      //       }
      //     }
      //   ],
      //   series: [
      //     {
      //       name: '柱状图',
      //       type: 'bar',
      //       data: barData,
      //       itemStyle: {
      //         color: function (params) {
      //           return barColors[params.dataIndex] // 每个柱子的颜色
      //         }
      //       }
      //     },
      //     {
      //       name: '折线图',
      //       type: 'line',
      //       yAxisIndex: 1,
      //       data: lineData
      //     }
      //   ]
      // }
      // chart.setOption(option)
    },
    TaskSubmit () {
      this.buildThemeVisible = false
    },
    onSubmit () {
      this.$router.push({
        name: 'ScientistRiskPrediction'
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
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
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

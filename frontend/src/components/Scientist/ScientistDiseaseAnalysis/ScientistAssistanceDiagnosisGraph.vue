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
                      <el-form-item label="诊断模型:">
                        {{detail.model}}
                      </el-form-item>
            </el-col>
<!--            <el-col :span="24">-->
<!--                      <el-form-item >-->
<!--                          <div id="chart" style="width: 1200px; height: 500px;"></div>-->
<!--                      </el-form-item>-->
<!--              </el-col>-->
                      <el-form-item style="display: flex; justify-content: flex-end;">
                        <el-button type="primary" @click="onSubmit">返回</el-button>
                      </el-form-item>
                    </el-form>
          <div style="margin-left: 20px">下图展示了您选择的模型在四种认知分数上预测的平均绝对误差(MAE)和加权相关系数(wR),以及与其他模型的比较情况
            <br>点击相应认知分数即可查看该分数的详细情况
          <br>MAE相对越小、wR相对越大则说明您的模型性能更好</div>
          <el-divider></el-divider>
          <div id="chart" style="width: 1100px; height: 325px;"></div>
          <div id="chart2" style="width: 1100px; height: 325px;"></div>
        </el-main>
</el-container>
    </el-container>

</template>

<script>
import ScientistMenu from '../ScientistMenu'
import * as echarts from 'echarts'
export default {
  name: 'ScientistAssistanceDiagnosisGraph',
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
    this.initChart1()
    this.initChart2()
  },
  methods: {
    drawManyBar (container, titleName, legendData, xData, seriesDatas, seriess, maxy) {
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
            var maxX = -Infinity
            var maxP = 0
            var minP = 0
            var minX = Infinity
            for (var i = 0, l = params.length; i < l; i++) {
              if (maxX < params[i].value) {
                maxP = i
              }
              if (minX > params[i].value) {
                minP = i
              }
              maxX = Math.max(maxX, params[i].value)
              minX = Math.min(minX, params[i].value)
              // res += '<br/>' +
              // params[i].seriesName + ' : ' +
              //   (params[i].value * 100).toFixed(2) + '%'
            }
            res += '<br/>' + 'Max : ' + params[maxP].seriesName
            res += '<br/>' + 'MaxValue : ' + (params[maxP].value * 100).toFixed(2) + '%'
            res += '<br/>' + 'Min : ' + params[minP].seriesName
            res += '<br/>' + 'MinValue : ' + (params[minP].value * 100).toFixed(2) + '%'
            res += '<br/>' + 'YoursValue : ' + (params[14].value * 100).toFixed(2) + '%'
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
          max: maxy,
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
      this.drawManyBar('chart', titleName, legendData, xData, seriesDatas, seriess, 0.16)
      console.log(seriess)
    },
    initChart2 () {
      var titleName = '性能比较-wR'
      var seriess = []
      const barColors = ['#fe4f4f', '#fead33', '#feca2b', '#fef728', '#c5ee4a', '#87ee4a', '#46eda9', '#47e4ed', '#4bbbee', '#7646d8', '#924ae2', '#C6E579', '#F4E001', '#F0805A', '#26C0C0']
      var legendData = ['Lasso-MeanF', 'Lasso-FF', 'Lasso-LF', 'SVR-MeanF', 'SVR-FF', 'SVR-LF', 'GRU-MeanF', 'GRU-FF', 'GRU-LF', 'GRU-ModelF', 'cFSGL', 'LSTM-P', 'LSTM-T', 'MinimalRNN', 'Yours']
      var xData = [ 'MMSE', 'CDRG', 'CDRS', 'ADAS' ]
      var seriesDatas = [[ 0.7795, 0.7076, 0.7613, 0.6796 ], [ 0.6858, 0.6979, 0.7459, 0.6500 ], [ 0.7674, 0.6778, 0.7540, 0.6685 ], [ 0.5776, 0.5755, 0.6528, 0.5941 ], [ 0.5847, 0.5732, 0.6455, 0.5944 ], [ 0.6320, 0.5908, 0.6536, 0.6233 ], [ 0.7612, 0.7160, 0.7879, 0.7060 ], [ 0.7633, 0.7182, 0.7901, 0.6985 ], [ 0.7615, 0.7025, 0.7871, 0.7117 ], [ 0.7559, 0.7264, 0.7884, 0.6825 ], [ 0.6969, 0.5526, 0.6207, 0.6209 ], [ 0.7449, 0.6862, 0.7309, 0.6364 ], [0.6599, 0.6527, 0.6841, 0.6654], [ 0.5963, 0.5112, 0.5909, 0.5224 ], [ 0.7620, 0.7415, 0.7979, 0.7249 ]]
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
      this.drawManyBar('chart2', titleName, legendData, xData, seriesDatas, seriess, 0.15)
      console.log(seriess)
    },
    TaskSubmit () {
      this.buildThemeVisible = false
    },
    onSubmit () {
      this.$router.push({
        name: 'ScientistAssistanceDiagnosis'
      })
    },
    beforeHandleCommand (rowIndex, ope) {
      return {
        row: rowIndex,
        ope: ope
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

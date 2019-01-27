<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div>
    <h2>自动化测试报告</h2>
    <div id="BarColumn" style="width: 600px;height: 400px;float:left"></div>
    <div id="main" style="width: 600px;height: 400px;float:right"></div>
    <div id="select_time" style="width: 100%;height: 400px;float:left">
      <el-select v-model="time" @change="search_report">
        <el-option v-for="item in reports" :key="item.test_time"
                   :value="item.test_time">{{item.test_time}}
        </el-option>
      </el-select>
      <el-table :data="select_time_list" style="margin-top: 20px;width: 100%"
                stripe>
        <!--<el-table-column type="expand">-->
          <!--<template slot-scope="'props">-->
            <!--<el-form label-position="left" inline class="demo-table-expand">-->
              <!--<el-form-item label="用例名称"><span>{{props.row.case_name}}</span>-->
              <!--</el-form-item>-->
              <!--<el-form-item label="接口地址"><span>{{props.row.request_url}}</span>-->
              <!--</el-form-item>-->
              <!--<el-form-item label="请求方式"><span>{{props.row.request_type}}</span>-->
                <!--<el-form-item label="测试结果">-->
                  <!--<span>{{props.row.case_result}}</span></el-form-item>-->
                <!--<el-form-item label="请求参数">-->
                  <!--<span>{{props.row.request_param}}</span></el-form-item>-->
                <!--<el-form-item label="返回结果">-->
                  <!--<span>{{props.row.return_result}}</span></el-form-item>-->
              <!--</el-form-item>-->
            <!--</el-form>-->
          <!--</template>-->
        <!--</el-table-column>-->
      <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="用例名称:">
            <span>{{ props.row.case_name }}</span>
          </el-form-item>
          <el-form-item label="请求方式:" style="padding-left: 30%">
            <span>{{ props.row.request_type }}</span>
          </el-form-item>
          <br>
          <el-form-item label="接口地址:">
            <span>{{ props.row.request_url }}</span>
            <br>
          </el-form-item>
          <el-form-item label="测试结果:" style="padding-left: 15%">
            <span>{{ props.row.result }}</span>
          </el-form-item>
          <br>
          <el-form-item label="请求参数:">
            <span>{{ props.row.request_param }}</span>
          </el-form-item>
          <el-form-item label="返回结果:">
            <span>{{ props.row.case_result }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
        <el-table-column prop="case_name" label="用例名称"></el-table-column>
        <el-table-column prop="request_url" label="请求地址"></el-table-column>
        <el-table-column prop="result" label="用例执行结果"></el-table-column>
      </el-table>
    </div>
  </div>


</template>
<script>
  import echarts from 'echarts'

  export default {
    name: 'report',
    data() {
      return {
        charts: '',
        report_result: '',
        opinion: ['成功', '失败'],
        opinionData: [
          {value: 0, name: '成功'},
          {value: 0, name: '失败'},

        ],
        pass_number: 0,
        fail_number: 0,
        option: '',
        select_time_list: [],
        time: '',
        reports: [],
        status_list: [],
        case_name: '',
        request_url: ''
      }

    },
    methods: {
      // 获取用例执行情况的柱状图、饼图
      getreport() {
        this.$axios.get('case_report/').then((res) => {
          this.report_result = res.data.results;
          this.report_result.forEach(v => {
            // console.log(v.pass_number)
            console.log(this.opinionData[0]);
            this.opinionData[0].value = v.pass_number;
            this.opinionData[1].value = v.fail_number;
            this.pass_number = v.pass_number;
            this.fail_number = v.fail_number;
            this.$nextTick(function () {
              this.barcolumn('BarColumn')
            });
            this.$nextTick(function () {
              this.drawPie('main')
            });
          })


        })
      },
      // 获取最近一次运行的用例
      get_time_report() {
        this.$axios.get('get_detail_report/').then((res) => {
          console.log(res);
          this.select_time_list = res.data.results

        }).catch((err) => {
          console.log(err)
        })

      },
      // 获取前十次运行用例的时间
      get_reports() {
        this.$axios.get('get_report/').then((res) => {
          this.reports = res.data.results;
          // this.time = res.data.results[0]

        }).catch((err) => {
          console.log(err)
        })
      },
      // 根据运行用例日期搜索用例
      search_report() {
        this.$axios.get('search_report/', {
          params: {
            search: this.time
          }
        }).then((res) => {
          this.select_time_list = res.data.results;
          this.search_reports()
        }).catch((err) => {
          console.log(err)
        })
      },
      // 根据运行用例时间实时绘制柱状图、饼图
      search_reports() {
        this.$axios.get('search_reports/', {
          params: {
            search: this.time
          }
        }).then((res) => {
          // 绘制柱状图、饼图
          this.status_list = res.data.results;
          this.status_list.forEach(v => {
            // console.log(v.pass_number)
            console.log(this.opinionData[0]);
            this.opinionData[0].value = v.pass_number;
            this.opinionData[1].value = v.fail_number;
            this.pass_number = v.pass_number;
            this.fail_number = v.fail_number;
            this.$nextTick(function () {
              this.barcolumn('BarColumn')
            });
            this.$nextTick(function () {
              this.drawPie('main')
            });
          })
        }).catch((err) => {
          console.log(err)
        })
      },
      // 绘制饼图
      drawPie(id) {
        this.charts = echarts.init(document.getElementById(id))
        this.charts.setOption({
          tooltip: {
            trigger: 'item',
            formatter: '{a}<br/>{b}:{c} ({d}%)'
          },
          color: ["#32CD32", "red"],
          legend: {
            orient: 'vertical',
            x: 'left',
            data: this.opinion
          },
          series: [
            {
              name: '用例执行状态',
              type: 'pie',
              radius: ['50%', '70%'],
              avoidLabelOverlap: false,
              label: {
                normal: {
                  show: false,
                  position: 'center'
                },
                emphasis: {
                  show: true,
                  textStyle: {
                    fontSize: '30',
                    fontWeight: 'blod'
                  }
                }
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              data: this.opinionData
            }
          ]
        })
      },
      // 绘制柱状图
      barcolumn(id) {
        app.title = '坐标轴刻度与标签对齐';

        this.charts = echarts.init(document.getElementById(id))
        this.charts.setOption({
          color: ["#32CD32", "red"],
          tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              data: ['成功', '失败'],
              axisTick: {
                alignWithLabel: true
              }
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: [
            {
              name: '用例状态',
              type: 'bar',
              barWidth: '60%',
              data: [this.pass_number, this.fail_number]
            }
          ]
        });

      }

    },
    //调用
    mounted() {
      this.getreport();
      this.get_time_report();
      this.get_reports();


    },

  }
</script>
<style scoped>
  * {
    margin: 0;
    padding: 0;
    list-style: none;
  }
</style>

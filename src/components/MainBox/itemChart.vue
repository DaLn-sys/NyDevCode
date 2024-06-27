<template>
    <div>
        <div ref="chart" style=" height: 600px;margin-top: 0px;margin-bottom: 20px;"></div>
        
    </div>
</template>
<script setup>
import {ref,reactive,onMounted} from 'vue'
import *as echarts from 'echarts'

const chart = ref ();
onMounted(()=>{
    fn ();
})

function fn(){
    var myChart = echarts.init(chart.value);
    var option = {
        title: {
          text: '本周耗能表'
        },
        tooltip: {},
        legend: {
          data: ['耗能量']
        },
        xAxis: {
          data: ['周一', '周二', '周三', '周四', '周五', '周六','周日']
        },
        yAxis: {},
        series: [
          {
            name: '耗能量',
            type: 'bar',
            data: [45, 60, 20, 88, 50, 66,30]
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
}



</script>

<style lang="scss" scoped>


</style>
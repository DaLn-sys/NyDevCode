<template>

    <div>

      <el-row :gutter="16">
    <el-col :span="8">
      <div class="statistic-card">
        <el-statistic :value="5">
          <template #title>
            <div style="display: inline-flex; align-items: center">
              设备数量
              <el-tooltip
                effect="dark"
                content="已添加的所有用电设备的总数"
                placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <!-- <span>than yesterday</span>
            <span class="green">
              24% -->
              <!-- <el-icon>
                <CaretTop />
              </el-icon>
            </span> -->
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="8">
      <div class="statistic-card">
        <el-statistic :value="278">
          <template #title>
            <div style="display: inline-flex; align-items: center">
              本周能耗总数（kw.h）
              <el-tooltip
                effect="dark"
                content="所有设备在本周的总耗能量"
                placement="top"
              >
                <el-icon style="margin-left: 4px" :size="12">
                  <Warning />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>比上周</span>
            <span class="red">
              12%
              <el-icon>
                <CaretBottom />
              </el-icon>
            </span>
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="8">
      <div class="statistic-card">
        <el-statistic :value="196" title="New transactions today">
          <template #title>
            <div style="display: inline-flex; align-items: center">
              最低耗能（kw.h）
            </div>
          </template>
        </el-statistic>
        <div class="statistic-footer">
          <div class="footer-item">
            <span>比上周</span>
            <span class="green">
              16%
              <el-icon>
                <CaretTop />
              </el-icon>
            </span>
          </div>
          <div class="footer-item">
            <el-icon :size="14">
              <ArrowRight />
            </el-icon>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>

    </div>

<!-- 插入表格 -->
   <div class="container">
      <itemChart />
   </div>
    
    
  </template>


  <script setup>

import itemChart from "../../components/MainBox/itemChart.vue"

import {
  ArrowRight,
  CaretBottom,
  CaretTop,
  Warning,
} from '@element-plus/icons-vue'

</script>

<style lang="scss" scoped>

.container{
height: inherit;
width: inherit;
margin-top: 30px;
padding: 10px 20px ;
// background-color: gray;

}

:global(h2#card-usage ~ .example .example-showcase) {
  background-color: var(--el-fill-color) !important;
}

.el-statistic {
  --el-statistic-content-font-size: 28px;
}

.statistic-card {
  height: 100%;
  padding: 20px;
  border-radius: 4px;
  background-color: var(--el-bg-color-overlay);
}

.statistic-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  font-size: 12px;
  color: var(--el-text-color-regular);
  margin-top: 16px;
}

.statistic-footer .footer-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.statistic-footer .footer-item span:last-child {
  display: inline-flex;
  align-items: center;
  margin-left: 4px;
}

.green {
  color: var(--el-color-success);
}
.red {
  color: var(--el-color-error);
}
</style>
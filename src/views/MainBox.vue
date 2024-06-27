<template>



  <div class="common-layout">
    <el-container :direction="VERTICAL">
        <TopHeader> </TopHeader>
      
      <el-main>
        <el-scrollbar>
            <router-view></router-view>
        </el-scrollbar>
      </el-main>
    </el-container>


  </div>
</template>

<script setup>


import TopHeader from '../components/MainBox/TopHeader.vue'
import { VERTICAL } from 'element-plus/es/components/virtual-list/src/defaults.mjs';


</script>
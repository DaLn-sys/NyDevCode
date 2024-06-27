<template>
  <el-table :data="filterTableData" style="width: 100%">
    <el-table-column label="设备名称" prop="devicename">
      <template #default="scope">
        <el-link type="primary" @click="jump(scope.row)">{{ scope.row.devicename }}

        </el-link>
      </template>
    </el-table-column>
    <el-table-column label="购入日期" prop="date" />
    <el-table-column label="所在位置" prop="address" />
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" size="default" placeholder="Type to search" />
      </template>
      <template #default="scope">
        <el-button size="default" @click="handleEdit(scope.$index, scope.row)">
          更新
        </el-button>
        <el-button size="default" type="danger" @click="handleDelete(scope.$index, scope.row)">
          删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>

  <!-- 全屏dialog展示设备详情 -->

  <el-dialog v-model="dialogVisible" title="设备详情" :fullscreen="true">
    <div>
      <devicedetail>

      </devicedetail>


    </div>

  </el-dialog>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'

interface User {
  date: string
  devicename: string
  address: string
}

const search = ref('')
const filterTableData = computed(() =>
  tableData.filter(
    (data) =>
      !search.value ||
      data.devicename.toLowerCase().includes(search.value.toLowerCase())
  )
)
const handleEdit = (index: number, row: User) => {
  console.log(index, row)
}
const handleDelete = (index: number, row: User) => {
  console.log(index, row)
}


// json信息
const tableData: User[] = [
  {
    date: '2024-06-24',
    devicename: '空调',
    address: '客厅',
  },
  {
    date: '2024-06-24',
    devicename: '冰箱',
    address: '厨房',
  },
  {
    date: '2024-06-24',
    devicename: '窗帘',
    address: '客厅',
  },
  {
    date: '2024-06-24',
    devicename: '台灯',
    address: '卧室',
  },

  {
    date: '2024-06-24',
    devicename: '洗衣机',
    address: '卫生间',
  },
  {
    date: '2024-06-24',
    devicename: '油烟机',
    address: '厨房',
  },
]

//预览
const dialogVisible = ref(false)
const jump = (item) => {
  dialogVisible.value = true
  currentItem.value = item

}
const currentItem = ref({})
</script>

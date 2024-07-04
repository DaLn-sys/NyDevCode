<template>
  <el-table :data="store.list" style="width: 100%">
    <el-table-column label="设备名称" width="180">
      <template #default="scope">
        <el-link type="primary" @click="jump(scope.row)">
          <b style="margin-left: 10px">
            {{ scope.row.devicename }}
          </b>
        </el-link>
      </template>
    </el-table-column>

    <el-table-column label="所处位置" prop="address" />
    <el-table-column label="耗能等级" prop="type" />

    <el-table-column label="操作" width="180">
      <template #default="scope">
        <div>
          <el-button type="warning" round @click="handleEdit(scope.row)"
            >编辑</el-button
          >
          <el-button type="danger" round @click="handleDelete(scope.row)"
            >删除</el-button
          >
        </div>
      </template>
    </el-table-column>
  </el-table>

</template>
  
  <script setup>
import useDevicesStore from "../../store/useDevicesStore";
import { useRouter } from 'vue-router'

const store = useDevicesStore();

const handleEdit = (item) => {
  console.log(item);
};
const handleDelete = (item) => {
  console.log(item);
};

const router = useRouter()
//预览
const jump = () => {

  router.push('/device-manage/SmartDevice')
}
</script>
  
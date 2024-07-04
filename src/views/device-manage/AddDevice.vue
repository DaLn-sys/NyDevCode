<template>
  <!-- 设备名称 -->
  <el-form :model="form" label-width="auto" style="max-width: 600px">
      <el-form-item label="设备名称">
          <el-input v-model="form.devicename" />
      </el-form-item>
      <!-- 所处位置 -->
      <el-form-item label="所处位置">
          <el-select v-model="form.address" placeholder="请选择设备所处位置">
              <el-option label="客厅" value="客厅" />
              <el-option label="主卧" value="主卧" />
              <el-option label="厨房" value="厨房" />
              <el-option label="卫生间" value="卫生间" />
              <el-option label="客卧" value="客卧" />

          </el-select>
      </el-form-item>
      <!-- 购入日期 -->
   
      <!-- 耗能等级 -->
      <el-form-item label="耗能等级">

          <el-radio-group v-model="form.type">
              <el-radio :value="1">等级1</el-radio>
              <el-radio :value="2">等级2</el-radio>
              <el-radio :value="3">等级3</el-radio>
          </el-radio-group>
      </el-form-item>

      <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button>取消</el-button>
      </el-form-item>
  </el-form>
</template>

<script setup>
import { reactive } from 'vue'
import useDevicesStore from '../../store/useDevicesStore'
import { useRouter } from 'vue-router'

// do not use same name with ref
const form = reactive({
  devicename: '',
  address: '',
  type: '',
})

const store = useDevicesStore()
const router = useRouter()
//提交
const onSubmit = () => {
  console.log('submit!', form)
  store.add(form)
  router.push('/device-manage/DeviceList')
}
</script>
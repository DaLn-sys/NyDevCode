<template>
      <vue-particles
            id="tsparticles"
            @particles-loaded="particlesLoaded"
            :options="config"/>
                   

    <div class="formContainer">
        <h3>节能安全用电系统</h3>
        <el-form
    ref="ruleFormRef"
    style="max-width: 600px"
    :model="ruleForm"
    :rules="rules"
    label-width="auto"
    class="ruleForm"
    :size="formSize"
    status-icon
  >

    <el-form-item label="用户名" prop="username">
      <el-input v-model="ruleForm.username" />
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="ruleForm.password" type="password"/>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)">
        登录
      </el-button>
    </el-form-item>

      </el-form>
    </div>
</template>

<script setup>
import {useUserStore} from '../store/useUserStore'
import {useRouter} from 'vue-router'
import { reactive, ref } from 'vue'

import { config } from '../util/config';


const particlesLoaded = async container => {
    console.log("Particles container loaded", container);
};

const ruleFormRef = ref()
const ruleForm = reactive({
    username:"",
    password:""
})


const rules = reactive({
    username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
  ],
    password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
  ],

})

const {changeUser} = useUserStore()

const router = useRouter()

const submitForm =async (formEl)=>{
    if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      if (ruleForm.username==="admin"){
        handleLogin1()
      }else{
        handleLogin2()
      }
    } else {
      console.log('error submit!', fields)
    }
  })
}

const handleLogin1 = ()=>{
    changeUser(
        {
        "id":1,
        "username":"admin",
        "password":"123",
        "role":{
            "roleName":"管理员",
            "roleType":1,
            "rights":[
                "/index",
                "/user-manage",
                "/user-manage/list",
                "/right-manage",
                "/right-manage/rightlist",
                "/device-manage",
                "/device-manage/devicelist",
                "/device-manage/adddevice",
                "/device-manage/smartdevice"
            ]
        }

        }
    )
    router.push("/")

}
const handleLogin2 = ()=>{
    changeUser(
        {
            "id":2,
        "username":"user",
        "password":"111",
        "role":{
            "roleName":"用户",
            "roleType":2,
            "rights":[
                "/index",
                "/device-manage",
                "/device-manage/devicelist",
                "/device-manage/adddevice",
                "/device-manage/smartdevice"
            ]
        }
        }
    )
    router.push("/")

}

</script>

<style lang="scss" scoped >

.formContainer{
    width: 500px;
    height: 300px;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    color: white;
    text-shadow: 2px 2px 5px black;
    text-align: center;
    .ruleForm{
        margin-top: 50px;
    }

    h3{
        font-size: 40px;
    }
    :deep(.el-form-item__label){
        color: white;
        font-size: 16px;
        font-weight: 700;
    }
}
</style>
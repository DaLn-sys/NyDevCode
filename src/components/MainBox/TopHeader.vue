<template>
  <div>

  </div>
  <el-header>
    <el-menu :default-active="route.fullPath" class="el-menu-demo" mode="horizontal" @select="handleSelect"
      :router="true">

      <template v-for="data in datalist" :key="data.path">
        <el-sub-menu :index="data.path" v-if="data.children.length && checkAuth(data.path)">
          <template #title>
            <span>{{ data.title }}</span>
          </template>

          <template v-for="item in data.children" :key="item.path">
            <el-menu-item :index="item.path" v-if="checkAuth(item.path)">
              <span>
                {{ item.title }}
              </span>
            </el-menu-item>
          </template>

        </el-sub-menu>

        <el-menu-item :index="data.path" v-else-if="checkAuth(data.path)">

          <span>{{ data.title }}</span>
        </el-menu-item>


      </template>

      <div class="current-time"
        style="margin-top: 20px;margin-bottom: 20px;font-weight: bold;position: absolute;right: 260px;">{{
          time.currentTime }}
      </div>

      <!-- mqtt -->
      <div>
        <span style="position: absolute;right: 200px;margin-top: 20px;margin-bottom: 20px;font-weight: bold;">
          {{ status.mqttConnectionStatus }}
        </span>
      </div>


      <span style="position: absolute;right: 70px;margin-top: 20px;margin-bottom: 20px;">
        欢迎{{ user.username }}回来
      </span>

      <el-dropdown style="position: absolute;right: 10px;margin-top: 10px;margin-bottom: 10px;">
        <el-avatar :size="40" :src="circleUrl" />
        <span class="el-dropdown-link">
          Dropdown List
          <el-icon class="el-icon--right">
            <arrow-down />
          </el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>{{ user.role.roleName }}</el-dropdown-item>
            <el-dropdown-item @click="handleExit">退出</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>




    </el-menu>


  </el-header>
</template>

<script setup>
import { useUserStore } from '../../store/useUserStore'

import { useRouterStore } from '../../store/useRouterStore'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router';

import { onMounted } from 'vue';
import axios from 'axios'

import { reactive, ref } from 'vue'

import { ArrowDown, SetUp } from '@element-plus/icons-vue'

import mqtt from "mqtt";

const status = reactive({
  mqttConnectionStatus: '',
})

const time = reactive({
  currentTime: '',
})

setInterval(updateCurrentTime, 1000);

function updateCurrentTime() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  time.currentTime = `${hours}:${minutes}:${seconds}`;
}

const options = {
  port: 8083,
  connectTimeout: 4000, // 超时时间
  clientId: "", // 不填默认随机生成一个ID
  username: "admin",
  password: "cyh991103",
};

const client = mqtt.connect('ws://122.51.210.27:8083/mqtt', options)



// 连接事件处理
client.on('connect', function () {
  status.mqttConnectionStatus = "已连接"
  console.log('连接成功');

  // 订阅主题
  client.subscribe('hello', { qos: 0 }, (error) => {
    if (!error) {
      console.log('订阅成功')
      client.publish('hello', 'Hello EMQ', { qos: 1, rein: false }, (error) => {
        console.log(error || '发布成功')
      })
    } else {
      console.log('订阅失败')
    }
  })
});

client.on("reconnect", (error) => {
  status.mqttConnectionStatus = "正在重连"
  console.log("正在重连", error)
})
client.on("error", (error) => {
  status.mqttConnectionStatus = "连接失败"
  console.log("连接失败", error)
})

//监听消息
client.on('message', (topic, message) => {
  console.log('收到来自', topic, '的消息', message.toString())
});




const route = useRoute()

const circleUrl = "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"

// 权限列表的获取
const datalist = ref([])

onMounted(
  () => {
    handleSelect()
  }
)
const handleSelect = async () => {

  var res = await axios.get("/right.json")
  console.log(res.date)
  datalist.value = res.data
}

const { changeUser, user } = useUserStore()
const { changeRouter } = useRouterStore()
const router = useRouter()

const handleExit = () => {

  changeUser({})
  changeRouter(false)

  router.push("/login")


}
const checkAuth = (path) => {
  return user.role.rights.includes(path)
}

</script>

<style lang="scss" scoped></style>
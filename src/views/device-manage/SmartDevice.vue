<template>
 
    <el-button type="primary" @click="doConnected">连接</el-button>

    <div class="slider-demo-block"  max-width='100px'>
    <span class="demonstration">Default value</span>
    <el-slider v-model="key" :max="9" />
    <el-button type="primary" style="margin-left: 50px;" @click="sendMqttMessage('testSlider', key)"
  >发送</el-button>
  </div>
  

    <el-button type="primary" @click="doDisconnected">断开连接</el-button>
    <p>收到的消息: {{ recvData }}</p>

</template>
 
<script>
import mqtt from "mqtt"; // 引入mqtt模块

export default {
  components: {},
  data() {
    return {
      client: null,
      options: {
        connectTimeout: 4000, // 超时时间
        clientId: "", // id
        username: "admin", // 用户名
        password: "cyh991103", // 密码
        cleanSession: false,
        keepAlive: 60, // 心跳值，心跳值太大可能会连接不成功，这个参考文档
      },
      subscription: {
        topic: "emqx/ir",
        qos: 0,
      },
      publication: {
        topic: "emqx/ir",
        qos: 0,
      },
      recvData: "", // 接收的消息
      key: 0,
    };
  },
  methods: {
    doConnected() {
      console.log("正在连接...");
      try {
        this.client = mqtt.connect(
          "ws://122.51.210.27:8083/mqtt",
          this.options
        );
      } catch (error) {
        console.log("mqtt连接失败: ", error);
      }
      this.client.on("connect", (e) => {
        console.log("连接成功");
        this.doSubscribe(); // 订阅主题
      });
      // 接收消息处理
      this.client.on("message", (topic, message) => {
        console.log("收到来自", topic, "的消息", message.toString());
        this.recvData = message.toString();
      });
      // 连接错误处理
      this.client.on("error", (error) => {
        console.log("连接出错: ", error);
      });
      // 重新连接处理
      this.client.on("reconnect", () => {
        console.log("重新连接...");
      });
    },
    doDisconnected() {
      try {
        this.doUnSubscribe();
        this.client.end();
        console.log("断开连接");
      } catch (error) {
        console.log("断开连接失败: ", error.toString());
      }
    },
    doSubscribe() {
      const { topic, qos } = this.subscription;
      this.client.subscribe(topic, qos, (error) => {
        if (!error) {
          console.log("订阅成功");
        } else {
          console.log("订阅失败");
        }
      });
    },
    doUnSubscribe() {
      const { topic } = this.subscription;
      this.client.unsubscribe(topic, (error) => {
        if (error) {
          console.log("取消订阅失败", error);
        }
      });
    },

    // publish() {
    //   const { topic, qos, message } = this.publication;
    //   this.client.publish(topic, message, qos, (error) => {
    //     if (!error) {
    //       console.log("发出了主题为", topic, "的消息是", message.toString());
    //     } else {
    //       console.log("发布失败", error);
    //     }
    //   });
    // },

    publish(topic, message) {
      // if (!this.client.connected) {
      //   console.log('客户端未连接')
      //   return
      // }
      this.client.publish(topic, message, {qos: 0}, (err) => {
        if (!err) {
          console.log(`主题为：${topic},内容为：${message} 发布成功`)
        }
      })
    },

    sendMqttMessage(action, mode) {
      const message = {
        action:action,
        // params: mode !== undefined ? `${mode}` : "", // 根据 mode 的存在性设置 params
        key: mode!==undefined?`${mode}`:""
      };
      const jsonString = JSON.stringify(message, null, 2);
      this.publish("emqx/ir", jsonString);
    },
  },
};
</script>

<style scoped>
.slider-demo-block {
  max-width: 600px;
  display: flex;
  align-items: center;
}
.slider-demo-block .el-slider {
  margin-top: 0;
  margin-left: 12px;
}
.slider-demo-block .demonstration {
  font-size: 14px;
  color: var(--el-text-color-secondary);
  line-height: 44px;
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-bottom: 0;
}
</style>
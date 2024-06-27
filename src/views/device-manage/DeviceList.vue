<template>
    <div>
        <el-button type="primary" plain >添加设备</el-button>
        <span>
            
        </span>


    </div>
    <div style="display: flex;justify-content: space-between; margin-top: 20px;">
        <div style="height: 320px; width: 270px;">
            <el-descriptions direction="horizontal" :column="1" width="50px" border>
                <el-descriptions-item label="设备名称" label-align='center'>
                    <p style="text-align: center;">空调</p>
                </el-descriptions-item>
                <el-descriptions-item label="所处位置" label-align='center'>
                    <p style="text-align: center;">客厅</p>
                </el-descriptions-item>
                <el-descriptions-item label="开启状态" label-align='center'>
                    <p style="text-align: center;"><el-switch v-model="value1" /></p>
                </el-descriptions-item>
                <el-descriptions-item label="模式选择" label-align='center'>
                    <p style="text-align: center;">
                        <el-select v-model="value" placeholder="模式选择" style="width: 150px">
                            <el-option v-for="item in options1" :key="item.value" :label="item.label"
                                :value="item.value" />
                        </el-select>
                    </p>

                </el-descriptions-item>
            </el-descriptions>
        </div>

        <div style="height: 320px; width: 270px;">
            <el-descriptions direction="horizontal" :column="1" width="50px" border>
                <el-descriptions-item label="设备名称" label-align='center'>
                    <p style="text-align: center;">冰箱</p>
                </el-descriptions-item>
                <el-descriptions-item label="所处位置" label-align='center'>
                    <p style="text-align: center;">厨房</p>
                </el-descriptions-item>
                <el-descriptions-item label="开启状态" label-align='center'>
                    <p style="text-align: center;"><el-switch v-model="value2" /></p>
                </el-descriptions-item>
                <el-descriptions-item label="模式选择" label-align='center'>
                    <p style="text-align: center;">
                        <el-select v-model="value02" placeholder="模式选择" style="width: 150px">
                            <el-option v-for="item2 in options2" :key="item2.value02" :label="item2.label2"
                                :value="item2.value02" />
                        </el-select>
                    </p>

                </el-descriptions-item>
            </el-descriptions>
        </div>

        <div style="height: 320px; width: 270px;">
            <el-descriptions direction="horizontal" :column="1" width="50px" border>
                <el-descriptions-item label="设备名称" label-align='center'>
                    <p style="text-align: center;">窗帘</p>
                </el-descriptions-item>
                <el-descriptions-item label="所处位置" label-align='center'>
                    <p style="text-align: center;">客厅</p>
                </el-descriptions-item>
                <el-descriptions-item label="开启状态" label-align='center'>
                    <p style="text-align: center;"><el-switch v-model="value3" /></p>
                </el-descriptions-item>
                <el-descriptions-item label="模式选择" label-align='center'>
                    <p style="text-align: center;">
                        <el-select v-model="value03" placeholder="模式选择" style="width: 150px">
                            <el-option v-for="item3 in options3" :key="item3.value03" :label="item3.label3"
                                :value="item3.value03" />
                        </el-select>
                    </p>

                </el-descriptions-item>
            </el-descriptions>
        </div>
    </div>

    <div style="display: flex;justify-content: space-between;">
        <div style="height: 320px; width: 270px;">
            <el-descriptions direction="horizontal" :column="1" width="50px" border>
                <el-descriptions-item label="设备名称" label-align='center'>
                    <p style="text-align: center;">台灯</p>
                </el-descriptions-item>
                <el-descriptions-item label="所处位置" label-align='center'>
                    <p style="text-align: center;">卧室</p>
                </el-descriptions-item>
                <el-descriptions-item label="开启状态" label-align='center'>
                    <p style="text-align: center;"><el-switch v-model="value4" /></p>
                </el-descriptions-item>
                <el-descriptions-item label="模式选择" label-align='center'>
                    <p style="text-align: center;">
                        <el-select v-model="value04" placeholder="模式选择" style="width: 150px">
                            <el-option v-for="item4 in options4" :key="item4.value04" :label="item4.label04"
                                :value="item4.value04" />
                        </el-select>
                    </p>

                </el-descriptions-item>
            </el-descriptions>
        </div>

        <div style="height: 320px; width: 270px;">
            <el-descriptions direction="horizontal" :column="1" width="50px" border>
                <el-descriptions-item label="设备名称" label-align='center'>
                    <p style="text-align: center;">洗衣机</p>
                </el-descriptions-item>
                <el-descriptions-item label="所处位置" label-align='center'>
                    <p style="text-align: center;">卫生间</p>
                </el-descriptions-item>
                <el-descriptions-item label="开启状态" label-align='center'>
                    <p style="text-align: center;"><el-switch v-model="value5" /></p>
                </el-descriptions-item>
                <el-descriptions-item label="模式选择" label-align='center'>
                    <p style="text-align: center;">
                        <el-select v-model="value05" placeholder="模式选择" style="width: 150px">
                            <el-option v-for="item5 in options5" :key="item5.value05" :label="item5.label5"
                                :value="item5.value05" />
                        </el-select>
                    </p>

                </el-descriptions-item>
            </el-descriptions>
        </div>

        <div style="height: 320px; width: 270px;">
            <el-descriptions direction="horizontal" :column="1" width="50px" border>
                <el-descriptions-item label="设备名称" label-align='center'>
                    <p style="text-align: center;">油烟机</p>
                </el-descriptions-item>
                <el-descriptions-item label="所处位置" label-align='center'>
                    <p style="text-align: center;">厨房</p>
                </el-descriptions-item>
                <el-descriptions-item label="开启状态" label-align='center'>
                    <p style="text-align: center;"><el-switch v-model="value6" /></p>
                </el-descriptions-item>
                <el-descriptions-item label="模式选择" label-align='center'>
                    <p style="text-align: center;">
                        <el-select v-model="value06" placeholder="模式选择" style="width: 150px">
                            <el-option v-for="item6 in options6" :key="item6.value06" :label="item6.label6"
                                :value="item6.value06" />
                        </el-select>
                    </p>

                </el-descriptions-item>
            </el-descriptions>
        </div>





    </div>
</template>

<script setup>

import { ref } from 'vue'



const value1 = ref(true)
const value2 = ref(true)
const value3 = ref(true)
const value4 = ref(true)
const value5 = ref(true)
const value6 = ref(true)


const value = ref('')
const value02 = ref('')
const value03 = ref('')
const value04 = ref('')
const value05 = ref('')
const value06 = ref('')

const options1 = [
    {
        value: '自动模式',
        label: '自动模式',
    },
    {
        value: '制冷模式',
        label: '制冷模式',
    },
    {
        value: '除湿模式',
        label: '除湿模式',
    },
    {
        value: '制热模式',
        label: '制热模式',
    },

]

const options2 = [
    {
        value02: '速冷模式',
        label2: '速冷模式',
    },
    {
        value02: '保鲜模式',
        label2: '保鲜模式',
    },
    {
        value02: '除臭模式',
        label2: '除臭模式',
    },
    {
        value02: '节能模式',
        label2: '节能模式',
    },

]

const options3 = [
    {
        value03: '自动模式',
        label3: '自动模式',
    },
    {
        value03: '手动模式',
        label3: '手动模式',
    },

]

const options4 = [
    {
        value04: '专注模式',
        label4: '专注模式',
    },
    {
        value04: '阅读模式',
        label4: '阅读模式',
    },
    {
        value04: '睡眠模式',
        label4: '睡眠模式',
    },
]
const options5 = [
    {
        value05: '快速洗',
        label5: '快速洗',
    },
    {
        value05: '混合洗',
        label5: '混合洗',
    },
    {
        value05: '除螨洗',
        label5: '除螨洗',
    },
    {
        value05: '漂洗',
        label5: '漂洗',
    },
    {
        value05: '单脱水',
        label5: '单脱水',
    },
    {
        value05: '筒自洁',
        label5: '筒自洁',
    },

]
const options6 = [
    {
        value06: '排烟模式',
        label6: '排烟模式',
    },
    {
        value06: '自旋洗',
        label6: '自旋洗',
    },
    {
        value06: '照明',
        label6: '照明',
    },

]
</script>
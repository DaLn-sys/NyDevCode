import {defineStore} from 'pinia'
import {ref} from 'vue'

const useDevicesStore = defineStore("devices",()=>{
    const list = ref([])

    const add = (value)=>{
        list.value.push({...value})
    }

    return {
        list,
        add
    }
},{
    persist:true
})

export default useDevicesStore
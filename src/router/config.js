import Page from '../views/page/Page.vue'
//用户管理
import UserList from '../views/user-manage/UserList.vue'
//权限管理
import RightList from '../views/right-manage/RightList.vue'

//设备管理
import DeviceList from '../views/device-manage/DeviceList.vue'
import AddDevice from '../views/device-manage/AddDevice.vue'
import SmartDevice from '../views/device-manage/SmartDevice.vue'


const routes = [
    {
        path:"/index",
        component:Page
    },
    {
        path:"/user-manage/list",
        component:UserList
    },

    {
        path:"/right-manage/rightlist",
        component:RightList
    },

    {
        path:"/device-manage/devicelist",
        component:DeviceList
    },
    {
        path:"/device-manage/adddevice",
        component:AddDevice
    },
    {
        path:"/device-manage/smartdevice",
        component:SmartDevice
    }
]

export default routes;
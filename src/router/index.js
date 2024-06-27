import {createRouter,createWebHashHistory} from 'vue-router'
import Login from '../views/Login.vue'
import MainBox from '../views/MainBox.vue'
import NotFound from '../views/notfound/NotFound.vue'
import RouteConfig from './config'
import {useRouterStore} from '../store/useRouterStore'
import {useUserStore} from '../store/useUserStore'

const routes = [
    {
        path:"/login",
        name:"login",
        component:Login
    },

    {
        path:"/mainbox",
        name:"mainbox",
        component:MainBox
    }

]


const router = createRouter({
    history:createWebHashHistory(),
    routes

})

//添加路由
// router.addRoute("mainbox",{
//     path:"/index",
//     component:Page
// })


//路由拦截
router.beforeEach((to,from,next)=>{
    const {isGetterRouter} = useRouterStore()
    const {user} = useUserStore()

    if(to.name ==="login"){
        next()
    }else{
        if(!user.role){
            next({
                path:"/login"
            })
        }else{
           
            if(!isGetterRouter){
                router.removeRoute("mainbox")
                ConfigRouter()
                next({
                    path:to.fullPath
                })
            }else{
                next()
            }  
        }
    }   
})


const ConfigRouter = ()=>{
    router.addRoute({
        path:"/mainbox",
        name:"mainbox",
        component:MainBox
    })

    let {changeRouter} = useRouterStore()
    RouteConfig.forEach(item=>{
        checkPermission(item.path) && router.addRoute("mainbox",item)
    })

//重定向

    router.addRoute("mainbox",{
        path:"/",
        redirect:"/index"

    })
    router.addRoute("mainbox",{
        path:"/:pathMatch(.*)*",
        name:"not found",
        component:NotFound

    })
    changeRouter(true)
    
    console.log(router.getRoutes())

}
const checkPermission = (path)=>{
    const {user} = useUserStore()
    return user.role.rights.includes(path)


}
export default router
<template>
  <div id="home">
    <button @click="showLogin(1)">登录</button>
    <button @click="showLogin(2)">注册</button>
    <div class="header">
        <h1>网易标题</h1>
        <img src="./assets/logo.png" alt="">
        
     </div>
    <hr/>
      <div class="content">
        
        <div class="menu">
          
         <div v-for="item in menuList" :key="item.id" class="item">
           <div v-if="item.id == choosed"  style="background:#777;color:#fff">

            <a style="color:#fff" >{{item.text}}</a>
           
           </div>
          <div v-else style="color:#000" @click="chooseMenu(item.id)">
            <a  style="color:#000">{{item.text}}</a>
          </div>
         </div>
       </div>
        <div  class="userlist">
          <p>{{choosed_text}}</p>
            <hr/>
             <router-view/>
            
             <p>没有用户</p>
            
            
            </div>
        </div>
      <loginBox v-if="boxtarget" :target="boxtarget" @hideBox="hideLgoin"></loginBox>
        <div class="foot">Copyreight @ 2020 Mili工作室</div>
    
   
   
  </div>
</template>

<script>
import axios from 'axios';
import LoginBox from '../src/components/LoginBox'
//impirt axios from 'axios'
export default {
  components: { LoginBox },
  data(){
    return{
      menuList:[],
      choosed:1,
      choosed_text:'Django框架',
      boxtarget:0
    }
  },
  mounted(){
    this.getMenuList()
  },
  methods:{
    getMenuList(){
      console.log("开始或获取分类");
       axios({
         url:'http://127.0.0.1:9000/get-menu-list',
         type:'json',
         method:'get'
       }).then(res=>{
         console.log(res);
         this.menuList=res.data;
       });
    },
    chooseMenu(id){
      console.log(id)
      this.choosed=id
      for (let i = 0; i < this.menuList.length; i++) {
        if (id==this.menuList[i].id) {
          this.choosed_text=this.menuList[i].text
        }
        
        
      }
      //进行id参数传值跳转
      this.$router.push({path:'/',query:{menuId:id}})
    },
    //展示登录注册框体
   showLogin(value){
     this.boxtarget=value
   },
    //隐藏父组件
   hideLgoin(){
     this.boxtarget = 0
   }
  },
  
  
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

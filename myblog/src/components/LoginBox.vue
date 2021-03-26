<template>
    <div id="login" @click.self="hideSelf">
     <div id="loginbox">
       <div class="from">
           <div v-if="target==2 || target==1" class="item">
               用户名：
               <input v-model="username" type="text" placeholder="输入用户名" >
           </div>
           
            <div v-if="target==2 || target==1" class="item">
               密 码：
               <input v-model="password" type="text" placeholder="输入密码" >
               
           </div>
           <div v-if="target==2" class="item">
               重复密码：
               <input v-model="password2" type="text" placeholder="重新输入密码" >
               
           </div>
           <div v-if="target==3" class="item">
               <div class="span">网站名称：</div>
               <input v-model="sitename" type="text" placeholder="输入网站名称" >
               
           </div>
           <div v-if="target==3" class="item">
               <div class="span">图片上传：</div>
               <input id="uploadlogo" type="file" style="whith:10px" />
               
           </div>
           <button v-if="target==1" @click="toLogin">点击登录</button>
           <button v-if="target==2" @click="toRegister">点击注册</button>
           <button v-if="target==3" @click="toRegister">点击确定</button>
       </div>
     </div>
    </div>
    
</template>

<script>
import axios from "axios"
import Qs from "qs"
export default {
    name:"LoginBox",
    props:['target'],
    data(){
        return{
            username:'',
            password:'',
            password2:'',
            sitename:""
        };
    },
    mounted(){
        console.log(this.target)
    },
    methods:{
        toUpload(){

        }
        hideSelf(){
           this.$emit("hideBox")
        },
        //注册
        toRegister(){
           var username=this.username
           var password=this.password
           var password2=this.password2
           console.log(username,password,password2)
           if(username.length>0&password.length>0&password2.length>0){
               if(password!=password2){
                 alert("两次输入密码不同")
               }else{
                   axios({
                url:'http://127.0.0.1:9000/register/',
                data:Qs.stringify({
                    username,
                    password,
                    password2
                }),
                method:'post',
                headers:{
                    "Content-Type":"application/x-www-form-urlencoded"
                }
            }).then((res)=>{
                alert("注册成功!")
                 console.log(res)
                 })
               }
           }
        },
        //登录
        toLogin(){
            console.log(this.username,this.password);
            var username = this.username
            var password = this.password
            if (username.length>0 && password.length>0) {
                 axios({
                url:'http://127.0.0.1:9000/login/',
                data:Qs.stringify({
                    username,
                    password
                }),
                method:'post',
                headers:{
                    "Content-Type":"application/x-www-form-urlencoded"
                }
            }).then((res)=>{
                console.log(res);
                switch(res.data){
                    case 'none':
                    alert('用户名不存在')
                    break;
                    case 'pwderr':
                    alert('密码错误')
                    break;
                    default:
                      console.log(res.data.token)
                      alert('登录成功')
                }
            });
            }else{
                alert('用户名或密码不能为空')
            }
           
        }
    },
};
</script>>
  
<style>
 #login{
       position: absolute;
       top: 0;
       widows: 700px;
       height: 100vh;
       display: flex;
       justify-content: center;
       align-items: center;
       background: #00000020;
   }
#loginbox{
       widows: 300px;
       height: 300px;
       border: 1px solid#000;
       
       background: #00000070;
      
       color: #fff;
   }
#loginbox .from .item {
       font-weight: 700;
       margin: 10px auto;
   }
</style>
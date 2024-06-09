<template>
<div class="login" clearfix>
    <div class="login-wrap">
    <el-row type="flex" justify="end">
        <el-col :span="1">  
        </el-col>
        <el-col :span="8">  
            <div class="moduleImg" :style="backgroundStyle"></div>
        </el-col>  
        <el-col :span="15"> 
            <el-form ref="loginForm" :model="user" :rules="rules" status-icon label-width="80px">
            <h3>欢迎回来</h3>
            <hr>
            <el-form-item id="username" prop='username'>
                <el-input v-if="!focused_user" @focus="focused_user = true" v-model="user.username" placeholder="用户名" prefix-icon="el-icon-user" maxlength="40"></el-input>
                <el-input v-else @blur="focused_user = false" v-model="user.username" placeholder="" prefix-icon="el-icon-user" maxlength="40"></el-input>
                <span class="label" :style="{opacity: focused_user ? 1:0, top: focused_user ? '-30px':'0px'}">用户名</span>
            </el-form-item>
            <el-form-item id="password" prop='password'>
                <el-input v-if="!focused_passwd" @focus="focused_passwd = true" v-model="user.password" show-password placeholder="密码" prefix-icon="el-icon-lock" maxlength="40"></el-input>
                <el-input v-else @blur="focused_passwd = false" v-model="user.password" show-password placeholder="" prefix-icon="el-icon-lock" maxlength="40"></el-input>
                <span class="label" :style="{opacity: focused_passwd ? 1:0, top: focused_passwd ? '-30px':'0px'}">密码</span>
            </el-form-item>
                <span class="tip">新用户？</span>
                <router-link id='register' to="/register">去注册</router-link>
            <el-form-item>
                <el-button type="primary" @click="doLogin">登录</el-button>
            </el-form-item>
            </el-form>
        </el-col>
    </el-row>
    </div>
</div>
</template>

<script>
import axios from "axios";
import { login } from "../api/api.js"
export default {
name: "login",
data() {
    return {
    user: {
        username: "",
        password: ""
    },
    focused_user: false,
    focused_passwd: false,
    moduleUrl: require("../assets/images/login&register/basic.png"),
    }
},
computed: {  
    backgroundStyle() {  
      return {  
        backgroundImage: `url(${this.moduleUrl})`,  
      };  
    }  
},
mounted() {  
    setTimeout(() => {
        this.moduleUrl = require("../assets/images/login&register/basic.png")
    }, 1000) 
},
created() {},
methods: {
    doLogin() {
    if (!this.user.username) {
        this.$message.error("请输入用户名！");
        return;
    } else if (!this.user.password) {
        this.$message.error("请输入密码！");
        return;
    } else {
        login(this.user.username, this.user.password).then(respond =>{
            if(respond && respond.data.code === 200){
                this.$message({
                    message: `欢迎回来, ${this.user.username}!`,
                    type: 'success'
                });
                // this.$store.commit("setLoggedIn", true)
                this.$router.push({ path: "/" });
            }
            else{
                console.log("Login failed");   
                this.$message.error(respond.data.msg || "登录失败！"); 
            }
        }).catch(error => {  
                console.error('Request failed:', error);  
                this.$message.error("请求失败，请检查网络或稍后再试！");  
            });  
    }}
}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login::before{
    content:"";
    background-image: url("../assets/images/login&register/basic_bg.jpg"), linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7));
    background-blend-mode: overlay;
    /* background-image: url("../assets/images/bg1.jpg"); */
    mix-blend-mode: multiply;
    opacity:1;
    z-index:-1;
    background-size:100% 100%;
    background-attachment:fixed;
    width: 100%;
    height: 100%;
    position:absolute;
    top:0px;
    left:0px;
}
.login {
    margin: 0px;
    width: 100%;
    height: 100%;
}
.login-wrap {
    background: url("../assets/images/login&register/basic_rect.png") no-repeat;
    background-size: cover;
    width: 800px;
    height: 450px;
    margin: 250px auto;
    overflow: hidden;
    padding-top: 10px;
    line-height: 80px;
    font-size: 20px;
}
.label{
    position: absolute;
    /* top: -30px;
    left: 5px; */
    top: 0px;
    left: 5px;
    color: #000000;
    transition: 0.1s ease-out;
    opacity: 0;
    font-size: small;
}
.moduleImg{
    width: 283px;
    height: 474px;
    background-size: cover;
    background-repeat: no-repeat;
    transition: 0.25s ease-in-out;
    margin-bottom: 90px;
}
.tip{
    color: #a09d9d;
    font-size: 17px;
    margin-right: 0px;
}
#username{
    width: 440px; 
    margin-bottom: 30px;
}
#password {
    width: 440px;
    margin-bottom: 0px;
    margin-right: 60px;
}
h3 {
    color: #e55e5e;
    font-size: 30px;
    margin-right: 0px;
    margin-bottom: -10px;
}
hr {
    background-color: #444;
    margin: 5px auto 30px;
    width: 400px;
    }
a {
    text-decoration: none;
    color: #aaa;
    font-size: 15px;
}
a:hover {
    color: coral;
}
#findback {
    width: 80%;
    margin-right: 30px;
    font-size: 17px;
}
#register {
    width: 80%;
    margin-right: 0px;
    font-size: 17px;
}
.el-button {
    width: 80%;
    margin-right: 55px;
    color: #ffffff;
    font-size: large;
}
</style>
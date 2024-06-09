<template>
<div class="login clearfix">
    <div class="login-wrap">
    <el-row type="flex" justify="end">
        <el-col :span="1">  
        </el-col>
        <el-col :span="8">  
            <div class="moduleImg" :style="backgroundStyle" @click="(isMaster && isReady)? switch2D():switch2M()"></div>
        </el-col>  
        <el-col :span="15"> 

        <el-form v-if="!isReady || (isReady && isMaster)" ref="loginForm" :model="user" status-icon label-width="80px">
        <h3>创建你的账户</h3>
        <hr>
        <el-form-item id="username" prop="username">
            <el-input v-if="!focused_user" @focus="focused_user = true" v-model="user.username" placeholder="用户名" prefix-icon="el-icon-user" maxlength="40"></el-input>
            <el-input v-else @blur="focused_user = false" v-model="user.username" placeholder="" prefix-icon="el-icon-user" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_user ? 1:0, top: focused_user ? '-30px':'0px'}">用户名</span>
        </el-form-item>
        <el-form-item id="email" prop="email">
            <el-input v-if="!focused_email" @focus="focused_email = true" v-model="user.email" placeholder="邮箱" prefix-icon="el-icon-message" maxlength="40"></el-input>
            <el-input v-else @blur="focused_email = false" v-model="user.email" placeholder="" prefix-icon="el-icon-message" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_email ? 1:0, top: focused_email ? '-30px':'0px'}">邮箱</span>
        </el-form-item>
        <el-form-item id="password" prop="password">
            <el-input v-if="!focused_passwd" @focus="focused_passwd = true" v-model="user.password" show-password placeholder="密码" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <el-input v-else @blur="focused_passwd = false" v-model="user.password" show-password placeholder="" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_passwd ? 1:0, top: focused_passwd ? '-30px':'0px'}">密码</span>
        </el-form-item>
        <el-form-item id="password" prop="password">
            <el-input v-if="!focused_repasswd" @focus="focused_repasswd = true" v-model="user.repass" show-password placeholder="确认密码" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <el-input v-else @blur="focused_repasswd = false" v-model="user.repass" show-password placeholder="" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_repasswd ? 1:0, top: focused_repasswd ? '-30px':'0px'}">确认密码</span>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" style="margin-top: 0px;" @click="doNormRegister()">注册账号</el-button>
        </el-form-item>
        </el-form>

        <el-form v-if="!isMaster && isReady" class="doctorRegis" ref="loginForm" :model="user" status-icon label-width="80px">
        <h3>创建你的账户</h3>
        <hr>
        <el-form-item id="username" prop="username">
            <el-input v-if="!focused_user" @focus="focused_user = true" v-model="user.username" placeholder="用户名" prefix-icon="el-icon-user" maxlength="40"></el-input>
            <el-input v-else @blur="focused_user = false" v-model="user.username" placeholder="" prefix-icon="el-icon-user" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_user ? 1:0, top: focused_user ? '-30px':'0px'}">用户名</span>
        </el-form-item>
        <el-form-item id="name" prop="name">
            <el-input v-if="!focused_name" @focus="focused_name = true" v-model="user.name" placeholder="姓名" prefix-icon="el-icon-user-solid" maxlength="10"></el-input>
            <el-input v-else @blur="focused_name = false" v-model="user.name" placeholder="" prefix-icon="el-icon-user-solid" maxlength="10"></el-input>
            <span class="label" :style="{opacity: focused_name ? 1:0, top: focused_name ? '-30px':'0px'}">姓名</span>
        </el-form-item>
        <el-form-item id="identity" prop="identity">
            <el-input v-if="!focused_identity" @focus="focused_identity = true" v-model="user.id" placeholder="身份证号" prefix-icon="el-icon-postcard" maxlength="18"></el-input>
            <el-input v-else @blur="focused_identity = false" v-model="user.id" placeholder="" prefix-icon="el-icon-postcard" maxlength="18"></el-input>
            <span class="label" :style="{opacity: focused_identity ? 1:0, top: focused_identity ? '-30px':'0px'}">身份证号</span>
        </el-form-item>
        <el-form-item id="email" prop="email">
            <el-input v-if="!focused_email" @focus="focused_email = true" v-model="user.email" placeholder="邮箱" prefix-icon="el-icon-message" maxlength="40"></el-input>
            <el-input v-else @blur="focused_email = false" v-model="user.email" placeholder="" prefix-icon="el-icon-message" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_email ? 1:0, top: focused_email ? '-30px':'0px'}">邮箱</span>
        </el-form-item>
        <el-form-item id="password" prop="password">
            <el-input v-if="!focused_passwd" @focus="focused_passwd = true" v-model="user.password" show-password placeholder="密码" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <el-input v-else @blur="focused_passwd = false" v-model="user.password" show-password placeholder="" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_passwd ? 1:0, top: focused_passwd ? '-30px':'0px'}">密码</span>
        </el-form-item>
        <el-form-item id="repassword" prop="repassword">
            <el-input v-if="!focused_repasswd" @focus="focused_repasswd = true" v-model="user.repass" show-password placeholder="确认密码" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <el-input v-else @blur="focused_repasswd = false" v-model="user.repass" show-password placeholder="" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_repasswd ? 1:0, top: focused_repasswd ? '-30px':'0px'}">确认密码</span>
        </el-form-item>
        <el-form-item id="post" prop="post">
            <el-input v-if="!focused_post" @focus="focused_post = true" v-model="user.post" placeholder="执业编号" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <el-input v-else @blur="focused_post = false" v-model="user.post" placeholder="" prefix-icon="el-icon-lock" maxlength="40"></el-input>
            <span class="label" :style="{opacity: focused_post ? 1:0, top: focused_post ? '-30px':'0px'}">执业编号</span>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" style="margin-top: 30px;" @click="doDocRegister()">注册账号</el-button>
        </el-form-item>
        </el-form>

        </el-col>
    </el-row>
    </div>
</div>
</template>

<script>
import axios from "axios";
import { normRegister , DocRegister } from "../api/api";
export default {
name: "login",
data() {
    return {
    user: {
        username: "",
        email: "",
        password: ""
    },
    focused_user: false,
    focused_passwd: false,
    focused_repasswd: false,
    focused_email: false,
    focused_identity: false,
    focused_name: false,
    focused_post: false,
    moduleUrl: require("../assets/images/login&register/basic.png"),
    isMaster: true,
    isReady: false,
    };
},
computed: {  
    backgroundStyle() {  
      return {  
        backgroundImage: `url(${this.moduleUrl})`,  
      }
    }  
},
mounted() {  
    setTimeout(() => {
        this.moduleUrl = require("../assets/images/login&register/master.png")
    }, 200) 
    this.isReady = true
},
created() {
    // console.log($);
    // console.log("1111");
},
methods: {
    doNormRegister() {
    if (!this.user.username) {
        this.$message.error("请输入用户名！");
        return;
    } else if (!this.user.email) {
        this.$message.error("请输入邮箱！");
        return;
    } else if (this.user.email != null) {
        var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        if (!reg.test(this.user.email)) {
        this.$message.error("请输入有效的邮箱！");
        } else if (!this.user.password || !this.user.repass) {
        this.$message.error("请输入密码并确认！");
        return;
        } else {
            normRegister(this.user.username, this.user.email, this.user.password, this.user.repass).then(respond =>{
            if(respond && !(`detail` in respond.data) && respond.data.code === 200){
                this.$message({
                    message: `注册成功! 欢迎${this.user.username}和您的爱宠加入我们!`,
                    type: 'success'
                });
                this.$router.push({ path: "/login" });
            }
            else{
                if(`username` in respond.data.detail){
                        this.$message.error(`${respond.data.detail.username}`); 
                }
                else if(`user_email` in respond.data.detail){ // 前后端实际上都做了邮箱格式检测，后续可以把前端此部分删除
                    this.$message.error(`${respond.data.detail.user_email}`);
                }
                else if(`confirm_password` in respond.data.detail){ // 前后端实际上都做了邮箱格式检测，后续可以把前端此部分删除
                    this.$message.error(`${respond.data.detail.confirm_password}`);
                }
                else
                {
                    this.$message.error("注册失败！请检查输入的信息或网络连接情况"); 
                }
            }
            }).catch(error => {  
                console.error('Request failed:', error);  
                    this.$message.error("注册失败！请检查输入的信息或网络连接情况"); 
            });

            
        }
    }
    },
    doDocRegister() {
    if (!this.user.username) {
        this.$message.error("请输入用户名！");
        return;
    } else if (!this.user.email) {
        this.$message.error("请输入邮箱！");
        return;
    } else if (!this.user.name) {
        this.$message.error("请实名认证！");
        return;
    } else if (!this.user.id) {
        this.$message.error("请输入身份证号！");
        return;
    } else if ((this.user.id.length) != 18) {
        this.$message.error("身份证号不合法！");
        return;
    } else if (!this.user.post) {
        this.$message.error("请输入执业编号！");
        return;
    } else if (this.user.email != null) {
        var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        if (!reg.test(this.user.email)) {
        this.$message.error("请输入有效的邮箱！");
        } else if (!this.user.password || !this.user.repass) {
        this.$message.error("请输入密码并确认！");
        return;
        } else {
            DocRegister(this.user.username, this.user.email, this.user.password, 
                this.user.repass, this.user.id, this.user.name, this.user.post).then(respond =>{
            if(respond && !(`detail` in respond.data) && respond.data.code === 200){
                this.$message({
                    message: `注册成功! 您的认证申请已经提交, 请关注平台消息！`,
                    type: 'success'
                });
                this.$router.push({ path: "/login" });
            }
            else{
                if(`username` in respond.data.detail){
                    this.$message.error(`${respond.data.detail.username}`); 
                }
                else if(`user_email` in respond.data.detail){
                    this.$message.error(`${respond.data.detail.user_email}`);
                }
                else if(`confirm_password` in respond.data.detail){ // 前后端实际上都做了邮箱格式检测，后续可以把前端此部分删除
                    this.$message.error(`${respond.data.detail.confirm_password}`);
                }
                else
                {
                    this.$message.error("注册失败！请检查输入的信息或网络连接情况"); 
                }
            }
            }).catch(error => {  
                console.error('Request failed:', error);  
                    this.$message.error("注册失败！请检查输入的信息或网络连接情况"); 
            });

            
        }
    }
    },
    switch2M(){
        this.isMaster= !this.isMaster;
        this.moduleUrl = require("../assets/images/login&register/master.png");
        setTimeout(() => {}, 1000);
    },
    switch2D(){
        this.isMaster= !this.isMaster;
        this.moduleUrl = require("../assets/images/login&register/doctor.png");
        setTimeout(() => {}, 1000);
    },
}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.fade-enter-active, .fade-leave-active {  
  transition: opacity 0.25s ease-out;  
}  
.fade-enter, .fade-leave-to {  
  opacity: 0;  
}  
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
    transition: 0.25s ease-out;
    opacity: 0;
    font-size: small;
}
.moduleImg{
    width: 283px;
    height: 474px;
    background-size: cover;
    background-repeat: no-repeat;
    transition: 0.25s ease-in-out;
}
.doctorRegis{
    height: 470px;
    overflow-y: auto;
}
#username {
width: 440px; 
margin-bottom: 20px;
}
#email {
width: 440px;
margin-bottom: 20px;
margin-right: 60px;
}
#password {
width: 440px;
margin-bottom: 20px;
margin-right: 60px;
}
#repassword {
width: 440px;
margin-bottom: 20px;
margin-right: 60px;
}
#name {
width: 440px;
margin-bottom: 20px;
margin-right: 60px;
}
#identity {
width: 440px;
margin-bottom: 20px;
margin-right: 60px;
}
#post {
width: 440px;
margin-bottom: 20px;
margin-right: 60px;
}
h3 {
color: #e55e5e;
font-size: 30px;
margin-right: 0px;
margin-bottom: 0px;
}
hr {
background-color: #444;
margin: 5px auto 30px;
width: 400px;
}
.el-button {
width: 80%;
margin-right: 55px;
margin-top: -20px;
color: #ffffff;
font-size: large;
}
</style>
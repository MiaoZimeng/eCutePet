<template>
<div class="homePage">
    <div style="background-color: #FFFEF8;">
        <div class="header">
            <el-menu
                :default-active="activeIndex"
                class="tinyNav"
                mode="horizontal"
                background-color="#e55e5e"
                text-color="#ffffff"
                active-text-color="#ffd04b"
                >
                <el-menu-item index="1" class="tinyNavPage">回到首页</el-menu-item>
                <el-menu-item index="2" class="tinyNavPage">宠物医生在线预约</el-menu-item>
                <el-submenu index="3" style="float: right; background-color: #e55e5e;" class="tinyNavPage">
                    <template slot="title">快速导航</template>
                    <el-menu-item index="4-1" style="margin-top: -29px;">商品库</el-menu-item>
                    <el-menu-item index="4-2">疾病百科</el-menu-item>
                    <el-menu-item index="4-3">问诊预约</el-menu-item>
                </el-submenu>
                <el-menu-item index="5" style="float: right" class="tinyNavPage">关于我们</el-menu-item>
                <el-menu-item v-if=true index="4" style="float: right" class="tinyNavPage">
                    <router-link to="/login" tag="span" @click.native="$event.preventDefault()">  
                        立即登录  
                    </router-link>
                </el-menu-item>
                <el-menu-item v-else  index="4" style="float: right" class="tinyNavPage">个人中心</el-menu-item>
            </el-menu>
        </div>

        <div>
            <el-menu
                :default-active="activeIndex2"
                class="el-menu-demo"
                mode="horizontal"
                @select="handleSelect"
                text-color="#BB7052"
                style="background-color: #fdf9db;
                margin-top: -1px;
                font-weight: bold;
                justify-content: center;
                align-items: center;"
                active-text-color="#ffd04b">
                <el-menu-item index="1" style="font-size: 22px;">E购商品库</el-menu-item>
                <el-menu-item index="2" style="margin-left:80px; font-size: 22px;">宠物疾病百科</el-menu-item>
                <el-menu-item index="3" style="margin-left:70px; font-size: 22px;">萌宠论坛</el-menu-item>
                <el-menu-item index="4" style="margin-left:70px; font-size: 22px;">问诊预约</el-menu-item>
            </el-menu>
        </div>
    </div>



    <div class="container">
        <div class="rounded-box">
            <div class="boxcontent">
                <div>
                    <img src="../assets/images/logo.png" alt="" 
                        style="display: inline-block;
                        width: 60px;
                        height: 60px;
                        margin-right: 10px;
                        margin-bottom: -20px;">
                    <p style="display: inline-block;
                            font-size: 30px;
                            margin-top: 20px;
                            margin-right: 10px;">E购商品库</p>
                    <el-input placeholder="搜索你感兴趣的商品" 
                        style="display: inline-block;
                            max-width: 600px;" 
                        v-model="keyWord" clearable></el-input>
                    <el-button type="primary" @click='searchList' class="shopButton" 
                      style="background-color: #9c91ff;
                            border-color: #9c91ff;">搜索</el-button>
                </div>

                <div>
                    <el-button v-if="sortType1===0" type="primary" @click='sortByPrice' class="shopButton">价格⬇</el-button>
                    <el-button v-else type="primary" @click='sortByPrice' class="shopButton">价格⬆</el-button>

                    <el-button v-if="sortType2===0" type="primary" @click='sortBySold' class="shopButton">销量⬇</el-button>
                    <el-button v-else type="primary" @click='sortBySold' class="shopButton">销量⬆</el-button>

                    <el-button v-if="sortType3===0" type="primary" @click='sortByClick' class="shopButton">点击量⬇</el-button>
                    <el-button v-else type="primary" @click='sortByClick' class="shopButton">点击量⬆</el-button>
                </div>

                <el-divider content-position="left"></el-divider>

                <!-- <ul> 之前的示例
                    <li v-for='item in filterGoods' :key=item.id>
                    {{item.title}} —— 单价： {{item.price}} —— 类型：{{item.type}}
                    </li>
                </ul> -->

                <div id="shoplist">
                    <ul v-for="(item,index) in filterGoods" style="list-style-type: none;">
                        <li class="item">
                            <div class="img_box"><img v-bind:src="item.image_url" alt=""></div>
                            <h5 v-html="item.title"></h5>
                            <p v-if="item.category === 1">标签：宠物零食</p>  
                            <p v-else-if="item.category === 2">标签：宠物药品</p>
                            <p v-else-if="item.category === 3">标签：宠物玩具</p>    
                            <p v-else>标签：其他类别</p>
                            <div class="product-details">
                              <p>点击量：{{ item.click_num }}</p>
                              <p>点赞数：{{ item.favor_count }}</p>
                              <p>销量：{{ item.sold_num }}</p>
                            </div>
                            <span :style="{textAlign: 'left', color: 'red', fontSize: '21px'}">&yen;{{item.price}}</span>
                        </li>
                    </ul>
                </div>

            </div>
        </div>
    </div>
    
    <div>
        <div class="footer">
            <div class="footer-logo">
            <img src="../assets/images/logo.png" alt="">
            <h3>E萌宠</h3>
            </div>
            <div class="footer-link">
            <a href="https://www.hit.edu.cn" target="_blank">HIT主页</a><span>|</span>
            <a href="https://cn.vuejs.org/" target="_blank">Vue.js官网</a><span>|</span>
            <a href="https://space.bilibili.com/102597382?spm_id_from=333.1007.0.0" target="_blank">bilibili</a><span>|</span>
            <a href="https://blog.csdn.net/qq_60595239?type=blog" target="_blank">csdn</a>
            </div>
            <div class="copyright">Copyright ©2024 <span class="domain">www.Epet.com</span> All Rights Reserved.</div>
        </div>

    </div>
</div>
</template>

<script>
import axios from "axios";
import { getNormList, sortList, searchList } from "../api/api.js"
export default {
    name: "login",
    data () {
        return { 
        goods:[],
        keyWord:'', 
        sortType1:0,
        sortType2:0,
        sortType3:0,
        }
    },

    async created() {  
      getNormList().then(respond =>{
        if(respond){
            this.goods = respond.data.results
        }
        else{
            this.$message.error("请求商品列表失败！"); 
        }
    }).catch(error => {  
            console.error('Request failed:', error);  
            this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
        });    
    },  
    computed:{
    filterGoods(){  //这个  filterGoods  就是我们上面循环商品的数据列表，也是我们要计算的属性
        //使用 computed 一定要于返回值，但是因为需要多条件过滤，所以先用变量 filterArr 先储存，最后过滤完再返回
        const filterArr = this.goods.filter((item)=>{  //使用 filter 进行过滤，必须使用 return 的方式返回，注： filter不会改变原数组,它返回过滤后的新数组
        return item.title;  //判断是否包含输入的关键词， -1代表没找着
        })
        return filterArr   //最后把排序好的数据return 回去
        },
    },
    methods:{
      isLogin(){
        return this.$store.state.isLoggedIn; 
      },
      sortByPrice(){
        if(this.sortType1 === 0)
        {
          sortList("-price").then(respond =>{
          if(respond){
              this.goods = respond.data.results
          }
          else{
              this.$message.error("请求商品列表失败！"); 
          }
          }).catch(error => {  
              console.error('Request failed:', error);  
              this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
          });    
          this.sortType1 = 1;
        }
        else
        {
          sortList("price").then(respond =>{
          if(respond){
              this.goods = respond.data.results
          }
          else{
              this.$message.error("请求商品列表失败！"); 
          }
          }).catch(error => {  
              console.error('Request failed:', error);  
              this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
          });    
          this.sortType1 = 0;
        }
        
      },
      sortBySold(){
        if(this.sortType2 === 0)
        {
          sortList("-sold_num").then(respond =>{
          if(respond){
              this.goods = respond.data.results
          }
          else{
              this.$message.error("请求商品列表失败！"); 
          }
          }).catch(error => {  
              console.error('Request failed:', error);  
              this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
          });    
          this.sortType2 = 1;
        }
        else
        {
          sortList("sold_num").then(respond =>{
          if(respond){
              this.goods = respond.data.results
          }
          else{
              this.$message.error("请求商品列表失败！"); 
          }
          }).catch(error => {  
              console.error('Request failed:', error);  
              this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
          });    
          this.sortType2 = 0;
        }
      },
      sortByClick(){
        if(this.sortType3 === 0)
        {
          sortList("-click_num").then(respond =>{
          if(respond){
              this.goods = respond.data.results
          }
          else{
              this.$message.error("请求商品列表失败！"); 
          }
          }).catch(error => {  
              console.error('Request failed:', error);  
              this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
          });    
          this.sortType3 = 1;
        }
        else
        {
          sortList("click_num").then(respond =>{
          if(respond){
              this.goods = respond.data.results
          }
          else{
              this.$message.error("请求商品列表失败！"); 
          }
          }).catch(error => {  
              console.error('Request failed:', error);  
              this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
          });    
          this.sortType3 = 0;
        }
      },
      searchList(){
        searchList(this.keyWord).then(respond =>{
        if(respond){
            this.goods = respond.data.results
        }
        else{
            this.$message.error("请求商品列表失败！"); 
        }
        }).catch(error => {  
            console.error('Request failed:', error);  
            this.$message.error("请求商品列表失败，请检查网络或稍后再试！");  
        });    
      },
    }
}
</script>

<style scoped>
.homePage::before{
content:"";
background-color: #FEFFF9;
/* background-image: url("../assets/images/bg1.jpg"); */
mix-blend-mode: multiply;
opacity:1;
background-repeat: repeat;
z-index:-1;
background-size: 100% 100%;
background-attachment:fixed;
width: 100%;
height: 100%;
position:absolute;
top:0px;
left:0px;
}
.homePage{
    margin: 0px;
    width: 100%;
    height: 100%;
    min-height: 100vh;
}
.footer{
  height: 234px;
  border-top: 4px solid #FF6600;
  background-color: #e55e5e;
  color: rgb(230, 169, 161);
  font-size: 16px;
  text-align: center;
.footer-logo{
  margin-top: 20px;
  margin-bottom: 20px;
}
img{
  width: 100px;
  height: 100px;
  margin-bottom: -15px;
  margin-left: -10px;
}
h3{
    color: rgb(255, 255, 255);
}
.footer-link{
  a{
    color: rgb(230, 169, 161);
    display: inline-block;
  }
  span{
    margin: 0 10px;
  }
  margin-bottom: 13px;
}
.copyright{
  .domain{
    color: rgb(230, 169, 161);
  }
}
}
.tinyNav{
    align-items: center;
    max-height: 40px;
    margin-top: -20px;

}
.tinyNavPage{
    background-color: none;
    position: relative;
}
.shopButton{
    background-color: #e55e5e;
    border-color: #e55e5e;
}
.container {  
  display: flex;  
  justify-content: center; /* 水平居中 */   
  min-height: 120vh; /* 假设你想让容器占据整个视口高度 */  
}  
  
.rounded-box {  
  position: relative; /* 为了定位伪元素 */  
  width: calc(100vw * 4 / 5); /* 宽度为页面的三分之二 */  
  padding: 10px;  
  border-radius: 10px;  
  background-color: #FEFFF9;  
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); /* 立体阴影 */  
  /* 其他你需要的样式，如margin等 */  
    
  /* 伪元素用于发光边框 */  
  ::before {  
    content: '';  
    position: absolute;  
    top: -2px; /* 根据边框宽度调整 */  
    left: -2px; /* 根据边框宽度调整 */  
    right: -2px; /* 根据边框宽度调整 */  
    bottom: -2px; /* 根据边框宽度调整 */  
    border-radius: 12px; /* 稍大于.rounded-box的border-radius */  
    z-index: -1; /* 确保在内容之下 */  
    pointer-events: none; /* 防止伪元素干扰点击事件 */  
      
    /* 发光边框效果，使用box-shadow */  
    box-shadow: 0 0 10px 2px rgba(255, 255, 200, 0.5);  
  }  
}  
  
/* 如果有需要，给内容添加一些样式 */  
.rounded-box .content {  
  position: relative;  
  z-index: 2; /* 确保在伪元素之上 */  
  /* 其他内容样式 */  
} 
  
.box-content {  
  display: flex;  
  flex-direction: column;  
  align-items: center; /* 垂直居中内容 */  
  /* 其他你需要的样式 */  
}  
  
/* 图片和文本的样式 */  
.rounded-box img {  
  width: 60px;  
  height: 60px;  
  margin-right: 10px;  
  display: inline-block;  
  vertical-align: middle; /* 与文本垂直对齐 */  
}  
  
.rounded-box p {  
  font-size: 30px;  
  margin-top: 10px; /* 根据需要调整与图片的间距 */  
  margin-right: 10px;  
  display: inline-block;  
  vertical-align: middle; /* 与图片垂直对齐 */  
}  

#ashoplist {
    width: 960px;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
}

.product-details {  
  /* 使用 flex 布局让子元素在同一行显示 */  
  display: flex;  
  align-items: center; /* 垂直居中 */  
  margin-bottom: 10px;
}  
.product-details p {  
  margin: 10px 0px; /* 移除所有外边距 */  
  padding: 0; /* 移除所有内边距 */ 
}

.item {
    border: 2px solid #ccc; /* 边框样式 */  
    border-radius: 10px; /* 边框圆角 */  
    padding: 10px; /* 内边距 */  
    margin-bottom: 20px; /* 下外边距，用于分隔不同的商品列表 */  
    background-color: #fff; /* 背景色 */  
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 阴影效果 */  
    float: left;
    width: 240px;
    height: 340px;
    margin: 0 5px 20px;
    text-align: center;
    background: #fff;
}

.item .img_box {
    width: 180px;
    height: 180px;
    margin: 30px auto;
}

.img_box img {
    width: 100%;
    height: 100%;
}

.item h5 {
    font-size: 12px;
    line-height: 20px;
    height: 40px;
    padding: 0 10px;
    /* white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis; */
    display: -webkit-box;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    margin-bottom: -10px;
}


.item p {
    font-size: 12px;
    line-height: 20px;
    height: 20px;
    padding: 0 10px;
    /* white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis; */
    display: -webkit-box;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    margin-bottom: -10px;
}

.more2_info_self {
    background-color: #e1251b;
    border-radius: 2px;
    color: #fff;
    padding: 0 5px;
    margin-right: 4px;
    line-height: 16px;
    height: 16px;
    font-size: 12px;
    font-style: normal;
}

</style>
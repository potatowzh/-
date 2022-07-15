<!--<template>-->
<!--    <div class="login">-->
<!--        <el-dialog-->
<!--                title="登录"-->
<!--                :visible.sync="centerVisible"-->
<!--                width="30%"-->
<!--                center>-->
<!--            <div style="margin: 20px;"></div>-->
<!--            <div style="margin-left: 30px; margin-right: 30px">-->
<!--                <el-form :model="form">-->
<!--                    <el-form-item>-->
<!--                        <el-input v-model="form.username" placeholder="username">-->
<!--                            <el-button slot="prepend" icon="el-icon-user"></el-button>-->
<!--                        </el-input>-->
<!--                    </el-form-item>-->
<!--                    <el-form-item>-->
<!--                        <el-input v-model="form.password" placeholder="password" show-password>-->
<!--                            <el-button slot="prepend" icon="el-icon-lock"></el-button>-->
<!--                        </el-input>-->
<!--                    </el-form-item>-->
<!--                </el-form>-->

<!--&lt;!&ndash;                <el-form>&ndash;&gt;-->
<!--&lt;!&ndash;                    <div class="inputElement">&ndash;&gt;-->
<!--&lt;!&ndash;                        <el-input v-model="form.username" placeholder="请输入用户名/手机号 "></el-input>&ndash;&gt;-->
<!--&lt;!&ndash;                    </div>&ndash;&gt;-->
<!--&lt;!&ndash;                    <div class="inputElement">&ndash;&gt;-->
<!--&lt;!&ndash;                        <el-input v-model="form.password" placeholder="请输入密码 "></el-input>&ndash;&gt;-->
<!--&lt;!&ndash;                    </div>&ndash;&gt;-->
<!--&lt;!&ndash;                    <div>&ndash;&gt;-->
<!--&lt;!&ndash;                        <el-button type="primary" @click="login">登录</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;                    </div>&ndash;&gt;-->
<!--&lt;!&ndash;                    <div style="text-align: right;color: white;">&ndash;&gt;-->
<!--&lt;!&ndash;                        <el-link type="warning">没有账号？去注册</el-link>&ndash;&gt;-->
<!--&lt;!&ndash;                    </div>&ndash;&gt;-->
<!--&lt;!&ndash;                </el-form>&ndash;&gt;-->

<!--            </div>-->
<!--            <div style="margin-top: 100px">-->
<!--                <el-button style="position:absolute;left: 130px;bottom: 30px" @click="setHide">取 消</el-button>-->
<!--                <el-button style="position:absolute;right: 130px;bottom: 30px" type="primary" @click="login">登 录</el-button>-->
<!--            </div>-->
<!--        </el-dialog>-->
<!--    </div>-->
<!--</template>-->


<template>
    <div class="login">
        <el-dialog
                :visible.sync="centerVisible"
                width="0%"
                center>
<!--            <div style="margin: 20px;"></div>-->
            <div class="loginPart" >
                <el-form :model="form">
                    <div class="inputElement">
                    <el-form-item>
                        <el-input v-model="form.username" placeholder="username">
                            <el-button slot="prepend" icon="el-icon-user"></el-button>
                        </el-input>
                    </el-form-item>
                    </div>
                    <div class="inputElement">
                    <el-form-item>
                        <el-input v-model="form.password" placeholder="password" show-password>
                            <el-button slot="prepend" icon="el-icon-lock"></el-button>
                        </el-input>
                    </el-form-item>
                    </div>
                </el-form>

<!--                <el-button style="position:absolute;left: 130px;bottom: 30px" @click="setHide">取 消</el-button>-->
<!--                <el-button style="position:absolute;right: 130px;bottom: 30px" type="primary" @click="login">登 录</el-button>-->

                <div style="background-color: transparent">
                    <!--登陆-->
                    <div style="position:absolute;right: 30px;bottom: 10px">
                        <el-button type="primary" @click="login()"
                                   style="width: 100%;border: solid 2px #fff;background-color: transparent;letter-spacing:10px;font-size: 18px;font-weight: bold"
                                   onmouseover="this.style.backgroundColor='#fff';this.style.color='#161616'"
                                   onmouseout="this.style.backgroundColor='transparent';this.style.color='#fff'"
                                   round>登 录
                        </el-button>
                    </div>
                    <!--注册-->
                    <div style="position:absolute;left: 30px;bottom: 10px">
                        <el-button type="primary" @click="setHide"
                                   style="width: 100%;border: solid 2px #fff;background-color: transparent;letter-spacing:10px;;font-size: 18px;font-weight: bold"
                                   onmouseover="this.style.backgroundColor='#fff';this.style.color='#161616'"
                                   onmouseout="this.style.backgroundColor='transparent';this.style.color='#fff'"
                                   round>取 消
                        </el-button>
                    </div>
                </div>
                <!--                <el-form>-->
                <!--                    <div class="inputElement">-->
                <!--                        <el-input v-model="form.username" placeholder="请输入用户名/手机号 "></el-input>-->
                <!--                    </div>-->
                <!--                    <div class="inputElement">-->
                <!--                        <el-input v-model="form.password" placeholder="请输入密码 "></el-input>-->
                <!--                    </div>-->
                <!--                    <div>-->
                <!--                        <el-button type="primary" @click="login">登录</el-button>-->
                <!--                    </div>-->
                <!--                    <div style="text-align: right;color: white;">-->
                <!--                        <el-link type="warning">没有账号？去注册</el-link>-->
                <!--                    </div>-->
                <!--                </el-form>-->

            </div>
<!--            <div style="margin-top: 300px">-->
<!--                <el-button style="position:absolute;left: 130px;bottom: 30px" @click="setHide">取 消</el-button>-->
<!--                <el-button style="position:absolute;right: 130px;bottom: 30px" type="primary" @click="login">登 录</el-button>-->
<!--            </div>-->
        </el-dialog>
    </div>
</template>

<script>
    import POST from "../../api/POST";
    import Cookies from "js-cookie";

    export default {
        name: "loginWindow",
        data() {
            return {
                centerVisible: false,
                passwordAgain: '',
                form: {
                    username: '',
                    password: ''
                }
            }
        },
        methods: {
            setVisible() {
                this.centerVisible = true
            },
            setHide() {
                this.centerVisible = false
            },
            login() {
                POST.login(this.form).then(res => {
                    if (res.code === 200) {
                        Cookies.set('token', res.token);
                        this.$message({
                            type: 'success',
                            message: '登录成功！'
                        });
                        let info={
                            username: this.form.username,
                        };
                        Cookies.set('info', info);
                        this.$router.push({path: `/camera`});
                    } else {
                        this.$message({
                            type: 'info',
                            message: '登录失败，请检查用户名与密码是否正确。'
                        });
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .loginPart{
        position:absolute;
        /*定位方式绝对定位absolute*/
        top:70%;
        left:50%;
        /*顶和高同时设置50%实现的是同时水平垂直居中效果*/
        transform:translate(-50%,-50%);
        /*实现块元素百分比下居中*/
        width:450px;
        padding:75px;
        background: rgba(0,0,0,.5);
        /*背景颜色为黑色，透明度为0.8*/
        box-sizing:border-box;
        /*box-sizing设置盒子模型的解析模式为怪异盒模型，
        将border和padding划归到width范围内*/
        box-shadow: 0px 15px 25px rgba(0,0,0,.5);
        /*边框阴影  水平阴影0 垂直阴影15px 模糊25px 颜色黑色透明度0.5*/
        border-radius:15px;
        /*边框圆角，四个角均为15px*/
    }
    .loginPart h2{
        margin:0 0 30px;
        padding:0;
        color: #fff;
        text-align:center;
        /*文字居中*/
    }
    .loginPart .inputbox{
        position:relative;
    }
    .loginPart .inputElement input{
        width: 100%;
        padding:10px 0;
        font-size:16px;
        color:#fff;
        letter-spacing: 1px;
        /*字符间的间距1px*/
        margin-bottom: 50px;
        border:none;
        border-bottom: 1px solid #fff;
        outline:none;
        /*outline用于绘制元素周围的线
        outline：none在这里用途是将输入框的边框的线条使其消失*/
        background: transparent;
        /*背景颜色为透明*/
    }

    .login{
        width:100%;
        height:100%;
    }

</style>

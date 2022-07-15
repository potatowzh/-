<template>
    <el-dialog

            :visible.sync="centerVisible"
            width="0%"
            center>
        <div style="margin: 20px;"></div>
        <!--        账号注册-->
        <div  v-if="active===0" class="form">

            <div class="signPart" style="margin-left: 30px; margin-right: 50px">
                <el-form :model="form"
                         label-width="120px"
                         label-position="labelPosition"
                         :rules="rules"
                >
                    <el-form-item label="用户名" prop="username">
                        <el-input v-model="form.username"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="password">
                        <el-input v-model="form.password" show-password></el-input>
                    </el-form-item>
                    <el-form-item label="再次输入密码" prop="checkPass">
                        <el-input v-model="form.checkPass" show-password></el-input>
                    </el-form-item>
                    <el-form-item label="身份验证码" prop="verificationID">
                        <el-input v-model="form.verificationID"></el-input>
                    </el-form-item>
                </el-form>
                <span slot="footer" class="dialog-footer">
<!--                <el-button style="position:absolute;left: 200px;bottom: 30px" @click="setHide">取 消</el-button>-->
<!--                <el-button style="position:absolute;right: 200px;bottom: 30px" type="primary"-->
<!--                           @click="signUp">注册</el-button>-->
                    <div style="background-color: transparent">
                    <!--登陆-->
                    <div style="position:absolute;right: 30px;bottom: 10px">
                        <el-button type="primary" @click="signUp"
                                   style="width: 100%;border: solid 2px #fff;background-color: transparent;letter-spacing:10px;font-size: 18px;font-weight: bold"
                                   onmouseover="this.style.backgroundColor='#fff';this.style.color='#161616'"
                                   onmouseout="this.style.backgroundColor='transparent';this.style.color='#fff'"
                                   round>注 册
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

            </span>
            </div>
        </div>

        <!--        个人信息-->
        <div v-if="active===1" class="form">
            <div class="signPart" style="margin-left: 30px; margin-right: 50px">
                <el-form :model="info"
                         label-width="120px"
                         label-position="labelPosition"
                         :rules="rules"
                >
                    <el-form-item label="用户名" >
                        <el-input v-model="info.account" disabled="disabled"></el-input>
                    </el-form-item>
                    <el-form-item label="真实姓名" prop="realname">
                        <el-input v-model="info.REAL_NAME"></el-input>
                    </el-form-item>
                    <el-form-item label="性别" prop="sex">
                        <el-select v-model="info.SEX" placeholder="请选择性别" value="">
                            <el-option label="男" value="男"></el-option>
                            <el-option label="女" value="女"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="邮箱">
                        <el-input v-model="info.EMAIL"></el-input>
                    </el-form-item>
                    <el-form-item label="电话">
                        <el-input v-model="info.PHONE"></el-input>
                    </el-form-item>
                    <el-form-item label="移动电话" prop="mobile">
                        <el-input v-model="info.MOBILE"></el-input>
                    </el-form-item>
                    <el-form-item label="说明">
                        <el-input v-model="info.DESCRIPTION"></el-input>
                    </el-form-item>
                </el-form>
                <span slot="footer" class="dialog-footer">
<!--                <el-button style="position:absolute;left: 200px;bottom: 30px" @click="setHide">取 消</el-button>-->
<!--                <el-button style="position:absolute;right: 200px;bottom: 30px" type="primary"-->
<!--                           @click="setInfo">录 入</el-button>-->
                    <div style="background-color: transparent">
                    <!--登陆-->
                    <div style="position:absolute;right: 30px;bottom: 10px">
                        <el-button type="primary" @click="setInfo"
                                   style="width: 100%;border: solid 2px #fff;background-color: transparent;letter-spacing:10px;font-size: 18px;font-weight: bold"
                                   onmouseover="this.style.backgroundColor='#fff';this.style.color='#161616'"
                                   onmouseout="this.style.backgroundColor='transparent';this.style.color='#fff'"
                                   round>录 入
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
            </span>
            </div>
        </div>
    </el-dialog>
</template>

<script>
    import POST from "../../api/POST";
    import PUT from "../../api/PUT";
    import Cookies from "js-cookie";

    export default {
        name: "signupWindow",
        data() {
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    // if (this.form.checkPass !== '') {
                    //     this.$refs.form.validateField('checkPass');
                    // }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.form.password) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                rules: {
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {required: true, validator: validatePass2, trigger: 'blur'}
                    ],
                    verificationID: [
                        {required: true, message: '请输入身份验证码', trigger: 'blur'}
                    ],
                    realname: [
                        {required: true, message: '请输入真实姓名', trigger: 'blur'}
                    ],
                    sex: [
                        {required: true, message: '请选择性别', trigger: 'blur'}
                    ],
                    mobile: [
                        {required: true, message: '请输入移动电话', trigger: 'blur'},
                        {min: 11, max: 11, message: '长度为11的数字', trigger: 'blur'}
                    ],
                },
                centerVisible: false,
                disabled: true,
                checkPass: '',
                form: {
                    username: '',
                    password: '',
                    checkPass: '',
                    verificationID: '',
                },
                active: 0,
                info: {
                    "account": "",
                    "ORG_ID": null,
                    "CLIENT_ID": null,
                    "REAL_NAME": "",
                    "SEX": "",
                    "EMAIL": "",
                    "PHONE": "",
                    "MOBILE": "",
                    "DESCRIPTION": "",
                    "ISACTIVE": "",
                    "CREATED": null,
                    "CREATEBY": null,
                    "UPDATED": null,
                    "UPDATEBY": null,
                    "REMOVE": "",
                    "DATAFILTER": "",
                    "theme": "",
                    "defaultpage": "",
                    "logoimage": "",
                    "qqopenid": "",
                    "appversion": "",
                    "jsonauth": ""
                },
            }
        },
        methods: {
            setVisible() {
                this.centerVisible = true;
                console.log('come out')
            },
            setHide() {
                this.centerVisible = false
            },
            signUp() {
                let newForm = {
                    username: this.form.username,
                    password: this.form.password,
                };
                console.log(newForm);
                POST.signUp(newForm).then(res => {
                    if (res.code === 200) {
                        Cookies.set('token', res.token);
                        this.$message({
                            type: 'success',
                            message: '注册成功！请填写个人信息'
                        });
                        this.active = 1;
                        this.info.account = this.form.username;
                    } else {
                        this.$message({
                            type: 'info',
                            message: '注册失败，请稍后再试'
                        });
                    }
                });
            },
            setInfo() {
                this.info.account = this.form.username;
                console.log(this.info);
                PUT.setInfo(this.info).then(res => {
                    if (res.code === 200) {
                        this.$message({
                            type: 'success',
                            message: '个人信息已录入'
                        });
                        let info = {
                            username: this.form.username,
                        };
                        Cookies.set('info', info);
                        this.$router.push({path: `/camera`});
                    } else {
                        this.$message({
                            type: 'info',
                            message: '个人信息录入失败，请稍后再试'
                        });
                    }
                });
            },
        }
    }
</script>

<style>
    .stepCard {
        width: 30%;
        height: 60%;
        position: absolute;
        top: 50px;
        right: 0;
        left: 20px;
        margin: auto;
    }

    .form {
        margin-top: 100px;
        margin-bottom: 80px;
    }

    .signPart{
        position:absolute;
        /*定位方式绝对定位absolute*/
        top:70%;
        left:50%;
        /*顶和高同时设置50%实现的是同时水平垂直居中效果*/
        transform:translate(-50%,-50%);
        /*实现块元素百分比下居中*/
        width:450px;
        padding:75px;
        background: rgba(0,0,0,.65);
        /*背景颜色为黑色，透明度为0.8*/
        box-sizing:border-box;
        /*box-sizing设置盒子模型的解析模式为怪异盒模型，
        将border和padding划归到width范围内*/
        box-shadow: 0px 15px 25px rgba(0,0,0,.5);
        /*边框阴影  水平阴影0 垂直阴影15px 模糊25px 颜色黑色透明度0.5*/
        border-radius:15px;
        /*边框圆角，四个角均为15px*/
    }
    .signPart h2{
        margin:0 0 30px;
        padding:0;
        color: #fff;
        text-align:center;
        /*文字居中*/
    }
    .signPart .inputbox{
        position:relative;
    }
    .signPart .inputElement input{
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


</style>

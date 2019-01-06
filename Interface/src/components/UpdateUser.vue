<template>
  <div class="login-wrap" style="text-align: center">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px"
             class="demo-ruleForm">
      <el-form-item prop="username">
        用户名：<el-input v-model="ruleForm.username" placeholder="用户名"
                  style="width: 300px"></el-input>
      </el-form-item>
      <el-form-item prop="sex">
        性别：
        <el-radio v-model="ruleForm.sex" label="男">男</el-radio>
        <el-radio v-model="ruleForm.sex" label="女">女</el-radio>
      </el-form-item>
      <el-form-item prop="iphone">
        手机号：<el-input placeholder="手机号" v-model="ruleForm.iphone"
                  style="width: 300px"></el-input>
      </el-form-item>
      <el-form-item prop="iphone">
        头像：
        <el-upload
          class="upload-demo"
          drag
          action="https://jsonplaceholder.typicode.com/posts/"
          multiple>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>
      <div class="login-btn">
        <el-button type="primary" style="width: 300px"
                   @click="submitForm('ruleForm')">确定
        </el-button>
      </div>
      <div>
        <router-link to="/user/">返回</router-link>
      </div>
    </el-form>
  </div>
</template>

<script>
  export default {
    data: function () {
      return {
        ruleForm: {
          username: '',
          sex: '',
          iphone: '',
          head_portrait: ''
        },
        rules: {
          username: [
            {required: true, message: '请输入用户名', trigger: 'blur'}
          ],
          sex: [
            {required: true, message: '请选择性别', trigger: 'blur'}
          ],
          iphone: [
            {required: true, message: '请输入手机号', trigger: 'blur'}
          ],

        },
        state: false,
        sites: []
      }
    },
    mounted: function () {
      this.getuser();
    },
    methods: {
      submitForm(formName) {
        var _this = this;
        _this.state = false;
        this.$refs[formName].validate((valid) => {
          if (valid) {
            var id = _this.$route.params.id;
            this.$axios.put('update_user/' + id, _this.ruleForm).then((res) => {
              this.$router.push('/user/');
            }).catch((err) => {
              _this.state = true;
              console.log(err);
            });
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      getuser() {
        var id = this.$route.params.id;
        this.$axios.get('update_user/' + id).then((res) => {
          this.sites = res.data;
          this.ruleForm.username = this.sites.username;
          this.ruleForm.sex = this.sites.sex;
          this.ruleForm.iphone = this.sites.iphone;
        })
      },
      handleAvatarSuccess(res, file) {
        this.ruleForm.head_portrait = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      }
    }
  }
</script>

<style scoped>
  .login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .ms-title {
    position: absolute;
    top: 50%;
    width: 100%;
    margin-top: -230px;
    text-align: center;
    font-size: 30px;
    color: #fff;

  }

  .ms-login {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 300px;
    height: 160px;
    margin: -150px 0 0 -190px;
    padding: 40px;
    border-radius: 5px;
    background: #fff;
  }

  .login-btn {
    text-align: center;
  }

  .login-btn button {
    width: 100%;
    height: 36px;
  }

  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }

  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }

  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }

  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }


</style>

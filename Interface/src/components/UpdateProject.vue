<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-dropdown-item>
                <router-link to="/project/" style="text-decoration: none;">项目
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/testcase/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/user/"
                             style="text-decoration: none;">用户管理
                </router-link>
              </el-dropdown-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>
                <router-link to="/url_list/" style="text-decoration: none;">域名
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_list/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/case_suite_list/"
                             style="text-decoration: none;">测试套件
                </router-link>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span>
        </el-header>
        <el-main>
          <el-form :model="ruleForm" :rules="rules" ref="ruleForm"
                   label-width="0px" class="demo-ruleForm">
            <el-form-item prop="project_name">
              <label for="project_name"
                     style="padding-left: 400px">项目名称：</label>
              <el-input name="project_name" v-model="ruleForm.project_name"
                        style="width: 300px;"></el-input>
            </el-form-item>
            <span v-if="error_message.project_name !== ''"
                  style="color: red; padding-left: 550px">{{error_message.project_name}}</span>
            <el-form-item prop="permanent_address">
              <label for="permanent_address"
                     style="padding-left: 430px">域名：</label>
              <el-input name="permanent_address"
                        v-model="ruleForm.permanent_address"
                        style="width: 300px"
                        @keyup.enter.native="updateproject('ruleForm')"></el-input>
            </el-form-item>
            <span v-if="error_message.permanent_address !== ''"
                  style="color: red; padding-left: 550px">{{error_message.permanent_address}}</span>
            <br>
            <el-form-item prop="login_way">
              <label for="login_way"
                     style="padding-left: 430px">登陆方式：</label>
              <!--<el-input name="request_header"-->
              <!--v-model="ruleForm.request_header"-->
              <!--style="width: 300px"-->
              <!--@keyup.enter.native="addproject('ruleForm')"></el-input>-->
              <el-select v-model="ruleForm.login_way">
                <el-option v-for="item in loginway_list" :key="item"
                           :value="item">
                  {{item}}
                </el-option>
              </el-select>
            </el-form-item>
            <span v-if="error_message.login_way !== ''"
                  style="color: red; padding-left: 550px">{{error_message.login_way}}</span>
            <el-form-item prop="request_header">
              <label for="request_header"
                     style="padding-left: 430px">请求头：</label>
              <!--<el-input name="request_header"-->
              <!--v-model="ruleForm.request_header"-->
              <!--style="width: 300px"-->
              <!--@keyup.enter.native="addproject('ruleForm')"></el-input>-->
              <el-select v-model="ruleForm.request_header">
                <el-option v-for="item in header_list" :key="item"
                           :value="item">
                  {{item}}
                </el-option>
              </el-select>
            </el-form-item>
            <span v-if="error_message.request_header !== ''"
                  style="color: red; padding-left: 550px">{{error_message.request_header}}</span>
            <br>
            <el-button type="button" value="保存"
                       @click="updateproject('ruleForm')"
                       size="middle"
                       style="margin-left: 500px">保存
            </el-button>
            <router-link to="/project/">
              <el-button value="取消" size="middle" style="margin-left: 80px">取消
              </el-button>
            </router-link>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "UpdateProject",
    data() {
      return {
        ruleForm: {
          project_name: '',
          permanent_address: '',
          request_header: '',
          login_way: '',
        },
        rules: {
          project_name: [
            {required: true, message: '请输入项目名称', trigger: 'blur'}
          ],
          permanent_address: [
            {required: true, message: '请输入固定IP', trigger: 'blur'}
          ],
          request_header: [
            {required: true, message: '请输入请求头', trigger: 'blur'}
          ],
          login_way: [
            {required: true, message: '请输入登陆方式', trigger: 'blur'}
          ],

        },
        error_message: [],
        update_list: [],
        loginway_list: ['cookies', 'JWT'],
        header_list: ["{'Content-Type': 'application/json'}",
          "{'Content-Type: application/x-www-form-urlencoded'}"]
      }
    },
    mounted: function () {
      this.getproject();
    },
    methods: {
      updateproject(formName) {
        var id = this.$route.params.id;
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$axios.put('update_project/' + id, this.ruleForm).then((response) => {
              if (response.status === 200) {
                console.log(response);
                this.addOpen();
                this.$router.push('/project/')

              }


            }).catch((error) => {
              console.log(error);
              this.error_message = error.response.data

            });
          }
        })
      },
      addOpen() {
        this.$notify({
          title: '成功',
          message: '修改域名成功',
          type: 'success'
        });
      },
      getproject() {
        var id = this.$route.params.id;
        this.$axios.get('update_project/' + id).then((res) => {
          console.log(res.data);
          if (res.status === 200) {
            this.update_list = res.data;
            this.ruleForm.project_name = this.update_list.project_name;
            this.ruleForm.permanent_address = this.update_list.permanent_address;
            this.ruleForm.request_header = this.update_list.request_header;
            this.ruleForm.login_way = this.update_list.login_way
          }

        }).catch((err) => {
          console.log(err.data.results);
        })
      },
      // updateproject() {
      //
      // }
    },
  }
</script>

<style scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
</style>

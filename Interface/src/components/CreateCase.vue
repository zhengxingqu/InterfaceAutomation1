<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-dropdown-item>
                <router-link to="/project/" style="text-decoration: none;">域名
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/testcase/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-dropdown-item>
              <el-dropdown-item>
                <router-link to="/user_list/"
                             style="text-decoration: none;">测试套件
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
            <el-form-item prop="case_name">
              <label for="case_name"
                     style="padding-left: 400px">项目名称：</label>
              <el-input name="case_name" v-model="ruleForm.case_name"
                        style="width: 300px;"></el-input>
            </el-form-item>
            <span v-if="error_message.project_name !== ''"
                  style="color: red; padding-left: 550px">{{error_message.case_name}}</span>
            <el-form-item prop="request_type">
              <label for="request_type"
                     style="padding-left: 430px">请求类型：</label>
              <!--<el-input name="request_type"-->
              <!--v-model="ruleForm.request_type"-->
              <!--style="width: 300px"></el-input>-->
              <el-select v-model="ruleForm.request_type">
                <el-option v-for="item in type_list" :key="item"
                           :value="item">{{item}}
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item prop="project_name">
              <label for="project_name"
                     style="padding-left: 430px">项目名称：</label>
              <!--<el-input name="request_type"-->
              <!--v-model="ruleForm.request_type"-->
              <!--style="width: 300px"></el-input>-->
              <el-select v-model="ruleForm.project_name">
                <el-option v-for="item in sites" :key="item.project_name"
                           :value="item.project_name">{{item.project_name}}
                </el-option>
              </el-select>
            </el-form-item>
            <span v-if="error_message.project_name !== ''"
                  style="color: red; padding-left: 550px">{{error_message.project_name}}</span>
            <el-form-item prop="request_param">
              <label for="request_param"
                     style="padding-left: 430px">请求参数：</label>
              <el-input name="request_param"
                        v-model="ruleForm.request_param"
                        style="width: 300px"></el-input>
            </el-form-item>
            <span v-if="error_message.request_param !== ''"
                  style="color: red; padding-left: 550px">{{error_message.request_param}}</span>
            <!--<el-form-item prop="request_header">-->
              <!--<label for="request_header"-->
                     <!--style="padding-left: 430px">请求头：</label>-->
              <!--<el-input name="request_header"-->
                        <!--v-model="ruleForm.request_header"-->
                        <!--style="width: 300px"></el-input>-->
            <!--</el-form-item>-->
            <!--<span v-if="error_message.request_header !== ''"-->
                  <!--style="color: red; padding-left: 550px">{{error_message.request_header}}</span>-->
            <el-form-item prop="expected_result">
              <label for="expected_result"
                     style="padding-left: 430px">预期结果：</label>
              <el-input name="expected_result"
                        v-model="ruleForm.expected_result"
                        style="width: 300px"></el-input>
            </el-form-item>
            <span v-if="error_message.expected_result !== ''"
                  style="color: red; padding-left: 550px">{{error_message.expected_result}}</span>
            <el-form-item prop="login_way">
              <label for="login_way"
                     style="padding-left: 430px">登陆方式：</label>
              <el-input name="login_way"
                        v-model="ruleForm.login_way"
                        style="width: 300px"></el-input>
            </el-form-item>
            <span v-if="error_message.login_way !== ''"
                  style="color: red; padding-left: 550px">{{error_message.login_way}}</span>

            <br>
            <el-button type="button" value="保存" @click="addcase('ruleForm')"
                       size="middle"
                       style="margin-left: 500px">保存
            </el-button>
            <router-link to="/testcase/">
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
    name: "CreateCase",
    data() {
      return {
        ruleForm: {
          case_name: '',
          request_type: '',
          request_param: '',
          // request_header: '',
          expected_result: '',
          login_way: '',
          project_name: '',
        },
        rules: {
          case_name: [
            {required: true, message: '请输入测试用例名称', trigger: 'blur'}
          ],
          request_type: [
            {required: true, message: '请输入请求类型', trigger: 'blur'}
          ],
          request_param: [
            {required: true, message: '请输入请求参数', trigger: 'blur'}
          ],
          // request_header: [
          //   {required: true, message: '请输入请求头', trigger: 'blur'}
          // ],
          expected_result: [
            {required: true, message: '请输入预期结果', trigger: 'blur'}
          ],
          login_way: [
            {required: true, message: '请输入登陆方式', trigger: 'blur'}
          ],
          project_name: [
            {required: true, message: '请输入项目名称', trigger: 'blur'}
          ]
        },
        error_message: [],
        type_list: ['get', 'post', 'delete', 'put'],
        sites: [],
      }
    },
    mounted: function () {
      // this.addurls();
      this.getprojects()
    },
    methods: {
      addcase(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {

            this.$axios.post('create_case/', this.ruleForm).then((response) => {
              if (response.status === 201) {
                console.log(response);
                // this.addOpen();
                // this.success_message();
                this.$router.push('/testcase/')

              }


            }).catch((error) => {
              console.log(error);
              this.error_message = error.response.data

            });
          }
        })
      },
      getprojects: function () {
          this.$axios.get('project_list/?page=' + this.currentPage).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results
          })
        }
      },
      success_message() {
        this.$notify({
          title: '成功',
          message: '新增域名成功',
          type: 'success'
        });
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

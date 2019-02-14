<template>
  <div>
    <el-container style="height: 800px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '4']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <router-link to="/project/" style="text-decoration: none;">项目
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/testcase/" style="text-decoration: none;">
                  测试用例
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-4">
                <router-link to="/user/" style="text-decoration: none;">
                  用户管理
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-5">
                <router-link to="/echarts/" style="text-decoration: none;">
                  报告
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-6">
                <router-link to="/timing_task/" style="text-decoration: none;">
                  定时任务
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-7">
              </el-menu-item>
              <el-menu-item index="1-8">
              </el-menu-item>
              <el-menu-item index="1-9">
              </el-menu-item>
              <el-menu-item index="1-10">
              </el-menu-item>
              <el-menu-item index="1-11">
              </el-menu-item>
              <el-menu-item index="1-12">
              </el-menu-item>
              <el-menu-item index="1-13">
              </el-menu-item>
              <el-menu-item index="1-14">
              </el-menu-item>
              <el-menu-item index="1-15">
              </el-menu-item>
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
                <router-link to="/login/" style="text-decoration: none;">退出
                </router-link>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>{{username}}</span>
        </el-header>

        <el-main>
          <el-form>
            <!--<el-button type="primary" style="color: #fff;-->
            <!--background-color: #71c7ad;-->
            <!--border-color: #71c7ad;-->
            <!--transition: all .2s ease-out;">-->
            <!--<i class="el-icon-plus"></i>-->
            <!--新增-->
            <!--</el-button>-->
            <!--</router-link>-->
            <el-button size="small" @click="dialogFormVisible = true"><i
              class="el-icon-plus"></i>新增
            </el-button>
            <el-dialog title="定时任务" :visible.sync="dialogFormVisible">
              <el-form :model="ruleForm" :rules="rules" ref="ruleForm"
                       class="demo-ruleForm">
                <el-form-item label="任务名称" prop="task_name">
                  <el-input v-model="ruleForm.task_name"
                            autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="执行时间" prop="time">
                  <div class="block">
                    <el-date-picker
                      v-model="ruleForm.time"
                      type="datetime"
                      placeholder="选择日期时间"
                      value-format="yyyy-MM-dd HH:mm:ss">
                    </el-date-picker>
                  </div>
                </el-form-item>
                <el-form-item label="状态" prop="is_stop">
                  <el-radio v-model="ruleForm.is_stop" label="正常">正常</el-radio>
                  <el-radio v-model="ruleForm.is_stop" label="停用">停用</el-radio>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="create_task('ruleForm')">确
                  定
                </el-button>
              </div>
            </el-dialog>
            <el-input name="search_case_name" placeholder="定时任务名称"
                      v-model="search_timing_task" size="medium"
                      style="width: 200px;padding-right: 36px"
                      @change="search"></el-input>
            <el-button type="button" value="搜索" icon="el-icon-search"
                       @click="search">搜索
            </el-button>
            <br>
            <br>
            <div class="dxy-dividing-line"
                 style="margin-top: 0px; margin-bottom: 24px;"></div>
            <el-button class="small" type="warning" size="small"
                       @click="removeBatch"
                       :loading=delete_status>批量删除
            </el-button>
            <!--<el-button size="small" @click="dialogTableVisible = true">定时任务</el-button>-->


          </el-form>
          <el-table
            :data="cases"
            style="margin-top: 20px;width: 100%" stripe
            ref="multipleTable" tooltip-effect="dark"
            @selection-change="handleSelectionChange" border
            :header-cell-style="getRowClass">
            <el-table-column type="selection" width="55"
                             class="selection"></el-table-column>
            <el-table-column prop="id" label="编号" width="140" fixed sortable>
            </el-table-column>
            <el-table-column prop="task_name" label="定时任务名称" width="120">
            </el-table-column>
            <el-table-column prop="time" label="执行时间" width="120">
            </el-table-column>
            <el-table-column prop="is_stop" label="状态" width="120">
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <!--<el-button size="mini" @click="getUpdate(scope.row.ym_id)" type="primary">编辑</el-button>-->
                <!--&lt;!&ndash;<el-button size="mini" type="danger" @click="getDelete(scope.row.ym_id)">删除</el-button>&ndash;&gt;-->
                <!--<el-button type="danger" @click="dialogVisible = true" size="mini">删除</el-button>-->
                <el-button @click="getUpdate(scope.row.id)" type="button"
                           style="border: transparent;background-color: transparent">
                  <span style="color: #71c7ad;">编辑</span>
                </el-button>
                <el-button @click="getDelete(scope.row.id)" type="button"
                           style="border: transparent;background-color: transparent">
                  <span style="color: #71c7ad;">删除</span>
                </el-button>
                <el-button type="button" @click="getStop(scope.row.id)"
                           style="border: transparent;background-color: transparent"><span v-if="scope.row.is_stop === '正常'"
                  style="color: #71c7ad;">暂停</span><span v-else-if="scope.row.is_stop === '停用'"
                  style="color: #71c7ad;">启用</span></el-button>
                <!--<el-button type="button" @click="getStop(scope.row.id)"-->
                           <!--style="border: transparent;background-color: transparent"><span v-show="scope.row.is_stop === '停用'"-->
                  <!--style="color: #71c7ad;">启用</span></el-button>-->
                <!--<el-dialog-->
                <!--title="提示"-->
                <!--:visible.sync="dialogVisible"-->
                <!--width="30%"-->
                <!--:modal-append-to-body='false'>-->
                <!--<span>确定要删除该数据吗？</span>-->
                <!--<span slot="footer" class="dialog-footer">-->
                <!--<el-button @click="dialogVisible = false">取 消</el-button>-->
                <!--<el-button type="primary"-->
                <!--@click="getDelete(scope.row.id)">确 定</el-button>-->
                <!--</span>-->
                <!--</el-dialog>-->
              </template>


            </el-table-column>
          </el-table>
          <div class="block" style="margin-top: 30px;margin-left: 750px">
            <!--<el-pagination-->
            <!--:page-sizes="[5, 10, 20, 40]"-->
            <!--layout="total, sizes, prev, pager, next, jumper"-->
            <!--:total="totalNum">-->
            <!--</el-pagination>-->
          </div>
        </el-main>
      </el-container>
    </el-container>

  </div>
</template>

<script>
  export default {
    name: "TimeingTask",
    data() {
      return {
        ruleForm: {
          task_name: '',
          time: '',
          is_stop: ''
        },
        rules: {
          task_name: [
            {required: true, message: '请输入名称', trigger: 'blur'}
          ],
          time: [
            {required: true, message: '请输入执行时间', trigger: 'blur'}
          ],
          is_stop: [
            {required: true, message: '请选择状态', trigger: 'blur'}
          ],
        },
        search_timing_task: '',
        cases: [],
        delete_status: false,
        username: localStorage.username,
        dialogFormVisible: false,
        error_message: [],
        multipleSelection: [],
        case_list: [],


      }
    },
    methods: {
      getStop: function (row) {
        this.$confirm('此操作将停用该定时任务, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.delete_status = true;
          this.$axios.delete('stop_task/' + row).then((res) => {
            if (res.data !== '') {
              this.delete_status = false
            }
            console.log(res);
            // this.dialogVisible = false;
            // this.deleteOpen();
            this.getTask();
            this.$message({
              type: 'success',
              message: '操作成功!'
            });
            this.case_list.splice(0, this.case_list.length)


          }).catch((error) => {
            if (error.response.status === 417) {
              this.$message({
                type: 'warning',
                message: '该用例已被使用'

              });
            }
            if (error.response.status === 404) {
              this.$message({
                type: 'warning',
                message: error.response.data.detail
              });
              this.getTask()
            }
            console.log(error)
          })

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消暂停'
          });
        });
      },
      getDelete: function (row) {
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.delete_status = true;
          this.$axios.delete('delete_task/' + row).then((res) => {
            if (res.data !== '') {
              this.delete_status = false
            }
            console.log(res);
            // this.dialogVisible = false;
            // this.deleteOpen();
            this.getTask();
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
            this.case_list.splice(0, this.case_list.length)


          }).catch((error) => {
            if (error.response.status === 417) {
              this.$message({
                type: 'warning',
                message: '该用例已被使用'

              });
            }
            if (error.response.status === 404) {
              this.$message({
                type: 'warning',
                message: error.response.data.detail
              });
              this.getTask()
            }
            console.log(error)
          })

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      create_task(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {

            this.$axios.post('add_task/', this.ruleForm).then((res) => {
              console.log(res);
              if (res.status === 201) {
                this.addOpen();
                this.getTask();
              }
              this.dialogFormVisible = false;

            }).catch((err) => {
              console.log(err.response);
              this.error_message = err

            });
          }
        })
      },
      addOpen() {
        this.$notify({
          title: '成功',
          message: '新增定时任务成功',
          type: 'success'
        });
      },
      search: function () {
        this.$axios.get('search_task/', {
          params: {
            search: this.search_timing_task,
          }
        }).then((res) => {
          console.log(res.data.results);
          this.cases = res.data.results
        }).catch(function (error) {

          console.log(error)

        })
      },
      handleSelectionChange(multipleSelection) {
        this.multipleSelection = multipleSelection;
      },
      removeBatch() {
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.multipleSelection.forEach(i => {
            this.case_list.push(i.id)
          });
          this.delete_status = true;
          this.$axios.put('delete_tasks/', {"ids": this.case_list}).then((res) => {
            if (res.data !== '') {
              this.delete_status = false
            }
            console.log(res);
            this.getTask();
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
            this.case_list.splice(0, this.case_list.length)
          }).catch((err) => {
            console.log(err)
          })

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      getRowClass({row, column, rowIndex, columnIndex}) {
        if (rowIndex == 0) {
          return 'background: #F0FFFF'
        } else {
          return ''
        }
      },
      getTask() {
        this.$axios.get('get_task/').then((res) => {
          this.cases = res.data.results;
        }).catch((err) => {
          console.log(err.response)
        })
      }
    },



    mounted() {
      this.getTask();
    }
  }
</script>

<style scoped>

</style>

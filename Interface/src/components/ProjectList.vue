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
            <router-link to="/add_project/">
              <el-button type="primary" style="color: #fff;
              background-color: #71c7ad;
              border-color: #71c7ad;
              transition: all .2s ease-out;">
                <i class="el-icon-plus"></i>
                新增
              </el-button>
            </router-link>
            <label for="project_name"
                   style="padding-left: 680px;padding-right: 5px">项目搜索</label>
            <el-input name="search_project_name" placeholder="项目名称/固定地址"
                      v-model="project_name" size="medium"
                      style="width: 200px;padding-right: 10px"
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
            <el-upload
              ref="upload"
              action="http://127.0.0.1:8000/upload/"
              name="picture"
              :limit="1"
              :file-list="fileList"
              :on-exceed="onExceed"
              :before-upload="beforeUpload"
              :on-preview="handlePreview"
              :on-success="handleSuccess"
              :on-remove="handleRemove">
              <el-button size="small" type="primary" style="margin-top: 10px">点击上传</el-button>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
            <!--<el-dialog-->
            <!--title="提示"-->
            <!--:visible.sync="dialogVisible"-->
            <!--width="30%"-->
            <!--:modal-append-to-body='false'>-->
            <!--<span>确定要删除该数据吗？</span>-->
            <!--<span slot="footer" class="dialog-footer">-->
            <!--<el-button @click="dialogVisible = false">取 消</el-button>-->
            <!--<el-button type="primary" @click="removeBatch(val)">确 定</el-button>-->
            <!--</span>-->
            <!--</el-dialog>-->

          </el-form>
          <el-table
            :data="sites.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="margin-top: 20px;width: 100%" stripe
            ref="multipleTable" tooltip-effect="dark"
            @selection-change="handleSelectionChange" border
            :header-cell-style="getRowClass">
            <el-table-column type="selection" width="55"
                             class="selection"></el-table-column>
            <el-table-column prop="id" label="编号" width="140" fixed sortable>
            </el-table-column>
            <el-table-column prop="project_name" label="项目名称" width="120">
            </el-table-column>
            <el-table-column prop="permanent_address" label="固定ip">
            </el-table-column>
            <el-table-column prop="request_header" label="请求头">
            </el-table-column>
            <el-table-column prop="login_way" label="登陆方式">
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
            <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[10, 20, 50, 100]"
              :page-size="10"
              layout="total, sizes, prev, pager, next, jumper"
              :total="totalNum">
            </el-pagination>
          </div>
        </el-main>
      </el-container>
    </el-container>

  </div>
</template>

<script>

  export default {
    name: "search-url",
    data() {
      return {
        sites: [],
        check_list: [],
        totalNum: 0,
        dialogVisible: false,
        currentPage: 1,
        pageSize: 10,
        multipleSelection: [],
        checklist: [],
        disabled: true,
        list1: [],
        delete_status: false,
        project_name: '',
        username: localStorage.username,
        fileList: [],
        fileName: '',
        dialogImageUrl: '',


      };

    },


    mounted: function () {
      this.getprojects();
    },
    methods: {
      handleSizeChange: function (size) {
        this.pageSize = size;
        console.log(this.pageSize);  //每页下拉显示数据
        let t = (size / 10);
        if (t <= 1) {
          this.$axios.get('project_list/').then((res) => {
            this.sites = res.data.results;
          })

        }

      },
      handleCurrentChange: function (currentPage) {
        this.currentPage = currentPage;
        console.log(this.currentPage); //点击第几页
        if (this.pageSize === 10 && currentPage <= 10) {
          this.$axios.get('project_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 10 && currentPage > 10) {
          let t = parseInt(currentPage / 10) + 1;
          this.$axios.get('project_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 20 && currentPage <= 5) {
          this.$axios.get('project_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 20 && currentPage > 5) {
          let t = parseInt(currentPage / 5) + 1;
          this.$axios.get('project_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 50 && currentPage <= 2) {
          this.$axios.get('project_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 50 && currentPage > 2) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('project_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 100 && currentPage <= 1) {
          this.$axios.get('project_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 100 && currentPage > 1) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('project_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
      },
      getprojects: function () {
        if (this.currentPage === 1) {
          this.$axios.get('project_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
            this.totalNum = res.data.count
          }).catch(function (error) {
            console.log(error)
          })
        } else {
          this.$axios.get('project_list/?page=' + this.currentPage).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results
          })
        }
      },
      search: function () {
        this.$axios.get('search_project/', {
          params: {
            search: this.project_name,
          }
        }).then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results
        }).catch(function (error) {
          console.log(error)

        })
      },
      getUpdate: function (row) {
        this.$router.push({path: "/update_project/" + row});
      },
      getDelete: function (row) {
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$axios.delete('delete_project/' + row).then((res) => {
              console.log(res);
              // this.dialogVisible = false;
              // this.deleteOpen();
              if (res.status === 204) {
                this.$router.push('/project/');
                this.getprojects();
                this.$message({
                  type: 'success',
                  message: '删除成功!'
                });
              }

              this.case_list.splice(0, this.list1.length)
            }
          ).catch((error) => {
            console.log(error.response);
            // 错误信息保护在response中
            if (error.response.status === 417) {
              this.$message({
                type: 'warning',
                message: error.response.data.message

              });
            }
            if (error.response.status === 404) {
              this.$message({
                type: 'warning',
                message: error.response.data.detail
              });
              this.getprojects()
            }

            //   if (error.status !== ''){
            //     this.$message({
            //   type: 'warning',
            //   message: '项目已被删除'
            //
            // });
            //
            //   this.getprojects();
            //   }
            console.log(error)
          })

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      // deleteOpen() {
      //   this.$notify({
      //     title: '成功',
      //     message: '删除项目成功',
      //     type: 'success'
      //   });
      // },
      handleSelectionChange(multipleSelection) {
        this.multipleSelection = multipleSelection;
      },
      removeBatch() {
        // this.multipleSelection.forEach(i => {
        //   this.list1.push(i.id)
        // });
        // this.$axios.put('delete_projects/', {"ids": this.list1}).then((res) => {
        //   if (res.data !== '') {
        //     this.delete_status = false
        //   }
        //   console.log(res);
        //   this.getprojects();
        //   this.list1.splice(0, this.list1.length)
        // }).catch((err) => {
        //   console.log(err)
        // })
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.multipleSelection.forEach(i => {
            this.list1.push(i.id)
          });
          this.delete_status = true;
          this.$axios.put('delete_projects/', {"ids": this.list1}).then((res) => {
            if (res.data !== '') {
              this.delete_status = false
            }
            console.log(res);
            this.getprojects();
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
            this.list1.splice(0, this.list1.length)
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
      handleSuccess(res, file) {
        this.$message({
          type: 'info',
          message: '文件上传成功',
          duration: 6000
        });
        if (file.response.success) {
          this.picture = file.response.message; //将返回的文件储存路径赋值picture字段
        }
        this.$axios.post('upload/', {filename: file.src})
      },
      //删除文件之前的钩子函数
      handleRemove(file, fileList) {
        this.$message({
          type: 'info',
          message: '已删除原有文件',
          duration: 6000
        });
      },
      //点击列表中已上传的文件事的钩子函数
      handlePreview(file) {
      },
      //上传的文件个数超出设定时触发的函数
      onExceed(files, fileList) {
        this.$message({
          type: 'info',
          message: '最多只能上传一个文件',
          duration: 6000
        });
      },
      //文件上传前的前的钩子函数
      //参数是上传的文件，若返回false，或返回Primary且被reject，则停止上传
      beforeUpload(file) {
        const isCSV = file.name.split('.')[1] === 'xlsx';
        const isLt5M = file.size / 1024 / 1024 < 5;

        if (!isCSV) {
          this.$message.error('上传图片必须是csv 格式!');
        }
        if (!isLt5M) {
          this.$message.error('上传图片大小不能超过 5MB!');
        }
        let formData = new FormData();
        formData.append("file", file);
        this.$axios.post('upload_project/', formData).then((res) => {
          console.log(res.data);
          this.$message.success('上传文件成功')
          this.getprojects()
        }).catch((err) => {
          console.log(err);
          this.$message.error('上传文件失败')
        });

        return isCSV && isLt5M;
      },
      handleSizeChange: function (size) {
        this.pageSize = size;
        console.log(this.pageSize);  //每页下拉显示数据
        let t = (size / 10);
        if (t <= 1) {
          this.$axios.get('case_list/').then((res) => {
            this.sites = res.data.results;
          })

        }

      },


    }
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

  .dxy-dividing-line {
    height: 0;
    margin: 16px 0;
    border: 1px dashed #f0f2f5;
  }
</style>

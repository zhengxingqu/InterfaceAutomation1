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
                <router-link to="/user_list/" style="text-decoration: none;">
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
            <router-link to="/add_user/">
              <el-button type="primary" style="color: #fff;
              background-color: #71c7ad;
              border-color: #71c7ad;
              transition: all .2s ease-out;">
                <i class="el-icon-plus"></i>
                新增
              </el-button>
            </router-link>
            <label for="project_name"
                   style="padding-left: 680px;padding-right: 5px">用例搜索</label>
            <el-input name="search_user_name" placeholder="用户名/手机号"
                      v-model="search_user" size="medium"
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
            <el-table-column prop="username" label="姓名" width="120">
            </el-table-column>
            <el-table-column prop="iphone" label="手机号码" width="120">
            </el-table-column>
            <el-table-column prop="sex" label="性别" width="120">
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
                <el-button @click="resetpwd(scope.row.id)" type="button"
                           style="border: transparent;background-color: transparent">
                  <span style="color: #71c7ad;">重置</span>
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
        search_user: "",
        id: '',
        totalNum: 0,
        dialogVisible: false,
        currentPage: 1,
        pageSize: 10,
        multipleSelection: [],
        checklist: [],
        disabled: true,
        user_list: [],
        delete_status: false,
        run_status: false,
        username: localStorage.username


      };

    },


    mounted: function () {
      this.getuser();
    },
    methods: {
      handleSizeChange: function (size) {
        this.pageSize = size;
        console.log(this.pageSize);  //每页下拉显示数据
        let t = (size / 10);
        if (t <= 1) {
          this.$axios.get('user_list/').then((res) => {
            this.sites = res.data.results;
          })

        }

      },
      handleCurrentChange: function (currentPage) {
        this.currentPage = currentPage;
        console.log(this.currentPage); //点击第几页
        if (this.pageSize === 10 && currentPage <= 10) {
          this.$axios.get('user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 10 && currentPage > 10) {
          let t = parseInt(currentPage / 10) + 1;
          this.$axios.get('user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 20 && currentPage <= 5) {
          this.$axios.get('user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 20 && currentPage > 5) {
          let t = parseInt(currentPage / 5) + 1;
          this.$axios.get('user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 50 && currentPage <= 2) {
          this.$axios.get('user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 50 && currentPage > 2) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
        if (this.pageSize === 100 && currentPage <= 1) {
          this.$axios.get('user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          })
        }
        if (this.pageSize === 100 && currentPage > 1) {
          let t = parseInt(currentPage / 2) + 1;
          this.$axios.get('user_list/?page=' + t).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
          });
        }
      },
      getuser: function () {
        if (this.currentPage === 1) {
          this.$axios.get('user_list/').then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results;
            this.totalNum = res.data.count
          }).catch(function (error) {
            console.log(error)
          })
        } else {
          this.$axios.get('user_list/?page=' + this.currentPage).then((res) => {
            console.log(res.data.results);
            this.sites = res.data.results
          })
        }
      },
      search: function () {
        this.$axios.get('search_user/', {
          params: {
            search: this.search_user,
          }
        }).then((res) => {
          console.log(res.data.results);
          this.sites = res.data.results
        }).catch(function (error) {
          console.log(error)

        })
      },
      getUpdate: function (row) {
        this.$router.push({path: "/user_update/" + row});
      },
      getDelete: function (row) {
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.delete_status = true;
          this.$axios.delete('delete_user/' + row).then((res) => {
            if (res.data !== '') {
              this.delete_status = false
            }
            console.log(res);
            // this.dialogVisible = false;
            // this.deleteOpen();
            this.getuser();
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
            this.user_list.splice(0, this.user_list.length)


          }).catch((error) => {


            console.log(error)
          })

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
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
            this.user_list.push(i.id)
          });
          this.delete_status = true;
          this.$axios.put('delete_users/', {"ids": this.user_list}).then((res) => {
            if (res.data !== '') {
              this.delete_status = false
            }
            console.log(res);
            this.getuser();
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
            this.list1.splice(0, this.user_list.length)
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
      resetpwd(id) {
        this.$router.push('/pwd_reset/' + id)
      }


      // open2() {
      //   this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
      //     confirmButtonText: '确定',
      //     cancelButtonText: '取消',
      //     type: 'warning'
      //   }).then(() => {
      //     this.getDelete(id);
      //     this.$message({
      //       type: 'success',
      //       message: '删除成功!'
      //     });
      //   }).catch(() => {
      //     this.$message({
      //       type: 'info',
      //       message: '已取消删除'
      //     });
      //   });
      // }
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

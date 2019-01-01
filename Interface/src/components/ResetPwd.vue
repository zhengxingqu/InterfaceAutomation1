<template>
  <div>
    <label for="password" style="padding-left: 450px">新密码:</label>
    <el-input v-model="password" style="width: 300px;"></el-input>
    <br>
    <label for="confirmPwd" style="padding-left: 440px">确认密码</label>
    <el-input v-model="confirmPwd" style="width: 300px;"></el-input>
    <br>
    <br>
    <el-button type="primary" style="margin-left: 550px" @click="reset">提交</el-button>
    <router-link to="/user_list/">
      <el-button type="primary" style="margin-left: 70px">取消</el-button>
    </router-link>
  </div>
</template>

<script>
  export default {
    name: "ResetPwd",
    data: function () {
      return {
        password: "",
        confirmPwd: "",
        error_message: "两次密码不一致，请确认密码",
        ids: 0
      }
    },
    methods: {
      reset: function () {
        var id = this.$route.params.id;
        this.ids = id;
          this.$axios.put("reset_pwd/" + id, {password: this.password, user_id: this.ids}).then((res) => {
            console.log(res);
            this.$router.push('/user_list/');
          }).catch((err) => {
            console.log(err)
          })


        }
      }
  }
</script>

<style scoped>

</style>

<template>
  <div id="app">
    send msg
    <img src="http://www.runoob.com/wp-content/uploads/2017/01/vue.png">
    <el-button @click.native="startHacking()">Let's do it</el-button>
    <div class="block">
      <span class="demonstration">显示默认颜色</span>
      <span class="wrapper">
    <el-button type="success">成功按钮</el-button>
    <el-button type="warning">警告按钮</el-button>
    <el-button type="danger">危险按钮</el-button>
    <el-button type="info">信息按钮</el-button>
    </span>
    </div>
    <br/>
    <div class="block">
      <span class="demonstration">hover 显示颜色</span>
      <span class="wrapper">
    <el-button :plain="true" type="success">成功按钮</el-button>
    <el-button :plain="true" type="warning">警告按钮</el-button>
    <el-button :plain="true" type="danger">危险按钮</el-button>
    <el-button :plain="true" type="info">信息按钮</el-button>
    </span>
    </div>
    <button type="button" @click="get_friends()">get friends</button>
    <p>发送到 ：</p>
    <input placeholder="userName……" ref="toUser">
    <p>content ：</p>
    <textarea placeholder="消息内容……" ref="content"></textarea>
    <div>
      <button type="button" @click="send_msg()">发送</button>
    </div>
    <ul id="ul_1">
      <li v-for="item in ITEMS">
        <img :src=item.HeadImgUrl>
        <p @click="select_user">{{item.NickName}}</p>
        <p @click="select_user">{{item.UserName}}</p>
        <p @click="select_user">__________________________________________</p>

      </li>
    </ul>
  </div>

</template>

<script>

  import axios from 'axios'

  export default {
    name: 'App',
    data: function () {
      return {
        ITEMS: [],
        img_path: "/Users/vampire/PycharmProjects/wx_helper/app/model/190123-222001.png"
      }
    },
    beforeCreate: function () {
      var context = this
      this.$post('/login').then((response) => {
        console.log(response)
      })
      // axios.post('http://127.0.0.1:7587/login').then(function (res) {
      //   // console.log(res.data.path)
      //   context.img_path = res.data.path
      //   // console.log(context.img_path)
      // })
      // console.group('beforeCreate 创建前状态===============》');

    },
    created: function () {
      console.group('created 创建完毕状态===============》');

    },
    beforeMount: function () {
      console.group('beforeMount 挂载前状态===============》');
    },
    methods: {
      startHacking() {
        // alert("1111111111")
        this.$notify({
          title: 'It Works',
          message: 'We have laid the groundwork for you. Now it\'s your time to build something epic!',
          duration: 6000
        })
      },
      send_msg() {
        var params = new URLSearchParams();
        params.append('toUser', this.$refs.toUser.value);
        params.append('msg', this.$refs.content.value);
        axios.post('http://127.0.0.1:7587/sendMsg', params).then(function (r) {
          console.log(r)
        }).catch(function (e) {
          console.log(e)
        })

      },
      get_friends() {
        var _this = this
        axios.post('http://127.0.0.1:7587/getFriends').then(function (res) {
          console.log(res)
          _this.ITEMS = res.data
          console.log(_this.ITEMS)
          // _this.refresh()
        }).catch(function (e) {
          console.log(e)
        })
      },
      refresh() {
        window.location.reload();
        setTimeout(refresh, 5000);
      },
      select_user() {

      }
    }
  }
</script>

<style>
  body {
    font-family: Helvetica, sans-serif;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>

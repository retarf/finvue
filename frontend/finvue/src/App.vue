<template>
  <div id="app">
    <userList :users="users" />
    <Form @addUser="addUser"/>
  </div>
</template>

<script>
import userList from './components/userList.vue'
import Form from './components/form.vue'
import axios from "axios";

export default {
  name: 'App',
  components: {
    userList,
    Form
  },
  data () {
    return {
      users: null,
    }
  },
  methods: {
    refreshParser (value) {
      this.Parser.created();
      console.log("Parent");
      console.log(value);
    },
    getUsers () {
      this.users = [];
      axios.get('http://localhost:8080/users/users/')
        .then(response => {
          this.users = response.data;
        })
    },
    addUser (user) {
      console.log(user);
      this.users.push(user);
    },
  },
  created() {
    this.getUsers();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

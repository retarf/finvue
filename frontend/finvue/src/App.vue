<template>
  <div id="app">
    <List v-bind:users="users" />
    <Form @addUser="addUser"/>
  </div>
</template>

<script>
import List from './components/list.vue'
import Form from './components/form.vue'
import axios from "axios";

export default {
  name: 'App',
  components: {
    List,
    Form
  },
  data () {
    return {
      users: null,
    }
  },
  methods: {
    getUsers () {
      axios.get('http://localhost:8080/users/users/')
        .then(response => {
          this.users = response.data;
        });
    },
    addUser (user) {
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

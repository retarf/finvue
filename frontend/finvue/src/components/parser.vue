<template>
  <div class="Parser">
    <table>
      <tr>
        <th>First name:</th>
        <th>Last name:</th>
      </tr>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.first_name }}</td>
        <td>{{ user.last_name }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
import User from './user';

export default {
  name: 'Parser',
  data () {
    return {
      users: null
    }
  },
  methods: {
    fetch() {
      this.users = [];
      axios.get('http://localhost:8080/users/users/')
        .then(response => {
          response.data.forEach(user => {
            let userObject = User;
            userObject.id = user.id;
            userObject.fname = user.first_name;
            userObject.lname = user.last_name;
            this.users.push(userObject);
          })
      }).catch(() => {
        console.log("Error");
      });
    }
  },
  created() {
    this.fetch();
  }
}
</script>

<style>
</style>

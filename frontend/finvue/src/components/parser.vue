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

export default {
  name: 'Parser',
  data () {
    return {
      users: null
    }
  },
  methods: {
    fetch() {
      axios.get('http://localhost:8080/users/users/')
        .then(response => {
          this.users = response.data;
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

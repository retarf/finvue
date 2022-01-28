<template>
  <div class="UserList">
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
export default {
  name: 'userList',
  props: [
      'users',
  ],
  created() {
    this.users.forEach(user => {
      console.log(user);
    })
  }
}
</script>

<style>
</style>

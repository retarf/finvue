<template>
  <div>
    <table>
      <tr>
        <th>First name:</th>
        <th>Last name:</th>
        <th></th>
      </tr>
      <div v-for="(user, index) in users" :key="user.id">
        <Row :user="user" :index="index"/>
      </div>
    </table>
  </div>
</template>

<script>
import Row from './row.vue';

export default {
  name: 'List',
  components: {
    Row,
  },
  props: {
    users: {
      type: Array
    },
  },
}
</script>
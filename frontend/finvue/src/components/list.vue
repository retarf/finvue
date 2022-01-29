<template>
  <div>
    <table>
      <tr>
        <th>First name:</th>
        <th>Last name:</th>
      </tr>
      <tr v-for="user in users" :key="user.id">
        <Row :user="user"></Row>
      </tr>
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
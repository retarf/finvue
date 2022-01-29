<template>
  <tr class="Modify">
    <td><input type="text" v-model="user.first_name"/></td>
    <td><input type="text" v-model="user.last_name"/></td>
    <td>
      <button v-on:click="apply">Apply</button>
    </td>
  </tr>
</template>


<script>

export default {
  name: "Modify",
  props: [
    'index',
    'user',
  ],
  methods: {
    apply() {
      console.log("test")
    }
  }
}

</script>

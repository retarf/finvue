<template>
  <tr class="Parser">
    <td>{{ user.first_name }}</td>
    <td>{{ user.last_name }}</td>
    <td>
      <button v-on:click="del">del</button>
    </td>
  </tr>
</template>

<script>
import axios from "axios";

export default {
  name: 'Parser',
  props: [
    'user',
    'index',
  ],
  methods: {
    del() {
      let url = "http://localhost:8080/users/users/" + this.user.id + "/";
      axios.delete(url)
          .then(() => {
                this.$emit("delete", this.$parent.users.splice(this.index, 1));
              }
          ).catch((e) => {
        console.log(e)
      });
    }
  }
}

</script>
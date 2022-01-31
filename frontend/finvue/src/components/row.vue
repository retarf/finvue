<template>
  <tr class="Row">
    <div v-if="user_input">
      <input v-model="user.first_name">
      <input v-model="user.last_name">
      <button @click="apply">apply</button>
    </div>
    <div v-else>
      <td>{{ user.first_name }}</td>
      <td>{{ user.last_name }}</td>
      <td>
        <button @click="del">del</button>
      </td>
      <td>
        <button @click="edit">edit</button>
      </td>
    </div>
  </tr>
</template>

<script>
import axios from "axios";

export default {
  name: 'Row',
  props: [
    'user',
    'index',
  ],
  data() {
    return {
      user_input: false,
    }
  },
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
    },
    edit() {
      this.$data.user_input = !this.$data.user_input;
    },
    apply() {
      this.$data.user_input = !this.$data.user_input;
      let url = "http://localhost:8080/users/users/" + this.user.id + "/";
      let patch_data = {first_name: this.user.first_name, last_name: this.user.last_name};
      axios.patch(url, patch_data)
          .then(() => {
              }
          ).catch((e) => {
        console.log(e)
      });

    },
    modify() {
      this.$parent.$emit("modify", {first_name: this.first_name, last_name: this.last_name})
      this.$parent.$parent
    }
  },
}

</script>
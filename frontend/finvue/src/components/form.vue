<template>
  <tr class="Form">
    <td>
      <input v-model="first_name">
    </td>
    <td>
      <input v-model="last_name">
    </td>
    <td>
    <button v-on:click="submit">Submit</button>
    </td>
  </tr>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Form',
  data () {
    return {
      id: null,
      first_name: null,
      last_name: null,
    }
  },
  methods: {
    submit: function (event) {
      this.event = event;
      axios.post('http://localhost:8080/users/users/',
          {
            id: this.id,
            first_name: this.first_name,
            last_name: this.last_name,
          }
      ).then(response => {
        this.$emit('addUser', response.data);
      }).catch(() => {
            console.log("Error occured when user " + this.first_name + " " + this.last_name /
            " has been added."
          );
        }
      )
    }
  },
}
</script>

<style>
  .Form {
    position: absolute;
  }
</style>

<template>
  <div class="Form">
      <br/>
      <label>First name:</label>
      <input v-model="first_name">
      <br/>
      <label>Last name:</label>
      <input v-model="last_name">
      <br/>
      <br/>
      <button v-on:click="submit">Submit</button>
  </div>
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
        this.first_name = null;
        this.last_name = null;
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

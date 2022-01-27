<template>
  <div class="Form">
      <label>First name:</label>
      <input v-model="fname">
      <br/>
      <label>Last name:</label>
      <input v-model="lname">
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
      fname: null,
      lname: null,
      event: null
    }
  },
  methods: {
    submit: function (event) {
      this.event = event;
      this.$emit('clicked', "clicked")
      axios.post('http://localhost:8080/users/users/',
          {
            first_name: this.fname,
            last_name: this.lname,
          }
      )
    }
  },
  created() {
  }
}
</script>

<style>
  .Form {
    position: absolute;
  }
</style>

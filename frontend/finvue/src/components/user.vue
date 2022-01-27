
<template>
  <div class="User">
      <td>{{ user.first_name }}</td>
      <td>{{ user.last_name }}</td>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'User',
  data () {
    return {
      url: null,
      id: null,
      firstName: null,
      lastName: null
    }
  },
  methods: {
    setId (id) {
      this.id =  id;
      this.url = 'http://localhost:8080/users/users/' + this.id + '/'
    },
    fetch () {
      axios.get(this.url)
          .then(response => {
            this.firstName = response.data.first_name;
            this.lastName = response.data.last_name;
          }).catch(() => {
        console.log("Error while fetching " + this.id + " user.");
      });
    },
    add (fname, lname) {
      let url = 'http://localhost:8080/users/users/'
      axios.post(url)
        .then(response => {
          this.setId(response.data.id)
          this.$emit("userAdded", this.id)
        }).catch(() => {
            console.log("Error while posting user " + fname + " " + lname + ".");
        })
    },
  },
  created() {
    this.fetch();
  }
}
</script>

<style>
</style>

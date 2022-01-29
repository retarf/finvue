<template>
  <td class="Del">
    <button>del</button>
  </td>
</template>

<script>
import axios from "axios"

export default {
  name: 'Del',
  props: [
    'id',
    'event',
  ],
  methods: {
    del(event) {
      this.event = event;
      axios.delete('http://localhost:8080/users/users/' + this.id + "/",)
          .then(() => {
                this.$emit('del', this.data);
              }
          ).catch(() => {
            console.log("Error occured when user " + this.first_name + " " + this.last_name /
                " has been deleted."
            );
          }
      )
    }


  },
};
</script>

<style>
</style>

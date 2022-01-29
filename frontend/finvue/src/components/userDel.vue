<template>
  <button class="userDel">
    del
  </button>
</template>

<script>
import axios from "axios"

export default {
  name: 'userDel',
  props: [
    'id',
    'event',
  ],
  methods: {
    del(event) {
      this.event = event;
      axios.delete('http://localhost:8080/users/users/' + this.id + "/",
      ).catch(() => {
            console.log("Error occured when user " + this.first_name + " " + this.last_name /
                " has been deleted."
            );
          }
      )
      this.$emit('delUser', this.$data)
    }


  },
}
,

}
</script>

<style>
</style>

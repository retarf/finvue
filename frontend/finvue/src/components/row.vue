<template>
  <tr class="Row" >
    <Line :user="user" :index="index"/>
    <p>test Row</p>
  </tr>
</template>

<script>
//import axios from "axios";
import Line from "./line.vue";

export default {
  name: 'Row',
  components: [
      Line,
  ],
  props: [
    'user',
    'index'
  ],
  // methods: {
  //   del() {
  //     let url = "http://localhost:8080/users/users/" + this.user.id + "/";
  //     axios.delete(url)
  //         .then(() => {
  //               this.$emit("delete", this.$parent.users.splice(this.index, 1));
  //             }
  //         )
  //   }
  // },
}

</script>
<template>
  <tr class="Line" >
    <p>test Line</p>
  </tr>
</template>

<script>
//import axios from "axios";
// import Input from "./input";
// import Text from "./text";

export default {
  name: 'Line',
  // components: [
  //   Input,
  //   Text
  // ],
  props: [
    'user',
    'index'
  ],
  //data() {
  //  return {
  //    firstNameComponent: 0,
  //    lastNameComponent: 0,
  //    first_name: this.user.first,
  //  };
  //},
  // methods: {
  //   dynamicFirstName() {
  //     if (this.firstNameComponent) {
  //       return 'Text'
  //     } else {
  //       return 'Input'
  //     }
  //   },
  //   dynamicLastName() {
  //     if (this.lastNameComponent) {
  //       return 'Text'
  //     } else {
  //       return 'Input'
  //     }
  //   }
  // },
  created() {
    console.log(this.user)
  }
}
</script>
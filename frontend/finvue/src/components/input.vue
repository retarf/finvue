<template>
  <td class="Input">
    <input tyep="text" v-model="value"/>
    <button v-on:click="save">OK</button>
  </td>
</template>

<script>

export default {
  name: "Input",
  props: [
    'value',
    'index',
    'field'
  ],
  methods: {
    save() {
      this.$emit("save")
    }
  }
}

</script>
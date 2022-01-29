<template>
  <td class="Text" v-on:click="edit">
    {{ value }}
  </td>
</template>

<script>

export default {
  name: "Text",
  props: [
    'value',
    'index',
    'field'
  ],
  methods: {
    edit () {
      this.$emit("edit")
    }
  }
}
</script>
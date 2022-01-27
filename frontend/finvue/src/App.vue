<template>
  <div id="app">
    <Parser />
    <Form @clicked="refreshParser"/>
  </div>
</template>

<script>
import Parser from './components/parser.vue'
import Form from './components/form.vue'

export default {
  name: 'App',
  components: {
    Parser,
    Form
  },
  data () {
    return {
      Parser,
    }
  },
  methods: {
    refreshParser (value) {
      this.Parser.created();
      console.log("Parent");
      console.log(value);
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

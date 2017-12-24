<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    created: function () {
      this.$http.post('http://127.0.0.1:5000/').then(response => {
        // success callback
        console.log(response.data)
      }, response => {
        // error callback
      })
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

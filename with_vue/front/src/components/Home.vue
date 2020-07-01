<template>
  <div class='home'>
    <h1>This is a home page</h1>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click='updateRandom'>New random number</button>
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'home',
  data () {
    return {
      randomNumber: 0
    }
  },
  mounted () {
    this.updateRandom()
  },
  methods: {
    updateRandom: async function () {
      const response = await axios.get('/api/random')
      this.randomNumber = response.data.randomNumber
    }
  }
}
</script>

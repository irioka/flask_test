const axios = require('axios')

axios.get('http://localhost:3000/task')
  .then(resp => {
    data = resp.data
    data.forEach(e => {
      console.log(`${e.id}, ${e.title}, ${e.text}`)
    })
  })
  .catch(error => {
    console.log(error)
  })

<template>
  <div class="home">
    <h1>This is a home page</h1>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="updateRandom">New random number</button>

    <div class="col-sm-8 col-md-6 col-lg-6">
      <p>タスクの登録</p>
      <b-form v-if="show">
        <b-form-group label="Title:" label-for="title">
          <b-form-input v-model="title"
            id="title"
            type="text"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group label="Text:" label-for="title">
          <b-form-textarea v-model="text"
            id="text"
            placeholder="Enter something"
            :rows="3"
            :max-rows="6"
          >
          </b-form-textarea>
        </b-form-group>
        <div align="center">
          <div class="col-sm-4 col-md-2 col-lg-2">
            <b-button block @click="addTask()" variant="success">Add</b-button>
          </div>
        </div>
      </b-form>
    </div>

    <!-- <el-table class="data-table" :data="tasks" stripe>
      <el-table-column prop="id" label="ID" width="180"></el-table-column>
      <el-table-column prop="title" label="Title" width="180"></el-table-column>
      <el-table-column prop="text" label="Text"></el-table-column>
    </el-table> -->

    <b-list-group v-for="(task, index) in tasks" :key="index">
      <b-list-group-item>
        {{ task.title }}<br />
        {{ task.text }}
        <b-button
          v-bind:src="task.id"
          block
          @click="deleteTask(index, task.id)"
          >削除</b-button
        >
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
const axios =
  process.env.VUE_APP_REST_SERVER === 'json-mock'
    ? require('axios').create({ baseURL: 'http://localhost:3000' })
    : require('axios').create()
export default {
  name: 'home',
  data () {
    return {
      randomNumber: 0,
      tasks: [],
      title: '',
      text: '',
      show: true
    }
  },
  mounted () {
    this.updateRandom()
    this.getTasks()
  },
  methods: {
    updateRandom: async function () {
      const response = await axios.get('/api/random')
      this.randomNumber = response.data.randomNumber
    },
    getTasks: async function () {
      const response = await axios.get('/api/task')
      this.tasks = response.data
    },
    addTask () {
      axios.post('/api/task', {'text': this.text, 'title': this.title})
        .then(response => {
          var id = response.data
          var task = {'id': id, 'text': this.text, 'title': this.title}
          this.tasks.unshift(task)
          this.text = ''
          this.title = ''
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteTask (index, id) {
      console.log(index)
      console.log(id)
      console.log(JSON.stringify(this.tasks[index]))
      axios.delete('/api/task/' + id)
        .then(response => {
          this.tasks.splice(index, 1)
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.data-table {
  width: 80%;
  margin: auto;
}
</style>

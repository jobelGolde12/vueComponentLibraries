<template>
  <div class="main-container bg-gradient d-flex flex-row justify-content-center align-items-center">
    <div class="todo-container container bg-light rounded p-3 shadow-sm">
      <div class="row">
        <div class="col-6">
          <h4 class="text-dark fw-normal mb-0">My Todo</h4>
          <p class="text-dark fw-lighter">Lorem, ipsum dolor.</p>
        </div>
        <div class="col-6">
          <div class="btn new-todo float-end text-light">
            <i class="bi bi-plus text-light me-1"></i>New
          </div>
        </div>
      </div>
      <p class="text-dark fw-semibold mb-0">Upcoming</p>
      <ul class="d-flex flex-column gap-2 p-0">
        <li
          class="list d-flex gap-3 justify-content-between align-items-center list-style-none p-2 rounded"
          v-for="(data, index) in todoData"
          :key="index"
        >
          <div class="d-flex align-items-center gap-2">
            <div><input type="checkbox" @click="finishedTodoFunc(index)" /></div>
            <div class="title">{{ data.title }}</div>
          </div>

          <div class="date">{{ data.dueDate }}</div>
          <div class="action btn btn-warning" @click="deleteTodo(index)">
            <i class="bi bi-trash"></i>
          </div>
        </li>
      </ul>

      <!-- If todo is Finised (but not deleted) -->
      <p class="text-dark fw-semibold mb-0" v-if="finishedTodo.length !== 0">Finished</p>
      <ul class="d-flex flex-column gap-2 p-0" v-if="finishedTodo.length !== 0">
        <li
          class="finish-list d-flex gap-3 justify-content-between align-items-center list-style-none p-2 rounded"
          v-for="(data, index) in finishedTodo"
          :key="index"
        >
          <div class="title">{{ data.title }}</div>
          <div class="action btn btn-warning" @click="deleteFinishedTodo(index)">
            <i class="bi bi-trash"></i>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
  <script>
export default {
  data() {
    return {
      todoData: [
        {
          title: 'lorem ipsum',
          isDone: false,
          isDeleted: false,
          dueDate: '2024/10/18',
          dateModify: '2024/10/18'
        },
        {
          title: 'lorem ipsum',
          isDone: false,
          isDeleted: false,
          dueDate: '2024/10/21',
          dateModify: '2024/10/21'
        },
        {
          title: 'lorem ipsum',
          isDone: false,
          isDeleted: false,
          dueDate: '2024/10/20',
          dateModify: '2024/10/20'
        },
        {
          title: 'lorem ipsum',
          isDone: false,
          isDeleted: false,
          dueDate: '2024/10/31',
          dateModify: '2024/10/31'
        }
      ],
      finishedTodo: []
    }
  },
  methods: {
    finishedTodoFunc(i) {
      this.finishedTodo.push(this.todoData[i])
      this.todoData.pop(i)
    },
    deleteTodo(i) {
      this.todoData.pop(i)
    },
    deleteFinishedTodo(i) {
      this.finishedTodo.pop(i)
    }
  }
}
</script>
  <style lang="css" scoped>
.main-container {
  width: 100vw;
  height: 100vh;
}
.bg-gradient {
  background-color: #f1e7d6;
  background-image: linear-gradient(160deg, rgb(183, 210, 48) 0%, #f3ee91 100%);
}
.todo-container {
  width: 40%;
}
.list {
  cursor: pointer;
}
.list:hover,
.finish-list:hover {
  background: rgba(0, 0, 0, 0.1);
}
.finish-list .title {
  text-decoration: line-through;
}
.new-todo {
  background: #e792c8;
}
</style>
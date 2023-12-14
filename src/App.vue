<template>
  <h1 class="title">Ingredient to meal</h1>
  <button @click="uploadImage" class="submit-button">Upload Image</button>
  <button @click="uploadImage" class="submit-button">Upload Image</button>
  <button @click="uploadImage" class="submit-button">Upload Image</button>
  <button @click="uploadImage" class="submit-button">Upload Image</button>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.title {
  font-size: x-large;
  color: rgb(0, 0, 0);
  margin-bottom: 20px;
  background: linear-gradient(to bottom, #000000, #333333);
  -webkit-background-clip: text;
  background-clip: text;
}
.submit-button {
  padding: 10px 20px;
  border: none;
  border-radius: 100px;
  background-color: #000000;
  color: rgb(255, 252, 252);
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: inline-flex;
  gap: 100vh;
}
.submit-button:hover {
  background-color: #36759e;
}
</style>

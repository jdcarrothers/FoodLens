<template>
  <div class="container">
    <p v-if="loading" class="title">Loading Response......</p>
    <p v-else class="confirmation-text">{{ confirmationMessage }}</p>
    <input type="file" @change="onFileChange" class="submit-button">Upload image>
    <img :src="image" style="max-width: 200px;">
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      imageFile: "",
      confirmationMessage: "" ,
      image: null,
      loading: false,
    };
  },
  methods: {
      sendURL(image) {
      //send image path to api 
      this.loading = true;
      fetch("http://127.0.0.1:5000/capture_and_save_frame", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          imageFile: image
        }),
      })
      //display the response from the API
        .then(response => response.json())
        .then(data => {
          this.loading = false;
          this.confirmationMessage = "message sent successfully! The API responded with: " + data.result;
        })
        .catch(error => {
          this.loading = false;
          console.error("Error:", error);
        });
    },
    onFileChange(e) {
      const file = e.target.files[0];
      this.previewImage(file);
    },
    previewImage(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.image = e.target.result;
        this.sendURL(e.target.result)
      };
      reader.readAsDataURL(file);
      
    },
  }
}

</script>
<style scoped>
.confirmation-text {
  color: white;
  font-size: x-large;
}
.container {
  font-size: 2em;
  color: white;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  height: 200vw;
  width: 100vw;
  background: linear-gradient(to bottom, #000000, #333333);
}
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
  color: rgb(235, 235, 235);
  margin-bottom: 20px;
  background: linear-gradient(to bottom, #000000, #333333);
  -webkit-background-clip: text;
  background-clip: text;
}
.submit-button {
  padding: 10px 20px;
  border: none;
  border-radius: 100px;
  background-color: #eee3e3;
  color: rgb(2, 1, 1);
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: inline-flex;
  gap: 100vh;
}
.submit-button:hover {
  background-color: #36759e;
}
</style>
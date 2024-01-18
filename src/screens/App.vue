<template>
  <div id="app">
    <nav class="navbar">
      <div class="brand">Food Lens</div>
      <div class="burger-menu" @click="toggleMenu">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
      </div>
      <div class="nav-buttons" :class="{ 'is-active': menuActive }">
        <div class="nav-label" @click="scrollToTop('home')">Home</div>
          <!-- home menu -->
        <div class="nav-label" @click="scrollToTop('how-it-works')">How It Works</div> 
          <!-- go into medium depth on how it connects to api flow chart -->
        <div class="nav-label" @click="scrollToTop('technologies')">Technologies</div>
          <!-- frame works and languages used -->
      </div>
    </nav>
    <div class="content">
      <div class="text-header">Upload an image to see what you can make</div>
      <div class="image-visual">
        <img :src="image" style="height: 400px; width: 400px;">
      </div>
      <div class="buttons">
          <label for="fileInput" class="button">
              <input type="file" id="fileInput" @change="onFileChange" class="file-input">
              {{ loading ? 'Loading Response......' : 'Upload' }}
          </label>
      </div>
      <div class="text-block">
        <p>{{ confirmationMessage }}</p>
      </div>
      <div class="header">How It Works</div>
      <div class="image-with-text">
        <div class="text">
          <p>
          When you upload an image, it undergoes a transformation into a series of letters that symbolize the visual content.
          These letters are then transmitted to a script located elsewhere. The script reverses the process, converting the letters back into the original image.
          <br>
          <br>
          Subsequently, the image is forwarded to an API that utilizes it to identify the ingredients depicted. The API then searches for a corresponding recipe based on the identified ingredients. The resulting recipe is sent back to the script, which in turn relays it to the website.
          <br>
          <br>
          Simultaneously, another API is employed to locate a YouTube video featuring the prepared recipe. The video is retrieved and sent back to the website, allowing you to watch it.
          </p>
        </div>
        <div class="flow-image">
          <img src="../assets/flowchart.png" alt="">
        </div>
      </div>
    </div>
  </div>
</template>
<!-- <input type="file" @change="onFileChange" class="file-input">
<div class="label">{{ loading ? 'Loading Response......' : 'Upload Image' }}</div> -->
<!-- <div class="text-wrapper">
  {{ confirmationMessage }}
</div> -->

<script>
export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      imageFile: "",
      confirmationMessage: "" ,
      image: null,
      menuActive: false,
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
        .then(response => response.json())
        .then(data => {
          this.loading = false;
          this.confirmationMessage = data.result;
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
    toggleMenu() {
      this.menuActive = !this.menuActive;
    },
    scrollToTop(distance) {
      if(distance === 'home'){
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      }
      else if(distance === 'how-it-works'){
        window.scrollTo({
          top: window.innerHeight -25,
          behavior: 'smooth'
        });
      }
      else if(distance === 'technologies'){
        window.scrollTo({
          top: window.innerHeight * 2,
          behavior: 'smooth'
        });
      }
    },
  },
}
</script>

<style scoped>
.flow-image{
  transform: scale(0.6);
  margin-top: -68%;
  margin-left: -15%;
}
.image-with-text{
  gap: 4%;
  margin-top: 4%;
  font-family: Arial, sans-serif;
  font-size: 36px;
  font-weight: bold;
}
.text{
  padding-left: 50%;
  padding-right: 11%;
  margin-bottom: 5%;
  line-height: 61px;
  color: white;
}
.text-header{
  font-family: Arial, sans-serif;
  margin-bottom: 5%;
  font-size: 36px;
  font-weight: bold;
  line-height: 61px;
  color: white;
  background-color: #0a3a2a;
  width: 100%;
  text-align: center;
}
.text-block{
  margin-top: 4%;
  font-family: Arial, sans-serif;
  font-size: 36px;
  font-weight: bold;
  padding-left: 11%;
  padding-right: 11%;
  margin-bottom: 5%;
  line-height: 61px;
  color: white;
}
.header {
  font-family: Arial, sans-serif;
  font-size: 36px;
  font-weight: bold;
  line-height: 61px;
  color: white;
  background-color: #0a3a2a;
  width: 100%;
  text-align: center;
}
.image-visual {
  background-color: #d9d9d9;
  border-radius: 42px;
  height: 400px;
  width: 400px;
  overflow: hidden;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#app {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #137A63;
  padding: 10px 20px;
  color: white;
  font-family: Arial, sans-serif;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 9999;
}
.content{
  background: linear-gradient(to bottom, #0A3A2A, #137a63);
  background: -webkit-linear-gradient(top, #0A3A2A, #137a63);
  color: white;
  height: 300vh;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-top: 5%;
}

.brand {
  padding-left: 10%;
  font-family:Arial, sans-serif;
  font-weight: bold;
  font-size: 40px;
}

.nav-buttons {
  display: flex;
  gap: 40px;
  font-weight: 650;
  padding-right: 10%;
}

.nav-buttons.is-active {
  display: block;
}

.nav-label {
  cursor: pointer;
  position: relative;
  transition: color 0.3s;
  font-weight: bold;
  font-family: Arial, sans-serif;
  font-size: 20px;
}

.nav-label::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  background: white;
  left: 50%;
  bottom: -5px;
  transition: width 0.3s, left 0.3s;
}

.nav-label:hover::after {
  width: 100%;
  left: 0;
}

.burger-menu {
  display: none;
  cursor: pointer;
}

.burger-menu .line {
  width: 25px;
  height: 3px;
  background-color: white;
  margin: 5px;
  transition: transform 0.3s;
}
.buttons{
  display: flex;
  flex-direction: row;
  gap: 4%;
  margin-top: 4%;
  font-family: Arial, sans-serif;
  font-size: 36px;
  font-weight: bold;

}
.button {
  position: relative;
  display: inline-block;
  overflow: hidden;
  background-color: #81b69d;
  border-radius: 149px;
  width: 500px;
  height: 61px;
  cursor: pointer;
  margin-top: 20px;
  font-family: Arial, sans-serif;
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  line-height: 61px;
}
.file-input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}
.button:hover {
  background-color: #719e89;
  color: #fff;
  border-color: #719e89;
  transition: background-color 0.3s ease-in, color 0.3s ease-in, border-color 0.3s ease-in;
}
.button:active {
  transform: translateY(2px);
}
@media (max-width: 768px) {
  .nav-buttons {
    display: none;
    flex-direction: column;
    width: 100%;
    position: absolute;
    top: 60px;
    left: 0;
    background: #137A63;
  }

  .nav-buttons.is-active {
    display: flex;
  }

  .burger-menu {
    display: block;
  }
}



</style>
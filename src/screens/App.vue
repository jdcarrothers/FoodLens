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
      <div class="text-block">Upload an image to see what you can make</div>
      <div class="image-visual">
        <img :src="image" style="width: 100%; height: 100%;">
      </div>
      <div class="buttons">
          <label for="fileInput" class="button">
              <input type="file" id="fileInput" @change="onFileChange" class="file-input">
              {{ loading ? 'Loading Response......' : 'Upload' }}
          </label>
      </div>
      <div class="text-block">
        <!-- <p>{{ confirmationMessage }}</p> -->
        <p>This code retains your existing button styles
           and integrates the file input into the button
            using the label element. The file input is
             positioned absolutely to cover the entire
              button, making the entire area clickable
               for file input.</p>
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
          top: window.innerHeight,
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
.text-block{
  margin-top: 4%;
  font-family: Arial, sans-serif;
  font-size: 36px;
  font-weight: bold;
  padding-left: 11%;
  padding-right: 11%;
  margin-bottom: 4%;
  line-height: 61px;
  color: white;
}
.image-visual {
  background-color: #d9d9d9;
  border-radius: 42px;
  overflow: hidden;
  height: 400px;
  width: 400px;
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
}
.content{
  background: linear-gradient(to bottom, #0A3A2A, #137a63);
  background: -webkit-linear-gradient(top, #0A3A2A, #137a63);
  color: white;
  height: 200vh;
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
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
    <div ref="homeElement"></div>
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
      <p class = "text-block">
        {{ confirmationMessage }}
      </p>
      <!-- <a href=""></a> YOUTUBE LINK TO RECIPE -->
    </div>
    <div class="header">How It Works</div>
    
    <div ref="howItWorksElement"></div>
    <HowItWorksScreen/>
    <div ref="technologiesElement"></div>
    <TechnologiesScreen/>
  </div>
  <!-- ending app id div ^^ -->
</template>


<script>
import HowItWorksScreen from '../components/HowItWorksScreen.vue'; 
import TechnologiesScreen from '../components/TechnologiesScreen.vue'; 
export default {
  name: 'App',
  components: {
    HowItWorksScreen,
    TechnologiesScreen,
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
      fetch(`${process.env.VUE_APP_HOST}/capture_and_save_frame`, {
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
    let targetElement;

    switch (distance) {
      case 'home':
        targetElement = this.$refs.homeElement;
        break;
      case 'how-it-works':
        targetElement = this.$refs.howItWorksElement;
        break;
      case 'technologies':
        targetElement = this.$refs.technologiesElement;
        break;
      default:
        return; // Do nothing if distance is not recognized
    }

    if (targetElement) {
      targetElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
        easing: 'cubic-bezier(0.4, 0, 0.2, 1)' // Add easing property for acceleration and deceleration
      });
    }
  },
},
};  
</script>

<style scoped>
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
  margin-bottom: 5%;
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
  background: #0a3a2a;
  padding: 10px 20px;
  color: white;
  font-family: Arial, sans-serif;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 9999;
}
.content{
  background-color: #2c4c3b;
  color: white;
  height: auto;
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

    .content {
      transform: scale(1);
      font-size: 16px;
      margin-top: 40px;
    }
    .text-header{
      font-size: 36px;;
    }
    .text-block{
    margin-top: 4%;
    font-family: Arial, sans-serif;
    font-size: 24px;
    font-weight: bold;
    color: white;
}

    .nav-label {
      font-size: 16px;
    }

    .button {
      width: 300px;
      height: 41px;
      font-size: 24px;
      line-height: 41px;
    }
    .brand {
      padding-left: 2%;
    }
    .image-visual {
      height: 300px;
      width: 300px;
      margin-top: 10%;
    }
  }
  .nav-buttons.is-active {
    display: flex;
  }

  .burger-menu {
    display: block;
  }
}
</style>
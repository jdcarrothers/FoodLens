<template>
  <div class="login">
    <div class="overlap-wrapper">
      <div class="overlap">
        <div class="screen">
          <div class="overlap-group">
            <div class="screen-size" />
            <div class="gradient" />
            <div class="div" />
          </div>
        </div>                                                    
        <div class="main-form">
          <div class="overlap-2">
            <header class="header">
              <div class="text-content">
                <div class="text-content-2">
                  <div class="text">Ingredients to meal</div>
                  <p class="upload-a-photo-of">
                    Upload a photo of your fridge and see
                    <br />
                    what you can make!
                  </p>
                </div>
              </div>
              <Ellipse class="ellipse-1" />
            </header>
            <img
              class="screenshot"
              alt="Screenshot"
              src="https://c.animaapp.com/uxh4LzEN/img/screenshot-2023-12-21-000741-1@2x.png"
            />
          </div>
        </div>
        <div class="rectangle"><img :src="image" style="width: 100%; height: 100%;"></div>
        <div class="text-wrapper">
          {{ confirmationMessage }}
        </div>
        <div class="loginbtn">
         <div class="label-wrapper">
            <input type="file" @change="onFileChange" class="file-input">
            <div class="label">{{ loading ? 'Loading Response......' : 'Upload Image' }}</div>
          </div> 
        </div>
        <img
          class="chat-bubble-square"
          alt="Chat bubble square"
          src="https://c.animaapp.com/uxh4LzEN/img/chat-bubble-square-question--bubble-square-messages-notification.svg"
        />
      </div>
    </div>
  </div>
</template>


<script>
import Ellipse from "../components/Ellipse.vue";
export default {
  name: 'App',
  components: {
    Ellipse
  },
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
  }
}

</script>
<style>
 .login {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
  height: 2000px;
}

.login .overlap-wrapper {
  background-color: #ffffff;
  height: 812px;
  overflow: hidden;
  width: 375px;
}

.login .overlap {
  height: 914px;
  left: -153px;
  position: relative;
  top: -100px;
  width: 658px;
}

.login .screen {
  height: 912px;
  left: 0;
  position: absolute;
  top: 0;
  width: 658px;
}

.login .overlap-group {
  height: 912px;
  position: relative;
}

.login .screen-size {
  background-color: #393939;
  filter: blur(4px);
  height: 2000px;
  left: 153px;
  position: absolute;
  top: 100px;
  width: 375px;
}

.login .gradient {
  background-color: #d9d9d9;
  border: 1px solid;
  border-color: #000000;
  border-radius: 140.5px/133px;
  filter: blur(4px);
  height: 266px;
  left: 377px;
  position: absolute;
  top: 294px;
  width: 281px;
}

.login .div {
  background-color: #d9d9d9;
  border: 1px solid;
  border-color: #000000;
  border-radius: 140.5px/133px;
  filter: blur(4px);
  height: 266px;
  left: 0;
  position: absolute;
  top: 0;
  width: 281px;
}

.login .main-form {
  height: 787px;
  left: 151px;
  position: absolute;
  top: 127px;
  width: 379px;
}

.login .overlap-2 {
  background-image: url(https://c.animaapp.com/uxh4LzEN/img/rectangle-2.png);
  background-size: 100% 100%;
  height: 785px;
  left: 2px;
  position: relative;
  width: 375px;
}

.login .header {
  background-color: transparent;
  height: 238px;
  left: 16px;
  position: absolute;
  top: 28px;
  width: 343px;
}

.login .text-content {
  align-items: center;
  box-shadow: 0px 4px 4px #00000040;  
  display: flex;
  gap: 16px;
  justify-content: center;
  left: 0;
  padding: 0px 24px;
  position: absolute;
  top: 115px;
  width: 343px;
}

.login .text-content-2 {
  align-items: center;
  display: flex;
  flex: 1;
  flex-direction: column;
  flex-grow: 1;
  gap: 8px;
  justify-content: center;
  padding: 16px 0px;
  position: relative;
}

.login .text {
  align-self: stretch;
  color: var(--ink-06);
  font-family: "Raleway", Helvetica;
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -1px;
  line-height: 41px;
  margin-top: -1px;
  position: relative;
  text-align: center;
}

.login .upload-a-photo-of {
  align-self: stretch;
  color: var(--ink-06);
  font-family: "Raleway", Helvetica;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0;
  line-height: 21px;
  position: relative;
  text-align: center;
}

.login .ellipse-1 {
  border-radius: 52px/51.8px !important;
  left: 120px !important;
  position: absolute !important;
  top: 0 !important;
}

.login .screenshot {
  height: 104px;
  left: 136px;
  object-fit: cover;
  position: absolute;
  top: 28px;
  width: 104px;
}

.login .rectangle {
  background-color: #d9d9d9;
  border-radius: 42px;
  height: 256px;
  left: 219px;
  position: absolute;
  top: 390px;
  width: 244px;
  overflow: hidden;
}

.login .text-wrapper {
  color: #ffffff;
  font-family: "Raleway", Helvetica;
  font-size: 14px;
  font-weight: 700;
  height: 10px;
  left: 195px;
  letter-spacing: 0;
  line-height: 21px;
  position: absolute;
  text-align: center;
  top: 747px;
  white-space: nowrap;
  padding: 10px;
  width: 300px; 
  height: 200px;
  border: 1px solid #000;
  padding: 20px;
  overflow: auto;
}

.login .loginbtn {
  height: 56px;
  left: 169px;
  position: absolute;
  top: 669px;
  width: 356px;
}

.login .label-wrapper {
  background-color: #d9d9d9;
  border-radius: 8px;
  height: 56px;
  position: relative;
  width: 354px;
}

.login .label {
  color: var(--ink-01);
  z-index: 1;
  font-family: var(--components-large-font-family);
  font-size: var(--components-large-font-size);
  font-style: var(--components-large-font-style);
  font-weight: var(--components-large-font-weight);
  height: 18px;
  left: 134px;
  letter-spacing: var(--components-large-letter-spacing);
  line-height: var(--components-large-line-height);
  position: absolute;
  text-align: center;
  top: 19px;
  white-space: nowrap;
  width: 86px;
}

.login .chat-bubble-square {
  height: 30px;
  left: 482px;
  position: absolute;
  top: 610px;
  width: 30px;
}
.file-input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
  z-index: 2;
}

</style>
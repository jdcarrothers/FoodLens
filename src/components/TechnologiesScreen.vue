<template>
    <div class="main-container">
        <p>My application is built using the following technologies:</p>
            
        <div class="text">
            <div class="box">
                Vue.js
                <img src="../assets/vue.png" alt="" class="img">
            </div>

            <div class="box">
                Node.js
                <img src="../assets/node-js.png" alt="" class="img">
            </div>

            <div class="box">
                HTML
                <img src="../assets/html.png" alt="" class="img">
            </div>

            <div class="box">
                CSS
                <img src="../assets/css.png" alt="" class="img">
            </div>

            <div class="box">
                Javascript
                <img src="../assets/js.png" alt="" class="img">
            </div>

            <div class="box">
                Python
                <img src="../assets/python.png" alt="" class="img">
            </div>

            <div class="box">
                API (GPT-VISION PREVIEW)
                <img src="../assets/api.png" alt="" class="img">
            </div>

            <div class="box">
                Flask
                <img src="../assets/flask.png" alt="" class="img">
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.box{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 10px;
    margin: 10px;
    border-radius: 10px;
    width: 200px;
    height: 400px;
    background-color: #0a3a2a;
    color: white;
    font-size: 20px;
    font-weight: bold;
    font-family: Arial, sans-serif;
    line-height: 1.5;
    text-align: center;
}

.box img {
    margin-top: 10px;
    width: 200px;
    height: 200px;
}
.text{
    padding-right: 11%;
    margin-bottom: 5%;
    line-height: 1.5;
    color: white;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    grid-gap: 10px;
    padding-left: 11%;
    justify-items: center;
    align-items: center;
}
.main-container{
  background-color: #2c4c3b;
  color: white;
  height: auto;
  padding-top: 5%;
  font-family: Arial, sans-serif;
  font-size: 30px;
  font-weight: bold;
  padding-bottom: 5%;
  text-align: center;
}
.main-container p{
    margin-bottom: 5%;
}
@media (max-width: 768px) {
    .main-container{
        font-size: 24px;
        min-height: 200vh;
        grid-template-columns: repeat(1, minmax(0, 1fr));
        gap:0 !important;
    }
    .grid-fix{
        height:100vh;
        background-size: contain;
        background-position: center;
    }
    .text{
    margin-bottom: 5%;
    line-height: 1.5;
    color: white;
    padding-left: 11%;
    grid-template-columns: repeat(1, minmax(0, 1fr));
        gap:0 !important;
    }
}
</style>
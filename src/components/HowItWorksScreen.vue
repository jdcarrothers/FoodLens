<template>
    <div class="main-container">
        <div class="grid-fix">
        </div>
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
    </div>
    <div class="header">Technologies</div>
</template>

<script>
export default {

}
</script>

<style scoped>
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
.grid-fix{
    background-image: url('../assets/flowchart.png');
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;
}
.text{
  padding-right: 11%;
  margin-bottom: 5%;
  line-height: 1.5;
  color: white;
  grid-column: span 2/span 2;
}
.main-container{
  background-color: #2c4c3b;
  color: white;
  height: auto;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  padding-top: 5%;
  font-family: Arial, sans-serif;
  font-size: 30px;
  font-weight: bold;
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
    }
}
</style>
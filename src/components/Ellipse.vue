
<template>
  <div :class="['ellipse', className]"></div>
</template>

<script>
export default {
  name: "EllipseShape",
  props: {
    className: {
      type: String,
      default: "",
    },
  },
};
</script>
<style>
.ellipse {
  background-color: #b5b5b5;
  border-radius: 52px;
  height: 104px;
  width: 104px;
}
</style>

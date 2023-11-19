<template>
  <main>
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <a href="/compare">
            <img src="src/assets/compare.jpg" class="d-block w-100">
          </a>
        </div>
        <div class="carousel-item">
          <a href="/calculator">
            <img src="src/assets/calculator.jpg" class="d-block w-100">
          </a>
        </div>
        <div class="carousel-item">
          <a href="/map">
            <img src="src/assets/map.jpg" class="d-block w-100">
          </a>
        </div>
        <div class="carousel-item">
          <a href="/board">
            <img src="src/assets/board.jpg" class="d-block w-100">
          </a>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </main>
</template>

<script setup>
</script>

<style scoped>
</style>
<template>
  <router-link
    class="card text-white text-center"
    :to="{ name: 'GenreView', params: { id: props.id } }"
  >
    <div class="card-body d-flex align-items-center justify-content-center" style="height: 120px; background-color: #6c757d;">
      <span class="h5 m-0">{{ props.label }}</span>
    </div>
  </router-link>
</template>

<script setup>
const props = defineProps({
  label: String,
  id: Number,
});
</script>

<style scoped>
.card {
  border-radius: 8px;
  overflow: hidden;
  text-decoration: none;
}
.card:hover {
  opacity: 0.9;
}
</style>

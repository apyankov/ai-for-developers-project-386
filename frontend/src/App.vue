<script setup lang="ts">
import HealthIndicator from "@/components/HealthIndicator.vue";
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <header
      class="flex items-center justify-between px-6 py-3 border-b border-gray-200 bg-white"
    >
      <span class="text-lg font-semibold">CalCom</span>
      <HealthIndicator />
    </header>
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Simple color mode toggle - can be enhanced with proper Nuxt UI composable later
const isDark = ref(false)

const toggleColorMode = () => {
  isDark.value = !isDark.value
  document.documentElement.classList.toggle('dark', isDark.value)
}
</script>

<template>
  <div
    class="sticky lg:absolute top-0 inset-x-0 border-b-0 z-10 bg-default/75 backdrop-blur lg:bg-transparent lg:backdrop-blur-none"
  >
    <div class="flex items-center justify-between px-4 h-16">
      <div class="flex items-center gap-4">
        <UButton
          icon="i-lucide-menu"
          color="neutral"
          variant="ghost"
          class="lg:hidden"
          aria-label="Toggle menu"
        />
      </div>

      <div class="flex items-center gap-2">
        <UButton
          :icon="isDark ? 'i-lucide-moon' : 'i-lucide-sun'"
          color="neutral"
          variant="ghost"
          @click="toggleColorMode"
          aria-label="Toggle color mode"
        />

        <UButton
          color="neutral"
          variant="ghost"
          icon="i-lucide-plus"
          to="/"
          class="lg:hidden"
          aria-label="New chat"
        />
      </div>
    </div>
  </div>
</template>

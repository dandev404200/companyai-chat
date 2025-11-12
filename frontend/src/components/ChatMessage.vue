<script setup lang="ts">
import type { Message } from '@/types/chat'

defineProps<{
  message: Message
}>()

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<template>
  <div
    class="group flex gap-4 py-4"
    :class="message.role === 'user' ? 'bg-transparent' : 'bg-elevated/30'"
  >
    <div class="shrink-0">
      <div
        class="w-8 h-8 rounded-full flex items-center justify-center"
        :class="
          message.role === 'user'
            ? 'bg-cambridge-blue-500 text-white'
            : 'bg-champagne-500 text-champagne-900'
        "
      >
        <UIcon
          :name="message.role === 'user' ? 'i-lucide-user' : 'i-lucide-bot'"
          class="w-5 h-5"
        />
      </div>
    </div>

    <div class="flex-1 min-w-0">
      <div class="flex items-center gap-2 mb-2">
        <span class="font-semibold text-sm">
          {{ message.role === 'user' ? 'You' : 'Assistant' }}
        </span>
        <span class="text-xs text-muted">
          {{ new Date(message.timestamp).toLocaleTimeString() }}
        </span>
      </div>

      <div class="prose prose-sm dark:prose-invert max-w-none">
        <p class="whitespace-pre-wrap">{{ message.content }}</p>
      </div>

      <!-- Assistant message actions -->
      <div
        v-if="message.role === 'assistant'"
        class="flex gap-2 mt-3 opacity-0 group-hover:opacity-100 transition-opacity"
      >
        <UButton
          icon="i-lucide-copy"
          size="xs"
          color="neutral"
          variant="ghost"
          @click="copyToClipboard(message.content)"
        />
      </div>
    </div>
  </div>
</template>

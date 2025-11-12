<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'
import type { Message } from '@/types/chat'
import ChatMessage from './ChatMessage.vue'

const props = defineProps<{
  messages: Message[]
  loading?: boolean
}>()

const messagesContainer = ref<HTMLElement | null>(null)

// Auto-scroll to bottom when new messages arrive
watch(
  () => props.messages.length,
  async () => {
    await nextTick()
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  }
)
</script>

<template>
  <div
    ref="messagesContainer"
    class="flex-1 overflow-y-auto px-4"
  >
    <div class="max-w-3xl mx-auto">
      <ChatMessage
        v-for="message in messages"
        :key="message.id"
        :message="message"
      />

      <!-- Loading indicator -->
      <div v-if="loading" class="flex gap-4 py-4">
        <div class="shrink-0">
          <div
            class="w-8 h-8 rounded-full flex items-center justify-center bg-champagne-500 text-champagne-900"
          >
            <UIcon name="i-lucide-bot" class="w-5 h-5" />
          </div>
        </div>
        <div class="flex-1">
          <div class="flex items-center gap-2 mb-2">
            <span class="font-semibold text-sm">Assistant</span>
          </div>
          <div class="flex gap-1">
            <div class="w-2 h-2 rounded-full bg-muted animate-bounce" style="animation-delay: 0ms" />
            <div class="w-2 h-2 rounded-full bg-muted animate-bounce" style="animation-delay: 150ms" />
            <div class="w-2 h-2 rounded-full bg-muted animate-bounce" style="animation-delay: 300ms" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

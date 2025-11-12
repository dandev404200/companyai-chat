<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useChat } from '@/composables/useChat'
import ChatMessages from '@/components/ChatMessages.vue'
import ChatPrompt from '@/components/ChatPrompt.vue'

const route = useRoute()
const chatId = computed(() => route.params.id as string)

const { messages, status, input, sendMessage, regenerate, stop } = useChat(chatId.value)

const handleSubmit = (value: string) => {
  sendMessage(value)
}

const handleStop = () => {
  stop()
}

const handleRegenerate = () => {
  regenerate()
}

const isLoading = computed(() => status.value === 'streaming')
</script>

<template>
  <div class="flex flex-col h-full">
    <!-- Messages area -->
    <ChatMessages
      :messages="messages"
      :loading="isLoading"
      class="flex-1"
    />

    <!-- Input area -->
    <ChatPrompt
      v-model="input"
      :status="status"
      @submit="handleSubmit"
      @stop="handleStop"
      @regenerate="handleRegenerate"
    />
  </div>
</template>

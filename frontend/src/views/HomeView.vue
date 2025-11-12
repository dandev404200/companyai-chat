<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useChatHistory } from '@/composables/useChatHistory'
import ChatPrompt from '@/components/ChatPrompt.vue'

const router = useRouter()
const { createChat } = useChatHistory()

const input = ref('')
const loading = ref(false)

const quickChats = [
  {
    label: 'Help me build a Vue 3 app',
    icon: 'i-lucide-code',
  },
  {
    label: 'Explain TypeScript generics',
    icon: 'i-lucide-book-open',
  },
  {
    label: 'Best practices for Tailwind CSS',
    icon: 'i-lucide-palette',
  },
  {
    label: 'How to use composables?',
    icon: 'i-lucide-lightbulb',
  },
  {
    label: 'Debug Vue Router issues',
    icon: 'i-lucide-bug',
  },
  {
    label: 'Optimize Vue performance',
    icon: 'i-lucide-zap',
  },
]

const handleCreateChat = async (prompt: string) => {
  if (!prompt.trim()) return

  loading.value = true
  try {
    const chat = await createChat(prompt)
    router.push(`/chat/${chat.id}`)
  } catch (error) {
    console.error('Failed to create chat:', error)
  } finally {
    loading.value = false
  }
}

const handleSubmit = (value: string) => {
  handleCreateChat(value)
}

const handleQuickChat = (label: string) => {
  handleCreateChat(label)
}
</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-full p-8">
    <div class="w-full max-w-3xl flex flex-col gap-8">
      <!-- Welcome message -->
      <div class="text-center">
        <h1 class="text-4xl sm:text-5xl font-bold text-highlighted mb-4">
          How can I help you today?
        </h1>
        <p class="text-lg text-muted">
          Start a conversation or choose a quick prompt below
        </p>
      </div>

      <!-- Chat prompt -->
      <ChatPrompt
        v-model="input"
        :status="loading ? 'streaming' : 'idle'"
        placeholder="Ask me anything..."
        @submit="handleSubmit"
      />

      <!-- Quick action buttons -->
      <div class="flex flex-wrap gap-3 justify-center">
        <UButton
          v-for="quickChat in quickChats"
          :key="quickChat.label"
          :icon="quickChat.icon"
          :label="quickChat.label"
          size="sm"
          color="neutral"
          variant="outline"
          class="rounded-full"
          @click="handleQuickChat(quickChat.label)"
        />
      </div>
    </div>
  </div>
</template>

import { ref, computed } from 'vue'
import type { Message, Chat, ChatStatus } from '@/types/chat'

export function useChat(chatId?: string) {
  const messages = ref<Message[]>([])
  const status = ref<ChatStatus>('idle')
  const error = ref<string | null>(null)
  const input = ref('')

  // Mock: Load chat messages
  const loadChat = async (id: string) => {
    // TODO: Replace with actual API call
    // Simulating async load
    return new Promise<Chat>((resolve) => {
      setTimeout(() => {
        resolve({
          id,
          title: 'Sample Chat',
          messages: [
            {
              id: '1',
              role: 'user',
              content: 'Hello!',
              timestamp: new Date(),
            },
            {
              id: '2',
              role: 'assistant',
              content: 'Hi! How can I help you today?',
              timestamp: new Date(),
            },
          ],
          createdAt: new Date(),
          updatedAt: new Date(),
        })
      }, 100)
    })
  }

  // Mock: Send a message
  const sendMessage = async (content: string) => {
    if (!content.trim()) return

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: content.trim(),
      timestamp: new Date(),
    }

    messages.value.push(userMessage)
    status.value = 'streaming'
    input.value = ''

    // Mock assistant response
    setTimeout(() => {
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: 'This is a mock response. Backend integration pending.',
        timestamp: new Date(),
      }
      messages.value.push(assistantMessage)
      status.value = 'idle'
    }, 1000)
  }

  // Mock: Regenerate last response
  const regenerate = () => {
    if (messages.value.length === 0) return

    // Remove last assistant message if exists
    if (messages.value[messages.value.length - 1].role === 'assistant') {
      messages.value.pop()
    }

    status.value = 'streaming'

    // Mock regeneration
    setTimeout(() => {
      const assistantMessage: Message = {
        id: Date.now().toString(),
        role: 'assistant',
        content: 'This is a regenerated mock response.',
        timestamp: new Date(),
      }
      messages.value.push(assistantMessage)
      status.value = 'idle'
    }, 1000)
  }

  // Stop streaming (mock)
  const stop = () => {
    status.value = 'idle'
  }

  // Initialize chat if ID provided
  if (chatId) {
    loadChat(chatId).then((chat) => {
      messages.value = chat.messages
    })
  }

  return {
    messages,
    status,
    error,
    input,
    sendMessage,
    regenerate,
    stop,
    loadChat,
  }
}

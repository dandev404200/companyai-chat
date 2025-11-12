import { ref, computed } from 'vue'
import type { ChatListItem } from '@/types/chat'

export function useChatHistory() {
  const chats = ref<ChatListItem[]>([
    // Mock data
    {
      id: '1',
      title: 'Getting Started with Vue 3',
      createdAt: new Date(Date.now() - 1000 * 60 * 60), // 1 hour ago
    },
    {
      id: '2',
      title: 'Tailwind CSS Best Practices',
      createdAt: new Date(Date.now() - 1000 * 60 * 60 * 24), // 1 day ago
    },
    {
      id: '3',
      title: 'TypeScript Tips',
      createdAt: new Date(Date.now() - 1000 * 60 * 60 * 24 * 3), // 3 days ago
    },
    {
      id: '4',
      title: 'Nuxt UI Components',
      createdAt: new Date(Date.now() - 1000 * 60 * 60 * 24 * 8), // 8 days ago
    },
  ])

  const loading = ref(false)

  // Group chats by date
  const groupedChats = computed(() => {
    const now = new Date()
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
    const yesterday = new Date(today)
    yesterday.setDate(yesterday.getDate() - 1)
    const lastWeek = new Date(today)
    lastWeek.setDate(lastWeek.getDate() - 7)

    const groups: Record<string, ChatListItem[]> = {
      Today: [],
      Yesterday: [],
      'Last 7 days': [],
      Older: [],
    }

    chats.value.forEach((chat) => {
      const chatDate = new Date(chat.createdAt)
      if (chatDate >= today) {
        groups.Today.push(chat)
      } else if (chatDate >= yesterday) {
        groups.Yesterday.push(chat)
      } else if (chatDate >= lastWeek) {
        groups['Last 7 days'].push(chat)
      } else {
        groups.Older.push(chat)
      }
    })

    // Filter out empty groups
    return Object.entries(groups)
      .filter(([, items]) => items.length > 0)
      .map(([label, items]) => ({ label, items }))
  })

  // Mock: Create new chat
  const createChat = async (input: string): Promise<ChatListItem> => {
    // TODO: Replace with actual API call
    return new Promise((resolve) => {
      setTimeout(() => {
        const newChat: ChatListItem = {
          id: Date.now().toString(),
          title: input.slice(0, 50) + (input.length > 50 ? '...' : ''),
          createdAt: new Date(),
        }
        chats.value.unshift(newChat)
        resolve(newChat)
      }, 100)
    })
  }

  // Mock: Delete chat
  const deleteChat = async (id: string) => {
    // TODO: Replace with actual API call
    return new Promise<void>((resolve) => {
      setTimeout(() => {
        const index = chats.value.findIndex((c) => c.id === id)
        if (index !== -1) {
          chats.value.splice(index, 1)
        }
        resolve()
      }, 100)
    })
  }

  // Mock: Refresh chat list
  const refresh = async () => {
    loading.value = true
    // TODO: Replace with actual API call
    await new Promise((resolve) => setTimeout(resolve, 500))
    loading.value = false
  }

  return {
    chats,
    groupedChats,
    loading,
    createChat,
    deleteChat,
    refresh,
  }
}

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useChatHistory } from '@/composables/useChatHistory'
import Logo from './Logo.vue'

const router = useRouter()
const { groupedChats, deleteChat } = useChatHistory()

const open = ref(true)

const handleDelete = async (id: string, event: Event) => {
  event.preventDefault()
  event.stopPropagation()

  if (confirm('Are you sure you want to delete this chat?')) {
    await deleteChat(id)

    // Navigate to home if current chat was deleted
    if (router.currentRoute.value.params.id === id) {
      router.push('/')
    }
  }
}
</script>

<template>
  <aside
    class="fixed lg:sticky top-0 left-0 h-screen w-64 bg-elevated/50 border-r border-muted flex flex-col transition-transform z-20"
    :class="open ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'"
  >
    <!-- Header -->
    <div class="flex items-center gap-2 p-4 border-b border-muted">
      <RouterLink to="/" class="flex items-center gap-2">
        <Logo />
        <span class="text-xl font-bold text-highlighted">Chat</span>
      </RouterLink>
    </div>

    <!-- Content -->
    <div class="flex-1 flex flex-col gap-4 p-4 overflow-y-auto">
      <!-- New Chat Button -->
      <UButton
        label="New chat"
        icon="i-lucide-plus"
        variant="soft"
        block
        to="/"
      />

      <!-- Chat History -->
      <div class="flex flex-col gap-4">
        <div
          v-for="group in groupedChats"
          :key="group.label"
          class="flex flex-col gap-1"
        >
          <div class="text-xs text-muted px-2 py-1">
            {{ group.label }}
          </div>

          <RouterLink
            v-for="chat in group.items"
            :key="chat.id"
            :to="`/chat/${chat.id}`"
            class="group flex items-center justify-between px-3 py-2 rounded-lg hover:bg-accented/50 transition-colors"
            active-class="bg-accented"
          >
            <div class="flex items-center gap-2 flex-1 min-w-0">
              <UIcon name="i-lucide-message-circle" class="shrink-0 text-muted" />
              <span class="text-sm truncate">{{ chat.title }}</span>
            </div>

            <UButton
              icon="i-lucide-x"
              color="neutral"
              variant="ghost"
              size="xs"
              class="opacity-0 group-hover:opacity-100 transition-opacity"
              @click="(e) => handleDelete(chat.id, e)"
            />
          </RouterLink>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="p-4 border-t border-muted">
      <div class="text-xs text-muted text-center">
        Mock UI - Backend pending
      </div>
    </div>
  </aside>
</template>

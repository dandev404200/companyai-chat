<script setup lang="ts">
import { ref } from 'vue'
import type { ChatStatus } from '@/types/chat'

const props = defineProps<{
  modelValue: string
  status?: ChatStatus
  placeholder?: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
  submit: [value: string]
  stop: []
}>()

const localValue = ref(props.modelValue)

const handleInput = (event: Event) => {
  const value = (event.target as HTMLTextAreaElement).value
  localValue.value = value
  emit('update:modelValue', value)
}

const handleSubmit = () => {
  if (localValue.value.trim() && props.status !== 'streaming') {
    emit('submit', localValue.value)
    localValue.value = ''
    emit('update:modelValue', '')
  }
}

const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault()
    handleSubmit()
  }
}

const handleStop = () => {
  emit('stop')
}
</script>

<template>
  <div class="sticky bottom-0 bg-default p-4">
    <div class="max-w-3xl mx-auto">
      <div class="flex flex-col gap-3">
        <!-- Input area -->
        <div class="relative">
          <textarea
            :value="localValue"
            :placeholder="placeholder || 'Type your message...'"
            :disabled="status === 'streaming'"
            class="w-full px-4 py-3 pr-12 rounded-lg border border-muted bg-elevated resize-none focus:outline-none focus:ring-2 focus:ring-cambridge-blue-500"
            rows="3"
            @input="handleInput"
            @keydown="handleKeydown"
          />

          <!-- Submit button -->
          <div class="absolute right-2 bottom-2">
            <UButton
              v-if="status !== 'streaming'"
              icon="i-lucide-send"
              color="neutral"
              size="sm"
              :disabled="!localValue.trim()"
              @click="handleSubmit"
            />
            <UButton
              v-else
              icon="i-lucide-square"
              color="neutral"
              size="sm"
              @click="handleStop"
            />
          </div>
        </div>

        <!-- Footer actions -->
        <div class="text-xs text-muted">
          Press Enter to send, Shift + Enter for new line
        </div>
      </div>
    </div>
  </div>
</template>

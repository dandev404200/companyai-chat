export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: Date
  streaming?: boolean
}

export interface Chat {
  id: string
  title: string
  messages: Message[]
  createdAt: Date
  updatedAt: Date
}

export interface ChatListItem {
  id: string
  title: string
  createdAt: Date
}

export type ChatStatus = 'idle' | 'streaming' | 'error'

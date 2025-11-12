
## Frontend

- **Framework:** Vue 3 (Composition API)
- **Build Tool:** Vite
- **UI Library:** @nuxt/ui v4.1.0
- **Styling:** Tailwind CSS v4
- **Router:** Vue Router 4
- **Markdown:** markdown-it
- **Utilities:** @vueuse/core
- **Date Handling:** date-fns
- **AI Stream Handling Framework:** AI SDK



frontend/src/
├── components/
│   ├── ChatMessage.vue       - Individual message component
│   ├── ChatMessages.vue      - Message list with auto-scroll
│   ├── ChatPrompt.vue        - Input area with submit/stop
│   ├── Logo.vue              - App logo
│   ├── Navbar.vue            - Top navigation with color mode toggle
│   └── Sidebar.vue           - Chat history sidebar
├── composables/
│   ├── useChat.ts            - Chat state management (mock data)
│   └── useChatHistory.ts     - Chat history management (mock data)
├── layouts/
│   └── DefaultLayout.vue     - Main layout with sidebar + navbar
├── types/
│   └── chat.ts               - TypeScript interfaces
└── views/
    ├── HomeView.vue          - Landing page with quick prompts
    └── ChatView.vue          - Active chat page





## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.


### Compile and Hot-Reload for Development

```sh
bun dev
```

### Type-Check, Compile and Minify for Production

```sh
bun run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
bun lint
```

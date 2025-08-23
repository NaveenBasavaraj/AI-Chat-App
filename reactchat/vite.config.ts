import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
   server: {
    host: true,  // needed in Gitpod
    allowedHosts: [
      '5173-naveenbasavar-aichatapp-hx0cvl40lsw.ws-us121.gitpod.io',
      '*.gitpod.io'   // allow all Gitpod hosts
    ]
  }
})

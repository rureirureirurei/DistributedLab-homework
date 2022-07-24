const path = require('path')
import { defineConfig } from 'vite'
import { resolve } from 'path'


export default defineConfig({
  root: path.resolve(__dirname, 'src'),
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/index.html'),
        login: resolve(__dirname, 'src/html/login.html'),
        loggedIn: resolve(__dirname, 'src/html/loggedIn.html'),
        myTrans: resolve(__dirname, 'src/html/myTrans.html'),
        register: resolve(__dirname, 'src/html/register.html'),
        sendMoney: resolve(__dirname, 'src/html/sendMoney.html')
      }
    }
  },
  resolve: {
    alias: {
      '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
    }
  },
  server: {
    port: 8080,
    hot: true
  }
})
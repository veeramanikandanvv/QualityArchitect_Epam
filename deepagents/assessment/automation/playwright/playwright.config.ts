import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: './tests',
  use: { baseURL: process.env.INVENTREE_UI_URL ?? 'http://localhost:8000', trace: 'on-first-retry' },
  reporter: [['list'], ['html', { open: 'never' }]],
});

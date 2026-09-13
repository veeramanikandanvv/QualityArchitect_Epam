import { test, expect } from '@playwright/test';

test('Parts page is reachable', async ({ page }) => {
  await page.goto('/part/part/');
  await expect(page).toHaveURL(/\/part\/part\//);
});

test('create part form workflow', async ({ page }) => {
  await page.goto('/part/part/');
  const button = page.getByRole('button', { name: /new part|create part/i }).first();
  await expect(button, 'The Parts page must expose a create-part action').toBeVisible();
  await button.click();
  await expect(page.getByRole('form')).toBeVisible();
});

test('parts search field accepts a query', async ({ page }) => {
  await page.goto('/part/part/');
  const search = page.getByRole('textbox').first();
  await expect(search, 'The Parts page must expose a search textbox').toBeVisible();
  await search.fill('QA');
  await expect(search).toHaveValue('QA');
});

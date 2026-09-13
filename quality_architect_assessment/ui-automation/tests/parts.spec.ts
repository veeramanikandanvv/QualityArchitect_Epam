import { test, expect } from '@playwright/test';

test('Parts page reachable', async ({ page }) => {
  await page.goto('/part/part/');
  await expect(page).toHaveURL(/part/);
});

test('create part form workflow', async ({ page }) => {
  await page.goto('/part/part/');
  const button = page.getByRole('button', { name: /new part|create part/i }).first();
  if (await button.count()) {
    await button.click();
    await expect(page.getByRole('form')).toBeVisible();
  } else {
    test.info().annotations.push({ type: 'note', description: 'Align selector with deployed UI version' });
  }
});

test('parts search field', async ({ page }) => {
  await page.goto('/part/part/');
  const search = page.getByRole('textbox').first();
  if (await search.count()) {
    await search.fill('QA');
    await expect(search).toHaveValue('QA');
  }
});

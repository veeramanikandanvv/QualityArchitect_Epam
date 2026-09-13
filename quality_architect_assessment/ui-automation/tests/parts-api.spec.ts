import { test, expect } from '@playwright/test';

const apiBaseUrl = process.env.API_BASE_URL ?? 'http://localhost:8000/api';

function uniqueIpn() {
  return `PW-${Date.now()}-${Math.floor(Math.random() * 10000)}`;
}

test.describe('Parts API', () => {
  test('lists parts', async ({ request }) => {
    const response = await request.get(`${apiBaseUrl}/parts/`);
    expect(response.ok()).toBeTruthy();
    const body = await response.json();
    expect(body).toBeTruthy();
  });

  test('rejects a part without required fields', async ({ request }) => {
    const response = await request.post(`${apiBaseUrl}/parts/`, {
      data: {},
    });
    expect(response.status()).toBeGreaterThanOrEqual(400);
    expect(response.status()).toBeLessThan(500);
  });

  test('creates and retrieves a part when the API supports mutations', async ({ request }) => {
    test.skip(process.env.RUN_MUTATION_TESTS !== 'true', 'Set RUN_MUTATION_TESTS=true for state-changing tests');

    const ipn = uniqueIpn();
    const create = await request.post(`${apiBaseUrl}/parts/`, {
      data: { name: 'Playwright API Part', IPN: ipn },
    });
    expect(create.ok()).toBeTruthy();
    const created = await create.json();
    const id = created.pk ?? created.id;
    expect(id).toBeTruthy();

    const detail = await request.get(`${apiBaseUrl}/parts/${id}/`);
    expect(detail.ok()).toBeTruthy();
    const detailBody = await detail.json();
    expect(detailBody.IPN ?? detailBody.ipn).toBe(ipn);
  });
});

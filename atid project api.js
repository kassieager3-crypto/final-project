const BASE_URL = "https://atid.store";
 
// ─── helpers ──────────────────────────────────────────────────────────────
 
async function getPage(path) {
  const res = await fetch(`${BASE_URL}${path}`);
  const body = await res.text();
  const titleMatch = body.match(/<title>(.*?)<\/title>/i);
  const title = titleMatch ? titleMatch[1] : "";
  return { res, body, title };
}
 
async function postForm(path, fields = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(fields),
  });
  const body = await res.text();
  const titleMatch = body.match(/<title>(.*?)<\/title>/i);
  const title = titleMatch ? titleMatch[1] : "";
  return { res, body, title };
}
 
// ─── products ─────────────────────────────────────────────────────────────
 
describe("Products", () => {
 
  test("Yellow Shoes page loads + title correct", async () => {
    const { res, title } = await getPage("/product/atid-yellow-shoes/");
    expect(res.status).toBe(200);
    expect(title).toContain("ATID Yellow Shoes");
  });
 
  test("Blue Shoes page loads + title correct", async () => {
    const { res, title } = await getPage("/product/atid-blue-shoes/");
    expect(res.status).toBe(200);
    expect(title).toContain("ATID Blue Shoes");
  });
 
  test("Flamingo T-shirt page loads + title correct", async () => {
    const { res, title } = await getPage("/product/flamingo-tshirt/");
    expect(res.status).toBe(200);
    expect(title).toContain("Flamingo Tshirt");
  });
 
  test("Invalid product returns 404", async () => {
    const { res } = await getPage("/product/not-a-real-product/");
    expect(res.status).toBe(404);
  });
 
  test("Product page title includes store name", async () => {
    const { title } = await getPage("/product/atid-blue-shoes/");
    expect(title).toContain("ATID Demo Store");
  });
 
});
 
// ─── contact form ─────────────────────────────────────────────────────────
 
describe("Contact form", () => {
 
  test("Contact page loads + title correct", async () => {
    const { res, title } = await getPage("/contact-us/");
    expect(res.status).toBe(200);
    expect(title).toContain("Contact Us");
  });
 
  test("Valid form submission returns 200", async () => {
    const { res } = await postForm("/contact-us/", {
      "your-name":    "Kassie Test",
      "your-email":   "kassie@test.com",
      "your-message": "Automated test message",
    });
    expect(res.status).toBe(200);
  });
 
  test("Empty form submission returns 200", async () => {
    const { res } = await postForm("/contact-us/", {});
    expect(res.status).toBe(200);
  });
 
  test("Page title stays correct after POST", async () => {
    const { title } = await postForm("/contact-us/", {
      "your-name":    "Kassie Test",
      "your-email":   "kassie@test.com",
      "your-message": "Checking title after submit",
    });
    expect(title).toContain("Contact Us");
  });
 
});
 
// ─── accessibility ────────────────────────────────────────────────────────
 
describe("Accessibility toolbar", () => {
 
  let body;
 
  beforeAll(async () => {
    const page = await getPage("/");
    body = page.body;
  });
 
  test("Accessibility toolbar is present in HTML", () => {
    expect(body).toContain("Accessibility Tools");
  });
 
  test("Grayscale toggle exists", () => {
    expect(body).toContain("Grayscale");
  });
 
  test("High Contrast toggle exists", () => {
    expect(body).toContain("High Contrast");
  });
 
  test("Increase Text option exists", () => {
    expect(body).toContain("Increase Text");
  });
 
  test("Reset option exists", () => {
    expect(body).toContain("Reset");
  });
 
});
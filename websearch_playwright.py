import asyncio
from playwright.async_api import async_playwright

async def fetch_news_duckduckgo():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://duckduckgo.com")

        # Wait for search input
        await page.wait_for_selector("input[name='q']")
        await page.fill("input[name='q']", "Aus Vs WI update")
        await page.press("input[name='q']", "Enter")

        # Wait for results to load
        await page.wait_for_selector(".result__title", timeout=10000)

        results = await page.query_selector_all(".result__title")
        print("Top DuckDuckGo News Results:")
        for i, result in enumerate(results[:5]):
            title = await result.inner_text()
            link = await result.query_selector("a")
            href = await link.get_attribute("href") if link else "No link"
            print(f"{i+1}. {title} - {href}")

        await browser.close()

asyncio.run(fetch_news_duckduckgo())

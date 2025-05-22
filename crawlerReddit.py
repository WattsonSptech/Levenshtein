from playwright.sync_api import sync_playwright

posts = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for pagina in range(1,5):
        url = f'https://www.reddit.com/r/saopaulo/search/?q=enel&restrict_sr=1&sort=new'
        page.goto(url)
        page.wait_for_timeout(3000) 

        cards = page.locator("a.absolute.inset-0")  
        count = cards.count()

        for i in range(count):
            post = cards.nth(i)

            try:
                titulo = post.get_attribute("aria-label")

                print(f"Post {i + 1}: {titulo}")

                posts.append({
                    "id": i + 1,
                    "titulo": titulo,
                    "subreddit": "saopaulo"
                })

            except Exception as e:
                print(f"Erro ao extrair post {i + 1}: {e}")

    browser.close()
from playwright.sync_api import sync_playwright

reclamacoes = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for pagina in range(1, 2): 
        url = f'https://www.reclameaqui.com.br/empresa/aes-eletropaulo/lista-reclamacoes/?pagina={pagina}'
        page.goto(url)
        page.wait_for_timeout(3000) 

        # Localizar os cards
        cards = page.locator("div.sc-1pe7b5t-0.eJgBOc")
        count = cards.count()

        print(f"Total de reclamações na página {pagina}: {count}")

        for i in range(count):
            card = cards.nth(i)

            try:
                titulo = card.locator("h4").inner_text().strip()
                descricao = card.locator("p.sc-1pe7b5t-2.eHoNfA").inner_text().strip()

                print(f"Reclamação {i + 1}: {titulo} - {descricao}")

                reclamacoes.append({
                    "titulo": titulo,
                    "descricao": descricao
                })

            except Exception as e:
                print(f"Erro ao extrair card {i + 1}: {e}")

    browser.close()

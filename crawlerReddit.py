from playwright.sync_api import sync_playwright
import time

def get_post_data(url:str)-> dict:
    post_data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url)
        page.wait_for_timeout(3000) 

        tittle = page.locator('h1#post-title-t3_172eh8n').inner_text()
        description = page.locator("div#t3_172eh8n-post-rtjson-content")
        post_data['titulo'] = tittle
        for text in range(description.count()):
            paragraph = description.nth(text)
            post_data['descricao'] = paragraph.inner_text()

        browser.close()
        return post_data

def get_post_comments(url:str):
    post_comments = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url)
        page.wait_for_timeout(5000) 

        previous_scroll = -1
        scroll_action = 0

        comment_section = page.locator("shreddit-comment")
        count = comment_section.count()
        while True:

             if count == previous_scroll:
                 scroll_action += 1
             else:
                 scroll_action = 0

             if scroll_action >= 2:
                 break

             previous_scroll = count 
             page.mouse.wheel(0, 2000)
             time.sleep(1)
        comments = []
        for i in range(comment_section.count()):
                comment = comment_section.nth(i)
                ps = comment.locator('p').all_inner_texts()
                comments.append(ps)
        for comment in comments:
            result = [comentario for texto in comments for comentario in texto]
            post_comments['comentarios']=result
        browser.close()
        return post_comments

url = 'https://www.reddit.com/r/saopaulo/comments/172eh8n/a_enel_funciona_muito_mal_na_sua_%C3%A1rea/'
print(get_post_comments(url))
# print(get_post_data(url))
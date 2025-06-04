from playwright.sync_api import sync_playwright
import time
import requests

def get_posts_links(subreddit: str, query: str, limit: int) -> dict:
    response_body = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/search.json"
    params = {
        'q': query,
        'restrict_sr': 'on',
        'sort': 'comments',
        't': 'all',
        'limit': limit
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        for post in data['data']['children']:
            post_id = post['data']['id']
            permalink = post['data']['permalink']
            full_url = f"https://www.reddit.com{permalink}"

            response_body[post_id] = {
                'link': full_url
            }
    except requests.exceptions.RequestException as e:
        print(f"{response.status_code}: {e}")
    return response_body

def get_post_comments(url: str, post_id: str) -> dict:
    post_comments = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            page.goto(url)
            page.wait_for_timeout(5000)
        except Exception as e:
            print(f"Erro ao carregar a página: {e}")
            browser.close()
            return post_comments

        previous_scroll = -1
        scroll_action = 0

        comment_section = page.locator("shreddit-comment")
        while True:
            count = comment_section.count()
            if count == previous_scroll:
                scroll_action += 1
            else:
                scroll_action = 0

            if scroll_action >= 2:
                break

            previous_scroll = count
            try:
                page.mouse.wheel(0, 1000)
            except Exception as e:
                print(f"Erro ao carregar a página: {e}")
                break
            time.sleep(2)

        comments = []
        for i in range(comment_section.count()):
            comment = comment_section.nth(i)
            try:
                content = comment.locator('p').all_inner_texts()
                comments.append(content)
            except Exception as e:
                print(f"Erro ao carregar o elemento: {e}")

        result = [comentario for texto in comments for comentario in texto]
        if post_id not in post_comments:
            post_comments[post_id] = {'comentarios': []}
        post_comments[post_id]['comentarios'] = result

        browser.close()
    return post_comments

def filter_comments(post:dict)-> list[str]:
    for key,item in post.items():
        phrase = item['comentarios']
        return phrase
        
        
    

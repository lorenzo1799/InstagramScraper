import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = "https://www.instagram.com/"
user = input("Inserisci nome utente: ")

user_url = url + user + "/"

driver = webdriver.Chrome()

try:
    driver.get(user_url)
    time.sleep(6) 
    html = driver.page_source
    soup = bs(html, 'html.parser')
    
    # numero di post
    post_count = None
    post_span = soup.find_all('span', {'class': 'xdj266r'})
    for span in post_span:
        if 'post' in span.text:
            post_count = span.find_next('span').text.replace(',', '')
            break
    
    if post_count:
        print(f"Number of posts: {post_count}")
    else:
        print("Posts count not found")

    # numero di follower
    followers_count = None
    followers_span = soup.find_all('span', {'class': 'xdj266r'})
    if len(followers_span) > 1:
        followers_count = followers_span[1].text.replace(',', '')
    else:
        print("Followers count not found")

    if followers_count:
        print(f"Number of followers: {followers_count}")

    # numero di following
    following_count = None
    following_span = soup.find_all('span', {'class': 'xdj266r'})
    if len(following_span) > 2:
        following_count = following_span[2].text.replace(',', '')
    else:
        print("Following count not found")
    
    if following_count:
        print(f"Number of following: {following_count}")
    
finally:
    driver.quit()

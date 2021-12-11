import feedparser, datetime

tistory_blog_uri="https://imksh.com"
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """# 블로그 동기화
티스토리 최신글을 동기화 합니다  

## 최신 게시글
"""

lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("Tistory.adoc",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
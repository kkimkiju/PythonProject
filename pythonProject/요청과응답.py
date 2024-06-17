
from bs4 import BeautifulSoup

# HTML 문서
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <a href="https://www.example.com">Link</a>
  </body>
</html>
'''

# HTML 문서를 파싱하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')

# 타이틀 태그를 검색
title_tag = soup.title
print(title_tag)

# 클래스가 "content"인 div 태그 검색 (CSS 선택자를 이용하여 태그를 추출)
div_tags = soup.select('div.content') #div 클래스 선택자인 content 추출
for div in div_tags:
    print(div)

# href 속성이 있는 모든 a 태그 검색
a_tags = soup.find_all('a', href=True)
for a in a_tags:
    print(a)

# Tag 객체 다루기
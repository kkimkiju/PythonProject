
from bs4 import BeautifulSoup

# HTML 문서
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body id = "container">
  <div class="example">여기는 example인 div 태그 입니다. </div>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <div id = "parent">
    <div class="child">첫 번째 자식</div>
    <div class="child">두 번째 자식</div>
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

# Tag 객체에서 요소의 이름 얻기
tag_name = title_tag.name
print(tag_name)  # 'title'

# Tag 객체에서 요소의 속성 얻기
tag_attrs = div_tags[0].attrs
print(tag_attrs)  # {'class': ['content']}

# Tag 객체에서 요소의 내용 얻기
tag_content = div_tags[0].text
print(tag_content)  # 'This is a paragraph.\nThis is another paragraph.'

div_tags =soup.select('div.example')
print(div_tags)

#id 선택자 사용하기
id_sel = soup.select_one("#container")
print(id_sel)

children = soup.select("#parent >.child")
print(children)

attrs = {"class" : "example"}
el = soup.find_all(attrs=attrs)
print(el)
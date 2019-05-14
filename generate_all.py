from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
    page = f"<html>{head} {body}</html>"
    return page

def generate_head(title):
    head = f"""<head>
    <meta charset = 'utf-8'>
    <title>{title}</title>
    </head>"""
    return head

def generate_body(header, paragraphs, link, textLink):
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = f"""{body}
        <p>{p}</p>"""
    body = f"{body} <p><a href = '{link}'>{textLink}</a>"
    return f"""<body> 
            {body} 
            </body>"""

def save_pages(title, header, paragraphs, link, textLink, output = 'index.html'):
    fp = open(output, "w")
    page = generate_page(
            head = generate_head(title), 
            body = generate_body(
                header = header, paragraphs = paragraphs, link = link, textLink = textLink)
            )
    print(page, file = fp)
    fp.close()
 

today = dt.now().date()
save_pages(
    title = "Гороскоп на сегодня",
    header = f"Сегодня, {str(today)}, Вас ожидает:",
    paragraphs = generate_prophecies(),
    link = "about.html",
    textLink = 'О реализации'
)    

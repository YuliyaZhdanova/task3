from horoscope import generate_prophecies, times, advices, promises

def generate_page(head, body):
    page = f"<html>{head}{body}</html>"
    return page

def generate_head(title):
    head = f"<head><meta charset = 'utf-8'><title>{title}</title></head>"
    return head

def generate_body(header, image, link):
    timesList = ""
    advicesList = ""
    promisesList = ""
    body = f"""<h1>{header}</h1>
    <img src='{image}' width='100px' height='100px' alt='horoscope'/>
    <ol><li>Время суток<ul>"""
    for i in range(len(times)):
        timesList += f"<li>{times[i]}</li>"
    body =  f"{body}{timesList}</ul></li><li>Глаголы<ul>"
    for i in range(len(advices)):
        advicesList += f"<li>{advices[i]}</li>"
    body =  f"{body}{advicesList}</ul></li><li>Ожидания<ul>"
    for i in range(len(promises)):
        promisesList += f"<li>{promises[i]}</li>"
    body =  f"""{body}{promisesList}</ul></li></ol>
    <p><a href = '{link}'>Назад</a></p>"""
    return f"<body>{body}</body>"

def save_page(title, header, image, link, output = 'about.html'):
    fp = open(output, "w")
    page = generate_page(
        generate_head(title = title),
        generate_body(header = header, image = image, link = link),
    )
    print(page, file = fp)
    fp.close 

save_page(
    title = "Информация",
    header = "О чем это все",
    image = 'horoscope.png',
    link = "/"
)
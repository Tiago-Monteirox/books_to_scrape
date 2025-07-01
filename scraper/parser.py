from bs4 import BeautifulSoup

def extrair_livros(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    livros = []
    for article in soup.select("article.product_pod"):
        titulo = article.h3.a["title"]
        preco = article.select_one(".price_color").text
        link = "http://books.toscrape.com/" + article.h3.a["href"]
        livros.append({
            "titulo": titulo,
            "preco": preco,
            "link" : link
        })
        print(f"Encontrados {len(livros)} livros.")
    driver.quit()
    return livros

import csv 
from scraper.fetcher import abrir_site
from scraper.parser import extrair_livros
from scraper.database import Session
from scraper.models import Livro
from sqlalchemy.exc import IntegrityError

def main():
    driver = abrir_site()
    livros = extrair_livros(driver)
    session = Session()
    for l in livros:
        try:
            livro = Livro(**l)
            session.merge(livro)
            session.commit()
        except IntegrityError:
             session.rollback() #ignora duplicados
    print("Scrapping terminado.")


    with open("livros.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Titulo", "Preço", "Link" ])
            for l in livros:
                writer.writerow([l["titulo"], l["preco"], l["link"]])
    print("Scraping e exportação terminados")

if __name__ == "__main__":
    main()
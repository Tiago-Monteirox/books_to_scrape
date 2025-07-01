
# from scraper.database import Session
# from scraper.models import Livro

# def exportar_csv():
#     session = Session() 
#     livros = session.query(Livro).all()

#     with open("livros.csv", newline='', encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Titulo", "Preço", "Link" ])
#         for l in livros:
#             writer.writerow([l.titulo, l.preco, l.link])
#     print(f"{len(livros)} livros exportados para livros.csv")

# if __name__ == "__main__":
#     exportar_csv()

## 🗂️ Projeto de Web Scraping – Books to Scrape

### 🎯 Objetivo

Fazer scraping dos livros da página [http://books.toscrape.com/](http://books.toscrape.com/), extrair título, preço e link de cada livro, guardar numa base de dados SQLite e exportar para CSV.

---

## 📁 Estrutura do Projeto


```python
bookstoscrape/
├── main.py                # Executa scraping, grava e exporta
├── requirements.txt       # Bibliotecas necessárias
├── livros.csv             # Resultado final (gerado)
├── books.db               # Base de dados SQLite (gerado)
└── scraper/
    ├── __init__.py
    ├── fetcher.py         # Abertura do site com Selenium
    ├── parser.py          # Extração de dados com BeautifulSoup
    ├── models.py          # Modelo Livro (SQLAlchemy)
    └── database.py        # Setup de SQLite

```

---

## 📦 requirements.txt


```txt
selenium<4.15
chromedriver-autoinstaller
beautifulsoup4
sqlalchemy
```

## 🔄 Fluxo de Execução

1. `main.py` chama `abrir_site()` → navegador abre página
    
2. `extrair_livros(driver)` → extrai dados HTML com BeautifulSoup
    
3. Salva dados na base de dados SQLite (`books.db`)
    
4. Exporta os livros scrapados para `livros.csv`
    

---

## 🧠 Notas Técnicas

- `chromedriver_autoinstaller` instala o ChromeDriver automaticamente
    
- `session.commit()` e `session.rollback()` controlam gravações
    
- `link` tem `unique=True` para evitar duplicados

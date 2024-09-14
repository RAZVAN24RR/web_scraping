
from myapp.models import Article
from myapp.services.selenium_service import search_wikipedia


def log_article_to_terminal(title, paragraph1, paragraph2):
    print(f"Received Article: Title: {title}, Paragraph 1: {paragraph1}, Paragraph 2: {paragraph2}")

def create_article(title, paragraph1, paragraph2):
    article = Article.objects.create(title=title, paragraph1=paragraph1, paragraph2=paragraph2 )
    log_article_to_terminal(title,paragraph1,paragraph2)
    return article

def get_subject_from_wikipedia(subject):
    article = search_wikipedia(subject);
    articleData = Article.objects.create(title=article["title"],paragraph1=article["paragraph1"], paragraph2=article["paragraph2"])
    log_article_to_terminal(article["title"],article["paragraph1"],article["paragraph2"])
    return article;
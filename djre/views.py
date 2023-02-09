"""
To render web pages
"""
from django.http import HttpResponse
import random
from articles.models import Article


def home_view(request):
    """takes in a request(django sends request)
    return html as a response(we pick up the return the response)
    """

    #grabing from the database article_obj
    name = "sunny"
    name2 = "babu"
    random_id = random.randint(1, 3)
    number2 = random.randint(12, 27379624)
    wc = "Welcome On Board"

    article_obj = Article.objects.get(id=random_id)

    H1_STRING = f""" 
    <h1> Hi {name} - {wc} {article_obj.title} (ID:{article_obj.id})</h1>
    """
    P_string = f"""
    <p> Hey {name2} - {number2} {wc} {article_obj.content}</p>
    """
    HTML_STRING = H1_STRING + P_string

    return HttpResponse(HTML_STRING)
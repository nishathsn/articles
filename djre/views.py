"""
To render web pages
"""
from django.http import HttpResponse
import random



def home_view(request):
    """takes in a request(django sends request)
    return html as a response(we pick up the return the response)
    """
    name = "sunny"
    name2 = "babu"
    number = random.randint(10, 33424234)
    number2 = random.randint(12, 27379624)
    wc = "Welcome On Board"
    H1_STRING = f""" 
    <h1> Hi {name} - {number} {wc} </h1>
    """
    P_string = f"""
    <p> Hey {name2} - {number2} {wc}</p>
    """
    HTML_STRING = H1_STRING + P_string

    return HttpResponse(HTML_STRING)
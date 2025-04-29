from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    """
    Контроллер главной траницы сайта
    """

    return HttpResponse("Здесь будет выведен список объявлений")

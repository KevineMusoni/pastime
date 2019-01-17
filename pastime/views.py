from django.shortcuts import render
from django.http import HttpResponse
from .models import Sport

def pastime(request):
    sports = Sport.all_sports()
    return render(request, 'pastime.html', {"sports":sports})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_sports = Sport.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"sports": searched_sports})
    else:
        message = "No results found under this category"
        return render(request, 'search.html',{"message":message})
    return render(request,"search.html")

def sport(request,sport_id):
    try:
        sport = Sport.objects.get(id = sport_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"sport.html",{"sport":sport})
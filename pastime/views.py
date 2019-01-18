from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sport,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

def pastime(request):
    sports = Sport.all_sports()
    return render(request, 'pastime.html', {"sports":sports})

def allsports(request):
    sports = Sport.all_sports()
    return render(request, 'allsports.html', {"sports":sports})

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

@login_required(login_url='/accounts/login/')
def sport(request,sport_id):
    try:
        sport = Sport.objects.get(id = sport_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"sport.html",{"sport":sport})
@login_required(login_url='/accounts/login/')
def mine(request):
    user_object = request.user
    return render(request, 'myprofile.html', locals())


@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            return redirect('myaccount')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', locals())

@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object=get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('myaccount')
    isfollowing = user_object.profile not in request.user.profile.follows
    user_images = user_object.profile.posts.all()
    return render(request, 'profile.html', locals())
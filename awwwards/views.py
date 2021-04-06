from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ReviewForm
from .models import Projects,Profile
from datetime import datetime
from django.contrib.auth.models import User
from .forms import ProfileForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Projects.objects.all()
    myDate = datetime.now()
    return render(request,'index.html',{"images":images,'date': myDate,})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    ordering=['-date_posted']
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,  user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    images = Projects.objects.filter(user=current_user)
    profile = Profile.objects.all()

    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.profile = request.user.profile
            post.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'updateprofile.html',{"form":form})

def ratings_views(request, post_id):
    project = get_object_or_404(Projects, pk=post_id)
    posts= Projects.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.save()
        return redirect('add_review',post_id)
    else:
        form=ReviewForm()
    return render(request, 'review/review_detail.html',{"project":project},locals())
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render (request, 'review/review_list.html', context)

def review_detail(request, review_id):  
    review = get_object_or_404(Projects, pk=review_id)
    return render(request, 'review/review_detail.html', {'review':review})

def search_results(request):
    if 'project' in request.GET and request.GET["project"]: 
        search_term = request.GET.get("project")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "projects": searched_projects})        
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
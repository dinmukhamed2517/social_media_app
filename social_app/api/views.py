from django.shortcuts import render, redirect
from django.contrib import messages
from api.models import Profile, Post
from api.forms import PostForm
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        success = False
        if request.method == "POST":
            if form.is_valid():
                success = True
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('home')
        posts = Post.objects.all().order_by("-created_data")
        return render(request, 'home.html', {"posts":posts, "form":form, "success":success},)
    else:
        posts = Post.objects.all().order_by("-created_data")
        return render(request, 'home.html', {"posts":posts})
def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {
        "profiles":profiles
        })
    else:
        messages.success(request, ("You must be logged in "))
        return redirect('home')


def profile(request, id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=id)
        if request.method == 'POST':
            current_profile = request.user.profile
            data = request.POST['button-follow']
            if data == 'follow':
                current_profile.follows.add(profile)
            elif data == "unfollow":
                current_profile.follows.remove(profile)
            current_profile.save()
        return render(request, "profile.html", {
            "profile": profile
        })
    else:
        messages.success(request, ("You must be logged in "))
        return redirect('home')



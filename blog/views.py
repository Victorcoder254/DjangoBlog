from django.shortcuts import render,redirect
from .forms import CommentForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def landingPage(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

@login_required
def detailPage(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', slug=post.slug)
    else:
            form =CommentForm()
 
    return render(request, 'blog/detail.html', {'post':post,'form':form})    

def signupPage(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        useremail = request.POST.get('email')

        new_user = User.objects.create_user(password=password, email=useremail, username=username)
       
        new_user.first_name = firstname
        new_user.last_name = lastname
        new_user.save()

        return redirect('login')
    return render(request, 'blog/signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("You are seeing this page because you are not registered")
            
    return render(request, 'blog/login.html') 

def logOut(request):
    logout(request)
    return redirect('home')       



from django.shortcuts import render_to_response, render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # context= {'posts': posts}
    #grab info inside database, put in variable
    return render(request, 'index.html', {'posts': posts})

@login_required
def post_new(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    text = request.POST.get('text')
    new_post = Post(author=author, title=title, text=text)
    new_post.save()

    return HttpResponseRedirect('/billboard')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            return HttpResponseRedirect('/billboard')
    form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
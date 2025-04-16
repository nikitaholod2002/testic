from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import comment

from authorization.models import User
from .models import Post, Comment
from .forms import PostForm

def index(request):
    if request.session['user']:
        test = request.session['user']
        post = Post.objects.all()
        print(post)
        return render(request, 'posts.html', {'test': test, 'posts':post})
    else:
        return render(request, 'posts.html',{'test': None})

def post_info(request):
    post_id = request.GET.get('id')
    info = Post.objects.filter(id=post_id)
    comments = Comment.objects.filter(post_id = post_id)

    if (request.method == 'POST' and request.POST.get('like') is not None):
        info.update(like = info[0].like+1)

    if(request.method == 'POST' and request.POST.get('comment') is not None):
        comment = Comment.objects.create(text = request.POST.get('comment'), user_email = User.objects.get(email = request.session['user']), post_id = info[0])
        comment.save()

    return render(request, 'post_info.html', {'post':info, 'test':request.session['user'], 'comments': comments})

def add_post(request):
    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            user = User.objects.get(email = request.session['user'])
            post = Post.objects.create(name = form.cleaned_data['name'], full_text = form.cleaned_data['full_text'], user_email = user)
            post.save()

            return redirect(index)

    else:
        form = PostForm()

    return render(request, "post_add.html", {"form": form, 'test':request.session['user']})

def my_posts(request):

    if request.method == "GET":
        posts = Post.objects.filter(user_email = request.session['user'])
        return render(request, 'my_posts.html', {'posts': posts, 'test':request.session['user']})
    else:
        post = Post.objects.get(id = request.POST.get('id'))
        post.delete()
        return redirect(my_posts)
    

def post_red(request):
    post = Post.objects.get(id = request.GET.get('id'))

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            post.name = form.cleaned_data['name']
            post.full_text = form.cleaned_data['full_text']
            post.save()

            return redirect(my_posts)

    else:
        form = PostForm(initial={'name': post.name, 'full_text': post.full_text})

        return render(request, "post_red.html", {"form": form, 'test':request.session['user']})


  
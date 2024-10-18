from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()

    if not request.user.is_staff:
        posts = posts.published()

    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    posts = Post.objects.all()

    if not request.user.is_staff:
        posts = posts.published()

    post = get_object_or_404(posts, slug=slug)
    return render(request, "blog/post_detail.html", {"title": post.title, "post": post})


@login_required
def post_new(request):
    if request.POST:
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            if "publish" in request.POST:
                post.publish(commit=False)

            post.save()

            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm()

    return render(request, "blog/post_edit.html", {"title": "New Post", "form": form})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.POST:
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save(commit=False)

            if "publish" in request.POST:
                post.publish(commit=False)

            post.save()

            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_edit.html", {"title": "Edit Post", "form": form})

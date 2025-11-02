from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.http import HttpResponse
from .models import Post, Comment, Category, Tag
from .forms import PostForm, CommentForm

def _is_htmx(request):
    return request.headers.get("HX-Request") == "true"

def post_list(request):
    q = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category")
    tag_slug = request.GET.get("tag")

    posts = Post.objects.select_related("author", "category").prefetch_related("tags")
    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(body__icontains=q))
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)

    categories = Category.objects.annotate(n=Count("posts")).order_by("name")
    tags = Tag.objects.annotate(n=Count("posts")).order_by("name")

    context = {"posts": posts, "q": q, "categories": categories, "tags": tags}

    # HTMX partial swap for results list
    if _is_htmx(request):
        return render(request, "blog/_post_list_results.html", context)

    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related("author", "category").prefetch_related("tags", "comments"),
        pk=pk
    )
    comments = post.comments.all()

    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post, author=request.user, text=form.cleaned_data["text"]
            )
            return redirect("blog:post_detail", pk=post.pk)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "comment_form": form},
    )


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        return redirect("blog:post_detail", pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_detail", pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {"form": form, "post": post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        return redirect("blog:post_detail", pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {"post": post})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        author_id = request.POST['author_id']
        status = request.POST['status']
        body = request.POST['body']

        post = Post.objects.create(
            title=title,
            slug=slug,
            author_id=author_id,
            status=status,
            body=body
        )

        return redirect('blog:post_list')

    users = User.objects.all()
    return render(request, 'blog/post/create-post.html', {
        'users': users,
    })

def post_update(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        author_id = request.POST['author_id']
        status = request.POST['status']
        body = request.POST['body']

        Post.objects.filter(id=id).update(
            title=title,
            slug=slug,
            author_id=author_id,
            status=status,
            body=body
        )

    users = User.objects.all()
    post = Post.objects.filter(id=id)
    return render(request, 'blog/post/create-post.html', {
        'users': users,
        'post': post[0],
    })

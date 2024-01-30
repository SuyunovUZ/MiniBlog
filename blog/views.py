from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .form import CommentForm, Comment


def home_page(request):
    articles = Article.objects.all().order_by('id')[:5]
    context = {'posts': articles}
    return render(request, 'index.html', context)


def article_page(request):
    posts = Article2.objects.all().order_by('-id')[:7]
    context = {'posts': posts}
    return render(request, 'category.html', context)


def article_detail_page(request, pk):
    comment = Comment.objects.all()[:5]
    post = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request, 'detail', pk=post.id)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form, 'comments': comment}
    return render(request, 'single.html', context)


def about_page(request):
    posts = Article.objects.all().order_by('-id')[:7]
    context = {'posts': posts}
    return render(request, 'single.html', context)

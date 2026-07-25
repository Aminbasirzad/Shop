from django.shortcuts import render

def blog(request):
  return render(request, 'blog/blog.html')

def blog_detail(request):
  return render(request, 'blog/single-blog.html')
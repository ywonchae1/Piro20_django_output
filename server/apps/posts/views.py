from django.shortcuts import render

# Create your views here.

def main(request):
  return render(request, "posts/post_list.html")

def create(request):
  pass
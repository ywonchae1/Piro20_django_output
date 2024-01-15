from django.shortcuts import render, redirect
from .forms import LocalUserForm
from .models import LocalUser

# Create your views here.
def user_list(request):
  search_txt = request.GET.get('search_txt')
  users = LocalUser.objects.all()
  if search_txt:
    users = users.filter(name__contains=search_txt)

  ctx = {'users': users}
  return render(request, 'users/user_list.html', ctx)

def create(request):
  if request.method == 'GET':
    form = LocalUserForm()
    ctx = {'form': form}
    return render(request, 'users/user_create.html', ctx)
  
  form = LocalUserForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('users:list')

def update(request, pk):
  user = LocalUser.objects.get(id=pk)
  if request.method == 'GET':
    form = LocalUserForm(instance=user)
    ctx = {'form': form, 'pk': pk}
    return render(request, 'users/user_update.html', ctx)
  
  form = LocalUserForm(request.POST, instance=user)
  if form.is_valid:
    form.save()
  return redirect('users:list')

def delete(request, pk):
  if request.method == 'POST':
    user = LocalUser.objects.get(id=pk)
    user.delete()
  return redirect('users:list')
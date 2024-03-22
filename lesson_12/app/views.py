from django.shortcuts import render,redirect
from .forms import UserForm 
from .models import CustomUser
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
def create_user(request):
    form =UserForm()
    if request.method=="POST":
        user=UserForm(request.POST)
        user.save()
        # return redirect('app:index')
    return render(request,'create.html', {'form':form} )

class UserList(ListView):
    model=CustomUser 
    template_name='list.html'
    context_object_name='users'

class UserCreate(CreateView):
   model=CustomUser 
   form_class=UserForm
   template_name='create.html'
   success_url=reverse_lazy('index')

class UserDetail(DetailView):
   model=CustomUser 
   template_name='detail.html'
   context_object_name='user'
#    pk_url_kwarg='user_id'

class UserUpdate(UpdateView):
 model=CustomUser 
 form_class=UserForm 
 template_name='update.html'
#  success_url=reverse_lazy('detail',kwargs={'pk':1})
 success_url=reverse_lazy('index')

class UserDelete(DeleteView):
    model=CustomUser 
    success_url=reverse_lazy('index')
    template_name='delete.html'

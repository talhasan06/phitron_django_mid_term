from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView

# Create your views here.
def car(request):
    return render(request,'car.html')

# registration
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
        
    return render(request,'register.html',{'form':register_form,'type':'Register'})

# login
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context

class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self,form):
        messages.success(self.request,'Car added successfully')
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Car'
        return context
    
class AddBrandCreateView(CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self,form):
        messages.success(self.request,'Brand created successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Brand'
        return context
    
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg='id'
    template_name='car_details.html'

    def post(self,request,*args,**kwargs):
            comment_form = forms.CommentForm(data=self.request.POST)
            post = self.get_object()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit = False)
                new_comment.post = post
                new_comment.save()
            return self.get(request,*args,**kwargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


def user_logout(request):
    logout(request)
    return redirect('homepage')

@login_required
def profile(request):
    data = models.Car.objects.filter(author = request.user)
    return render(request,'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account updates successfully')
            return redirect('profile')
    else:
        profile_form = forms.RegistrationForm(instance=request.user)
    return render(request,'edit_profile.html',{'form':profile_form})

class EditCarView(UpdateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

class DeleteCarView(DeleteView):
    model = models.Car
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg='id'
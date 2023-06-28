from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,  authenticate
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from admin_settings.models import Country, Language
from users.models import UserProfile
from users.forms import RegisterForm, UserUpdateForm, UserProfileForm



def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                context = {
                    'message': f'Login correcto, bienvenido... {username}'
                }
                return render(request, 'index.html', context=context)
        
        form = AuthenticationForm()
        context = {
            'form': form,
            'errors': 'Usuario o contraseña incorrecta'
        }
        return render(request, 'users/login.html', context=context)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request,'users/register.html', context=context )
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user = user )
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form': RegisterForm()
        }
        return render(request, 'users/register.html', context=context)
    
@login_required    
def update_user(request):
    user = request.user
    if request.method == 'GET':
        
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request,'users/update_user copy.html', context=context )
        #return render(request,'users/update_user.html', context=context )
    
    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form': UserUpdateForm()
        }
        #return render(request, 'users/update_user.html', context=context)
        return render(request,'users/update_user copy.html', context=context )

def update_user_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial = {
            'phone': user.profile.phone,
            'birth_date': user.profile.birth_date,
            'company_name':user.profile.company_name,
            'occupation':user.profile.occupation,
            'profile_picture': user.profile.profile_picture,
            
        })
        context = {
            'form': form
        }
        #return render(request,'users/update_profile.html', context=context )
        return render(request,'users/update_profile copy.html', context=context )
    
    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)        
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.company_name = form.cleaned_data.get('company_name')
            user.profile.occupation = form.cleaned_data.get('occupation')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form': UserProfileForm()
        }
        #return render(request, 'users/update_profile.html', context=context)
        return render(request, 'users/update_profile copy.html', context=context)
    
def user_profile_view(request):    
    if request.method == 'GET':
        context = {
            'languages': Language.objects.all(),
            'countries': Country.objects.all(),
        }
        return render(request, 'users/user_profile.html',context=context)
    

def users_list_view(request):
    return render(request, 'users/users_list.html')

# con la creacion de un usuario, le crea el perfil
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs ):
    if created:
        UserProfile.objects.create(user=instance)

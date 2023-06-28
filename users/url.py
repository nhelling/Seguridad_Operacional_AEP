from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_view, register, update_user,update_user_profile,register,users_list_view,user_profile_view

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/', register, name = 'register'),
    path('update/', update_user, name = 'update_user'),
    path('update/profile/', update_user_profile, name = 'update_profile'),

    path('list/', users_list_view, name = 'list'),
    path('profile/', user_profile_view, name = 'profile'),


]
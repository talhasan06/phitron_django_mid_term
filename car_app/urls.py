
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('add_car/',views.AddCarCreateView.as_view(),name="add_car"),
    path('add_brand/',views.AddBrandCreateView.as_view(),name="add_brand"),
    path('register/',views.register,name="register"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="homepage"),name="logout"),
    path('profile/',views.profile,name="profile"),
    path('profile/edit/',views.edit_profile,name="edit_profile"),
    path('details/<int:id>/',views.DetailCarView.as_view(),name="car_detail"),
    path('edit/<int:id>/',views.EditCarView.as_view(),name="edit_car"),
    path('delete/<int:id>/',views.DeleteCarView.as_view(),name="delete_car"),

]

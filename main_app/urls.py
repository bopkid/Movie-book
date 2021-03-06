from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/new', views.profile_new, name = 'profile_new'),
    path('accounts/profile/<int:profile_id>', views.profile, name = 'profile'),
    path('accounts/profile/<int:profile_id>/<int:film_id>/remove_movie', views.remove_movie, name = 'remove_movie'),
    path('accounts/profile/<int:profile_id>/add_photo', views.add_photo, name = 'add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/<int:profile_id>/edit', views.edit_profile, name='edit_profile'),
    path('accounts/profile/<int:profile_id>/delete/', views.delete_profile, name='delete_profile'),
    path('movie/index' , views.movie_show ,name= ' movie_index'),
    path('movie/<str:movie_name>/', views.movie_details, name='movie_details'),
    path('movie/<str:movie_name>/comment', views.add_comment_to_movie, name='add_comment_to_movie'),
    path('movie/<str:movie_name>/add_movie', views.add_movie, name = 'add_movie'),
    path('about/us', views.about_us, name='about_us'),
    path('tv/index' , views.tv_show ,name= ' tv_index'),
    path('tv/<str:tv_name>', views.tv_details, name='tv_details'),
    path('tv/<str:tv_name>/comment', views.add_comment_to_tv, name='add_comment_to_tv'),
]


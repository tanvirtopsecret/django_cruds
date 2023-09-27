from django.urls import path
from .views import home, delete, create, single_page, update_page
urlpatterns = [
   path('', home, name="home"),
   path('delete-profile/<int:id>/', delete, name="delete"),
   path('create/', create, name="create"),
   path('single_page/<int:id>/', single_page, name="single_page"),
   path('update_page/<int:id>/', update_page, name="update_page"),
]
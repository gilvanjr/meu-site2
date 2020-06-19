from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   # post views
   path('', views.post_list, name='post_list'),
   path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
   path('create', views.post_create, name='post_create'),
   path('update/<int:id>', views.post_update, name='post_update')
]

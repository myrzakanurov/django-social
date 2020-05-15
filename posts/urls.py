from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('add/', views.PostCreateView.as_view(), name='add'),
    path('all/', views.MyPostListView.as_view(), name='my_list'),
    path('all/<slug:slug>/', views.post_detail_view, name='detail'),
    path('<slug:slug>/', views.post_detail_view, name='detail'),
    # path('all/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('<slug:slug>/add-comment/', views.CommentCreateView.as_view(), name='add_comment'),
]
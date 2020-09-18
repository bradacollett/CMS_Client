from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    ComputerUpdateView,
    ComputerDeleteView,
    ComputerCreateView,
    CommentUpdateView,
    CommentDeleteView,
    CommentCreateView,


)

urlpatterns = [
    # client urls
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),

    # computer urls
    path('computer/<int:pk>/edit/',
        ComputerUpdateView.as_view(), name='computer_edit'),
    path('computer/<int:pk>/delete/',
        ComputerDeleteView.as_view(), name='computer_delete'),
    path('computer/new/',
        ComputerCreateView.as_view(), name='computer_new'),

    #comment urls
    path('comment/<int:pk>/edit/',
        CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/',
        CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/new/',
        CommentCreateView.as_view(), name='comment_new'),
]
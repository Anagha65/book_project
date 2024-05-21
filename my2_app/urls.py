from django.urls import path
from .import views
urlpatterns = [

path("createbook",views.createBook,name='createbook'),

path('author',views.create_Author,name='author'),
path('',views.listBook,name='booklist'),
path('detailsview/<int:book_id>',views.detailsView,name='details'),
path('updateviews/<int:book_id>',views.updateBook,name='updates'),
path('deleteview/<int:book_id>',views.deleteView,name='delete'),
path('index',views.index),

path('search',views.search_Book,name='search')

]
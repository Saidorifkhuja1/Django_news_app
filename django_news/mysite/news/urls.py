from django.urls import path
from .views import news_home, create, NewsDetailView, NewsUpdateView,\
   NewsDeleteView
urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create'),
    path('<int:pk>', NewsDetailView.as_view(), name='details'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete'),
]


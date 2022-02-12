from django.urls import path, include
from . import views

urlpatterns = [
    path('characters/', views.CharacterList.as_view(), name='character_list'),
    path('characters/<int:pk>', views.CharacterDetail.as_view(), name='character_detail'),
    path('quotes/', views.QuoteList.as_view(), name='quote_list'),
    path('quotes/<int:pk>', views.QuoteDetail.as_view(), name='quote_detail'),
]

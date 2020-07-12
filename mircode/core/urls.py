from django.urls import path, include

from .views import *

app_name = 'core'


urlpatterns = [
    path('authors/', AuthorsListAPIView.as_view(), name='authors'),
    path('books/', BooksListAPIView.as_view(), name='books'),
    path('purchase_request/', PurchaseRequestCreateAPIView.as_view(), name='purchase_request'),
    path('registration/', include('rest_auth.registration.urls')),
    path('', include('rest_auth.urls')),
]

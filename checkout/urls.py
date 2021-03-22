from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
<<<<<<< HEAD
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
=======
    path('wh/', webhook, name='webhook'),
]
>>>>>>> e8df62291f8eb5225d15da98c1c3ab80fe22d1a7

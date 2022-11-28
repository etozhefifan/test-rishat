from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('config/', views.stripe_config),
    path('item/<int:id>', views.item_detail, name='item_detail'),
    path('buy/<int:id>', views.buy_item, name='buy'),
]

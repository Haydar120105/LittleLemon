from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemview.as_view(), name="menu"),
    path("menu/<int:pk>/", views.SingleMenuItemview.as_view(), name="singlemenuitem"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
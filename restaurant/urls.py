from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.MenuItemview.as_view(), name="menu"),
    path("menu/<int:pk>/", views.SingleMenuItemview.as_view(), name="singlemenuitem"),
]
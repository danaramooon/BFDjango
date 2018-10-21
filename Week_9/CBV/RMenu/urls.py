from django.urls import path
from RMenu import views

urlpatterns=[
    path('home/',views.HomeView.as_view(),name = 'home'),
    path('restaurant/',views.RestaurantListView.as_view(),name = "restaurant"),
    path('restaurant/<int:id>/delete/',views.DeleteRestaurantView.as_view(),name ="delete_res"),
    path('restaurant/add_new/',views.RestaurantCreateView.as_view(),name = "add_res"),
    path('restaurant/<int:id>/update/',views.RestaurantUpdateView.as_view(),name = "update_res"),
]
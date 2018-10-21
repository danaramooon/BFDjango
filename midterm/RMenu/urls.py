from django.urls import path
from RMenu import views

urlpatterns=[
    path('home/',views.home,name = "home" ),
    path('restaurant/',views.restaurant,name = "restaurant"),
    path('restaurant_detail/<int:id>/',views.restaurant_detail,name = "restaurant_detail"),
    path('restaurant/<int:id>/delete/',views.delete_res,name ="delete_res"),
    path('dish/<int:id>/delete/',views.delete_dish,name ="delete_dish"),
    path('restaurant/<int:id>/dishes/', views.dishes, name = "dish"),
    path('restaurant/<int:id>/review/',views.res_rev,name = "res_rev"),
    path('dish/<int:id>/review_dish/',views.dish_rev, name = "rev_dish"),
    path('add_dish/',views.add_dish, name = "add_dish"),
    path('add_restaurant/',views.add_restaurant, name = "add_restaurant"),
    path('add_res_rev/',views.add_res_rev, name = "add_res_rev"),
    path('user_detail/<int:id>',views.user_detail,name = "user_detail"),
    path('dish_detail/<int:id>',views.dish_detail,name = "dish_detail"),
]
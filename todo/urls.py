from django.contrib import admin
from django.urls import path
from . import views


admin.site.site_header = "My Activity"
admin.site.site_title = "My Activity"
admin.site.index_title = "welcome to  My Activity"



urlpatterns = [
  path("", views.index, name="index"),
  path("delete/<uuid:id>",views.delete_view, name="delete"),
  path("login/",views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout"),
  path("signup/", views.signup, name="signup"),
  path("update/<uuid:id>",views.update_todo,name="update"),
]
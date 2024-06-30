
from django.urls import path
from frontend import views
urlpatterns = [
    path('list',views.showEmp),
    path('addemp',views.addemp),
    path('delete/<empid>',views.delete),
    path('update/<empid>',views.update)
]


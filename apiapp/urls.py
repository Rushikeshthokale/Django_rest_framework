from django.urls import path
from apiapp import views
urlpatterns=[
    path('employees',views.employees),
    path('employees/<empid>',views.empDetails)
]

'''
/employees=> Get fetching all the employees
          =>  POST

/employees/empid=>GET get by id
                 =>Delete
                 =>PUT by id

'''
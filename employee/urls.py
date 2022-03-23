from django.urls import path
from employee import views


urlpatterns = [
    path('departament/',
         views.DepartamentListCreate.as_view(),
         name='departament_list'),

    path('departament/<int:pk>/',
         views.DepartamentRetriveUpdateDestroy.as_view(),
         name='departament_detail'),

    path('employee/',
         views.EmployeetListCreate.as_view(),
         name='employee_list'),

    path('employee/<int:pk>/',
         views.EmployeeRetriveUpdateDestroy.as_view(),
         name='employee_detail'),

]

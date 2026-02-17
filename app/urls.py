from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('category/listCreate/', views.ListCreateDesignCategoryView.as_view()),
    path('category/updateDelete/<int:id>/', views.UpdateDestroyDesignCategoryView.as_view()),
    path('design/listCreate/', views.ListCreateDesignView.as_view()),
    path('design/updateDelete/<int:id>/', views.UpdateDestroyDesignView.as_view()),
]   
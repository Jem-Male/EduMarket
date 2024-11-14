from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path("jobs/",views.jobs_page, name="jobs_page"),
    path("categories/" , views.categories_page, name="categories_page"),
    path("guides/", views.guides_page, name="guides_page"),
    path('jobs/detail/<int:pk>/', views.jobs_detail_page, name='job_detail_page'),
    path('guides/detail/<int:pk>/', views.guide_detail_page, name='guide_detail_page'),
    path('test/<int:pk>/', views.test_page, name='test_page'), 
    path('test_detail_page/<int:pk>', views.test_detail_page, name='test_detail_page'),
    path('api/get_additional_data/<int:pk>/', views.get_additional_data, name='get_additional_data'),
    path("test/", views.test_page, name="test_page"),
    path('category/jobs/<slug:slug>/', views.jobs_by_category, name='jobs_by_category_page'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')
]
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
     path('', views.main_page, name='main_page'),
     path('articles/', views.articles_page, name='articles_page'),
     path('articles/article/<int:pk>/', views.article_page, name="article-page"),
     path('about/', views.about_page, name='about_page'),
     path('shop/', views.product_list, name='product_list'),
     path('news/', views.news_page, name='new_page'),
     path('glossary/', views.glossary_page, name='glossary_page'),
     path('contacts/', views.contacts_page, name='contacts_page'),
     path('policy/', views.privacy_policy_page, name='privacy_policy_page'),
     path('reviews/', views.reviews_page, name='reviews_page'),
     path('promocodes/', views.promo_codes_page, name='promo_codes_page'),
     path('<int:id>', views.product_detail, name='product_detail'),
     path("create/", views.product_create),
     path("edit/<int:id>/", views.product_edit),
     path("delete/<int:id>/", views.product_delete),
     path('<str:product_type_name>/', views.product_list, name='product_list_by_category'),
]
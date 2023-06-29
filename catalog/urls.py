from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, \
    ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView, \
    BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='product_item'),
    path('products/create/', ProductsCreateView.as_view(), name='product_create'), #product_form.html, product_list.html
    path('products/update/<slug:pk>/', ProductsUpdateView.as_view(), name='product_update'),#product_form, inc_cat_card.html
    path('products/delete/<slug:pk>/', ProductsDeleteView.as_view(), name='product_delete'), #product_confirm_delete.html
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<slug:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/toggle/<slug:slug>/', toggle_activity, name='toggle_activity'),
]



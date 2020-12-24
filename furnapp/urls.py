from django.urls import path,reverse_lazy
from django.conf.urls.static import static
from furnapp import views
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomLoginForm,UserPasswordResetForm
from django.contrib.auth import views as auth_views
from django.conf import settings

app_name='furnapp'

urlpatterns = [
    
    path('', views.home,name="main"),
    
    
    path('products/', views.products,name="product"),
    path('about/', views.about,name="aboutus"),
    path('contact/', views.contact,name="contact"),
    path('product-details/<str:product_name>/', views.productsdet,name="productsdet"),
    path('cart/', views.cart,name="cart"),
    path('checkout/', views.checkout,name="checkout"),
    path('updateitem/', views.update_item,name="updateitem"),
    path('process_order/', views.processorder,name="process_order"),
    path('search',views.search,name="search"),
    path('category/<str:category_n>/',views.category,name="category"),
     
    
    path('register/', views.register,name="register"),
    path('login/',LoginView.as_view(template_name="furnapp/login.html",form_class=CustomLoginForm),name="login"),
    path('logout/',LogoutView.as_view(),name='logout'),
     
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name="furnapp/password_reset.html",
        form_class=UserPasswordResetForm,success_url=reverse_lazy('furnapp:password_reset_done')),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="furnapp/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="furnapp/password_reset_form.html",success_url=reverse_lazy('furnapp:password_reset_complete')), 
     name='password_reset_confirm'),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="furnapp/password_reset_done.html"), 
        name="password_reset_complete"),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

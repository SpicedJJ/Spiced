from django.urls import path
from . import views
from .views import InquiryListView, InquiryCreateView, InquiryUpdateView, InquiryDeleteView

urlpatterns = [
    path ('', views.home_page, name="homePage"),
    path ('about/', views.about_page, name="aboutPage"),
    path ('services/', views.services_page, name="servicesPage"),
    path ('contact/', views.contact_page, name="contactPage"),
    path('list/', InquiryListView.as_view(), name='inquiry_list'),
    path('create/', InquiryCreateView.as_view(), name='inquiry_create'),
    path('<int:pk>/update/', InquiryUpdateView.as_view(), name='inquiry_update'),
    path('<int:pk>/delete/', InquiryDeleteView.as_view(), name='inquiry_delete'),
    path('create/', views.create_inquiry, name='create_inquiry'),
    path('<int:pk>/update/', views.update_inquiry, name='update_inquiry'),
    path('<int:pk>/delete/', views.delete_inquiry, name='delete_inquiry'),
]
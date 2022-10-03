from django.urls import path
from pictures.views import landing_page, PictureCreateView, CategoryCreateView

app_name = 'pictures'

urlpatterns = [
    path('', landing_page, name='pictures-landing-page'),
    path('create/', PictureCreateView.as_view(), name='picture-create'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create')
]

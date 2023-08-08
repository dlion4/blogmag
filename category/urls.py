from django.urls import path

from . import views

app_name = "category"

urlpatterns = [
    path("<category_slug>/<pk>/<sub_category_slug>/", views.SubCategoryListView.as_view(), name="sub_category_detail")
]
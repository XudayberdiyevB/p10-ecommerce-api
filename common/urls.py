from django.urls import path

from common.views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="categories-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail")
]

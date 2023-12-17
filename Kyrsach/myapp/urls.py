from django.urls import path
from myapp.views import index, add_item, update_item,  ProductListView, ProductDetailView, ProductDeleteView

app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/myapp/
    # path("", index, name='index'),
    path("", ProductListView.as_view(), name='index'),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    # path("<int:my_id>/", indexItem, name="detail"),
    
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:pk>/", ProductDeleteView.as_view(), name="delete_item"),
    # path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
]
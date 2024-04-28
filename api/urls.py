from . import views
from django.urls import path

urlpatterns = [
    # ------------kategoriyani api dagi urllari-----------
    path('category/list', views.category_list),
    path('category/detail/<int:id>/', views.category_detail),

    # ------------regionni api dagi urllari-----------
    path('region/list', views.region_list),
    path('region/detail/<int:id>/', views.region_detail),

    # ------------postni api dagi urllari-----------
    path('post/list/', views.post_list),
    path('post/detail/<int:id>/', views.post_detail),
    path('post/comment/<int:id>', views.post_comment), # postga aloqador komentariyalar

    # --------postni kategoriya bo'yicha saralash uchun url--------
    path('category-post/<int:id>/', views.category_post),

    # ---------kommentariyani api dagi urllari----------
    path('create-comment/<int:id>', views.comment_create),
    path('comment/detail/<int:id>', views.comment_detail),

    # path('log-in', views.log_in),
    # path('auth/', include('rest_framework.urls'))
]
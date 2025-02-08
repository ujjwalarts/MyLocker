
# from django.urls import path
# from .views import (
#     home, upload_page, document_list_page, access_page, signup_view, login_view, logout_view,verify_document,view_document
# )

# urlpatterns = [
#     path('', home, name='home'),
#     path('signup/', signup_view, name='signup'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('upload/', upload_page, name='upload'),
#     path('documents/', document_list_page, name='documents'),
#     path('access/', access_page, name='access'),
#     path('documents/<int:pk>/view/', view_document, name='view-document'),
#     path('documents/<int:pk>/verify/', verify_document, name='verify-document'),
# ]
#
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, upload_page, document_list_page, access_page, signup_view, login_view, logout_view, verify_document, view_document
)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('upload/', upload_page, name='upload'),
    path('documents/', document_list_page, name='documents'),
    path('access/', access_page, name='access'),
    path('documents/<int:pk>/view/', view_document, name='view-document'),
    path('documents/<int:pk>/verify/', verify_document, name='verify-document'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

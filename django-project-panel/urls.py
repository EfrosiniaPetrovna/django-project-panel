from django.urls import path, include
from django.conf.urls import url

from .views import *


urlpatterns = [
    path('panel/', Panel.as_view(), name='project_panel'),
    path('clean_table/<alias>/<table>/', CleanTable.as_view(), name='project_panel_clean_table'),
]

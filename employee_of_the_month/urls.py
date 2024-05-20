from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('area/', include('employee.urls')),
    path('documenttype/', include('employee.urls')),
    path('person/', include('employee.urls')),
    path('photoperson/', include('employee.urls')),
    path('vote/', include('employee.urls')),
    path('description/', include('employee.urls')),
    path('', include('employee.urls')),
]

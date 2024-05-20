# urls.py
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from employee import views

router = routers.DefaultRouter()
router.register(r'areas', views.AreaView, 'area')
router.register(r'documenttypes', views.DocumentTypeView, 'documenttype')
router.register(r'persons', views.PersonView, 'person')
router.register(r'photopersons', views.PhotoPersonView, 'photoperson')
router.register(r'votes', views.VoteView, 'vote')
router.register(r'descriptions', views.DescriptionView, 'description')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Employee API Documentation'))
]

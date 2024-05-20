# views.py
from rest_framework import viewsets
from .models import Area, DocumentType, Person, PhotoPerson, Vote, Description
from .serializer import AreaSerializer, DocumentTypeSerializer, PersonSerializer, PhotoPersonSerializer, VoteSerializer, DescriptionSerializer

class AreaView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class DocumentTypeView(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PhotoPersonView(viewsets.ModelViewSet):
    queryset = PhotoPerson.objects.all()
    serializer_class = PhotoPersonSerializer

class VoteView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class DescriptionView(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

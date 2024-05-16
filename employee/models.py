from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Area(models.Model):
    AREAS_CHOICES = (
        ('Desarrollo', 'Desarrollo'),
        ('Soporte', 'Soporte'),
    )
    name = models.CharField(max_length=100, choices=AREAS_CHOICES)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class DocumentType(models.Model):
    DOCS_CHOICES = (
        ('C.C', 'Cédula de Ciudadanía'),
        ('C.E', 'Cédula de Extranjería'),
    )
    type = models.CharField(max_length=100, choices=DOCS_CHOICES, default='C.C')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.type

class Person(models.Model):
    name = models.CharField(max_length=250)
    identification = models.CharField(max_length=10, unique=True)
    id_type_document = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    id_person_picture = models.ForeignKey('PhotoPerson', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['name', 'identification']

    def display_area(self):
        return self.id_area.name

    display_area.short_description = 'Area'

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class PhotoPerson(models.Model):
    url_photo = models.ImageField(upload_to='PhotoPerson/')
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'PhotoPerson'
        verbose_name_plural = 'PhotoPeople'
        ordering = ['id']


    def __str__(self):
        return self.id_person.name

class Vote(models.Model):
    PERIOD_CHOICES = (
        ('01', 'Enero'),
        ('02', 'Febrero'),
        ('03', 'Marzo'),
        ('04', 'Abril'),
        ('05', 'Mayo'),
        ('06', 'Junio'),
        ('07', 'Julio'),
        ('08', 'Agosto'),
        ('09', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
    )
    period = models.CharField(max_length=100, choices=PERIOD_CHOICES)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)

    class Meta:
        ordering = ['vote_date', 'period']

    def display_area(self):
        return  self.id_area.name

    display_area.short_description = 'Area'

    def __str__(self):
        return self.period



class Description(models.Model):
    id_vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    id_voter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='voter')
    id_voted = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='voted')
    state = models.BooleanField(default=True)

    class Meta:
        ordering = ['id_voter', 'id_voted']

    def display_voter(self):
        return self.id_voter.name

    display_voter.short_description = 'Voter'

    def display_voted(self):
        return self.id_voted.name

    display_voted.short_description = 'Voted'

    def display_vote_period(self):
        return self.id_vote.period

    display_vote_period.short_description = 'Period'



    def __str__(self):
        return self.id_voted.name




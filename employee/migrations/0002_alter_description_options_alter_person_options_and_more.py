# Generated by Django 5.0.6 on 2024-05-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'ordering': ['id_voter', 'id_voted']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name', 'identification'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='photoperson',
            options={'ordering': ['id'], 'verbose_name': 'PhotoPerson', 'verbose_name_plural': 'PhotoPeople'},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'ordering': ['vote_date', 'period']},
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(choices=[('Desarrollo', 'Desarrollo'), ('Soporte', 'Soporte')], max_length=100),
        ),
        migrations.AlterField(
            model_name='area',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='type',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería')], default='C.C', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='identification',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='period',
            field=models.CharField(choices=[('01', 'Enero'), ('02', 'Febrero'), ('03', 'Marzo'), ('04', 'Abril'), ('05', 'Mayo'), ('06', 'Junio'), ('07', 'Julio'), ('08', 'Agosto'), ('09', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')], max_length=100),
        ),
    ]
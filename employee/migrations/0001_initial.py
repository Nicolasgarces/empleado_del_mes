# Generated by Django 5.0.6 on 2024-05-10 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('identification', models.CharField(max_length=10)),
                ('state', models.BooleanField(default=True)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.area')),
                ('id_type_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.documenttype')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_photo', models.ImageField(upload_to='PhotoPerson/')),
                ('state', models.BooleanField(default=True)),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='id_person_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.photoperson'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=100)),
                ('vote_date', models.DateTimeField(auto_now_add=True)),
                ('state', models.BooleanField(default=True)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.area')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('id_voted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voted', to='employee.person')),
                ('id_voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to='employee.person')),
                ('id_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.vote')),
            ],
        ),
    ]

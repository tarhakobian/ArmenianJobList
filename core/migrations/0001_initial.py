# Generated by Django 4.2 on 2023-04-18 09:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3d0e5d57-59a6-4adf-ac81-c0e09883b9a3'), editable=False,
                                        primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('eca93acc-f068-42c8-9563-5ffc5698978b'), editable=False,
                                        primary_key=True, serialize=False)),
                ('category', models.CharField(db_index=True, default='Mixed', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('requirements', models.TextField(default='No Requirements', null=True)),
                ('salary', models.CharField(max_length=255, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]
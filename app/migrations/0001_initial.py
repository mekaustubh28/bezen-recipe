# Generated by Django 4.1 on 2022-08-12 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(default='', max_length=1000)),
                ('recipe_description', models.TextField(default='', max_length=10000)),
                ('ingredients', models.CharField(default='', max_length=10000)),
                ('category', models.CharField(default='', max_length=1000)),
                ('images', models.ImageField(default='', upload_to='images/')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

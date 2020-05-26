# Generated by Django 3.0.6 on 2020-05-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.CharField(blank=True, max_length=50)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

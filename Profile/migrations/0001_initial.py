# Generated by Django 3.2.4 on 2021-07-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('bio', models.CharField(max_length=1000)),
            ],
        ),
    ]
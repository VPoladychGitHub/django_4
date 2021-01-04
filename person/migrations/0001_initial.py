# Generated by Django 3.1.4 on 2021-01-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='username')),
                ('last_name', models.CharField(max_length=100, verbose_name='password')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]

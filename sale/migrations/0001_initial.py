# Generated by Django 3.1.4 on 2021-01-15 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='path')),
                ('number_inhabitants', models.CharField(max_length=100, verbose_name='method')),
            ],
            options={
                'ordering': ['name', 'number_inhabitants'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='path')),
                ('price', models.FloatField(verbose_name='method')),
            ],
            options={
                'ordering': ['name', 'price'],
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sale.city')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.city')),
                ('product', models.ManyToManyField(help_text='Select a product for this customer', to='sale.Product', verbose_name='product')),
            ],
            options={
                'ordering': ['-timestamp', 'city'],
            },
        ),
    ]

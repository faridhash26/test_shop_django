# Generated by Django 3.2.9 on 2021-11-18 08:03

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title of Product')),
                ('description', models.TextField(verbose_name='description')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='child of which category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title of Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title of Product')),
                ('is_active', models.BooleanField(default=True, verbose_name='is available item?')),
                ('price', models.PositiveIntegerField(verbose_name='price of Product')),
                ('qty_stock', models.PositiveIntegerField(verbose_name='quantity of Product form supplier')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user that sell this item')),
                ('tags', models.ManyToManyField(to='product.Tag', verbose_name='tags')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]

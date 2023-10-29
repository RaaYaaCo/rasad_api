# Generated by Django 4.2.6 on 2023-10-28 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degrees',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/images/', verbose_name='image')),
                ('slug', models.CharField(blank=True, db_index=True, max_length=100, unique=True, verbose_name='slug')),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.degree', verbose_name='degree')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Products Type',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(db_index=True, verbose_name='price')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date and time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product price',
                'verbose_name_plural': 'Products price',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.producttype', verbose_name='product type'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.unit', verbose_name='Unit'),
        ),
    ]

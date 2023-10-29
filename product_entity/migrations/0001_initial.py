
# Generated by Django 4.2.6 on 2023-10-28 05:04


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice_sale', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_sales_item_price', models.PositiveIntegerField(verbose_name='Invoice Sales price')),
                ('sale_price', models.PositiveIntegerField(verbose_name='sale price')),
                ('weight', models.PositiveIntegerField(verbose_name='weight')),
                ('is_active', models.BooleanField(default=True, verbose_name='active/deactivate')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('invoice_sales_item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice_sale.invoicesales', verbose_name='Invoice Sales')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product Entity',
                'verbose_name_plural': 'Products Entity',
            },
        ),
    ]

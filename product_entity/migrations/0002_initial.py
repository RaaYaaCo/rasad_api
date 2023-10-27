# Generated by Django 4.2.6 on 2023-10-27 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_entity', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productentity',
            name='store_ugo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storeProductEntity', to='user.usergrouporganization', verbose_name='store'),
        ),
    ]

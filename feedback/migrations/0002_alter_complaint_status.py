# Generated by Django 4.2.6 on 2023-10-26 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.ForeignKey(default='درحال بررسی', on_delete=django.db.models.deletion.PROTECT, to='feedback.complaintstatus', verbose_name='status'),
        ),
    ]

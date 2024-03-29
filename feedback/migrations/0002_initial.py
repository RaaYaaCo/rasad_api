
# Generated by Django 4.2.6 on 2023-10-28 05:11


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('feedback', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintresponse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.usergrouporganization', verbose_name='user'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.complaintresponse', verbose_name='response'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feedback.complaintstatus', verbose_name='status'),

        ),
        migrations.AddField(
            model_name='complaint',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='store_id', to='user.usergrouporganization', verbose_name='store id'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to='user.usergrouporganization', verbose_name='user'),
        ),
    ]

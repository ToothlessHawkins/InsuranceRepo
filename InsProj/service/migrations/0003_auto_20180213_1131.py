# Generated by Django 2.0.2 on 2018-02-13 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180212_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job', to='service.Request'),
        ),
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='request',
            name='mechanic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mechanic', to='service.Mechanic'),
        ),
    ]
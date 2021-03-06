# Generated by Django 2.0.2 on 2018-02-19 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_Account', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_Account', to='accounts.account'),
        ),
    ]

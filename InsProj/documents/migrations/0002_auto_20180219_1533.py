# Generated by Django 2.0.2 on 2018-02-19 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_auto_20180219_1533'),
        ('accounts', '0002_auto_20180219_0948'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='policy',
        ),
        migrations.AddField(
            model_name='transaction',
            name='t_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='t_account', to='accounts.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='t_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='t_policy', to='policies.policy'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='NewBalance',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='PriorBalance',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]

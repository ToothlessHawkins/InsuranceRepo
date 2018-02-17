# Generated by Django 2.0.2 on 2018-02-16 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180216_1610'),
        ('policies', '0003_auto_20180216_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='actual_date_of_payment',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='car_model',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='policy_plan',
        ),
        migrations.AddField(
            model_name='policy',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='account', to='accounts.account'),
        ),
        migrations.AddField(
            model_name='policy',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='payment_due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='policy',
            name='payment_plan',
            field=models.CharField(choices=[('Y', 'Yearly'), ('M', 'Monthly'), ('W', 'Weekly')], default='Yearly', max_length=1),
        ),
        migrations.AlterField(
            model_name='policy',
            name='suspended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='policy',
            name='total_rate',
            field=models.DecimalField(choices=[('12000.00', 'Full'), ('6000.00', 'Half'), ('3000.00', 'Liability')], decimal_places=2, max_digits=8),
        ),
    ]

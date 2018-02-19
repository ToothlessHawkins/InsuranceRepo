# Generated by Django 2.0.2 on 2018-02-18 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='make_payment',
            fields=[
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='policies.policy')),
                ('payment', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
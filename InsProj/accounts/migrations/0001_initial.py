# Generated by Django 2.0.2 on 2018-02-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField(auto_created=True, default='0', null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('corporation', models.CharField(max_length=50)),
                ('billing_address', models.CharField(max_length=50)),
                ('phone_number', models.BigIntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suffix', models.CharField(max_length=50)),
                ('license_plate_num', models.CharField(max_length=7)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('n', 'prefer not to answer')], default='n', max_length=1)),
                ('active_driver', models.CharField(choices=[('LP', 'Learners Permits'), ('DL', 'Drivers License'), ('R', 'Revoked'), ('S', 'Suspended')], max_length=2)),
                ('driver_state_of_residence', models.CharField(max_length=50)),
                ('num_of_collisions', models.IntegerField(default=0)),
                ('first_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='firstname', to='accounts.account')),
                ('last_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lastname', to='accounts.account')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='username', to='accounts.account')),
            ],
        ),
    ]
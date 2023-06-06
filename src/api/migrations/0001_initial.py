# Generated by Django 3.2 on 2023-06-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10, unique=True)),
                ('iq_time', models.DateTimeField(null=True)),
                ('iq_score', models.IntegerField(null=True)),
                ('eq_letters', models.CharField(max_length=5, null=True)),
                ('eq_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
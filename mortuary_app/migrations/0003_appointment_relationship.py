# Generated by Django 4.1 on 2024-06-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortuary_app', '0002_appointment_age_of_deceased_appointment_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='relationship',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1 on 2024-06-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortuary_app', '0004_alter_appointment_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicktix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='payment_reference',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment_status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

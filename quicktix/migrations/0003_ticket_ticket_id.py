# Generated by Django 4.0.6 on 2022-07-23 22:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quicktix', '0002_ticket_payment_reference_ticket_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_id',
            field=models.UUIDField(default=uuid.UUID('fcc25e1c-3b14-42d2-a54b-e2895e16a11b'), verbose_name='Ticket ID'),
        ),
    ]
# Generated by Django 4.0.1 on 2023-05-29 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_rename_invitation_number_invitationletter_total_invitation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitationletter',
            name='invitation_date',
        ),
    ]

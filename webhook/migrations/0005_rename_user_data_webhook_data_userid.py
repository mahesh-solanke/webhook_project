# Generated by Django 4.1.3 on 2022-11-26 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0004_webhook_data_user_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webhook_data',
            old_name='user_data',
            new_name='userid',
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-26 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0003_user_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook_data',
            name='user_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webhook.user_data'),
        ),
    ]

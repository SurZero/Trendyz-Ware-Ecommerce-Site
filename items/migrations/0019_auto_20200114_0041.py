# Generated by Django 2.2.7 on 2020-01-13 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_auto_20200111_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-28 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_auth_token_customuser_is_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='auth_token',
            new_name='verify_token',
        ),
    ]
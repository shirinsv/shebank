# Generated by Django 4.1.7 on 2023-03-26 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbank', '0002_delete_user_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='account_type',
            new_name='accounttype',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='materials_providing',
            new_name='material_providing',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='branch',
            new_name='subdistrict',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='name',
            new_name='username',
        ),
    ]
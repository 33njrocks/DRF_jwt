# Generated by Django 3.2.4 on 2021-07-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_contoller', '0004_remove_user_jwt_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_message_body_alter_message_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]

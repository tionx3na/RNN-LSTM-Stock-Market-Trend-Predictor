# Generated by Django 3.0.2 on 2020-04-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.TextField(),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticeTemlte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelplaces',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

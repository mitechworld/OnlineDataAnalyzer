# Generated by Django 2.2 on 2019-05-28 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_predict_predications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predict',
            old_name='predications',
            new_name='predictions',
        ),
    ]

# Generated by Django 2.1 on 2018-11-18 04:56

from django.db import migrations


def add_prefectures(apps, schema_editor):
    Prefecture = apps.get_model('shops', 'Prefecture')
    Prefecture.objects.create(name='北海道')
    Prefecture.objects.create(name='茨城県')


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_prefectures,
            migrations.RunPython.noop
        )
    ]

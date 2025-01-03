# Generated by Django 3.2.18 on 2023-05-16 09:55

from django.db import migrations
from django.db.models import Q


def migrate_needs_human_review_field(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('versions', '0038_auto_20230511_1416'),
        ('reviewers', '0026_auto_20230516_0949'),
    ]

    operations = [
        migrations.RunPython(migrate_needs_human_review_field, lambda *args: None)
    ]

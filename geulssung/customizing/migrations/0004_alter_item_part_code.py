# Generated by Django 5.2.1 on 2025-06-16 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customizing', '0003_alter_item_part_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='part_code',
            field=models.IntegerField(choices=[(1, '수트'), (2, '수경'), (3, '악세서리'), (4, '모자'), (5, '옷'), (6, '악세서리')]),
        ),
    ]

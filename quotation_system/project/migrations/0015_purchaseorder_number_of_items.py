# Generated by Django 4.1.4 on 2023-01-12 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_quotation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='number_of_items',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]

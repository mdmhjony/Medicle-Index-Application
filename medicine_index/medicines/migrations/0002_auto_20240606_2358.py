# Generated by Django 3.2.25 on 2024-06-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='other_details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

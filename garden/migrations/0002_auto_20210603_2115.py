# Generated by Django 3.2.4 on 2021-06-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='plant',
            name='NC_native',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='bee_friendly',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='butterfly_friendly',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='flowering_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='hummingbird_friendly',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='moisture_need',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.5 on 2019-11-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(blank=True, max_length=74, null=True)),
                ('address', models.CharField(blank=True, max_length=195, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=26, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'bank_branches',
            },
        ),
    ]
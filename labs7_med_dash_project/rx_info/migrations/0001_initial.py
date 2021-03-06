# Generated by Django 2.0.2 on 2018-09-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rx_claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DrugLabelName', models.CharField(max_length=200)),
                ('Generic', models.CharField(max_length=1)),
                ('NDCCode', models.CharField(max_length=20)),
                ('PBMVendor', models.CharField(max_length=200)),
                ('PharmacyCity', models.CharField(max_length=200)),
                ('PharmacyName', models.CharField(max_length=200)),
                ('PharmacyState', models.CharField(max_length=2)),
                ('PharmacyStreetAddress1', models.CharField(max_length=200)),
                ('PharmacyZip', models.CharField(max_length=5)),
                ('TotalCost', models.FloatField()),
                ('UnitCost', models.FloatField()),
                ('PharmacyID', models.CharField(max_length=200)),
                ('DrugShortName', models.CharField(max_length=200)),
                ('PharmZip', models.CharField(max_length=3)),
            ],
        ),
    ]

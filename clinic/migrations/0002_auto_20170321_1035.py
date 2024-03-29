# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('brandName', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('managerID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='calendarAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('userID', models.CharField(max_length=8)),
                ('customerID', models.CharField(max_length=8)),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('estimatedTime', models.IntegerField()),
                ('estimatedDifficulty', models.IntegerField()),
                ('content', models.TextField(max_length=500)),
                ('status', models.TextField(max_length=500)),
                ('note', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CalendarDentist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('userID', models.CharField(max_length=8)),
                ('time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('customerID', models.CharField(max_length=8)),
                ('customerName', models.CharField(max_length=32)),
                ('dOB', models.DateTimeField(verbose_name='date published')),
                ('phoneNumber', models.CharField(max_length=11)),
                ('address', models.TextField(max_length=500)),
                ('source', models.TextField(max_length=500)),
                ('fingerprint', models.TextField(max_length=500)),
                ('medicalBiography', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('itemID', models.CharField(max_length=8)),
                ('itemName', models.IntegerField()),
                ('unit', models.CharField(max_length=32)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('userID', models.CharField(max_length=8)),
                ('customerID', models.CharField(max_length=8)),
                ('treatmentID', models.CharField(max_length=8)),
                ('invoiceID', models.CharField(max_length=8)),
                ('pay', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Labo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('laboName', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=500)),
                ('phoneNumber', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID1', models.CharField(max_length=8)),
                ('customerID2', models.CharField(max_length=8)),
                ('relationship', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('userID', models.IntegerField()),
                ('customerID', models.IntegerField()),
                ('treatmentID', models.IntegerField()),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('describe', models.TextField(max_length=500)),
                ('totalPayment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatmentID', models.CharField(max_length=8)),
                ('treatmentDetailID', models.CharField(max_length=8)),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('content', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentDetailLabo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboID', models.CharField(max_length=8)),
                ('treatmentID', models.CharField(max_length=8)),
                ('sendDay', models.DateTimeField(verbose_name='date published')),
                ('receivedDay', models.DateTimeField(verbose_name='date published')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(max_length=8)),
                ('userID', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('dOB', models.DateTimeField(verbose_name='date published')),
                ('phone_Number', models.CharField(max_length=11)),
                ('address', models.TextField(max_length=500)),
                ('specialize', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

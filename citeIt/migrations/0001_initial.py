# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('withers_thesis_number', models.IntegerField(help_text=b'Thesis Number', verbose_name=b"Withers' Thesis Number", blank=True)),
                ('author', models.CharField(help_text=b"Author's name formatted Last, First Middle", max_length=255)),
                ('initial_article', models.CharField(help_text=b'Initial Article (The, A)', max_length=20, verbose_name=b'Initital Article', blank=True)),
                ('title', models.TextField(help_text=b'Title (omit initial article)')),
                ('pagination', models.IntegerField(help_text=b'Number of pages formatted as number <em>55</em> <br />Note: the pp is added by the system later ')),
                ('year', models.IntegerField(help_text=b'Year degree was awarded, formatted as <em>yyyy</em>')),
                ('local_call_no', models.CharField(max_length=200, verbose_name=b'Local Call Number', blank=True)),
                ('abstract', models.TextField()),
                ('citation_added_date', models.DateField(auto_now_add=True)),
                ('citation_edited_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DegreeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree_abbreviation', models.CharField(max_length=10)),
                ('degree_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['degree_abbreviation'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_abbreviation', models.CharField(max_length=30)),
                ('institution_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['institution_abbreviation'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(help_text=b'Locations should be in the format of <em>Country > State > County > Township</em>', max_length=255)),
            ],
            options={
                'ordering': ['location'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['subject'],
            },
        ),
        migrations.AddField(
            model_name='citation',
            name='coverage',
            field=models.ManyToManyField(to='citeIt.Location', blank=True),
        ),
        migrations.AddField(
            model_name='citation',
            name='degree_level',
            field=models.ForeignKey(on_delete=models.CASCADE, help_text=b'Type of degree', to='citeIt.DegreeLevel'),
        ),
        migrations.AddField(
            model_name='citation',
            name='granting_institution',
            field=models.ForeignKey(on_delete=models.CASCADE, help_text=b'Institution awarding Degree', to='citeIt.Institution'),
        ),
        migrations.AddField(
            model_name='citation',
            name='subjects',
            field=models.ManyToManyField(to='citeIt.Subject'),
        ),
    ]

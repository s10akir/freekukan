# Generated by Django 2.1.3 on 2019-01-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=5)),
                ('last_name', models.CharField(max_length=5)),
                ('first_name_kana', models.CharField(max_length=10)),
                ('last_name_kana', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=11)),
                ('zip_code', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='region.Region')),
            ],
        ),
    ]

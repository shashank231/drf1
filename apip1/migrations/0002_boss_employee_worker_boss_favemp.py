# Generated by Django 4.1.1 on 2022-11-14 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apip1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('department', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('in_dept', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=7)),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apip1.boss')),
            ],
        ),
        migrations.AddField(
            model_name='boss',
            name='favemp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apip1.employee'),
        ),
    ]
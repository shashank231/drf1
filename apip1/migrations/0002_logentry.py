# Generated by Django 4.1.1 on 2023-04-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apip1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('instance_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

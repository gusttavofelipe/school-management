# Generated by Django 4.2.6 on 2023-10-10 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serie', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('school_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
                ('serie_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serie.serie')),
            ],
        ),
    ]

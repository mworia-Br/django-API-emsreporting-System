# Generated by Django 3.0.2 on 2020-02-03 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_type', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('details', models.TextField()),
                ('approve', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('P', 'Processing'), ('F', 'Failed'), ('A', 'Approved')], default='P', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'security',
                'verbose_name_plural': 'securities',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddIndex(
            model_name='station',
            index=models.Index(fields=['name'], name='ReportSyste_name_44bbb5_idx'),
        ),
        migrations.AddField(
            model_name='security',
            name='crime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crimes', to='ReportSystem.Crime'),
        ),
        migrations.AddField(
            model_name='security',
            name='officer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='security',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='ReportSystem.Station'),
        ),
        migrations.AddField(
            model_name='reporter',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='crime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportSystem.Crime'),
        ),
        migrations.AddField(
            model_name='report',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportSystem.Reporter'),
        ),
        migrations.AddField(
            model_name='report',
            name='security',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportSystem.Security'),
        ),
        migrations.AddField(
            model_name='crime',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportSystem.Reporter'),
        ),
    ]

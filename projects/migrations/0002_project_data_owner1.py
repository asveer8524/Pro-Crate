# Generated by Django 2.0.7 on 2019-04-12 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='owner1',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'), max_length=120),
        ),
    ]
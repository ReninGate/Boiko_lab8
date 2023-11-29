# Generated by Django 4.2.7 on 2023-11-29 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_position_position_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectexecution',
            name='department_id',
        ),
        migrations.AddField(
            model_name='projectexecution',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.department'),
            preserve_default=False,
        ),
    ]
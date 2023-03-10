# Generated by Django 4.1.7 on 2023-02-28 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='home.races'),
        ),
        migrations.AlterField(
            model_name='events',
            name='type',
            field=models.CharField(choices=[('QUAL', 'Qualifying'), ('P1', 'Practice 1'), ('P2', 'Practice 2'), ('P3', 'Practice 3'), ('SPRT', 'Sprint')], max_length=4),
        ),
        migrations.AlterField(
            model_name='races',
            name='circuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to='home.circuit'),
        ),
    ]

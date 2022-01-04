# Generated by Django 3.2.7 on 2022-01-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_hours', models.CharField(max_length=5)),
                ('end_hours', models.CharField(max_length=5)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='rent.client')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Thema',
        ),
        migrations.RemoveField(
            model_name='item',
            name='ativo',
        ),
        migrations.AddField(
            model_name='theme',
            name='itens',
            field=models.ManyToManyField(related_name='themes', to='rent.Item'),
        ),
        migrations.AddField(
            model_name='rent',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='rent.theme'),
        ),
    ]
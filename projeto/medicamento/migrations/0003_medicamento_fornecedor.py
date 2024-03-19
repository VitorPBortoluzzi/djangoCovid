# Generated by Django 3.0.4 on 2024-03-19 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
        ('medicamento', '0002_auto_20230420_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='fornecedor',
            field=models.ForeignKey(blank='False', null='True', on_delete=django.db.models.deletion.PROTECT, related_name='fornecedor', to='fornecedor.Fornecedor', verbose_name='Fabricante do medicamento*'),
            preserve_default='True',
        ),
    ]

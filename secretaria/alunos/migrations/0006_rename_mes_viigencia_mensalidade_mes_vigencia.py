# Generated by Django 4.1.5 on 2023-01-23 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_valores_valor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensalidade',
            old_name='mes_viigencia',
            new_name='mes_vigencia',
        ),
    ]

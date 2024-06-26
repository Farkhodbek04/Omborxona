# Generated by Django 5.0.4 on 2024-05-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_user_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productoutput',
            options={'verbose_name': 'Chiqim', 'verbose_name_plural': 'Chiqimlar'},
        ),
        migrations.AddField(
            model_name='productoutput',
            name='removed_quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='password',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.SmallIntegerField(choices=[(0, 'bugalter'), (1, 'omborchi')], default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel_number',
            field=models.CharField(default='+998902078177', max_length=13),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-08 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_drinks_my_name_nutrition'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size_ml', models.CharField(max_length=100)),
                ('size_fluid_ounce', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='drink_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.drinks'),
        ),
        migrations.AlterModelTable(
            name='nutrition',
            table='Nutrition',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('drink_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('drinks', models.ManyToManyField(related_name='allergies', to='products.drinks')),
            ],
        ),
        migrations.AddField(
            model_name='drinks',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrition',
            name='size_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.sizes'),
            preserve_default=False,
        ),
    ]

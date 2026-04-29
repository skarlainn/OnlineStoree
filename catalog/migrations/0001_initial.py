import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',
                 models.CharField(help_text='Введите категорию товара', max_length=100, verbose_name='Категория')),
                ('description',
                 models.TextField(help_text='Введите описание категории', verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название товара', max_length=100, verbose_name='Товар')),
                ('description', models.TextField(help_text='Введите описание товара', verbose_name='Описание товара')),
                ('image', models.ImageField(help_text='Загрузите изображение товара', upload_to='images/',
                                            verbose_name='Изображение товара')),
                ('price', models.FloatField(help_text='Введите цену товара', verbose_name='Цена товара')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, help_text='Введите категорию', null=True,
                                               on_delete=django.db.models.deletion.SET_NULL, related_name='products',
                                               to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
    ]
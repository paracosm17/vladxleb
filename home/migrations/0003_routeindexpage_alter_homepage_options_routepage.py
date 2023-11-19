# Generated by Django 4.2.7 on 2023-11-18 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Главная страница Рейсов',
                'verbose_name_plural': 'Главная страница Рейсов',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главные страницы'},
        ),
        migrations.CreateModel(
            name='RoutePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateTimeField(verbose_name='Время создания рейса')),
                ('expeditions', wagtail.fields.StreamField([('expedition', wagtail.blocks.StructBlock([('name', wagtail.blocks.ChoiceBlock(choices=[('A', 'Expedition A'), ('B', 'Expedition B'), ('C', 'Expedition C'), ('D', 'Expedition D')])), ('gate', wagtail.blocks.IntegerBlock()), ('description', wagtail.blocks.TextBlock(required=False)), ('date', wagtail.blocks.DateTimeBlock()), ('completed', wagtail.blocks.BooleanBlock(default=False, required=False))]))], use_json_field=True)),
                ('finished', models.BooleanField(default=False, verbose_name='Рейс завершён')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
            bases=('wagtailcore.page',),
        ),
    ]

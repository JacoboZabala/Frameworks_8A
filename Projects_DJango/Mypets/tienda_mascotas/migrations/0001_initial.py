# Generated by Django 3.2.7 on 2021-11-04 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='identifacion_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('number_id', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('passwork', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
                ('id_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.city')),
                ('id_identification_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.identifacion_type')),
            ],
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.user')),
            ],
        ),
        migrations.CreateModel(
            name='pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
                ('id_race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.race')),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.user')),
                ('identifacion_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.type')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='id_conutry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.country'),
        ),
    ]

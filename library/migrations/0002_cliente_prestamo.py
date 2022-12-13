# Generated by Django 3.1.2 on 2021-12-13 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('INE', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.CharField(max_length=10)),
                ('fecha_devolucion', models.CharField(max_length=10)),
                ('id_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.cliente')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.libro')),
            ],
        ),
    ]

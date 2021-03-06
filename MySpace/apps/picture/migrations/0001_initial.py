# Generated by Django 2.0.1 on 2020-07-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.PositiveIntegerField(choices=[(1, '发布'), (0, '删除'), (2, '待发布')], default=1, verbose_name='状态')),
                ('visit', models.SmallIntegerField(default=0, verbose_name='浏览量')),
                ('desc', models.CharField(max_length=512, verbose_name='描述')),
                ('file', models.FileField(upload_to='picture/YY-MM-dd', verbose_name='图片')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.PositiveIntegerField(choices=[(1, '发布'), (0, '删除'), (2, '待发布')], default=1, verbose_name='状态')),
                ('visit', models.SmallIntegerField(default=0, verbose_name='浏览量')),
                ('name', models.CharField(db_index=True, default='No Name', max_length=64, verbose_name='相册名')),
                ('desc', models.CharField(max_length=512, verbose_name='描述')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='filemanager',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='picture.Picture', verbose_name='所属相册'),
        ),
    ]

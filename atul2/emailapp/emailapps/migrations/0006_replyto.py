# Generated by Django 2.1.5 on 2019-01-24 11:02

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('emailapps', '0005_auto_20190124_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=500, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='emailapps.ReplyTo')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='emailapps.MailCompose')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
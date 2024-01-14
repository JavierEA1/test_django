from django.db import migrations, models

def create_post_table(apps, schema_editor):
    Post = apps.get_model('django_app', 'Post')
    db_alias = schema_editor.connection.alias
    Post.objects.using(db_alias).create(
        title='Ejemplo de título',
        content='Contenido de ejemplo',
        pub_date=models.DateTimeField('date published')
    )

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RunPython(create_post_table),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siteapp", "0002_eventattendance_data_evento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("login", models.CharField(max_length=120)),
                ("senha", models.CharField(max_length=128)),
            ],
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome_pai", models.CharField(max_length=120)),
                ("nome_filho", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="EventAttendance",
            fields=[
                ("id", models.PositiveIntegerField(primary_key=True, serialize=False)),
                ("nome_evento", models.CharField(max_length=150)),
                ("presencas", models.JSONField(blank=True, default=list)),
            ],
        ),
    ]

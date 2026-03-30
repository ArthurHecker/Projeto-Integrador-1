import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siteapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventattendance",
            name="data_evento",
            field=models.DateField(default=datetime.date(2000, 1, 1)),
            preserve_default=False,
        ),
    ]

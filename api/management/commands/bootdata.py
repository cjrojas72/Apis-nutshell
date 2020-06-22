from api.models import ShoeColor, ShoeType
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Adds Show color and Type data'

    def handle(self, *args, **options):
        shoe_types = [
            "sneaker",
            "boot",
            "sandal",
            "dress",
            "other",
        ]
        shoe_colors = [
            "RED",
            "ORANGE",
            "YELLOW",
            "GREEN",
            "BLUE",
            "INDIGO",
            "VIOLET",
            "WHITE",
            "BLACK",
        ]

        for item in shoe_types:
            ShoeType.objects.create(
                style=item
            )
        for item in shoe_colors:
            ShoeColor.objects.create(
                color=item
            )

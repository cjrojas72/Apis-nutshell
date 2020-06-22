from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    COLORS_CHOICES = [
        ("RD", "RED"),
        ("OR", "ORANGE"),
        ("YL", "YELLOW"),
        ("GR", "GREEN"),
        ("BL", "BLUE"),
        ("IN", "INDIGO"),
        ("VL", "VIOLET"),
        ("WH", "WHITE"),
        ("BK", "BLACK")
    ]

    color = models.CharField(
        max_length=2,
        choices=COLORS_CHOICES,
        default="WH"
    )

    def __str__(self):
        return self.color


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="manufacturer", on_delete=models.CASCADE)
    colors = models.ForeignKey(
        ShoeColor, related_name="colors", on_delete=models.CASCADE)
    shoe_type = models.ForeignKey(
        ShoeType, related_name="type", on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

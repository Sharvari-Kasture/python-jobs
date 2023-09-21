from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class TaggableMixin(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        abstract = True

    def add_tag(self, tag_name):
        tag, created = Tag.objects.get_or_create(name=tag_name)
        if tag not in self.tags.all():
            self.tags.add(tag)

    def remove_tag(self, tag_name):
        tag = Tag.objects.filter(name=tag_name).first()
        if tag and tag in self.tags.all():
            self.tags.remove(tag)

    def get_tags(self):
        return self.tags.all()

class Maker(TaggableMixin, models.Model):
    name = models.CharField(max_length=255)
    number_of_cars = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Car(TaggableMixin, models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=255, unique=True)
    hpp = models.PositiveIntegerField()
    launch_date = models.DateField()
    mileage = models.FloatField(null=True)

    def __str__(self):
        return self.car_name

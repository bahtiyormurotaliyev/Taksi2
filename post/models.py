from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Person(models.Model):
    model_name = models.TextField()
    color = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = "post"

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("model", "year", )

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
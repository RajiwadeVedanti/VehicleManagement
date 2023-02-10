from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_type_choices = (
        ("two_wheeler","two_wheeler"),
        ("three_wheeler","three_wheeler"),
        ("four_wheeler","four_wheeler")
    )
    number = models.CharField(max_length=10,unique=True)
    type = models.CharField(max_length=20,choices=vehicle_type_choices,null=True,blank=True)
    model = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)
from django.db import models


# Create your models here.
class RegionManager(models.Manager):
    def counts(self):
        return super(RegionManager, self).counts("districts")


class Region(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=100)

    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )

    def __str__(self):
        return self.title


class School(models.Model):
    title = models.CharField(max_length=100)

    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="schools"
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Result(models.Model):
    correct_answers = models.IntegerField()
    wrong_answers = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.DecimalField(max_digits=100, decimal_places=1)

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.full_name

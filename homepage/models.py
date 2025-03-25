from django.db import models


class Students(models.Model):

    class Meta:
        verbose_name_plural = 'Students'

    CLASS_CHOICES = [
        ('Play Group', 'Play Group'),
        ('Pre Primary 1', 'Pre Primary 1'),
        ('Pre Primary 2', 'Pre Primary 2'),
        ('Grade 1', 'Grade 1'),
        ('Grade 2', 'Grade 2'),
        ('Grade 3', 'Grade 3'),
        ('Grade 4', 'Grade 4'),
        ('Grade 5', 'Grade 5'),
        ('Grade 6', 'Grade 6'),
    ]

    RELIGION_CHOICES = [
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Other', 'Other'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    RELATIONSHIP_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Guardian', 'Guardian'),
    ]

    # Main Fields
    student_name = models.CharField(max_length=100)
    current_class = models.CharField(max_length=50, choices=CLASS_CHOICES)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
    dob = models.CharField(max_length=20)
    prev_school = models.CharField(max_length=100)
    assessment_no = models.CharField(max_length=20)

    parent_name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=20)
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    contact_1 = models.CharField(max_length=10)
    contact_2 = models.CharField(max_length=10)
    res_address = models.CharField(max_length=50)
    associate = models.CharField(max_length=100)
    ass_contact = models.CharField(max_length=10)


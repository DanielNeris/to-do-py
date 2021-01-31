from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meda:
        abstract = True


class Courses(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

      def __str__(self):
        return self.title

class Review(Base):
  course = models.ForeignKey(Courses, related_name='reviews', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  comment = models.TextField(blank=True, default='')
  review = models.DecimalField(max_digits=2, decimal_places=1)

  class Meta:
      verbose_name = 'Review'
      verbose_name_plural = 'Reviews'
      unique_togther = ['email', 'course']

      def __str__(self):
        return f'{self.name} review the course {self.course} with note {self.review}'

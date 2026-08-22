from django.db import models

# Create your models here.

class ContactMessage(models.Model):
  name = models.CharField(
    max_length=100,
    verbose_name='نام'
  )

  email = models.EmailField(
    verbose_name='ایمیل'
  )

  subject = models.CharField(
    max_length=200,
    verbose_name='موضوع'
  )

  message = models.TextField(
    verbose_name='پیام'
  )

  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name='تاریخ ارسال'
  )

  class Meta:
    ordering = ['-created_at']
    verbose_name = 'پیام تماس'
    verbose_name_plural = 'پیام های تماس'


  def __str__(self):
    return f"{self.name} - {self.subject}"

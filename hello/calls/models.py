from django.db import models
from django.utils import timezone
class CallLog(models.Model):
    CallFrom = models.CharField(max_length=15)
    DialCallDuration = models.CharField(max_length=20)  # e.g., 'completed', 'failed', etc.
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.CallFrom} - {self.date.strftime('%H:%M:%S')}"

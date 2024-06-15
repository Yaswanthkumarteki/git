from django.db import models

class FileUpload(models.Model):
    sheet_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    file = models.FileField(upload_to="userfiles/")

    def __str__(self):
        return self.file.name

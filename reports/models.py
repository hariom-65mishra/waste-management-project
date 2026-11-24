from django.db import models
from django.contrib.auth.models import User

class WasteComplaint(models.Model):
    CATEGORY_CHOICES = [
        ('Plastic', 'Plastic Waste'),
        ('Organic', 'Organic / Food Waste'),
        ('Paper', 'Paper & Cardboard'),
        ('Glass', 'Glass Bottles & Containers'),
        ('Metal', 'Metal & Scraps'),
        ('E-Waste', 'Electronic Waste (E-Waste)'),
        ('Hazardous', 'Hazardous / Chemical Waste'),
        ('Other', 'Other Waste Material'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending Review'),
        ('In Progress', 'In Progress / Dispatched'),
        ('Collected', 'Collected & Cleaned'),
        ('Rejected', 'Rejected / Invalid'),
    ]

    URGENCY_CHOICES = [
        ('Low', 'Low Priority'),
        ('Medium', 'Medium Priority'),
        ('High', 'High Priority (Hazardous/Blocking)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Plastic')
    location = models.CharField(max_length=255, help_text="Street name, colony, or area")
    landmark = models.CharField(max_length=150, blank=True, help_text="Nearby landmark for easy location")
    description = models.TextField(help_text="Detailed description of the waste accumulation")
    photo = models.ImageField(upload_to='waste_photos/', blank=True, null=True, help_text="Upload photo of waste site")
    urgency = models.CharField(max_length=15, choices=URGENCY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    admin_notes = models.TextField(blank=True, help_text="Internal notes or updates from admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Waste Complaint'
        verbose_name_plural = 'Waste Complaints'

    def __str__(self):
        return f"{self.tracking_number} - {self.category} ({self.status})"

    @property
    def tracking_number(self):
        return f"WM-{self.pk:04d}"

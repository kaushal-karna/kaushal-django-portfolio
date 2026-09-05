from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("web", "Web Development"),
        ("tools", "Tools & Other"),
    ]
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    level = models.PositiveIntegerField(default=70)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ("django", "Django"),
        ("web", "Web"),
        ("python", "Python"),
        ("ml", "Machine Learning"),
    ]
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=220)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tech_stack = models.CharField(max_length=250, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-featured", "order", "-id"]

    def __str__(self):
        return self.title

    @property
    def technologies(self):
        return [x.strip() for x in self.tech_stack.split(",") if x.strip()]

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'}"

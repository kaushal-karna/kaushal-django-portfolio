from django.core.management.base import BaseCommand
from portfolio.models import Project, Skill

class Command(BaseCommand):
    help = "Seed the portfolio with starter content."

    def handle(self, *args, **options):
        skills = [
            ("Python", "programming", 88),
            ("C++", "programming", 76),
            ("JavaScript", "programming", 72),
            ("HTML & CSS", "web", 90),
            ("Django", "web", 86),
            ("WordPress", "web", 78),
            ("Git & GitHub", "tools", 78),
            ("Machine Learning", "tools", 66),
        ]

        for order, (name, category, level) in enumerate(skills):
            Skill.objects.update_or_create(
                name=name,
                defaults={"category": category, "level": level, "order": order},
            )

        projects = [
            {
                "title": "Django Student Management System",
                "slug": "django-student-management-system",
                "short_description": "A database-driven student dashboard with courses, teachers, filters and detail views.",
                "description": "A practical Django project focused on CRUD workflows, relationships, templates, static files, filtering and clean dashboard UX. Built as part of hands-on full-stack learning.",
                "category": "django",
                "tech_stack": "Python, Django, SQLite, HTML, CSS, JavaScript",
                "featured": True,
                "order": 1,
            },
            {
                "title": "Boldmunk Ecommerce",
                "slug": "boldmunk-ecommerce",
                "short_description": "A Django ecommerce build covering products, categories, carts, accounts and orders.",
                "description": "A full ecommerce learning project exploring Django app architecture, authentication, product catalogues, cart workflows and order management.",
                "category": "django",
                "tech_stack": "Python, Django, SQLite, HTML, CSS, JavaScript",
                "featured": True,
                "order": 2,
            },
            {
                "title": "Wine Classification ML",
                "slug": "wine-classification-ml",
                "short_description": "Machine-learning experiments using KNN, Logistic Regression and Random Forest.",
                "description": "A hands-on machine learning project using the Wine dataset, model evaluation and confusion matrices. The work compares several classifiers and their predictive performance.",
                "category": "ml",
                "tech_stack": "Python, Scikit-learn, Pandas, Matplotlib",
                "featured": True,
                "order": 3,
            },
            {
                "title": "Custom Form Handler",
                "slug": "custom-form-handler",
                "short_description": "A WordPress plugin concept for processing custom form submissions.",
                "description": "A WordPress development project focused on handling custom form data and understanding plugin-based PHP workflows.",
                "category": "web",
                "tech_stack": "WordPress, PHP, HTML, CSS, JavaScript",
                "featured": False,
                "order": 4,
            },
            {
                "title": "Maithili Codewala",
                "slug": "maithili-codewala",
                "short_description": "A coding-content initiative focused on explaining programming concepts in Maithili.",
                "description": "A personal content project aimed at making coding education more approachable for Maithili-speaking learners through short-form programming content.",
                "category": "web",
                "tech_stack": "Content Creation, Python, Web Development",
                "featured": False,
                "order": 5,
            },
        ]

        for data in projects:
            Project.objects.update_or_create(slug=data["slug"], defaults=data)

        self.stdout.write(self.style.SUCCESS("Portfolio content seeded successfully."))

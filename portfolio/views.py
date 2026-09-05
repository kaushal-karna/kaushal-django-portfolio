import logging

from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .forms import ContactForm
from .models import Project, Skill

logger = logging.getLogger(__name__)


def send_contact_thank_you(contact_message):
    context = {
        "name": contact_message.name,
        "subject": contact_message.subject,
        "message": contact_message.message,
        "site_url": settings.SITE_URL,
    }
    text_body = render_to_string("emails/contact_thank_you.txt", context)
    html_body = render_to_string("emails/contact_thank_you.html", context)
    email = EmailMultiAlternatives(
        subject="Thanks for connecting with Kaushal",
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[contact_message.email],
    )
    email.attach_alternative(html_body, "text/html")
    email.send()


def send_contact_notification(contact_message):
    context = {
        "name": contact_message.name,
        "email": contact_message.email,
        "subject": contact_message.subject,
        "message": contact_message.message,
    }
    text_body = render_to_string("emails/contact_notification.txt", context)
    html_body = render_to_string("emails/contact_notification.html", context)
    email = EmailMultiAlternatives(
        subject=f"New portfolio message from {contact_message.name}",
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_RECEIVER_EMAIL],
        reply_to=[contact_message.email],
    )
    email.attach_alternative(html_body, "text/html")
    email.send()

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        "projects": projects,
        "skills": skills,
        "skill_categories": [
            ("programming", "Programming"),
            ("web", "Web Development"),
            ("tools", "Tools & Other"),
        ],
        "form": ContactForm(),
    }
    return render(request, "portfolio/home.html", context)

def contact(request):
    if request.method != "POST":
        return redirect("home")

    form = ContactForm(request.POST)
    if form.is_valid():
        contact_message = form.save()
        confirmation_sent = False
        notification_sent = False
        try:
            send_contact_thank_you(contact_message)
        except Exception:
            logger.exception("Unable to send contact confirmation to %s", contact_message.email)
        else:
            confirmation_sent = True
        try:
            send_contact_notification(contact_message)
        except Exception:
            logger.exception("Unable to send contact notification for %s", contact_message.email)
        else:
            notification_sent = True

        if confirmation_sent and notification_sent:
            messages.success(request, "Message received. A thank-you email is on its way!")
        elif notification_sent:
            messages.warning(request, "Message received and sent to Kaushal, but the confirmation email could not be sent.")
        elif confirmation_sent:
            messages.warning(request, "Thank-you email sent, but the message notification could not be delivered.")
        else:
            messages.warning(request, "Message received, but the email notifications could not be sent.")
    else:
        messages.error(request, "Please check the form and try again.")
    return redirect("home")

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "portfolio/project_detail.html", {"project": project})

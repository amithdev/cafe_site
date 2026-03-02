from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, "core/home.html")

def full_menu(request):
    return render(request, "core/full_menu.html")

def about_page(request):
    return render(request, "core/about.html")


# ✅ ADD THESE
def contact_page(request):
    return render(request, "core/contact.html")

def journals_page(request):
    return render(request, "core/journals.html")



def contact_send(request):
    if request.method != "POST":
        return redirect("contact")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not message:
        messages.error(request, "Please fill all fields.")
        return redirect("contact")

    subject = f"New Contact Message from {name}"
    body = (
        f"Name: {name}\n"
        f"Email: {email}\n\n"
        f"Message:\n{message}\n"
    )

    # Send to cafe email
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.CAFE_CONTACT_EMAIL],
        fail_silently=False,
        reply_to=[email],  # so you can reply directly to customer
    )

    messages.success(request, "Thanks! Your message has been sent.")
    return redirect("contact")

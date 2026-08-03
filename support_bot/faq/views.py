import logging

from django.conf import settings
from django.shortcuts import render
from .models import FAQ, UnmatchedQuestion, SuggestedFAQ
from rapidfuzz import process
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

# Minimum similarity score (0-100) before we treat an FAQ as a match
MATCH_THRESHOLD = 70

NO_MATCH_REPLY = "Sorry, I don't have an answer for that. I'll pass your question to our support team."


def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get('message', '').lower()

        # Get all questions from the database
        questions = list(FAQ.objects.values_list('question', flat=True))

        # Use fuzzy matching to find the best match. rapidfuzz returns
        # (choice, score, index), and returns None when there is nothing to
        # match against - so an empty FAQ table is not an error.
        match = process.extractOne(user_input, questions) if questions else None

        if match and match[1] >= MATCH_THRESHOLD:
            best_match = match[0]
            faq = FAQ.objects.filter(question=best_match).first()

        else:
            faq = None

        if faq:
            response = faq.answer
        else:
            # Log the unmatched question
            UnmatchedQuestion.objects.create(question=user_input)

            # Create SuggestedFAQ for admin review
            SuggestedFAQ.objects.create(question=user_input, answer="Suggested answer here")

            notify_admin_of_unmatched(user_input)

            response = NO_MATCH_REPLY

        return render(request, 'chatbot.html', {'response': response})

    return render(request, 'chatbot.html')


def notify_admin_of_unmatched(user_input):
    """Email the admin about an unmatched question.

    A misconfigured mailserver must not take the chatbot down with it, so
    failures are logged rather than raised.
    """
    recipient = getattr(settings, 'ADMIN_NOTIFICATION_EMAIL', None)
    if not recipient:
        return

    try:
        send_mail(
            'New Unmatched Question Submitted',
            f'A new question has been submitted that could not be matched:\n\n{user_input}',
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
    except Exception:
        logger.exception("Could not send unmatched-question notification")

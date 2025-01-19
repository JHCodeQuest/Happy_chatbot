from django.conf import settings
from django.shortcuts import render
from .models import FAQ, UnmatchedQuestion, SuggestedFAQ
from rapidfuzz import process
from django.core.mail import send_mail

def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get('message', '').lower()

        # Get all questions from the database
        questions = FAQ.objects.values_list('question', flat=True)

        # Use fuzzy matching to find the best match
        best_match, score = process.extractOne(user_input, questions)

        if score >= 70:
            faq = FAQ.objects.get(question=best_match)
            response = faq.answer
        else:
            # Log the unmatched question
            unmatched = UnmatchedQuestion.objects.create(question=user_input)

            # Create SuggestedFAQ for admin review
            SuggestedFAQ.objects.create(question=user_input, answer="Suggested answer here")

            # Send an email notification to admin
            send_mail(
                'New Unmatched Question Submitted',
                f'A new question has been submitted that could not be matched:\n\n{user_input}',
                settings.DEFAULT_FROM_EMAIL,
                ['admin-email@example.com'],  # Replace with admin's email
                fail_silently=False,
            )

            response = "Sorry, I don't have an answer for that. I'll pass your question to our support team."

        return render(request, 'chatbot.html', {'response': response})

    return render(request, 'chatbot.html')
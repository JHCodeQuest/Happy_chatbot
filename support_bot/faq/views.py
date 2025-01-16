from django.shortcuts import render
from .models import FAQ, UnmatchedQuestion
from rapidfuzz import process

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
            UnmatchedQuestion.objects.create(question=user_input)
            response = "Sorry, I don't have an answer for that. I'll pass your question to our support team."

        return render(request, 'chatbot.html', {'response': response})

    return render(request, 'chatbot.html')
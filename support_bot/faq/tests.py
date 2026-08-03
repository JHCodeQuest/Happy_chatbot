from django.test import TestCase

from .models import FAQ, SuggestedFAQ, UnmatchedQuestion


class ChatbotViewTests(TestCase):
    def setUp(self):
        FAQ.objects.create(
            question="Order Status",
            answer="Can you please provide your order number so I can check the status?",
        )

    def test_get_renders_the_chat_page(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_close_question_returns_the_faq_answer(self):
        response = self.client.post('/', {'message': 'what is my order staus'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "provide your order number")

    def test_unmatched_question_is_logged_for_review(self):
        response = self.client.post('/', {'message': 'do you sell bicycle helmets'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(UnmatchedQuestion.objects.count(), 1)
        self.assertEqual(SuggestedFAQ.objects.count(), 1)
        self.assertFalse(SuggestedFAQ.objects.get().is_approved)

    def test_empty_faq_table_does_not_error(self):
        FAQ.objects.all().delete()

        response = self.client.post('/', {'message': 'anything at all'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(UnmatchedQuestion.objects.count(), 1)

    def test_broken_mail_config_does_not_break_the_reply(self):
        with self.settings(
            ADMIN_NOTIFICATION_EMAIL='admin@example.com',
            EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
            EMAIL_HOST='127.0.0.1',
            EMAIL_PORT=1,
        ):
            response = self.client.post('/', {'message': 'something nobody has asked'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(UnmatchedQuestion.objects.count(), 1)

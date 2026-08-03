FAQ Chatbot App

Description

This Django-based chatbot application provides a simple FAQ support system. Users can ask questions, and the chatbot will match their input against a database of frequently asked questions (FAQs) to provide the best possible response. If no match is found, the unmatched question is logged for the admin to review and add to the FAQ database.

Features
	•	Fuzzy Matching with rapidfuzz:
	•	Matches user questions to stored FAQs with a configurable accuracy threshold.
	•	Provides answers for close matches even with typos or slight variations.
	•	Automated Learning:
	•	Logs unmatched questions in the database for later review.
	•	Admins can view and update FAQs based on logged unmatched questions.
	•	Admin Dashboard:
	•	Manage FAQs (add, edit, delete questions and answers).
	•	View and address unmatched user questions.

Tech Stack
	•	Backend: Django (Python)
	•	Frontend: HTML templates (extendable for custom designs)
	•	Database: SQLite3 (default, can be switched to other databases)
	•	Matching Logic: rapidfuzz for fuzzy string matching

Installation
	1.	Clone the repository:

git clone <repository_url>
cd faq-chatbot


	2.	Set up a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
pip install -r requirements.txt


	3.	Apply database migrations:

python manage.py migrate


	4.	(Optional) Load the sample FAQs, and create an admin login:

python manage.py loaddata sample_faqs
python manage.py createsuperuser


	5.	Start the development server:

python manage.py runserver


	6.	Access the app at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

Configuration

All settings have working development defaults, so the app runs with no setup.
Override via environment variables:

DJANGO_SECRET_KEY          Required for any real deployment
DJANGO_DEBUG               Set to False in production
DJANGO_ALLOWED_HOSTS       Comma-separated hostnames
EMAIL_HOST_USER            SMTP username. Unset = emails print to the console
EMAIL_HOST_PASSWORD        SMTP password. Never commit this
ADMIN_NOTIFICATION_EMAIL   Where unmatched-question alerts go. Unset = no alerts

Running the tests

python manage.py test faq

Usage
	1.	Chatbot:
	•	Users can ask questions through the chatbot interface on the home page.
	•	The chatbot provides answers for known questions and logs unmatched questions.
	2.	Admin Panel:
	•	Log in at http://127.0.0.1:8000/admin/.
	•	Manage FAQs and review unmatched questions for future updates.

Future Enhancements
	•	Improved Matching: Integrate advanced AI models for natural language understanding.
	•	Export/Import FAQs: Allow admins to import/export FAQs in bulk.
	•	Conversation history: Keep a session transcript rather than a single reply.


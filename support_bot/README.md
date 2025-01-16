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

python manage.py makemigrations
python manage.py migrate


	4.	Start the development server:

python manage.py runserver


	5.	Access the app at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

Usage
	1.	Chatbot:
	•	Users can ask questions through the chatbot interface on the home page.
	•	The chatbot provides answers for known questions and logs unmatched questions.
	2.	Admin Panel:
	•	Log in at http://127.0.0.1:8000/admin/.
	•	Manage FAQs and review unmatched questions for future updates.

Future Enhancements
	•	Email Notifications: Notify admins of new unmatched questions.
	•	Improved Matching: Integrate advanced AI models for natural language understanding.
	•	Export/Import FAQs: Allow admins to import/export FAQs in bulk.


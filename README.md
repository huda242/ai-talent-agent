# AI-Powered Talent Scouting & Engagement Agent

##  Overview

Recruiters often spend hours filtering candidates and assessing interest. This project automates the process by intelligently parsing job descriptions, matching candidates, simulating engagement, and generating a ranked shortlist.

---

##  Features

*  Job Description Parsing (skills + experience extraction)
*  Candidate Matching with explainable scoring
*  Simulated conversational engagement
*  Dual scoring:

  * Match Score
  * Interest Score
*  Final ranked shortlist for recruiters

---

##  Architecture

Frontend (HTML/CSS/JS)
→ Flask Backend API
→ Modules:

* JD Parser
* Candidate Matcher
* Interest Simulator
* Scoring Engine
  → JSON Candidate Database

---

##  Scoring Logic

Final Score = (Match Score × 0.6) + (Interest Score × 0.4)

* Match Score:

  * Skill match (70%)
  * Experience match (30%)

* Interest Score:

  * Simulated candidate response:

    * Interested (75–100)
    * Neutral (40–70)
    * Not Interested (0–30)

---

##  How to Run Locally

### Backend

cd backend
pip install flask flask-cors
python app.py

### Frontend

Open `frontend/index.html` in a browser

---

##  Sample Input

Looking for Python developer with Flask and SQL, 2+ years experience

---

##  Sample Output

| Name        | Match Score | Interest Score | Final Score |
| ----------- | ----------- | -------------- | ----------- |
| Ayesha Khan | 85%         | 90%            | 87          |
| Sneha Reddy | 80%         | 75%            | 78          |

---

##  Demo Video

(https://drive.google.com/file/d/1_iSJ6yZxJgn0_04BTUP0XLMfH17JRw4N/view?usp=sharing)

---

## Project URL

This project runs locally. Follow setup instructions in README to run it.
---

## Author

Huda Fatima

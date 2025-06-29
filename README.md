# 🎓 Scholarship Finder

A web application that helps students automatically discover scholarships that match their profile.

---

## 🚀 Features

- 🧠 Smart scholarship matching based on course, GPA, and location
- 🔍 Real-time web scraping from major and niche scholarship portals
- 📊 Sentiment analysis of scholarship descriptions to boost recommendation quality
- 💻 Modern, responsive UI using React.js and TailwindCSS
- 🛠 Backend APIs built with Node.js and Express.js
- 🗃 Data stored and served using MongoDB
- 🤖 Matching algorithm and NLP powered by Python (TextBlob & VADER)

---
## 🛠 Tech Stack

**Frontend:**
- React.js
- TailwindCSS

**Backend:**
- Node.js
- Express.js

**Database:**
- MongoDB

**Data Processing / Scraping:**
- Python (Selenium, TextBlob, VADER)

**📦 Installation**

```bash
🖥️ Clone The Repository

git clone https://github.com/kshitiz595/scholarFinder.git
cd SCHOLARSHIP-FINDER

📲 Frontend (React.js + TailwindCSS)

cd frontend
npm install
npm run dev

⚙️ Backend (Node.js + Express)

cd backend
npm install
npm start

🕸 Scraping 

pip install selenium beautifulsoup4 textblob vaderSentiment nltk
pip install pymango
pip install python-dateutil
python -m nltk.downloader vader_lexicon
python -m textblob.download_corpora

for script in buddy4u_com.py fastweb_com.py scholarships_com.py; do
  echo "→ Running $script..."
  python "WebScraping/$script"
done

#IMPORTANT : WRITE ALL THE COMMANDS FOR FRONTEND , BACKEND AND SCRAPING IN SEPRATE TERMINALS...


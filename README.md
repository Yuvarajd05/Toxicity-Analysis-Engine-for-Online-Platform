Toxicity-Analysis-Engine-for-Online-Platform

A machine learning engine that detects and classifies toxic content in online text using a fine-tuned BERT model.

📌 Features

✅ Classifies input text into six bullying categories:

toxic

severe_toxic

obscene

threat

insult

identity_hate

🧠 Fine-tuned BERT (bert-base-uncased)

💬 Supports web UI and chat interface

🌐 RESTful API using Flask + CORS

📈 Trained on 150,000+ social media comments

📂 Project Structure
Toxicity-Analysis-Engine-for-Online-Platform/
├── app.py                # Flask backend with BERT model
├── Bert.hdfs             # Fine-tuned BERT model directory
├── requirements.txt      # Python dependencies
├── templates/            # HTML frontend (if applicable)
├── static/               # CSS/JS assets (optional)
└── README.md             # Project documentation

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/Toxicity-Analysis-Engine-for-Online-Platform.git
cd Toxicity-Analysis-Engine-for-Online-Platform


Download fine-tuned model (Bert.hdfs)
Download the folder containing config.json and dataset file:
Google Drive Link

Place Bert.hdfs in the project root directory.

Set up a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt

▶️ Running the App
python app.py


Server will start at http://localhost:5000

🧪 API Usage

Endpoint: /process_text

Method: POST

Content-Type: application/json

🔸 Sample Request
{
  "input_text": "You're such an idiot and a complete failure!"
}

🔸 Sample Response
{
  "original_text": "You're such an idiot and a complete failure!",
  "predictedLables": ["toxic", "insult"],
  "status": 2
}

🧠 Model Details

Architecture: BERT (bert-base-uncased)

Task: Multi-label text classification

Dataset: 1.5 lakh annotated social media comments

Output: 6-dimensional binary vector

Framework: PyTorch + Transformers

📈 Evaluation Metrics

The model was trained and evaluated using:

Accuracy

Precision

Recall

F1 Score

📚 Future Enhancements

Add styled frontend UI

Enable file upload or batch detection

Add login/authentication for moderation dashboards

Visualize toxicity trends with charts

🤝 Acknowledgements

Hugging Face Transformers

Jigsaw Toxic Comment Dataset

Flask & PyTorch communities

📜 License

This project is licensed under the MIT License.

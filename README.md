# Toxicity-Analysis-Engine-for-Online-Platform
📌 Features
✅ Classifies input text into six bullying categories:
toxic
severe_toxic
obscene
threat
insult
identity_hate
🧠 Uses fine-tuned BERT (bert-base-uncased)
💬 Supports both web UI and chat interface
📈 Model trained on 150,000+ social media comments
🌐 RESTful API using Flask + CORS
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
**Download Bert.hdfs dataset **

Use the following link to download the folder containing config.json and Dataset file:
https://drive.google.com/drive/folders/1_zAqmicvePnifjnF9gMIL9ukIdvSpmCq?usp=sharing
Set up a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages

pip install -r requirements.txt
Download or place the fine-tuned model Ensure Bert.hdfs (your fine-tuned model folder) is in the root directory.

▶️ Running the App
python app.py
The server will start at http://localhost:5000
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
During training and evaluation, the following metrics were used:

Accuracy
Precision
Recall
F1 Score
📚 Future Enhancements
Add frontend with styled UI
Enable file upload or batch detection
Add login/authentication for moderation dashboards
Visualize results with charts (toxicity trends)
🤝 Acknowledgements
Hugging Face Transformers
Jigsaw Toxic Comment Dataset
Flask & PyTorch communities
📜 License
This project is licensed under the MIT License.

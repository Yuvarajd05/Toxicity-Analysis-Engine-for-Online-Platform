# 🛡️ Toxicity Analysis Engine For Online Platform

A BERT-powered machine learning application to detect and classify different types of cyberbullying in online text. This project uses a fine-tuned BERT model trained on a 1.5 lakh comment dataset, capable of identifying six types of toxicity with severity-based labels. The backend is built using Flask and includes a REST API, with both web and chat interface integrations.

---

## 📌 Features

- ✅ Classifies input text into six bullying categories:
  - `toxic`
  - `severe_toxic`
  - `obscene`
  - `threat`
  - `insult`
  - `identity_hate`
- 🧠 Uses fine-tuned BERT (`bert-base-uncased`)
- 💬 Supports both web UI and chat interface
- 📈 Model trained on 150,000+ social media comments
- 🌐 RESTful API using Flask + CORS

---

## 📂 Project Structure

```
Toxicity Analysis Engine For Online Platform/
├── app.py                # Flask backend with BERT model
├── Bert.hdfs             # Fine-tuned BERT model directory
├── requirements.txt      # Python dependencies
├── templates/            # HTML frontend (if applicable)
├── static/               # CSS/JS assets (optional)
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Cyberbullying-Detection-System.git
   cd Cyberbullying-Detection-System
   ```
2. **Download Bert.hdfs dataset **
   ```bash
   Use the following link to download the folder containing config.json and Dataset file:
   https://drive.google.com/drive/folders/1_zAqmicvePnifjnF9gMIL9ukIdvSpmCq?usp=sharing
   ```
   
3. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download or place the fine-tuned model**
   Ensure `Bert.hdfs` (your fine-tuned model folder) is in the root directory.

---

## ▶️ Running the App

```bash
python app.py
```

- The server will start at `http://localhost:5000`

---

## 🧪 API Usage

### Endpoint: `/process_text`  
**Method:** POST  
**Content-Type:** `application/json`  

#### 🔸 Sample Request
```json
{
  "input_text": "You're such an idiot and a complete failure!"
}
```

#### 🔸 Sample Response
```json
{
  "original_text": "You're such an idiot and a complete failure!",
  "predictedLables": ["toxic", "insult"],
  "status": 2
}
```

---

## 🧠 Model Details

- Architecture: `BERT (bert-base-uncased)`
- Task: Multi-label text classification
- Dataset: 1.5 lakh annotated social media comments
- Output: 6-dimensional binary vector
- Framework: `PyTorch` + `Transformers`

---

## 📈 Evaluation Metrics

During training and evaluation, the following metrics were used:
- Accuracy
- Precision
- Recall
- F1 Score

---

## 📚 Future Enhancements

- Add frontend with styled UI
- Enable file upload or batch detection
- Add login/authentication for moderation dashboards
- Visualize results with charts (toxicity trends)

---

## 🤝 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Jigsaw Toxic Comment Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
- Flask & PyTorch communities

---


## 📜 License

This project is licensed under the [MIT License](LICENSE).

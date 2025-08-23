from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BertForSequenceClassification, BertTokenizer
from torch.utils.data import DataLoader, TensorDataset
import torch

app = Flask(__name__)
CORS(app, resources={r"/process_text": {"origins": "*"}})

# Path to the pre-trained BERT model file
model_path = 'Bert.hdfs'
model = BertForSequenceClassification.from_pretrained(model_path)

#Load the tokenizer for the BERT model
# `do_lower_case=True` ensures that all input text is converted to lowercase

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Function to predict labels for the input text using the loaded BERT model

def predict_labels_from_text(input_text):
    user_input = [input_text]
    user_encodings = tokenizer(user_input, truncation=True, padding=True, return_tensors="pt")
    user_dataset = TensorDataset(user_encodings['input_ids'], user_encodings['attention_mask'])
    user_loader = DataLoader(user_dataset, batch_size=1, shuffle=False)

    model.eval()
    with torch.no_grad():
        for batch in user_loader:
            input_ids, attention_mask = [t.to(device) for t in batch]
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            predictions = torch.sigmoid(logits)

    predicted_labels = (predictions.cpu().numpy() > 0.5).astype(int)
    # Define label names corresponding to the model's output dimensions
    labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    result = [label for i, label in enumerate(labels) if predicted_labels[0][i] == 1]
    return result

@app.route('/process_text', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        inputText = data["input_text"]
          # Get predicted labels for the input text
        predicted_labels = predict_labels_from_text(inputText)

        # Return a JSON response with the original text, predicted labels, and status
        return jsonify({"original_text": inputText, "predictedLables":
           predicted_labels,"status":"No toxicity detected" if len(predicted_labels) == 0 else len(predicted_labels)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application on localhost, port 5000

if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')

const input_text = document.getElementById('inputField');
const enterButton = document.getElementById('enterButton');

enterButton.addEventListener('click', () => {
  const Data = input_text.value;
  const input = { "input_text": Data };

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/process_text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(input),
      });

      if (!response.ok) {
        console.error("Invalid response");
        return;
      }

      const data = await response.json();
      console.log(data);

      const responseDiv = document.getElementById('response');
      responseDiv.style = "visibility: visible; display: flex; gap: 10px; flex-wrap: wrap;";
      // backend labels
      if (data.predictedLables && data.predictedLables.length > 0) {
        // Clear previous labels
        responseDiv.innerHTML = '';

        // Define colors for severity levels
        const severityColors = {
          toxic: '#FF6F61',        // Light red
          severe_toxic: '#D32F2F', // Dark red
          obscene: '#FFA726',      // Orange
          threat: '#7E57C2',       // Purple
          insult: '#29B6F6',       // Blue
          identity_hate: '#66BB6A' // Green
        };

        // Create and style each label
        data.predictedLables.forEach(label => {
          const labelElement = document.createElement('span');
          labelElement.textContent = label;
          labelElement.style = `
            padding: 5px 10px;
            border-radius: 5px;
            color: white;
            background-color: ${severityColors[label] || '#9E9E9E'};
            font-weight: bold;
          `;
          responseDiv.appendChild(labelElement);
        });
      } else {
        responseDiv.textContent = data.status || "No labels found.";
      }
    } catch (error) {
      console.error("An error occurred:", error);
      const responseDiv = document.getElementById('response');
      responseDiv.style = "visibility: visible;";
      responseDiv.textContent = 'An error occurred while fetching the data.';
    }
  };

  fetchData();
});
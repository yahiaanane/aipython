const submitButton = document.getElementById('submit-button');
const promptInput = document.getElementById('prompt-input');
const outputContainer = document.querySelector('.output-container');

submitButton.addEventListener('click', async () => {
  const prompt = promptInput.value;
  const response = await getResponse(prompt);
  outputContainer.innerHTML += `<p><strong>You:</strong> ${prompt}</p>`;
  outputContainer.innerHTML += `<p><strong>OpenAI:</strong> ${response}</p>`;
  promptInput.value = '';
  outputContainer.scrollTop = outputContainer.scrollHeight;
});

async function getResponse(prompt) {
  const response = await fetch('https://aipython.onrender.com', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ prompt })
  });
  const { choices } = await response.json();
  return choices[0].text;
}

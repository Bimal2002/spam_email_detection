async function checkSpam() {
    let text = document.getElementById("emailText").value;
    let resultElement = document.getElementById("result");

    if (!text.trim()) {
        resultElement.innerText = "Please enter text.";
        return;
    }

    let response = await fetch("https://flask-spam-detector.vercel.app/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    let data = await response.json();
    resultElement.innerText = data.spam ? "🚨 This is SPAM!" : "✅ This is NOT spam.";
}

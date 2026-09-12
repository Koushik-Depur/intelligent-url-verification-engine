const urlInput = document.getElementById("urlInput");
const checkButton = document.getElementById("checkButton");

const result = document.getElementById("result");
const resultIcon = document.getElementById("resultIcon");
const resultTitle = document.getElementById("resultTitle");
const resultMessage = document.getElementById("resultMessage");

const riskScore = document.getElementById("riskScore");
const riskFill = document.getElementById("riskFill");


checkButton.addEventListener("click", async function () {

    const url = urlInput.value.trim();

    if (url === "") {
        alert("Please enter a URL.");
        return;
    }

    // Show analysis screen
    result.classList.remove("hidden");

    resultIcon.textContent = "🔍";
    resultTitle.textContent = "Analyzing...";
    resultMessage.textContent = "IVE is analyzing the URL using the ML model.";

    riskScore.textContent = "Analyzing...";
    riskFill.style.width = "30%";

    // Disable button while analyzing
    checkButton.disabled = true;
    checkButton.textContent = "Checking...";

    try {

        // Send URL to Flask backend
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

        // Handle backend error
        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        // Get prediction from ML model
        const score = data.risk_score;

        riskScore.textContent = score + "%";
        riskFill.style.width = score + "%";

        // Phishing prediction
        if (data.prediction === "Potential Phishing") {

            resultIcon.textContent = "🔴";

            resultTitle.textContent = "Potential Phishing";

            resultMessage.textContent =
                "The ML model detected characteristics commonly associated with suspicious URLs.";

        }

        // Legitimate prediction
        else {

            resultIcon.textContent = "🟢";

            resultTitle.textContent = "Predicted Legitimate";

            resultMessage.textContent =
                "The ML model did not detect strong phishing characteristics in this URL.";

        }

    } catch (error) {

        console.error(error);

        resultIcon.textContent = "⚠️";

        resultTitle.textContent = "Analysis Failed";

        resultMessage.textContent =
            "Unable to connect to the IVE backend. Make sure the Flask server is running.";

        riskScore.textContent = "--";

        riskFill.style.width = "0%";

    }

    // Enable button again
    checkButton.disabled = false;
    checkButton.textContent = "Check URL";

});
function uploadImage() {
    let fileInput = document.getElementById("fileInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select an image!");
        return;
    }

    // Preview
    let reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById("previewImage").src = e.target.result;
    }
    reader.readAsDataURL(file);

    // Show loader
    document.getElementById("loader").classList.remove("hidden");
    document.getElementById("resultCard").classList.add("hidden");
    document.getElementById("solutionCard").classList.add("hidden");

    let formData = new FormData();
    formData.append("file", file);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("loader").classList.add("hidden");

        let resultText = document.getElementById("resultText");
        let confidenceText = document.getElementById("confidenceText");
        let solutionCard = document.getElementById("solutionCard");

        if (data.label === "healthy") {
            resultText.innerHTML = "✅ Healthy Leaf";
            resultText.style.color = "#00ffcc";
        } else if (data.label === "anthracnose") {
            resultText.innerHTML = "⚠️ Anthracnose Detected";
            resultText.style.color = "#ff4d4d";

            // 🔥 show solution only here
            solutionCard.classList.remove("hidden");
        } else {
            resultText.innerHTML = "❓ Uncertain";
            resultText.style.color = "#ffaa00";
        }

        confidenceText.innerHTML = `Confidence: ${data.confidence}%`;

        document.getElementById("resultCard").classList.remove("hidden");
    });
}
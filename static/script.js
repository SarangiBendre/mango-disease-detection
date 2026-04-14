const fileInput = document.getElementById("fileInput");
const dropArea = document.getElementById("drop-area");

fileInput.addEventListener("change", uploadImage);

// Drag & Drop
dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.style.background = "#1f3b4d";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.background = "transparent";
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    fileInput.files = e.dataTransfer.files;
    uploadImage();
});

function uploadImage() {
    let file = fileInput.files[0];

    if (!file) {
        alert("Select image!");
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

        if (data.label === "healthy") {
            resultText.innerHTML = "✅ Healthy Leaf";
            resultText.style.color = "#00ffcc";
        } else {
            resultText.innerHTML = "⚠️ Anthracnose Detected";
            resultText.style.color = "#ff4d4d";
        }

        confidenceText.innerHTML = `Confidence: ${data.confidence}%`;

        document.getElementById("resultCard").classList.remove("hidden");
    });
}
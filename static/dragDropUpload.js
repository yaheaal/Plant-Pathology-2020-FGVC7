let currentFiles = [];

document.addEventListener("DOMContentLoaded", function () {
    let dropArea = document.getElementById('drop-area');

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    dropArea.addEventListener('drop', handleDrop, false);

    document.getElementById('fileElem').addEventListener('change', function() {
        currentFiles = [...this.files];
        handleFiles(this.files);
        document.getElementById('selectButton').style.display = 'none';
        document.getElementById('predictButton').style.display = 'block';
    });

    document.getElementById('predictButton').addEventListener('click', function() {
        // Show the loading spinner and change button text
        this.disabled = true; // Disables the button
        document.getElementById('loadingSpinner').style.display = 'inline-block'; // Shows the spinner
    
        currentFiles.forEach(file => {
            uploadFile(file);
        });
    });
    

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight(e) {
        dropArea.classList.add('highlight');
    }

    function unhighlight(e) {
        dropArea.classList.remove('highlight');
    }

    function handleDrop(e) {
        let dt = e.dataTransfer;
        let files = dt.files;
        
        if(files.length > 1) {
            alert("Please drag and drop only one image!");
            return;
        }
    
        currentFiles = [];
        document.getElementById('gallery').innerHTML = '';
        
        if (files.length) {
            handleFiles(files);
            currentFiles = [...files];
        } else {
            let imageURL = dt.getData('text/uri-list');
            if (imageURL) {
                fetch(imageURL)
                    .then(response => response.blob())
                    .then(blob => {
                        // Extract filename from the URL or default to "temp.jpg"
                        let filename = imageURL.split('/').pop() || "temp.jpg";
                        let file = new File([blob], filename, { type: "image/jpeg" });
                        currentFiles.push(file);
                        handleFiles([file]);
                    });
            }

        }
        
        document.getElementById('selectButton').style.display = 'none';
        document.getElementById('predictButton').style.display = 'block';
        preventDefaults(e);
    }
    
    function handleFiles(files) {
        ([...files]).forEach(previewFile);
    
        document.getElementById('predictionDisplay').innerText = '';
        document.getElementById('predictionDisplay').style.display = 'none';
    }
    

    function previewFile(file) {
        let reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function() {
            let img = document.createElement('img');
            img.src = reader.result;
            document.getElementById('gallery').appendChild(img);
        }
    }

    function uploadFile(file) {
        var url = '/';
        var xhr = new XMLHttpRequest();
        var formData = new FormData();
        xhr.open('POST', url, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var response = JSON.parse(xhr.responseText);
                document.getElementById('predictionDisplay').innerText = "Prediction: " + response.prediction;
                document.getElementById('predictionDisplay').style.display = 'block';
                document.getElementById('predictButton').style.display = 'none';
    
                // Hide the loading spinner and reset button text
                document.getElementById('predictButton').disabled = false; // Re-enables the button
                document.getElementById('loadingSpinner').style.display = 'none'; // Hides the spinner
            }
        };
        
        formData.append('file', file);
        xhr.send(formData);
    }
    
});

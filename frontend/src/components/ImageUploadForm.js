// export default ImageUploadForm;
import React, { useState } from "react";
import axios from "axios";
import "../styles/ImageUploadForm.css"; // Importing the CSS file for styles

const ImageUploadForm = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [pressureReadings, setPressureReadings] = useState([]);
    const [error, setError] = useState("");

    const handleFileChange = event => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = async event => {
        event.preventDefault();

        if (!selectedFile) {
            setError("Please select a file to upload.");
            return;
        }

        const formData = new FormData();
        formData.append("image", selectedFile);

        try {
            const response = await axios.post(
                "http://127.0.0.1:5000/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );
            // setPressureReadings(response.data.pressures || []);
            // setError("");
            if (response.data.pressures && response.data.pressures.length > 0) {
                setPressureReadings(response.data.pressures);
                setError("");
            } else {
                setPressureReadings([]); // Clear previous readings
                setError("Couldn't read image properly.");
            }
        } catch (err) {
            setError("Error uploading image. Please try again.");
        }
    };

    return (
        <div className="upload-form-container">
            <h2>Upload Image for Pressure Extraction</h2>
            <form onSubmit={handleSubmit} className="upload-form">
                <input
                    type="file"
                    onChange={handleFileChange}
                    accept="image/*"
                    className="file-input"
                />
                <button type="submit" className="upload-button">
                    Upload
                </button>
            </form>

            {error && <p className="error-message">{error}</p>}

            {pressureReadings.length > 0 && (
                <div className="results-container">
                    <h3>Extracted Pressure Readings:</h3>
                    <div className="pressure-list">
                        {pressureReadings.map((reading, index) => (
                            <div key={index} className="pressure-card">
                                <p className="pressure-reading">{reading}</p>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

export default ImageUploadForm;

import axios from "axios";
import { useState } from "react";

export function Form1() {
    const [formData, setFormData] = useState({
        Crop_Type: '',
        Crop_Name: '',
        N: '',
        P: '',
        K: '',
        pH: '',
        RainFall: '',
        Temperature: '',
        Area_in_hectares: ''
    });
    const [prediction, setPrediction] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("Form Data:", formData);  // Log the form data to check what is being sent
        try {
            const response = await axios.post('http://localhost:8000/crops1/', formData); 
            setPrediction(response.data.prediction);
            alert('Data submitted successfully');
        } catch (error) {
            console.error('Error submitting data:', error.response ?.data || error.message);
            alert('Error submitting data');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex-row justify-center text-center">
            {Object.keys(formData).map(key => (
                <div className='bg-black' key={key} style={{ marginBottom: '7px' }}>
                    <input
                        style={{ padding: 10, margin: 2, borderRadius: 3 }}
                        type={key === 'Crop_Type' || key === 'Crop_Name' ? "text" : "number"}
                        name={key}
                        placeholder={key}
                        value={formData[key]}
                        onChange={handleChange}
                    />
                    <br />
                </div>
            ))}
            <button
                type="submit"
                style={{
                    padding: 15,
                    borderRadius: "5px",
                    margin: 15,
                    backgroundColor: "black",
                    color: "white"
                }}
            >
                GET CROP YIELD!
            </button>
            {prediction !== null && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Prediction Result: {prediction}</h3>
                </div>
            )}
        </form>
    );
}


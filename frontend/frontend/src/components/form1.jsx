
import axios from "axios";
import { useState } from "react";
import * as z from "zod";

const formDataSchema = z.object({
  Nitrogen: z.number().nonnegative(),
  Phosphorus: z.number().nonnegative(),
  Potassium: z.number().nonnegative(),
  Temperature: z.number().nonnegative(),
  Humidity: z.number().nonnegative(),
  pH_Value: z.number().min(0).max(14),
  Rainfall: z.number().nonnegative(),
});

export function Form() {
  const [formData, setFormData] = useState({
    Nitrogen: '',
    Phosphorus: '',
    Potassium: '',
    Temperature: '',
    Humidity: '',
    pH_Value: '',
    Rainfall: ''
  });

  const [prediction, setPrediction] = useState(null); 
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value === '' ? '' : Number(value),
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      formDataSchema.parse(formData);
      setErrors({}); 
      const response = await axios.post('http://localhost:8000/crops2/', formData); 
      setPrediction(response.data.predicted_crop);
    } catch (error) {
      if (error instanceof z.ZodError) {
        const newErrors = {};
        error.errors.forEach(err => {
          newErrors[err.path[0]] = err.message;
        });
        setErrors(newErrors);
      } else {
        console.error('Error submitting data:', error.response?.data || error.message);
        alert('Error submitting data');
      }
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="flex-row justify-center text-center">
        {Object.keys(formData).map(key => (
          <div className='input-container' key={key} style={{ marginBottom: '7px' }}>
            <input
              style={{ padding:10, margin:2,borderRadius:3, }}
              type="number"
              name={key}
              placeholder={key}
              value={formData[key]}
              onChange={handleChange}
            />
            {errors[key] && <p style={{ color: 'red' }}>{errors[key]}</p>}
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
          Submit!
        </button>
      </form>
      {prediction && (
        <div style={{ 
          marginTop: '20px', 
          padding: '20px', 
          border: '1px solid black', 
          borderRadius: '5px', 
          backgroundColor: 'green', 
          color: 'white', 
          textAlign: 'center' 
        }}>
          <h3>Predicted Crop: {prediction}</h3>
        </div>
      )}
    </div>
  );
}

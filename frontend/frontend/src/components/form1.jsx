
import axios from "axios";
import { useState } from "react";

export function Form() {
  // Initialize state for form fields
  const [formData, setFormData] = useState({
    N: '',
    P: '',
    K: '',
    pH: '',
    EC: '',
    OC: '',
    S: '',
    Zn: '',
    Fe: '',
    Cu: '',
    Mn: '',
    B: '',
  });

  // Handle input change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Convert form data to numbers
      const numericFormData = Object.fromEntries(
        Object.entries(formData).map(([key, value]) => [key, Number(value)])
      );
      
      await axios.post('http://localhost:8000/crops2/', numericFormData); 
      alert('Data submitted successfully');
    } catch (error) {
      console.error('Error submitting data:', error.response?.data || error.message);
      alert('Error submitting data');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex-row justify-center text-center">
      {Object.keys(formData).map(key => (
        <div key={key} style={{ marginBottom: '10px' }}>
          <input
            style={{ padding: 10, margin: 10 }}
            type="number" // Use 'number' for numeric input
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
        Submit!
      </button>
    </form>
  );
}

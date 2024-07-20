
import axios from "axios"
import zod from 'zod';
import { useState } from "react";
export function Form() {
    // Initialize state for form fields
    const [formData, setFormData] = useState({
      N: zod.number(),
      P: zod.number(),
      K: zod.number(),
      pH: zod.number(),
      EC: zod.number(),
      OC: zod.number(),
      S: zod.number(),
      Zn: zod.number(),
      Fe: zod.number(),
      Cu: zod.number(),
      Mn: zod.number(),
      B: zod.number(),
    });
  
    // Handle input change
    const handleChange = (e) => {
      const { name, value } = e.target;
      setFormData(prevState => ({
        ...prevState,
        [name]: value === '' ? ' ': Number(value),
      }));
    };
  
    // Handle form submission
    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        
        await axios.post('http://localhost:4001/form', formData); 
        alert('Data submitted successfully');
      } catch (error) {
        console.error('Error submitting data:', error.response ?.data || error.message);
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
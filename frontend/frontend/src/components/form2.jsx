
import axios from "axios"
import zod from 'zod';
import { useState } from "react";
export function Form1() {
    const [formData, setFormData] = useState({
      Crop_Type: zod.string(),
      Crop_Name: zod.string(),
      N: zod.number(),
      P: zod.number(),
      K: zod.number(),
      pH: zod.number(),
      RainFall: zod.number(),
      Temperature: zod.number(),
      Area_in_hectares: zod.number(),
    });
  
    const handleChange = (e) => {
      const { name, value } = e.target;
      setFormData(prevState => ({
        ...prevState,
        [name]: value === '' ? ' ': Number(value),
      }));
    };
  
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
          <div  className='bg-black'key={key} style={{ marginBottom: '7px' }}>
            <input
              style={{ padding:0, margin:2,borderRadius:3, }}
              type="number"
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
            backgroundColor:"black",
            color: "white"
          }}
        >
          GET CROP YIELD!
        </button>
      </form>
    );
  }
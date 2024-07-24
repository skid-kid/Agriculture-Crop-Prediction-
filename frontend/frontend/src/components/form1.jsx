
import axios from "axios";
import { useState } from "react";
import zod from "zod";
export function Form() {
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
        
        await axios.post('http://localhost:8000/crops2/', formData); 
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
            backgroundColor: "black",
            color: "white"
          }}
        >
          Submit!
        </button>
      </form>
    );
  }

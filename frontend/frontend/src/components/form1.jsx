import { useState } from 'react';
import AxiosInstance from '../Axios'; 

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
    B: ''
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
      // Post the form data to Django API endpoint
      await AxiosInstance.post('/CropModel2/', formData); // Ensure the endpoint matches your Django view
      alert('Data submitted successfully');
    } catch (error) {
      console.error('Error submitting data:', error);
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

/*
export function Form() {
    const [formData, setFormData] = useState({
        Crop_type: '',
        Crop_name: '',
        N: '',
        P: '',
        K: '',
        pH: '',
        Rainfall: '',
        Temperature: '',
        Area_in_hectares: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        AxiosInstance.post('CropModel1/', formData)
            .then(response => {
                console.log('Data submitted successfully:', response.data);
            })
            .catch(error => {
                console.error('Error submitting data:', error.response?.data);
            });
    };

    return (
        <form onSubmit={handleSubmit} className="flex-row justify-center text-center">
            <input name="Crop_type" placeholder="Crop Type" onChange={handleChange} required />
            <input name="Crop_name" placeholder="Crop Name" onChange={handleChange} required />
            <input name="N" type="number" placeholder="N" onChange={handleChange} required />
            <input name="P" type="number" placeholder="P" onChange={handleChange} required />
            <input name="K" type="number" placeholder="K" onChange={handleChange} required />
            <input name="pH" type="number" step="0.01" placeholder="pH" onChange={handleChange} required />
            <input name="Rainfall" type="number" step="0.01" placeholder="Rainfall" onChange={handleChange} required />
            <input name="Temperature" type="number" step="0.01" placeholder="Temperature" onChange={handleChange} required />
            <input name="Area_in_hectares" type="number" step="0.01" placeholder="Area in Hectares" onChange={handleChange} required />
            <button type="submit" style={{ padding: 15, borderRadius: "5px", margin: 15, backgroundColor: "black", color: "white" }}>Submit!</button>
        </form>
    );
}
*/


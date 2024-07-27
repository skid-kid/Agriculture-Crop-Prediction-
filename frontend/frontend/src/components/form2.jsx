import axios from "axios";
import { useState } from "react";

export function Form1() {
    const [formData, setFormData] = useState({
        State_Name:'',
        Crop_Type: '',
        Crop: '',
        N: '',
        P: '',
        K: '',
        pH: '',
        rainfall: '',
        temperature: '',
        Area_in_hectares: '',
    });
    const [prediction, setPrediction] = useState(null);

    const states = ['andhra pradesh' ,'arunachal pradesh' ,'assam', 'bihar', 'goa', 'gujarat',
        'haryana', 'jammu and kashmir', 'karnataka' ,'kerala', 'madhya pradesh',
        'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland' ,'odisha',
        'punjab' ,'rajasthan', 'tamil nadu' ,'telangana' ,'uttar pradesh',
        'west bengal' ,'chandigarh' ,'dadra and nagar haveli', 'himachal pradesh',
        'puducherry' ,'sikkim', 'tripura' ,'andaman and nicobar islands',
        'chhattisgarh', 'uttarakhand', 'jharkhand'];
    const crops = ['cotton' ,'horsegram' ,'jowar' ,'maize', 'moong' ,'ragi' ,'rice', 'sunflower',
 'wheat', 'sesamum', 'soyabean', 'rapeseed', 'jute' ,'arecanut', 'onion',
 'potato', 'sweetpotato', 'tapioca' ,'turmeric', 'barley', 'banana', 'coriander',
 'garlic', 'blackpepper' ,'cardamom' ,'cashewnuts', 'blackgram' ,'coffee',
 'ladyfinger', 'brinjal', 'cucumber' ,'grapes' ,'mango' ,'orange', 'papaya',
 'tomato', 'cabbage', 'bottlegourd', 'pineapple' ,'carrot', 'radish',
 'bittergourd', 'drumstick', 'jackfruit' ,'cauliflower' ,'watermelon',
 'ashgourd', 'beetroot' ,'pomegranate', 'ridgegourd', 'pumpkin', 'apple',
 'ginger']; 

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("Form Data:", formData);  
        try {
            const response = await axios.post('http://localhost:8000/crops1/', formData); 
            setPrediction(response.data.prediction);
        } catch (error) {
            console.error('Error submitting data:', error.response ?.data || error.message);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex-row justify-center text-center">
            <div style={{ marginBottom: '7px' }}>
                <select
                    style={{ padding: 10, margin: 2, borderRadius: 3, width:200,}}
                    name="State_Name"
                    value={formData.State_Name}
                    onChange={handleChange}
                >
                    <option value="">Select State</option>
                    {states.map(state => (
                        <option key={state} value={state}>{state}</option>
                    ))} 
                </select>
                <br />
            </div>
            <div  style={{ marginBottom: '7px' }}>
                <select
                    style={{ padding: 10, margin: 2, borderRadius: 3 ,width:200,height:40}}
                    name="Crop"
                    value={formData.Crop}
                    onChange={handleChange}
                >
                    <option value="">Select Crop</option>
                    {crops.map(crop => (
                        <option key={crop} value={crop}>{crop}</option>
                    ))}
                </select>
                <br />
            </div>
            {Object.keys(formData).filter(key => key !== 'State_Name' && key !== 'Crop').map(key => (
                <div key={key} style={{ marginBottom: '7px' }}>
                    <input
                        style={{ padding: 10, margin: 2, borderRadius: 3 }}
                        type={key === 'Crop_Type' ? "text" : "number"}
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
                <div style={{ marginTop: '20px', fontSize:'50px' }}>
                    <h3>Expected Yield of Crop in Tons: {prediction}</h3>
                <div style={{ 
                    marginTop: '20px', 
                    padding: '20px', 
                    border: '1px solid black', 
                    borderRadius: '5px', 
                    backgroundColor: 'green', 
                    color: 'white', 
                    textAlign: 'center' 
                  }}
                >
                    <h3>Expected Crop yield: {prediction}</h3>
                </div>
                </div>
            )}
        </form>
    )
}

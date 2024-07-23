import farmer from './assets/farmer.jpg'
import farmer2 from './assets/farmer2.png'
import { Form } from './components/form1'
import { Form1 } from './components/form2'
const text="{AI}"
const text2="{Agriculture-Department!}"
const Soil="{SOIL-FERTILITY}!"
const Crop="{CROP-YIELD }!"

function App() {  

  return (
    <div >

  <div className="bg-farmer bg-cover z-0">
  <div className='bg-black z-10'>
  <h1 className="text-purple-400 font-mono subpixel-antialiased  font-bold justify-center text-center brightness-200 drop-shadow-xl " style={{ fontSize: "35px" }}>DiGiFarm!</h1>
  </div>
  <h2 className="font-mono justify-center text-center   font-medium" style={{fontSize:"60px"}}>
    A generative platform to provide <a className="text-purple-500 shadow-2xl">{text}</a> assistants to <a className="shadow-2xl text-red-400">{text2} </a>
  </h2>
</div>
   <div>
   <h2 className="font-sans justify-between text-center m-10 p-15  text-pretty font-bold text-purple-400 drop-shadow-xl" style={{fontSize:"50px"}}>CHECK YOUR <a className='text-black'>{Soil}</a> </h2>
   <h4 className='font-sans justfiy-between text-center '>*Provide float values only*</h4>
   <div className=" flex justify-center">
    <Form></Form>
   </div>
   
   </div>
   <div className='bg-farmer bg-cover'>  
   <h2 className="font-sans justify-between text-center m-10 p-15  text-pretty font-bold text-purple-600 drop-shadow-xl" style={{fontSize:"50px"}}>CHECK YOUR <a className='text-black'>{Crop}</a> </h2>
   <div className=" flex justify-center">
    <Form1></Form1>
   </div>
   
   </div> 

</div>
  )
}



export default App

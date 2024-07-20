import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import farmer from './assets/farmer.png'
import farmer2 from './assets/farmer2.png'
import { Form } from './components/form1'
const text="{AI}"
const text2="{Agriculture-Department!}"
const Soil="{SOIL-FERTILITY}"
import AxiosInstance from './Axios'

function App() {  

  return (
    <div >

  <div className="bg-slate-200 bg-cover">
  <h1 className="text-purple-800 font-mono subpixel-antialiased  font-bold m-0 p-0 justify-center text-center brightness-200 drop-shadow-xl animate-bounce" style={{ fontSize: "100px" }}>DiGiFarm!</h1>
  <h2 className="font-mono justify-center text-center   font-medium" style={{fontSize:"60px"}}>
    A generative platform to provide <a className="text-purple-500 shadow-2xl">{text}</a> assistants to <a className="shadow-2xl text-red-400">{text2} </a>
  </h2>
</div>
   <div className="container flex justify-between m-0 p-0 "> 
    <div className=''>
   <img className="brightness-120" src={farmer2} style={{width:"1200px"}}></img>
   <img className='' src={farmer}></img>
   </div> 
   <div className=" m-0 p-0 drop-shadow-xl " style={{height:"200px"}}>
   <h2 className="font-sans justify-center text-center m-10 p-15  text-pretty font-bold text-purple-400 drop-shadow-xl" style={{fontSize:"40px"}}>GET HELP IN CHECKING <a className='text-black'>{Soil}</a> BY FILLING THIS FORM AFTER GETTING THE VALUE OF PARTICULAR FIELDS</h2>
   <h4 className='font-sans justfiy-center text-center '>*Provide float values only*</h4>
   <div className=" flex justify-center ">
    <Form></Form>

   </div>
   </div>
   </div>

</div>
  )
}



export default App

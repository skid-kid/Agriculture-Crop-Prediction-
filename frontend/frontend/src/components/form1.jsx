export function Form(){
    return <div className="flex-row justify-center text-center">
        <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="N" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="P" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="k" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
        <input  style={{
            padding:10,
            margin:10,
        }} type="float" placeholder="pH" onChange={function(e){
            const value=e.target.value
        }}></input> <br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="EC" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="OC" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="S" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="Zn" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="Fe" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="Cu" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="Mn" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
         <input style={{
            padding:10,
            margin:10,
        }}type="float" placeholder="B" onChange={function(e){
            const value=e.target.value
        }}></input><br/>
        <button  style={{
            padding:15,
            borderRadius:"5px",
            margin:15,
            backgroundColor:"black",
            color:"white",
        }}>Submit!</button>
    </div>
}
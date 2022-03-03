import { useState, SyntheticEvent } from "react";
import { Navigate } from "react-router-dom";
import MyNavbar from "../components/MyNavbar";
import Tags from "./Tags";

function Hashtag(){
    const [hashtag, setHashtag] = useState('');
    const [redirect, setRedirect] = useState(false)
    const token = localStorage.getItem("token")

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        const send = await fetch('http://127.0.0.1:8000/hashtag/',{
            method:"POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${token}`

            },
            body:JSON.stringify({
                hashtag,
            })
          })
          setRedirect(true)
          const content = await send.json()
          console.log(content["Response"])
        }

    if (redirect){
        return <Navigate to="/login/"/>
    }

    return(
        <MyNavbar>
            <div>
            <form onSubmit={submit}>
                <input placeholder="Enter Hashtag name" name="hashtag" onChange={e => setHashtag(e.target.value) } />
                <button type="submit">Submit</button>
            </form>
            {/* <Tags/> */}
            </div>
        </MyNavbar>
    )
}

export default Hashtag;
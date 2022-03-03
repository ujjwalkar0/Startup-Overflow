import { Tag } from "@mui/icons-material";
import { Hash } from "crypto";
import { useEffect, useState, SyntheticEvent } from "react";
import { Navigate } from "react-router-dom";
import MyNavbar from "../components/MyNavbar";
import Hashtag from "../Hashtag/Hashtag";

function Interface(){
    return (
        <MyNavbar>
        <form onSubmit={submit}>
            <input placeholder="Title" name="title" onChange={e => setTitle(e.target.value) } />
            <input placeholder="Short Description" name="desc" onChange={e => setShrtDesc(e.target.value) }/>

            <select name="hashtag" onChange={e=>setHash(e.target.value)}>
                {hashtags.map((tag:any)=><option value={tag.name}>{tag.name}</option>)}                
            </select>
            <button type="submit">Submit</button>
        </form>
    </MyNavbar>
    )
}
function AddPost(){

    const [title, setTitle] = useState('');
    const [shrtdesc, setShrtDesc] = useState('');
    const [desc, setDesc] = useState('');
    const [hashtag, setHash] = useState('');
    const [redirect, setRedirect] = useState(false)
    const [hashtags, setHashtags] = useState([])
    const token = localStorage.getItem("token")

    useEffect(() => {
        fetch('http://127.0.0.1:8000/hashtag/tag/',{
          method:"GET",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${token}`
          }
      })
      .then(resp => resp.json())
      .then(resp => setHashtags(resp))
      .catch(error => console.log(error))
    },[])

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        console.log(
            title,
            desc,
            hashtag
        )

        const response = await fetch('http://127.0.0.1:8000/posts/',{
            method:"POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${token}`
            },
            body:JSON.stringify({
                title,
                desc,
                hashtag

            })
        })
        setRedirect(true)
        const content = await response.json()
        console.log(content)
    }
    if (redirect){
        return <Navigate to="/"/>
    }

    return (
    <MyNavbar>
        <form onSubmit={submit}>
            <input placeholder="Title" name="title" onChange={e => setTitle(e.target.value) } />
            <input placeholder="Short Description" name="desc" onChange={e => setShrtDesc(e.target.value) }/>

            <select name="hashtag" onChange={e=>setHash(e.target.value)}>
                {hashtags.map((tag:any)=><option value={tag.name}>{tag.name}</option>)}                
            </select>
            <button type="submit">Submit</button>
        </form>
    </MyNavbar>
    )
}

export default AddPost;
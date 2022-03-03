import { SyntheticEvent, useState } from "react";
import { Form, Container, Button, InputGroup, FormControl } from "react-bootstrap";
import { Navigate } from "react-router-dom";
import MyNavbar from "../components/MyNavbar";
import Posts from "../Posts/Posts";


function MyLogin(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false)
    const [msg, setMsg] = useState("")

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:8000/users/login/',{
            method:"POST",
            headers: {"Content-Type": "application/json"},
            body:JSON.stringify({
                username,
                password,
            })
        })
        const content = await response.json()
        if (typeof content.token !== 'undefined') {
            localStorage.setItem("token",content.token)
            console.log("token type",content.token)
            setRedirect(true)
        }
        else{
            setMsg("Invalid Username or Password")
        }

    }

    if (redirect){
        return <Navigate to="/posts"/>
    }


    return(
      <MyNavbar>
          <Container>
        <form onSubmit={submit}>
            {/* <h4>Username</h4> */}
            <label>Username</label>
            <input className="login" placeholder="Username" name="username" onChange={e => setUsername(e.target.value) }/>
            <label>Password</label>
            <input className="login" type='password' placeholder="Password" name="password" onChange={e => setPassword(e.target.value) }/>
            <br/>
            <Button variant="success" type="submit">Submit</Button>
            {msg}
            {/* <button type="submit">Submit</button> */}
        </form> 
        </Container>
        </MyNavbar>
    )
}

function Login(){
    return(
        <div>{localStorage.getItem('token')==null ? <MyLogin/> : <Navigate to="/posts"/>  }</div>
    )
}

export default Login;

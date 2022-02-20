import React, { SyntheticEvent, useState } from "react";
import {Navigate} from 'react-router-dom';

function Login(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false)

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:8000/login/',{
            method:"POST",
            headers: {"Content-Type": "application/json"},
            credentials: "include",
            body:JSON.stringify({
                username,
                password,
            })
        })
        setRedirect(true)

    }

    if (redirect){
        return <Navigate to="/"/>
    }


    return(
        <form onSubmit={submit}>
            <input placeholder="Username" name="username" onChange={e => setUsername(e.target.value) }/>
            <input type='password' placeholder="Password" name="password" onChange={e => setPassword(e.target.value) }/>
            <button type="submit">Submit</button>
        </form>
    )
}

export default Login;
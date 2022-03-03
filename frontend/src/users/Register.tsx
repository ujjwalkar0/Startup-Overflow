import { SyntheticEvent, useState } from "react";
import {Navigate} from 'react-router-dom';
import MyNavbar from "../components/MyNavbar";

const Register = () => {
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirm_password, setConfirmPassword] = useState('');
    const [redirect, setRedirect] = useState(false)

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        if (password===confirm_password){
          const response = await fetch('http://127.0.0.1:8000/users/register/',{
              method:"POST",
              headers: {"Content-Type": "application/json"},
              body:JSON.stringify({
                  first_name,
                  last_name,
                  email,
                  username,
                  password,
                  confirm_password
              })
          })
          setRedirect(true)
          const content = await response.json()
          console.log(content)
        }

    }

    if (redirect){
        return <Navigate to="/"/>
    }

    return (
    <MyNavbar>
        <form onSubmit={submit}>
            <input placeholder="First Name" name="first_name" onChange={e => setFirstName(e.target.value) } />
            <input placeholder="Last Name" name="last_name" onChange={e => setLastName(e.target.value) }/>
            <input placeholder="Email" name="email" onChange={e => setEmail(e.target.value) }/>
            <input placeholder="Username" name="username" onChange={e => setUsername(e.target.value) }/>
            <input placeholder="Password" name="password" onChange={e => setPassword(e.target.value) }/>
            <input placeholder="Confirm Password" name="confirm_password" onChange={e => setConfirmPassword(e.target.value) }/>
            <button type="submit">Submit</button>
        </form>
    </MyNavbar>
    )
}

export default Register;

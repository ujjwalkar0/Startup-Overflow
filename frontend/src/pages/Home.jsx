import React, { useEffect, useState } from "react";

function Home(){
    const [name, setName] = useState('')

    useEffect(()=> {
        (
            async () => {
                const response = await fetch('http://127.0.0.1:8000/user/',{
                    headers: {"Content-Type": "application/json"},
                    credentials: "include",
                });
            const content = await response.json()
            setName(content.name);
        }
        )();
    })

    return(
        <h1>{name ? 'Hi' + name : 'You are not logged in' } </h1>
    )
}

export default Home;
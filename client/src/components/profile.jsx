import { jwtDecode } from "jwt-decode";
import React, { useEffect, useState } from "react";

export default function Profile(){
    const [username, setUsername] = useState("");

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (token){
            try{
                const decoded = jwtDecode(token);
                setUsername(decoded.sub);
            } catch(err){
                console.error("Invalid Token");
            }
        }
    }, [])

    return(
        <>
            <h1>Profile Page</h1>
            <h2>Hello and welcome {username} </h2>
        </>
    );
}
import { jwtDecode } from "jwt-decode";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Profile(){
    const [username, setUsername] = useState("");
    const navigate = useNavigate();

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

    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/");
    };

    return(
        <>
            <h1>Profile Page</h1>
            <h2>Hello and welcome {username} </h2>
            <button onClick={handleLogout}>Logout</button>
        </>
    );
}
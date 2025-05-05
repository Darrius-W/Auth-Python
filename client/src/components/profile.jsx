import { jwtDecode } from "jwt-decode";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Profile(){
    const [username, setUsername] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token){
            navigate("/");
            return;
        }
        try{
            const decoded = jwtDecode(token);
            const isExpired = decoded.exp * 1000 < Date.now();
            
            if (isExpired){
                localStorage.removeItem("token");
                navigate("/");
            }
            else{
                setUsername(decoded.sub);
            }
        } catch(err){
            console.error("Invalid Token");
            navigate("/");
        }
    }, [navigate])

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
import { jwtDecode } from "jwt-decode";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

export default function Profile(){
    const [username, setUsername] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const checkAuth = async () => {
            try {
              const res = await axios.get("http://localhost:8000/protected", {
                withCredentials: true,
              });
              setUsername(res.data.username);
            } catch (err) {
              console.error("Not authenticated", err);
              navigate("/");
            }
          };
      
          checkAuth();

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
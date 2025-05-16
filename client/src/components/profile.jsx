import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

export default function Profile(){
    const [username, setUsername] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        // Function to check a users authentication status
        const checkAuth = async () => {
            try {
              // Attempt to call the protected route on the backend
              const res = await axios.get("http://localhost:8000/protected", {
                withCredentials: true,
              });

              // If successful, store the username from the response
              setUsername(res.data.username);
            } catch (err) {
              // If not, redirect to the login page
              console.error("Not authenticated", err);
              navigate("/");
            }
          };
      
          checkAuth();

    }, [navigate])

    // Logs the user out by sending a POST request to the backend logout endpoint,
    // which removes the HTTP-only cookie storing the access token.
    const handleLogout = async () => {
      try{
        const response = await axios.post("http://localhost:8000/logout", {}, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json"
          }
        });

        alert(response.data.message); // Display success message from backend
        navigate("/"); // redirect user to login page
      } catch(error){
        console.error("Logout failed:", error);
        alert("Logout failed. Please try again.");
      }
    };

    return(
        <>
            <h1>Profile Page</h1>
            <h2>Hello and welcome {username} </h2>
            <button onClick={handleLogout}>Logout</button>
        </>
    );
}
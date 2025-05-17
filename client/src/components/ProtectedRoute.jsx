import { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import axios from 'axios';

// A wrapper component that guards protected routes or componenets
function GetProtectedData({ children }) {
    // Track authentication state
    const [authorized, setAuthorized] = useState(null);
  
    useEffect(() => {
      // Check if the user is authenticated by hitting the backend `/protected` endpoint
      const checkAuth = async () => {
        try {
          const res = await axios.get("http://localhost:8000/protected", {
            withCredentials: true, // Ensure Http-only cookie is included in the request
          });
          setAuthorized(true); // If successful, mark user as authorized
        } catch (err) {
          console.error("Not authorized:", err);
          setAuthorized(false); // On failure, mark user as unauthorized
        }
      };
  
      checkAuth();
    }, []);
  
    // If unauthorized, redirect user back to the login page
    if (!authorized) return <Navigate to="/" replace />;

    // If authorized, render protected content
    return children;
};

export default GetProtectedData;
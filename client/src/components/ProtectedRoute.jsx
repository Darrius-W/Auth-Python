import { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import axios from 'axios';

function GetProtectedData({ children }) {
    const [authorized, setAuthorized] = useState(null);
  
    useEffect(() => {
      const checkAuth = async () => {
        try {
          const res = await axios.get("http://localhost:8000/protected", {
            withCredentials: true,
          });
          setAuthorized(true);
        } catch (err) {
          console.error("Not authorized:", err);
          setAuthorized(false);
        }
      };
  
      checkAuth();
    }, []);
  
    if (authorized === null) return <p>Loading...</p>;
    if (!authorized) return <Navigate to="/" replace />;
    return children;
};

export default GetProtectedData;
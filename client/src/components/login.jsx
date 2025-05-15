import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import React, { useState } from 'react';

export default function Login(){
    const [loginInfo, setLoginInfo] = useState({
        username: '',
        password: ''
    });
    const navigate = useNavigate();
    
    // Handles input changes and updates the corresponding field in loginInfo
    const handleChange = (e) => {
        const{ name, value } = e.target;
        setLoginInfo((prev) =>({
          ...prev,
          [name]: value
        }));
    };
    
    // Handles the submission of the login form, sending a POST request to the backend to validate the user
    const handleLogin = async (e) => {
        e.preventDefault(); // avoids page refresh upon submission

        // Ensure input is not blank
        if (!loginInfo.username || !loginInfo.password){
          alert("Username and password cannot be empty");
          return;
        }
    
        try{
          const response = await axios.post('http://localhost:8000/login', loginInfo, {
            withCredentials: true, 
            headers: {
              "Content-Type": "application/json",
            },
          });
          alert(response.data.message)
          navigate("/Profile")
        } catch(error) {
          alert(error.response.data.detail)
        }

        setLoginInfo({username:'', password:''}); // resets form fields after submission
    };

    return(
        <div>
            <form onSubmit={handleLogin}>
                <h1>Login</h1>
                <label for="username">Username:</label><br />
                <input
                  type="text"
                  name="username"
                  id="username"
                  value={loginInfo.username}
                  onChange={handleChange}
                  autoComplete='off'
                  placeholder="Enter username"
                /><br />
                <label for="password">Password:</label><br />
                <input
                  type="password"
                  name="password"
                  id="password"
                  value={loginInfo.password}
                  onChange={handleChange}
                  autoComplete='off'
                  placeholder="Enter password"
                /><br />
                <button type="submit" id="login-btn">Login</button>
            </form><br />
            <Link to="/Signup">Signup</Link>
        </div>
    );
}
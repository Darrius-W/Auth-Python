import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import React, { useState } from 'react';

export default function Signup(){
    const [userInfo, setUserInfo] = useState({
        username: '',
        password: '',
        passwordConfirm: ''
    });
    const [error, setError] = useState("");
    const navigate = useNavigate();
    
    // Handles input changes and updates the corresponding field in userInfo
    const handleChange = (e) => {
        const{ name, value } = e.target;
        setUserInfo((prev) =>({
          ...prev,
          [name]: value
        }));
    };
    
    // Handles the submission of the signup form, sending a POST request to the backend to create a new user
    const handleSignup = async (e) => {
        e.preventDefault(); // avoids page refresh upon submission

        // Ensure input is not blank
        if (!userInfo.username || !userInfo.password || !userInfo.passwordConfirm){
          alert("Username and password cannot be empty");
          return;
        }
    
        // Check if passwords match
        if (userInfo.password !== userInfo.passwordConfirm){
          setError("Passwords do not match!");
          return;
        }
        setError("")

        try{
          const response = await axios.post('http://localhost:8000/addUser', userInfo, {
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

        setUserInfo({username:'', password:'', passwordConfirm:''}); // resets form fields after submission
    };

    return(
        <div>
            <form onSubmit={handleSignup}>
                <h1>Signup</h1>
                <label htmlFor="username">Username:</label><br />
                <input
                  type="text"
                  name="username"
                  id="username"
                  value={userInfo.username}
                  onChange={handleChange}
                  autoComplete='off'
                  placeholder="Enter username"
                /><br />
                <label htmlFor="password">Password:</label><br />
                <input
                  type="password"
                  name="password"
                  id="password"
                  value={userInfo.password}
                  onChange={handleChange}
                  autoComplete='off'
                  placeholder="Enter password"
                /><br />
                <label htmlFor="passwordConfirm">Confirm Password:</label><br />
                <input
                  type="password"
                  name="passwordConfirm"
                  id="passwordConfirm"
                  value={userInfo.passwordConfirm}
                  onChange={handleChange}
                  autoComplete='off'
                  placeholder="Confirm password"
                /><br />
                {error && <p style={{ color: "red" }}>{error}</p>}
                <button type="submit" id="signup-btn">Create Account</button>
            </form><br />
            <Link to="/">Login</Link>
        </div>
    );
}

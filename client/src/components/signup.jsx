import { Link } from 'react-router-dom';
import axios from 'axios';
import React, { useState } from 'react';

export default function Signup(){
    const [userInfo, setUserInfo] = useState({
        username: '',
        password: '',
        passwordConfirm: ''
    });
    const [error, setError] = useState("");
    
    const handleChange = (e) => {
        const{ name, value } = e.target;
        setUserInfo((prev) =>({
          ...prev,
          [name]: value
        }));
    };
    
    const handleSignup = async (e) => {
        e.preventDefault();
    
        // Check if passwords match
        if (userInfo.password !== userInfo.passwordConfirm){
          setError("Passwords do not match!");
          return;
        }
        setError("")

        try{
          const response = await axios.post('http://localhost:8000/addUser', userInfo, { withCredentials: true}, {
            headers: {
              "Content-Type": "application/json",
            },
          });
          
          console.log(response.data);
        } catch(error) {
          console.error(error);
        }

        setUserInfo({username:'', password:'', passwordConfirm:''});
    };

    return(
        <div>
            <form onSubmit={handleSignup}>
                <h1>Signup</h1>
                <label for="username">Username:</label><br />
                <input type="text" name="username" id="username" value={userInfo.username} onChange={handleChange} autoComplete='off' placeholder="Enter username"/><br />
                <label for="password">Password:</label><br />
                <input type="password" name="password" id="password" value={userInfo.password} onChange={handleChange} autoComplete='off' placeholder="Enter password"/><br />
                <label for="passwordConfirm">Confirm Password:</label><br />
                <input type="password" name="passwordConfirm" id="passwordConfirm" value={userInfo.passwordConfirm} onChange={handleChange} autoComplete='off' placeholder="Confirm password"/><br />
                {error && <p style={{ color: "red" }}>{error}</p>}
                <button type="submit" id="signup-btn">Create Account</button>
            </form><br />
            <Link to="/">Login</Link>
        </div>
    );
}
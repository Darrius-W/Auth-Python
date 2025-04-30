import { Link } from 'react-router-dom';
import axios from 'axios';
import React, { useState } from 'react';

export default function Login(){
    const [loginInfo, setLoginInfo] = useState({
        username: '',
        password: ''
    });
    
    const handleChange = (e) => {
        const{ name, value } = e.target;
        setLoginInfo((prev) =>({
          ...prev,
          [name]: value
        }));
    };
    
    const handleLogin = async (e) => {
        e.preventDefault();
    
        try{
          const response = await axios.post('http://localhost:8000/authLogin', loginInfo, { withCredentials: true}, {
            headers: {
              "Content-Type": "application/json",
            },
          });
          
          console.log(response.data);
        } catch(error) {
          console.error(error);
        }
    };

    return(
        <div>
            <form onSubmit={handleLogin}>
                <h1>Login</h1>
                <label for="username">Username:</label><br />
                <input type="text" name="username" id="username" value={loginInfo.username} onChange={handleChange} autoComplete='off' placeholder="Enter username"/><br />
                <label for="password">Password:</label><br />
                <input type="password" name="password" id="password" value={loginInfo.password} onChange={handleChange} autoComplete='off'  placeholder="Enter password"/><br />
                <button type="submit" id="login-btn">Login</button>
            </form><br />
            <Link to="/Signup">Signup</Link>
        </div>
    );
}
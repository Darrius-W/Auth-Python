import { Link } from 'react-router-dom';
import axios from 'axios';
import React, { useState } from 'react';

export default function Login(){
    /*const [loginInfo, setLoginInfo] = useState({
        username: '',
        password: ''
    });*/
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    
    /*const handleChange = (e) => {
        const{ name, value } = e.target;
        setLoginInfo((prev) =>({
          ...prev,
          [name]: value
        }));
    };*/
    
    const handleLogin = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);
    
        try{
          const response = await axios.post('http://localhost:8000/authLogin', formData, { withCredentials: true}, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
          console.log(response.data);
        } catch(error) {
          console.error(error);
        }
    
        //setLoginInfo({username: '', password: ''});
    };

    return(
        <div>
            <form onSubmit={handleLogin}>
                <h1>Login</h1>
                <label for="username">Username:</label><br />
                <input type="text" name="username" id="username" value={username} onChange={(e) => setUsername(e.target.value)} autoComplete='off' placeholder="Enter username"/><br />
                <label for="password">Password:</label><br />
                <input type="password" name="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} autoComplete='off'  placeholder="Enter password"/><br />
                <button type="submit" id="login-btn">Login</button>
            </form><br />
            <Link to="/Signup">Signup</Link>
        </div>
    );
}
import { Link } from 'react-router-dom';

export default function Signup(){
    return(
        <div>
            <form>
                <h1>Signup</h1>
                <label for="username">Username:</label><br />
                <input type="text" name="username" id="username" placeholder="Enter username"/><br />
                <label for="password">Password:</label><br />
                <input type="password" name="password" id="password" placeholder="Enter password"/><br />
                <label for="confirm-password">Confirm Password:</label><br />
                <input type="password" name="confirm-password" id="confirm-password" placeholder="Confirm password"/><br />
                <button type="submit" id="signup-btn">Signup</button>
            </form><br />
            <Link to="/">Login</Link>
        </div>
    );
}
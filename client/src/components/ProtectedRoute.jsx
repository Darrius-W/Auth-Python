import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";

const isTokenValid = () => {
    const token = localStorage.getItem("token");
    if (!token) return false;

    try{
        const decoded = jwtDecode(token);
        return decoded.exp * 1000 > Date.now();
    } catch {
        return false;
    }
};

const ProtectedRoute = ({ children }) => {
    return isTokenValid() ? children : <Navigate to="/" replace />
};

export default ProtectedRoute;
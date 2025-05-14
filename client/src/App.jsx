import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login.jsx'
import Signup from './components/Signup.jsx';
import Profile from './components/Profile.jsx';
//import ProtectedRoute from './components/ProtectedRoute.jsx';
import GetProtectedData from './components/ProtectedRoute.jsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/Signup" element={<Signup />} />
        <Route path="/Profile" element={<GetProtectedData><Profile /></GetProtectedData>} />
      </Routes>
    </Router>
  );
}

export default App;

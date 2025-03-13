import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Login from '../components/auth/Login';
import Register from '../components/auth/Register';
import { useAuth } from '../contexts/AuthContext';

const AuthPage = () => {
  const [isLogin, setIsLogin] = useState(true);
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();
  
  useEffect(() => {
    // Redirect if already authenticated
    if (isAuthenticated) {
      navigate('/upload');
    }
  }, [isAuthenticated, navigate]);
  
  const toggleAuthMode = () => {
    setIsLogin(!isLogin);
  };
  
  return (
    <div className="py-16 fade-in">
      <div className="mb-10 text-center">
        <h1 className="text-5xl font-bold text-[#1d1d1f] tracking-tight mb-3">Timeline Visualizer</h1>
        <p className="mt-3 text-xl text-[#6e6e73] max-w-lg mx-auto">
          Upload your Excel files and visualize event timelines
        </p>
      </div>
      
      <div className="max-w-md mx-auto px-4">
        {isLogin ? (
          <Login onSwitchToRegister={toggleAuthMode} />
        ) : (
          <Register onSwitchToLogin={toggleAuthMode} />
        )}
      </div>
    </div>
  );
};

export default AuthPage;
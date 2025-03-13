import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';

const NavBar = () => {
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  
  const handleLogout = () => {
    logout();
    navigate('/');
  };
  
  return (
    <nav className="sticky top-0 z-40 bg-white/90 backdrop-blur-md shadow-sm border-b border-[#e8e8ed]">
      <div className="container mx-auto px-6">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <Link 
              to="/" 
              className="text-xl font-semibold text-[#1d1d1f] hover:text-[#0071e3] tracking-tight transition"
            >
              Timeline Visualizer
            </Link>
          </div>
          
          <div className="flex items-center">
            {isAuthenticated ? (
              <div className="flex items-center space-x-5">
                <Link 
                  to="/upload" 
                  className="text-[#1d1d1f] hover:text-[#0071e3] px-3 py-2 text-sm font-medium transition"
                >
                  Upload
                </Link>
                <Link 
                  to="/timeline" 
                  className="text-[#1d1d1f] hover:text-[#0071e3] px-3 py-2 text-sm font-medium transition"
                >
                  Timeline
                </Link>
                <button
                  onClick={handleLogout}
                  className="ml-3 bg-[#f5f5f7] hover:bg-[#e8e8ed] text-[#1d1d1f] rounded-lg px-4 py-1.5 text-sm font-medium transition"
                >
                  Logout
                </button>
              </div>
            ) : (
              <Link 
                to="/" 
                className="text-[#1d1d1f] hover:text-[#0071e3] px-3 py-2 text-sm font-medium transition"
              >
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
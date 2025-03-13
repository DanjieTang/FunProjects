import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import AuthPage from './pages/AuthPage';
import UploadPage from './pages/UploadPage';
import TimelinePage from './pages/TimeLinePage';
import NavBar from './components/common/NavBar';

// Protected route component
const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();
  
  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }
  
  return children;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="min-h-screen bg-gray-50 font-sans">
          <NavBar />
          <div className="container mx-auto px-4 py-8">
            <Routes>
              <Route path="/" element={<AuthPage />} />
              <Route 
                path="/upload" 
                element={
                  <ProtectedRoute>
                    <UploadPage />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/timeline" 
                element={
                  <ProtectedRoute>
                    <TimelinePage />
                  </ProtectedRoute>
                } 
              />
            </Routes>
          </div>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Input from '../common/Input';
import Button from '../common/Button';
import Card from '../common/Card';
import { useAuth } from '../../contexts/AuthContext';
import { loginUser } from '../../services/api';

const Login = ({ onSwitchToRegister }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [apiError, setApiError] = useState('');
  
  const { login } = useAuth();
  const navigate = useNavigate();
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    
    // Clear field error when user starts typing
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
    
    // Clear API error when user makes any change
    if (apiError) {
      setApiError('');
    }
  };
  
  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.email.trim()) {
      newErrors.email = 'Username or email is required';
    }
    
    if (!formData.password) {
      newErrors.password = 'Password is required';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    setIsLoading(true);
    setApiError('');
    
    try {
      const userData = await loginUser(formData);
      login(userData);
      navigate('/upload');
    } catch (error) {
      console.error('Login submission error:', error);
      
      // Try to extract more specific error details if available
      let errorMessage = 'Failed to login. Please try again.';
      
      if (error.message) {
        if (error.message.includes('Validation error')) {
          errorMessage = 'Invalid username or password format.';
        } else if (error.message.includes('401') || error.message.includes('Unauthorized')) {
          errorMessage = 'Invalid username or password.';
        } else if (error.message.includes('422')) {
          errorMessage = 'Username or password validation failed.';
        } else if (error.message.includes('Network')) {
          errorMessage = 'Network error. Please check your connection.';
        } else {
          // Use the error message if it's available
          errorMessage = error.message;
        }
      }
      
      setApiError(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <Card className="max-w-md mx-auto fade-in">
      <form onSubmit={handleSubmit} className="space-y-6">
        <h2 className="text-2xl font-semibold text-[#1d1d1f] tracking-tight mb-6">Login</h2>
        
        {apiError && (
          <div className="p-3.5 bg-[#ff3b30]/10 text-[#ff3b30] rounded-lg text-sm font-medium">
            {apiError}
          </div>
        )}
        
        <Input
          label="Username or Email"
          type="text"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Enter your username or email"
          error={errors.email}
          required
        />
        
        <Input
          label="Password"
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          placeholder="Enter your password"
          error={errors.password}
          required
        />
        
        <div className="pt-2">
          <Button 
            type="submit" 
            variant="primary" 
            disabled={isLoading}
            fullWidth
          >
            {isLoading ? 'Logging in...' : 'Login'}
          </Button>
        </div>
        
        <div className="text-center pt-2">
          <p className="text-sm text-[#6e6e73]">
            Don't have an account?{' '}
            <button
              type="button"
              onClick={onSwitchToRegister}
              className="text-[#0071e3] hover:text-[#0061c3] font-medium"
            >
              Register
            </button>
          </p>
        </div>
      </form>
    </Card>
  );
};

export default Login;
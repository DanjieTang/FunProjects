import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Input from '../common/Input';
import Button from '../common/Button';
import Card from '../common/Card';
import { useAuth } from '../../contexts/AuthContext';
import { registerUser } from '../../services/api';

const Register = ({ onSwitchToLogin }) => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    confirmPassword: ''
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [apiError, setApiError] = useState('');
  
  const { register } = useAuth();
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
    
    if (!formData.username.trim()) {
      newErrors.username = 'Username is required';
    }
    
    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }
    
    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
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
      // Remove confirmPassword before sending to API
      const { confirmPassword, ...registerData } = formData;
      
      const userData = await registerUser(registerData);
      register(userData);
      navigate('/upload');
    } catch (error) {
      console.error('Registration submission error:', error);
      
      // Try to extract more specific error details if available
      let errorMessage = 'Failed to register. Please try again.';
      
      if (error.message) {
        if (error.message.includes('Validation error')) {
          errorMessage = 'Invalid username or password format.';
        } else if (error.message.includes('409') || error.message.includes('Conflict')) {
          errorMessage = 'Username already exists. Please choose another.';
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
    <Card className="max-w-md mx-auto">
      <form onSubmit={handleSubmit}>
        <h2 className="text-2xl font-semibold text-gray-800 mb-6">Register</h2>
        
        {apiError && (
          <div className="mb-4 p-3 bg-red-50 text-red-500 rounded-lg text-sm">
            {apiError}
          </div>
        )}
        
        <Input
          label="Username"
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
          placeholder="Enter your username"
          error={errors.username}
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
        
        <Input
          label="Confirm Password"
          type="password"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
          placeholder="Confirm your password"
          error={errors.confirmPassword}
          required
        />
        
        <div className="mt-6">
          <Button 
            type="submit" 
            variant="primary" 
            disabled={isLoading}
            fullWidth
          >
            {isLoading ? 'Registering...' : 'Register'}
          </Button>
        </div>
        
        <div className="mt-4 text-center">
          <p className="text-sm text-gray-600">
            Already have an account?{' '}
            <button
              type="button"
              onClick={onSwitchToLogin}
              className="text-blue-500 hover:text-blue-700 font-medium"
            >
              Login
            </button>
          </p>
        </div>
      </form>
    </Card>
  );
};

export default Register;
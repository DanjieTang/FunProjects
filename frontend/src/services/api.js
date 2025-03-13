// API service for making requests to the backend
const API_URL = 'http://localhost:8000';

// Flag to use mock data (for development)
const USE_MOCK_DATA = false; // Set to false when your backend is ready

// Helper function to handle responses
const handleResponse = async (response) => {
  // For 422 errors, let the calling function handle them for detailed validation messages
  if (response.status === 422) {
    throw new Error(`422 Unprocessable Content: ${response.statusText}`);
  }
  
  if (!response.ok) {
    let errorMessage;
    try {
      const error = await response.json();
      errorMessage = error.detail || error.message || `Error: ${response.status} ${response.statusText}`;
    } catch (e) {
      // If parsing JSON fails, use the status text
      errorMessage = `Error: ${response.status} ${response.statusText}`;
    }
    throw new Error(errorMessage);
  }
  
  // Check if we received any cookies - browsers will automatically store cookies
  console.log('Cookies received:', document.cookie.split(';'));
  
  // If response is empty or not JSON, return empty object
  if (response.headers.get('content-length') === '0') {
    return {};
  }
  
  try {
    const data = await response.json();
    console.log('Response data:', data);
    
    // If the response includes a token, store it
    if (data.token || data.access_token || data.jwt) {
      const token = data.token || data.access_token || data.jwt;
      localStorage.setItem('token', token);
      console.log('JWT token stored in localStorage');
    }
    
    return data;
  } catch (error) {
    console.error('Failed to parse JSON response:', error);
    // For JSON parse errors, return an empty object to prevent crashing
    return {};
  }
};

// Mock data for development
const mockData = {
  user: {
    id: 'mock-user-id',
    name: 'Test User',
    email: 'test@example.com',
  },
  timeline: {
    "AAA": {
        "Lmao": [
            {"Event Name": "1.1", 
            "Start Date": "2025-02-28",
            "End Date": "",
            "Icon": "star"},
            {"Event Name": "1.2", 
            "Start Date": "2025-03-30",
            "End Date": "",
            "Icon": "star"}
        ],
        "Haha": [
            {"Event Name": "2.1", 
            "Start Date": "2025-07-01",
            "End Date": "2025-07-30",
            "Icon": "normal"}
        ]
    }
  }
};

// Authentication API calls
export const loginUser = async (credentials) => {
  if (USE_MOCK_DATA) {
    return new Promise((resolve) => {
      setTimeout(() => resolve(mockData.user), 500);
    });
  }
  
  try {
    // Simplify - just send exactly what the backend expects
    const loginData = {
      username: credentials.email || credentials.username,
      password: credentials.password
    };
    
    console.log('Sending login data:', loginData);
    
    const response = await fetch(`${API_URL}/api/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(loginData),
      credentials: 'include',
    });
    
    // Log the raw response for debugging
    console.log('Login response status:', response.status);
    
    // Special handling for 422 errors to get validation details
    if (response.status === 422) {
      const errorData = await response.json();
      console.error('Validation error:', errorData);
      throw new Error(`Validation error: ${JSON.stringify(errorData)}`);
    }
  
    const data = await handleResponse(response);
    return data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

export const registerUser = async (userData) => {
  if (USE_MOCK_DATA) {
    return new Promise((resolve) => {
      setTimeout(() => resolve(mockData.user), 500);
    });
  }
  
  try {
    // Simplify - just send exactly what the backend expects
    const registrationData = {
      username: userData.username,
      password: userData.password
    };
    
    console.log('Sending registration data:', registrationData);
    
    const response = await fetch(`${API_URL}/api/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(registrationData),
      credentials: 'include',
    });
    
    // Log the raw response for debugging
    console.log('Register response status:', response.status);
    
    // Special handling for 422 errors to get validation details
    if (response.status === 422) {
      const errorData = await response.json();
      console.error('Validation error:', errorData);
      throw new Error(`Validation error: ${JSON.stringify(errorData)}`);
    }
  
    const data = await handleResponse(response);
    return data;
  } catch (error) {
    console.error('Registration error:', error);
    throw error;
  }
};

// Get auth headers for authenticated requests
const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  const headers = {
    'Content-Type': 'application/json',
  };
  
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  
  return headers;
};

// File upload API call
// Modified upload function in api.jsx
export const uploadExcelFiles = async (files) => {
  if (USE_MOCK_DATA) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({ message: 'Files uploaded successfully' });
      }, 1000);
    });
  }
  
  const formData = new FormData();
  
  // FastAPI expects all files to be under the same field name "files"
  // This matches your backend's parameter: files: List[UploadFile] = File(...)
  files.forEach((file) => {
    formData.append('files', file);
  });
  
  try {
    // Your backend uses cookies for authentication, not Authorization header
    const response = await fetch(`${API_URL}/api/upload-excel/`, {
      method: 'POST',
      // No need for extra headers as authentication is via cookies
      body: formData,
      credentials: 'include', // Include cookies - this is crucial for authentication
    });
    
    // Improved error handling for 422 errors
    if (response.status === 422) {
      try {
        const errorData = await response.json();
        console.error('Validation error details:', errorData);
        throw new Error(`Validation error: ${JSON.stringify(errorData)}`);
      } catch (e) {
        // If parsing JSON fails, fall back to status text
        throw new Error(`422 Unprocessable Content: ${response.statusText}`);
      }
    }
  
    return handleResponse(response);
  } catch (error) {
    console.error('File upload error:', error);
    throw new Error(error.message || 'Network error. Please check your connection and try again.');
  }
};

// Get visualization data API call
export const getVisualizationData = async () => {
  if (USE_MOCK_DATA) {
    return new Promise((resolve) => {
      // Simulate network delay
      setTimeout(() => {
        resolve(mockData.timeline);
      }, 800);
    });
  }
  
  try {
    const response = await fetch(`${API_URL}/api/image`, {
      method: 'GET',
      headers: getAuthHeaders(),
      credentials: 'include', // Include cookies
    });
  
    return handleResponse(response);
  } catch (error) {
    console.error('Visualization data error:', error);
    throw new Error(error.message || 'Network error. Please check your connection and try again.');
  }
};
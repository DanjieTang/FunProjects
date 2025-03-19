import { useState } from "react";

function PasswordInputForm() {
    const [formData, setFormData] = useState({ password: "" });
    const [errors, setErrors] = useState({});
  
    // Handles input change
    const handleChange = (e) => {
      setFormData({ ...formData, [e.target.name]: e.target.value });
  
      // Clear error message when user starts typing
      setErrors({ ...errors, [e.target.name]: "" });
    };
  
    // Form submission
    const handleSubmit = (e) => {
      e.preventDefault();
  
      let newErrors = {};
  
      if (!formData.password) {
        newErrors.password = "Password is required";
      } else if (formData.password.length < 6) {
        newErrors.password = "Password must be at least 6 characters";
      }
  
      if (Object.keys(newErrors).length > 0) {
        setErrors(newErrors);
      } else {
        alert("Form submitted successfully!");
      }
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <div>
          <label>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Enter your password"
            style={{
              border: errors.password ? "2px solid red" : "1px solid black",
              padding: "8px",
              display: "block",
            }}
          />
          {errors.password && (
            <span style={{ color: "red", fontSize: "12px" }}>{errors.password}</span>
          )}
        </div>
        <button type="submit" style={{ marginTop: "10px" }}>Submit</button>
      </form>
    );
  }

export default PasswordInputForm
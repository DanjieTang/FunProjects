import React from 'react';

const Button = ({ 
  children, 
  onClick, 
  type = 'button', 
  variant = 'primary', 
  disabled = false,
  className = '',
  fullWidth = false
}) => {
  // Base classes for all buttons (Apple-style)
  const baseClasses = "font-medium tracking-tight rounded-xl transition-all duration-200 focus:outline-none text-sm";
  
  // Apple-specific variant styling
  const variantClasses = {
    primary: "bg-[#0071e3] hover:bg-[#0061c3] text-white shadow-sm hover:shadow focus:ring-2 focus:ring-[#0071e3] focus:ring-offset-2 active:translate-y-0.5",
    secondary: "bg-[#e9e9eb] hover:bg-[#dededf] text-[#1d1d1f] shadow-sm hover:shadow focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 active:translate-y-0.5",
    danger: "bg-[#ff3b30] hover:bg-[#e63028] text-white shadow-sm hover:shadow focus:ring-2 focus:ring-[#ff3b30] focus:ring-offset-2 active:translate-y-0.5",
    text: "bg-transparent text-[#0071e3] hover:bg-[#f5f5f7] focus:ring-2 focus:ring-[#0071e3] focus:ring-offset-2"
  };
  
  // Apple's button sizing
  const sizeClasses = "px-6 py-3";
  const disabledClasses = disabled ? "opacity-50 cursor-not-allowed pointer-events-none" : "cursor-pointer";
  const widthClasses = fullWidth ? "w-full" : "";
  
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`
        ${baseClasses} 
        ${variantClasses[variant]} 
        ${sizeClasses} 
        ${disabledClasses}
        ${widthClasses}
        ${className}
      `}
    >
      {children}
    </button>
  );
};

export default Button;
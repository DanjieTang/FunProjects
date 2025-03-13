import React from 'react';

const Input = ({ 
  label, 
  type = 'text', 
  name, 
  value, 
  onChange, 
  placeholder = '', 
  error = '', 
  required = false 
}) => {
  return (
    <div className="mb-4">
      {label && (
        <label 
          htmlFor={name} 
          className="block text-sm font-medium text-[#1d1d1f] mb-1.5"
        >
          {label} {required && <span className="text-[#ff3b30]">*</span>}
        </label>
      )}
      
      <input
        type={type}
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        required={required}
        className={`
          w-full px-4 py-2.5 rounded-lg border 
          text-[#1d1d1f] placeholder-[#86868b]
          focus:ring-2 focus:ring-[#0071e3] focus:ring-opacity-30 focus:border-[#0071e3] focus:outline-none
          transition duration-150 ease-in-out
          ${error ? 'border-[#ff3b30]' : 'border-[#d2d2d7]'}
          shadow-[inset_0_1px_2px_rgba(0,0,0,0.05)]
        `}
      />
      
      {error && (
        <p className="mt-1.5 text-sm text-[#ff3b30] font-medium">{error}</p>
      )}
    </div>
  );
};

export default Input;
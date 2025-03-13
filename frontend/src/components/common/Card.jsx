import React from 'react';

const Card = ({ 
  children, 
  title = '', 
  subtitle = '', 
  className = '',
  footer = null
}) => {
  return (
    <div className={`
      bg-white rounded-xl overflow-hidden
      shadow-[0_4px_14px_rgba(0,0,0,0.05)]
      backdrop-filter backdrop-blur-sm
      border border-[#e8e8ed]
      ${className}
    `}>
      {(title || subtitle) && (
        <div className="px-7 py-5 border-b border-[#e8e8ed]">
          {title && <h2 className="text-xl font-semibold text-[#1d1d1f] tracking-tight">{title}</h2>}
          {subtitle && <p className="mt-1 text-sm text-[#6e6e73]">{subtitle}</p>}
        </div>
      )}
      
      <div className="px-7 py-6">
        {children}
      </div>
      
      {footer && (
        <div className="px-7 py-4 bg-[#f5f5f7] border-t border-[#e8e8ed]">
          {footer}
        </div>
      )}
    </div>
  );
};

export default Card;
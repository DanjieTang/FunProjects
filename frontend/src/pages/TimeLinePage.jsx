import React from 'react';
import Timeline from '../components/timeline/Timeline';
import { Link } from 'react-router-dom';

const TimelinePage = () => {
  return (
    <div className="py-6 fade-in">
      <div className="mb-6 max-w-6xl mx-auto px-4 flex items-center justify-between">
        <h1 className="text-3xl font-bold text-[#1d1d1f] tracking-tight">Timeline Visualization</h1>
        
        <Link 
          to="/upload" 
          className="bg-[#0071e3] hover:bg-[#0061c3] text-white rounded-lg px-4 py-2 text-sm font-medium transition-colors"
        >
          Upload New Files
        </Link>
      </div>
      
      <Timeline />
    </div>
  );
};

export default TimelinePage;
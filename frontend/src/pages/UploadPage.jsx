import React from 'react';
import FileUpload from '../components/upload/FileUpload';

const UploadPage = () => {
  return (
    <div className="py-8 fade-in">
      <div className="mb-8 text-center">
        <h1 className="text-4xl font-bold text-[#1d1d1f] tracking-tight mb-4">Upload Files</h1>
        <p className="mt-2 text-lg text-[#6e6e73] max-w-2xl mx-auto">
          Upload your Excel files to generate a timeline visualization
        </p>
      </div>
      
      {/* Progress indicator */}
      <div className="max-w-md mx-auto mb-10">
        <div className="flex items-center justify-between">
          <div className="flex flex-col items-center">
            <div className="bg-[#0071e3] text-white w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium">
              1
            </div>
            <div className="text-sm font-medium mt-2 text-[#0071e3]">Upload</div>
          </div>
          
          <div className="flex-1 h-1 bg-gray-200 mx-2">
            <div className="bg-[#0071e3] h-1 w-0"></div>
          </div>
          
          <div className="flex flex-col items-center">
            <div className="bg-[#e8e8ed] text-[#86868b] w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium">
              2
            </div>
            <div className="text-sm font-medium mt-2 text-[#86868b]">Timeline</div>
          </div>
        </div>
      </div>
      
      <FileUpload />
    </div>
  );
};

export default UploadPage;
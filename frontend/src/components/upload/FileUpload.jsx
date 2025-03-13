import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '../common/Button';
import Card from '../common/Card';
import { uploadExcelFiles } from '../../services/api';

const FileUpload = () => {
  const [files, setFiles] = useState([]);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadError, setUploadError] = useState('');
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);
  
  const navigate = useNavigate();
  
  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    validateAndAddFiles(selectedFiles);
  };
  
  const validateAndAddFiles = (selectedFiles) => {
    // Filter for Excel files
    const excelFiles = selectedFiles.filter(file => {
      const fileType = file.type;
      return (
        fileType === 'application/vnd.ms-excel' || 
        fileType === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' ||
        file.name.endsWith('.xlsx') || 
        file.name.endsWith('.xls')
      );
    });
    
    if (excelFiles.length !== selectedFiles.length) {
      setUploadError('Only Excel files (.xlsx, .xls) are allowed.');
    } else {
      setUploadError('');
    }
    
    setFiles(prevFiles => [...prevFiles, ...excelFiles]);
  };
  
  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };
  
  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };
  
  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    
    const droppedFiles = Array.from(e.dataTransfer.files);
    validateAndAddFiles(droppedFiles);
  };
  
  const handleRemoveFile = (index) => {
    const newFiles = [...files];
    newFiles.splice(index, 1);
    setFiles(newFiles);
  };
  
  const handleUpload = async () => {
    if (files.length === 0) {
      setUploadError('Please select at least one Excel file.');
      return;
    }
    
    setIsUploading(true);
    setUploadError('');
    
    try {
      await uploadExcelFiles(files);
      navigate('/timeline');
    } catch (error) {
      setUploadError(error.message || 'Failed to upload files. Please try again.');
    } finally {
      setIsUploading(false);
    }
  };
  
  const openFileSelector = () => {
    fileInputRef.current.click();
  };
  
  return (
    <Card className="max-w-2xl mx-auto">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">Upload Excel Files</h2>
      
      {uploadError && (
        <div className="mb-6 p-3 bg-red-50 text-red-500 rounded-lg text-sm">
          {uploadError}
        </div>
      )}
      
      <div 
        className={`
          border-2 border-dashed rounded-xl p-8 mb-6 text-center cursor-pointer
          ${isDragging ? 'border-blue-500 bg-blue-50' : 'border-gray-300 hover:border-gray-400'}
          transition-colors duration-200
        `}
        onClick={openFileSelector}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          multiple
          accept=".xlsx,.xls"
          className="hidden"
        />
        
        <div className="flex flex-col items-center justify-center">
          <svg 
            className={`w-12 h-12 mb-3 ${isDragging ? 'text-blue-500' : 'text-gray-400'}`} 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24" 
            xmlns="http://www.w3.org/2000/svg"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth="2" 
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
            />
          </svg>
          <p className="text-lg font-medium text-gray-700">
            Drag and drop Excel files here
          </p>
          <p className="text-sm text-gray-500 mt-1">
            or click to browse files
          </p>
        </div>
      </div>
      
      {files.length > 0 && (
        <div className="mb-6">
          <h3 className="text-sm font-medium text-gray-700 mb-2">
            Selected Files ({files.length})
          </h3>
          
          <div className="space-y-2">
            {files.map((file, index) => (
              <div 
                key={`${file.name}-${index}`}
                className="flex items-center justify-between py-2 px-3 bg-gray-50 rounded-lg"
              >
                <div className="flex items-center">
                  <svg 
                    className="w-5 h-5 text-green-500 mr-2" 
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24" 
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth="2" 
                      d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                    />
                  </svg>
                  <span className="text-sm text-gray-700 truncate max-w-xs">
                    {file.name}
                  </span>
                </div>
                
                <button 
                  type="button"
                  onClick={() => handleRemoveFile(index)}
                  className="text-gray-400 hover:text-red-500 transition-colors"
                >
                  <svg 
                    className="w-5 h-5" 
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24" 
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth="2" 
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
      
      <div className="flex justify-end">
        <Button
          variant="primary"
          onClick={handleUpload}
          disabled={isUploading || files.length === 0}
        >
          {isUploading ? 'Uploading...' : 'Next'}
        </Button>
      </div>
    </Card>
  );
};

export default FileUpload;
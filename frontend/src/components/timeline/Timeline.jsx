import React, { useState, useEffect } from 'react';
import { getVisualizationData } from '../../services/api';

const Timeline = () => {
  const [timelineData, setTimelineData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const jsonData = await getVisualizationData();
        
        if (jsonData) {
          processData(jsonData);
        } else {
          setError('No data received from server');
        }
      } catch (error) {
        console.error("Error fetching timeline data:", error);
        setError('Failed to load visualization data. Please try again.');
      } finally {
        setIsLoading(false);
      }
    };
    
    fetchData();
  }, []);
  
  // Function to fix invalid dates
  const fixDateString = (dateStr) => {
    if (!dateStr) return null;
    
    const date = new Date(dateStr);
    if (isNaN(date.getTime())) {
      // Try to fix dates like "2025-09-31" (September only has 30 days)
      const parts = dateStr.split('-');
      if (parts.length !== 3) return null;
      
      const year = parseInt(parts[0]);
      const month = parseInt(parts[1]) - 1; // JS months are 0-based
      
      // Get the last day of the month
      const lastDay = new Date(year, month + 1, 0).getDate();
      const day = Math.min(parseInt(parts[2]), lastDay);
      
      return new Date(year, month, day);
    }
    return date;
  };

  // Process the JSON data into a format optimized for the timeline
  const processData = (jsonData) => {
    try {
      console.log("Processing data:", jsonData);
      
      // Extract all dates to find the min and max for timeline scaling
      const allDates = [];
      
      Object.keys(jsonData).forEach(company => {
        Object.keys(jsonData[company]).forEach(section => {
          jsonData[company][section].forEach(event => {
            const startDate = fixDateString(event["Start Date"]);
            if (startDate) allDates.push(startDate);
            
            const endDate = fixDateString(event["End Date"]);
            if (endDate) allDates.push(endDate);
          });
        });
      });
      
      if (allDates.length === 0) {
        setError('No valid dates found in the data');
        setIsLoading(false);
        return;
      }
      
      // Find min and max dates
      const minDate = new Date(Math.min(...allDates.map(date => date.getTime())));
      const maxDate = new Date(Math.max(...allDates.map(date => date.getTime())));
      
      // Add padding to the date range for better visualization
      minDate.setDate(1); // Start at the beginning of the month
      maxDate.setMonth(maxDate.getMonth() + 1, 0); // End at the end of the month
      
      const totalDays = (maxDate - minDate) / (1000 * 60 * 60 * 24);
      
      // Get all sections across all companies
      const allSections = new Set();
      Object.keys(jsonData).forEach(company => {
        Object.keys(jsonData[company]).forEach(section => {
          allSections.add(section);
        });
      });
      
      // Convert Set to Array and sort alphabetically
      const sections = Array.from(allSections).sort();
      const companies = Object.keys(jsonData);
      
      const formattedData = {
        minDate,
        maxDate,
        totalDays,
        sections: sections.map(sectionName => ({
          name: sectionName,
          companies: companies.map(companyName => ({
            name: companyName,
            events: jsonData[companyName][sectionName] ? 
              jsonData[companyName][sectionName].map(event => ({
                name: event["Event Name"],
                startDate: fixDateString(event["Start Date"]),
                endDate: event["End Date"] ? fixDateString(event["End Date"]) : null,
                isSingleDay: !event["End Date"],
                icon: event["Icon"]
              })).filter(event => event.startDate) : []
          }))
        }))
      };
      
      console.log("Formatted data:", formattedData);
      setTimelineData(formattedData);
    } catch (error) {
      console.error("Error in processData:", error);
      setError('Error processing timeline data. Please check the format.');
      setIsLoading(false);
    }
  };
  
  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-[#6e6e73] flex items-center space-x-3">
          <svg className="animate-spin h-5 w-5 text-[#0071e3]" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span>Loading timeline...</span>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-[#ff3b30] bg-[#ff3b30]/10 px-4 py-3 rounded-lg">
          {error}
        </div>
      </div>
    );
  }
  
  if (!timelineData || !timelineData.sections || timelineData.sections.length === 0) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-[#6e6e73]">No timeline data available. Please upload Excel files first.</div>
      </div>
    );
  }
  
  // Helper functions for positioning and sizing elements on the timeline
  const getPosition = (date) => {
    const days = (date - timelineData.minDate) / (1000 * 60 * 60 * 24);
    return (days / timelineData.totalDays) * 100;
  };
  
  const getWidth = (startDate, endDate) => {
    if (!endDate) return 0;
    const days = (endDate - startDate) / (1000 * 60 * 60 * 24) + 1; // Include end date
    return (days / timelineData.totalDays) * 100;
  };
  
  const formatDate = (date) => {
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  };
  
  // Generate month markers for the timeline
  const getMonthMarkers = () => {
    const markers = [];
    const currentDate = new Date(timelineData.minDate);
    
    while (currentDate <= timelineData.maxDate) {
      markers.push(new Date(currentDate));
      currentDate.setMonth(currentDate.getMonth() + 1);
    }
    
    return markers;
  };

  return (
    <div className="font-sans bg-[#f5f5f7]">
      <div className="max-w-6xl mx-auto bg-white rounded-xl shadow-sm p-8 mb-10">
        <h1 className="text-3xl font-semibold text-[#1d1d1f] mb-10 text-center tracking-tight">Project Timeline</h1>
        
        <div className="space-y-16">
          {timelineData.sections.map((section, sectionIndex) => (
            <div key={section.name} className="bg-[#f5f5f7] rounded-xl p-6">
              <h2 className="text-2xl font-medium text-[#1d1d1f] mb-6 tracking-tight">{section.name}</h2>
              
              <div className="space-y-10">
                {section.companies.map(company => (
                  <div key={`${section.name}-${company.name}`} className="relative">
                    <div className="flex items-center">
                      <div className="w-20 text-right pr-4 text-sm font-medium text-[#6e6e73]">
                        {company.name}
                      </div>
                      
                      <div className="flex-1 relative h-16">
                        {/* Timeline base */}
                        <div className="absolute top-8 w-full h-px bg-[#d2d2d7]"></div>
                        
                        {/* Month markers */}
                        {getMonthMarkers().map((month, idx) => {
                          const position = getPosition(month);
                          return (
                            <div 
                              key={idx}
                              className="absolute top-8 transform -translate-x-1/2"
                              style={{ left: `${position}%` }}
                            >
                              <div className="h-2 w-px bg-[#86868b]"></div>
                              <div className="text-xs text-[#86868b] mt-3">
                                {month.toLocaleDateString('en-US', { month: 'short' })}
                              </div>
                            </div>
                          );
                        })}
                        
                        {/* Events */}
                        {company.events.map((event, idx) => {
                          if (!event.startDate) return null;
                          
                          const position = getPosition(event.startDate);
                          
                          // Colors for the sections - Apple-inspired colors
                          const colors = [
                            "bg-[#0071e3]", // Blue
                            "bg-[#5e5ce6]", // Purple
                            "bg-[#ff3b30]", // Red
                            "bg-[#34c759]", // Green
                            "bg-[#ff9f0a]"  // Orange
                          ];
                          const bgColor = colors[sectionIndex % colors.length];
                          
                          if (event.isSingleDay) {
                            // Single day event (star or circle)
                            return (
                              <div 
                                key={idx}
                                className="absolute top-8 transform -translate-x-1/2 -translate-y-1/2"
                                style={{ left: `${position}%` }}
                              >
                                {event.icon === "star" ? (
                                  <div className="text-[#ff9f0a] text-lg">★</div>
                                ) : (
                                  <div className={`h-4 w-4 rounded-full ${bgColor}`}></div>
                                )}
                                <div className="absolute -top-6 transform -translate-x-1/2 text-xs font-medium text-[#1d1d1f] whitespace-nowrap">
                                  {event.name}
                                </div>
                                <div className="absolute top-5 transform -translate-x-1/2 text-xs text-[#6e6e73] whitespace-nowrap">
                                  {formatDate(event.startDate)}
                                </div>
                              </div>
                            );
                          } else {
                            // Multi-day event (narrow, normal, or wide)
                            const width = getWidth(event.startDate, event.endDate);
                            
                            let height = "h-2"; // normal
                            if (event.icon === "narrow") {
                              height = "h-1";
                            } else if (event.icon === "wide") {
                              height = "h-3";
                            }
                            
                            return (
                              <div 
                                key={idx}
                                className={`absolute top-8 transform -translate-y-1/2 ${height} ${bgColor} rounded-full`}
                                style={{ 
                                  left: `${position}%`, 
                                  width: `${Math.max(width, 0.5)}%` 
                                }}
                              >
                                <div className="absolute -top-6 left-0 text-xs font-medium text-[#1d1d1f] whitespace-nowrap">
                                  {event.name}
                                </div>
                                <div className="absolute top-5 left-0 text-xs text-[#6e6e73] whitespace-nowrap">
                                  {formatDate(event.startDate)}
                                </div>
                                {event.endDate && (
                                  <div className="absolute top-5 right-0 text-xs text-[#6e6e73] whitespace-nowrap">
                                    {formatDate(event.endDate)}
                                  </div>
                                )}
                              </div>
                            );
                          }
                        })}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
        
        <div className="mt-10 text-sm text-[#86868b] text-center">
          Timeline visualization in Apple style
        </div>
      </div>
    </div>
  );
};

export default Timeline;
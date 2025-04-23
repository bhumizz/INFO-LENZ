import React, { useState, useEffect } from 'react';
import Papa from 'papaparse';
import './light-trend.css';
import './dark-trend.css';

const Trend = () => {
  const [headlines, setHeadlines] = useState([]);

  useEffect(() => {
    const fetchHeadlines = () => {
      Papa.parse('/manual_testing.csv', {
        download: true,
        header: true,
        complete: ({ data }) => {
          const parsedHeadlines = data.map((row) => ({
            headline: row.title,
            content: row.text || '',
          }));
          setHeadlines(parsedHeadlines);
        },
      });
    };
    fetchHeadlines();
  }, []);

  const handleSelectHeadline = (headline, content) => {
    const isDarkMode = document.body.classList.contains('dark-mode');
    const themeLink = isDarkMode ? 'dark-trend.css' : 'light-trend.css';
    
    const newWindow = window.open(`article.html?headline=${encodeURIComponent(headline)}&content=${encodeURIComponent(content)}`, '_blank');
    
    newWindow.onload = () => {
      const themeLinkElement = newWindow.document.getElementById('theme-style');
      
      if (themeLinkElement) 
      themeLinkElement.href = themeLink;
      
    };
  };

  return (
    <div className="trend-container">
      <div className="trend-header">Trending News</div>
      <div className="headline-list">
        {headlines.map((item, index) => (
          <div
            key={index}
            className="trend-item"
            onClick={() => handleSelectHeadline(item.headline, item.content)}
          >
            {item.headline}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Trend;

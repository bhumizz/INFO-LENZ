import React, { useState } from 'react';
import './dark-widget.css';
import './light-widget.css';

const Widget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [expandedFAQ, setExpandedFAQ] = useState(null);

  const toggleWidget = () => setIsOpen((prev) => !prev);

  const toggleFAQ = (index) => {
    setExpandedFAQ((prev) => (prev === index ? null : index));
  };

  const faqs = [
    { question: "What is this web app about?", answer: "This app provides trending news and checks the authenticity of news using AI tools." },
    { question: "How does the app decide which news is trending?", answer: "It tracks engagement, shares, and mentions across online platforms and social media." },
    { question: "Can I use this app for free?", answer: "Yes, the app is free for browsing news and checking authenticity. Advanced features may require payment." },
    { question: "How frequently is the news updated?", answer: "The news feed updates every few minutes to show the latest trends." },
    { question: "How does the fake news detection feature work?", answer: "The app uses AI to analyze text, source credibility, and corroboration with trusted sources." },
    { question: "Does the fake news detector support all languages?", answer: "Currently, it supports select languages, with more being added soon." },
    { question: "What happens if the tool flags a trending news story as fake?", answer: "The story is flagged with a warning message based on the analysis results." },
    { question: "Can I share news articles with others?", answer: "Yes, articles can be shared via social media or direct links using the 'Share' button." }
  ];

  return (
    <div className={`fun-widget ${isOpen ? 'open' : ''}`} onClick={toggleWidget}>
      <div className="widget-icon">
        <span role="img" aria-label="detective">🕵️‍♂️</span>
      </div>
      
      {isOpen && (
        <div className="widget-content" onClick={(e) => e.stopPropagation()}>
          <h1 className="widget-title">FAQ's!!</h1>
          <div className="faq-container">
            {faqs.map((faq, index) => (
              <div key={index} className="faq-item">
                <div className="faq-question" onClick={() => toggleFAQ(index)}>
                  {faq.question}
                  {expandedFAQ === index && (
                  <div className="faq-answer">
                    {faq.answer}
                  </div>
                )}
                </div>
                
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default Widget;

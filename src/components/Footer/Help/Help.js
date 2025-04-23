import React from "react";
import "./Help.css";

const Help = () => {
  return (
    <div className="Help">
      <h1>Help & Support</h1>
      <h2>How can we assist you?</h2>
      
      <p>
        Welcome to our Help section! Whether you have questions about navigating the site,
        using our features, or troubleshooting issues, we are here to provide guidance.
      </p>
      
      <h3>Popular Topics:</h3>
      <ul>
        <li><strong>How to access latest news</strong> - Easily find the trending news on our homepage.</li>
        <li><strong>Fake News Detection</strong> - Understand how our AI-driven tool helps verify news authenticity.</li>
        <li><strong>Creating an account</strong> - Step-by-step guide to create and personalize your news feed.</li>
        <li><strong>Contacting support</strong> - Reach out to us for more personalized help via the <a href="/Contactus">CONTACT</a> page.</li>
      </ul>
      
      <p>
        If you have additional questions or need further assistance, feel free to get in touch
        with our support team. We’re here to help!
      </p>
    </div>
  );
};

export default Help;

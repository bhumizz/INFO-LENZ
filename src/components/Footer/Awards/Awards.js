import React from "react";
import "./Awards.css";

const Awards = () => {
  return (
    <div className="Awards">
      <h1>AWARDS AND RECOGNITION</h1>
      <h3>Excellence in Journalism and Innovation</h3>

      <ul className="achievements-list">
        <li><strong>Best Investigative Journalism Award (2023)</strong> - For our in-depth reporting on corruption in high-profile government sectors.</li>
        <li><strong>Fake News Prevention Leader Award (2022)</strong> - Recognized for integrating AI-powered fake news detection technology into our platform.</li>
        <li><strong>Innovative Media Solutions Award (2021)</strong> - Acknowledged for pioneering digital storytelling with data visualization and interactive content.</li>
        <li><strong>Community Impact Award (2019)</strong> - Celebrated for significant contributions to informing the public during the pandemic.</li>
      </ul>

      <p className="closing">
        These awards highlight our dedication to truth and transparency. We are grateful for the continued support and trust of our audience.
      </p>
      
    </div>
  );
};

export default Awards;

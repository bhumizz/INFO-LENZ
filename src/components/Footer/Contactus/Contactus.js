import React from "react";
import "./Contactus.css";

const Contactus = () => {
  return (
    <div className="Contactus">
      <h1>Contact Us</h1>
      <h2>We're Here to Help</h2>

      <p>
        Have questions or need assistance? Our team is ready to assist you 24/7.
        Reach out to us through any of the contact details below.
      </p>

      <h3>Contact Information</h3>
      <ul>
        <li><strong>Email:</strong> support@newswebsite.com</li>
        <li><strong>Phone:</strong> +1 (800) 123-4567</li>
        <li><strong>Address:</strong> 123 News Street, Media City, NY 12345</li>
      </ul>

      <p>
        You can also visit our <a href="/help">HELP</a> page for frequently asked questions.
      </p>
    </div>
  );
};

export default Contactus;

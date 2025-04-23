import React from "react"
import './light-footer.css';
import './dark-footer.css';
import { Link } from "react-router-dom"; 
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';

const Footer = () => {
  return (
    <>
        < div className='container'>

            <div className="footernav1">

                <div className="info">
                    
                    <Link to="/">HOME</Link>
                    <Link to="/Aboutus">ABOUT US</Link>
                    <Link to="/Awards">AWARDS</Link> 
                    <Link to="/Help">HELP</Link> 
                    <Link to="/Contactus">CONTACT US</Link>
                
                </div>
            </div>

            <div className="footernav2">
                
                <div className="socials">
                    <a href="https://facebook.com" > <FaFacebook  className="social-icon"/> </a>
                    <a href="https://twitter.com"  > <FaTwitter   className="social-icon"/> </a>
                    <a href="https://instagram.com"> <FaInstagram className="social-icon"/> </a>
                </div>

                <div className='legal'>
                    <p>© all rights reserved</p>
                    <p>made with &#10084; at JIIT</p>
                </div>

            </div>

        </div>      
   
    </>
  )
}

export default Footer
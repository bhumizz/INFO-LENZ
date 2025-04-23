import React, { useEffect, useState } from 'react';
import './SidePanel.css'; 

const SidePanel = () => {
    const [isVisible, setIsVisible] = useState(false);
    const [isGlidingOut, setIsGlidingOut] = useState(false);

    const handleMouseMove = (e) => {
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;

        if (e.clientX > 0.8 * windowWidth && e.clientY > 0.4 * windowHeight && e.clientY < 0.6 * windowHeight) {
            if (!isVisible) {
                setIsVisible(true);
            }
        }
        
    };

    const handleMouseLeave = (e) => {
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;
        
        if (isVisible)
        setIsVisible(false);
    
    };

    useEffect(() => {
        window.addEventListener('mousemove', handleMouseMove);

        return()=>{
            window.removeEventListener('mousemove',handleMouseMove);
        }
    }, []);


    return(
        
        < div className={`side-panel ${isVisible && 'visible' } ${isGlidingOut && 'gliding-out'}`} onMouseLeave={handleMouseLeave}>
            
            <div className="trending">
                <h2>Trending Now</h2>
                <ul>
                    <li>Breaking News: Major Earthquake in Region</li>
                    <li>New Study on Climate Change Impacts</li>
                    <li>Upcoming Elections: What You Need to Know</li>
                </ul>
            </div>
            

            <div className="poll">
                <h2>Participate</h2>
                <p>What do you think about the new education policy?</p>
                <h3>VOTE NOW !</h3>
            </div>
            
            <div className="subscription">
                <h2>Subscribe</h2>
                <p>Stay updated with the latest news!</p>
                <input type="email" placeholder="Enter your email" />
                <hr />
                <button>Subscribe </button>
            </div>
            
            
        </div>
    );
};

export default SidePanel;

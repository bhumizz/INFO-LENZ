import './light-card.css';
import './dark-card.css';

const Card=({data})=>{
    const altImage = "https://mediaengagement.org/wp-content/uploads/2022/12/News-Desert-Web-Tile-1.png";

    // Check if data is undefined or not an array, and provide a fallback
    if (!Array.isArray(data) || data.length === 0) {
        return <div className="empty-page">NO DATA AVAILABLE :( </div>; // Or return null or a loading state
    }

    return (
        <div className="cardcontainer">

           {data.map((currelement,index,data) => {
           
           if (currelement.title!='[Removed]')
           return (

                <div className="card" key={index}> 

                    <img src={currelement.urlToImage ? currelement.urlToImage : altImage} alt={currelement.title}/>
                    <div className="cardcontent">

                        <a href={currelement.title} onClick={()=>window.open(currelement.url)}>{currelement.title}</a>
                        <p>{currelement.description}  </p>
                        <button onClick={()=>window.open(currelement.url)}>READ MORE</button>
        
                    </div> 
                
                </div>

           );
           
           })}

        </div>
    );
}

export default Card;

import profilePic from "./assets/1661402554732.jpeg"

function Card(){
    return(
        <div className="card">
            <img alt="Danjie's LinkedIn Picture" src={profilePic}></img>
            <h2>Danjie Tang</h2>
            <p>Apple EPM</p>
        </div>
    );
}

export default Card
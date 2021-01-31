import React from 'react';

const DisplayItem = (props) => {
    return(
        <tr>
            <td>
                <div className="item">
                    <img src={props.item.image} alt={props.item.album + " picture"} className="image"></img>
                    <div className="column">
                        <p style={{fontSize : "30px"}}> {props.item.name} </p>
                    </div>
                    <div className="row">
                        <p style={{fontSize : "25px"}}>{props.item.artist}</p>
                    </div>
                </div>
            </td>
        </tr>
    );
}

export default DisplayItem;
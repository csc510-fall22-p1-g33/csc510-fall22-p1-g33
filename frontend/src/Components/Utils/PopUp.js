import React from "react";
import './style.css'
 
const Popup = props => {
  return (
    <div className="popup-box">
      <div className="box">
        <span className="close-icon" onClick={() => props.handleClose(false)}>x</span>
        {props.content}
      </div>
    </div>
  );
};
 
export default Popup;
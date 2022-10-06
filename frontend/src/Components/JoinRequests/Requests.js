import React, { Component } from "react";
// import Popup from 'reactjs-popup';
// import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";
import PopUp from '../Utils/PopUp'
import { TextField } from '@mui/material';

const options = [
    {
        label: "Accept",
        value: "accept",
    },
    {
        label: "Reject",
        value: "reject",
    }
];

// dummy users details 
const tableData = [
    {
        fullName: "Ryan",
        emailAddress: "r@gmail.com",
        projectName: "Pokemon",
        memberNeeded: 2,
        project: {
            id: 0,
            projectName: "Pokemon",
            members: {
                '0': 'udith',
                '1': 'aneesh',
                '3': 'ryan'
            }
        }
    },
    {
        fullName: "Aneesh",
        emailAddress: "a@gmail.com",
        projectName: "Team Formation Tool",
        memberNeeded: 1,
        project: {
            id: 1,
            projectName: "Pokemon",
            members: {
                '0': 'udith',
                '1': 'aneesh',
            }
        }
    },
    {
        fullName: "Udith",
        emailAddress: "u@gmail.com",
        projectName: "N/A",
        memberNeeded: 3,
        project: {
            id: 2,
            projectName: "N/A",
            members: ""
        }
    }
];

class Requests extends Component {
    constructor(props) {
        super(props);

        this.state = {
            isOpen: false,
            comments: ''
          };
      
        this.togglePopup = this.togglePopup.bind(this);
        this.setComments = this.setComments.bind(this);
    }

    togglePopup = (val) => {
        this.setState({isOpen: val});
        this.state.isOpen = val;
    }

    setComments = (e) => {
        console.log ("comments:", e)
        this.setState({comments: e});
        this.state.comments = e;
    }


    render() {
        return (
        <div>
            
            <div style={{marginLeft: '5%', marginTop: '5%'}}>

                {/* show project member details in a table */}
                <table className="table">
                    <thead>
                        <tr>
                            <th>User Name</th>
                            <th>Project Name</th>
                            <th>Request</th>
                            
                        </tr>
                    </thead>
                    <tbody>
                    {tableData.map((data, index)=> {
                        return (  
                            <tr key={index}>    
                            <td>{data.fullName}</td>
                            <td>{data.projectName}</td>
                            
                            <td><input
                                type="button"
                                value="Accept/Reject"
                                onClick = {() => this.togglePopup (!this.state.isOpen)}
                                style={{backgroundColor: '#0F3856', color: 'white'}}
                                /></td>
                            </tr>  
                            )
                        })
                    }             
                    </tbody>
                </table>

                {this.state.isOpen && <PopUp 
                    content={<>
                        <b style={{
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                        }}>
                            Confirm accept/reject request
                        </b>

                        <p>Add your comment/message below.</p>

                        <TextField
                            id="standard-textarea"
                            // label="Multiline Placeholder"
                            placeholder="Type here"
                            multiline
                            variant="standard"

                            value={this.state.comments}
                            label="Message"
                            onChange={(e) => {
                            this.setComments(e.target.value);
                            }}
                        />
                        {/* <h3>Your Enter Value is: {this.state.comments} </h3> */}
                        
                        <p style={{ marginTop: 10, textAlign: 'left', marginLeft: 16, marginBottom: '5%' }}>
                        <select  style={{ marginLeft: 13, borderRadius: 5, float: 'right'}}>{options.map((options) => (
                                <option value={options.value}>{options.label}</option>
                            ))}
                        </select>
                        </p>
                        
                        <button onClick={() =>this.togglePopup (false)} style={{float: 'right'}}>Confirm</button>
                    </>}
                    handleClose={this.togglePopup}
                />}

                {/* click this to go back to the dashboard page */}
                {/* <Link className="btn btn-primary" to="/dashboard"  style={{marginLeft: '25%'}}> Back to Dashboard </Link> */}
            </div>
        </div>
    )
}
}

export default Requests;

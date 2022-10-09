import React, { Component } from "react";
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
            comments: '',
            requests_sent_ids:  null,
            requests_sent: [],
            requests_received: []
          };
      
        this.togglePopup = this.togglePopup.bind(this);
        this.setComments = this.setComments.bind(this);
    }

    async componentDidMount () {
        console.log ("Loading sent requests")

        const res = await fetch('http://127.0.0.1:8010/proxy/user/'+this.props.user_id, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })
        
        const body = await res.json();
        console.log (body.user.join_requests)

       
        this.setState ({requests_sent_ids: body.user.join_requests})
        this.state.requests_sent_ids = body.user.join_requests

        let reqs_count = this.state.requests_sent_ids.length
        let req_list = []
        if (reqs_count > 0) {
            let i = 0
            for (i=0; i<reqs_count; i++) {
                const res2 = await fetch('http://127.0.0.1:8010/proxy/joinrequest/'+this.state.requests_sent_ids[i], {
                    method: 'GET',
                    headers: {
                        Accept: 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    }
                })
                const body2 = await res2.json();
                console.log (body2.join_request)
                if (body2.join_request.user != this.props.user_id)
                    req_list.push(body2.join_request)
                else {
                    console.log (this.props.user_id, body2.join_request.user)
                }
            }
            if (req_list.length > 0) {
                
                this.setState({requests_sent: req_list})
                this.state.requests_sent = req_list
            }

            console.log ( this.state.requests_sent)
        }
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
                Your sent requests: {this.state.requests_sent.length}
                {
                    this.state.requests_sent.length > 0 &&
                    <div>
                        <table className="table">
                    <thead>
                        <tr>
                            <th>Request No</th>
                            <th>Team No</th>
                            <th>Status</th>
                            
                        </tr>
                    </thead>
                    <tbody>
                    {this.state.requests_sent.map((data, index)=> {
                        return (  
                            <tr key={index}>   
                            <td>{index}</td> 
                            <td>{data.team}</td>
                            <td>{data.status}</td>
                            </tr>  
                            )
                        })
                    }             
                    </tbody>
                </table>
                    </div>
                }

                <br></br> <br></br>
                Your received requests: {this.state.requests_received.length}

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
            </div>
        </div>
    )
}
}

export default Requests;

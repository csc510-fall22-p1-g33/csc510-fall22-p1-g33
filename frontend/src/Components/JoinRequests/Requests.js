import React, { Component } from "react";
import { Link } from "react-router-dom";
import PopUp from '../Utils/PopUp'
import { TextField } from '@mui/material';

const options = [
    {
        label: "accept",
        value: "accept",
    },
    {
        label: "reject",
        value: "reject",
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
            requests_received_ids:  null,
            requests_received: [],
            team_id: null,
            is_accepted: "accept"
          };
      
        this.togglePopup = this.togglePopup.bind(this);
        this.setComments = this.setComments.bind(this);
        this.set_accepted = this.set_accepted.bind (this)
        this.confirmed = this.confirmed.bind (this)
    }

    // load all the join requests sent by this user
    // then, all the incoming join requests to this logged in user
    async componentDidMount () {
        // console.log ("Loading sent requests")

        const res = await fetch('http://127.0.0.1:8010/proxy/user/'+this.props.user_id, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })
        
        const body = await res.json();
        // console.log ("user_id:", this.props.user_id, "reqs:", body.user.join_requests, "teams:", body.user.teams)

        if (body.user.teams.length > 0){
            this.setState ({team_id: body.user.teams[0]})
            this.state.team_id = body.user.teams[0]
        }

       
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
                if (this.state.team_id != body2.join_request.team)
                    req_list.push(body2.join_request)
            }
            if (req_list.length > 0) {
                
                this.setState({requests_sent: req_list})
                this.state.requests_sent = req_list
            }

            // console.log ("user_id:", this.props.user_id)
            // console.log ( "reqs sent:", this.state.requests_sent)
        }


        // ----------------------------------------------------
        // console.log ("Loading received requests")

        if (this.state.team_id != null) {
            const res2 = await fetch('http://127.0.0.1:8010/proxy/joinrequest/received?user='+this.props.user_id+'&team='+this.state.team_id, {
                method: 'GET',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
                })
                
                const body2 = await res2.json();
                console.log (body2)

                this.setState ({requests_received: body2})
                this.state.requests_received = body2

                // his.setState ({requests_received_ids: body2.join_request})
                // this.state.requests_received = body2.join_request
        }
        else {
            console.log ("user id", this.props.user_id, "has not created any team yet.")
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

    set_accepted = (e) => {
        console.log ("is_accepted:", e.target.value)
        this.setState({is_accepted: e.target.value});
        this.state.is_accepted = e.target.value;
    }


// after submitting confirm, call the accept or reject joinrequest patch to change the status of the request
    confirmed = async (uid, jid, status) => {
        // console.log ("confirming -- who_sent -- req_id -- status")
        // console.log (uid, jid, status)

        if (this.state.is_accepted == 'accept') {
            const res3 = await fetch('http://127.0.0.1:8010/proxy/joinrequest/'+jid+'/'+status, {
                method: 'PATCH',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
                })
                
                const body3 = await res3.text();
                console.log (body3)
        }
        else if (this.state.is_accepted == "reject") {
            const res3 = await fetch('http://127.0.0.1:8010/proxy/joinrequest/'+jid+'/reject', {
                method: 'PATCH',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
                })
                
                const body3 = await res3.text();
                console.log (body3)
        }
        this.togglePopup (false)
        this.componentDidMount()
    }



    render() {
        return (
        <div>
            
            <div style={{marginLeft: '5%', marginTop: '5%'}}>

                {/* show project member details in a table */}
                <b>Your sent requests: {this.state.requests_sent.length}</b>
                <br></br><br></br>
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

                <br></br><br></br><br></br>
                <b>Your team received requests: {this.state.requests_received.length}</b>
                <br></br><br></br>

                {this.state.requests_received.length > 0 && 
                this.state.requests_received.map((data, index)=> {
                    return (
                        <div>
                        {data.join_request.status == "accepted" && 
                            <p>{data.join_request.who_sent_uname} is in your team now!</p>
                        }

                                {/* <input
                                type="button"
                                value="Leave this team"
                                onClick={() => this.leave_from_team ()}
                                style={{backgroundColor: 'red', color: 'white', marginLeft: '2%'}}
                                /> */}
                        </div>
                    )
                })}
                <br></br>

                {this.state.requests_received.length > 0 &&
                    <div>
                        <table className="table">
                    <thead>
                        <tr>
                            <th>User Name</th>
                            <th>Status</th>
                            <th>Request</th>
                            
                        </tr>
                    </thead>
                    <tbody>

                    
                    {this.state.requests_received.map((data, index)=> {

                        if (data.join_request.status != "accepted")
                        return (  
                            
                            <tr key={index}>    
                            <td>{data.join_request.who_sent_uname}</td>
                            <td>{data.join_request.status}</td>
                            

                            <td>
                                
                                {/* {data.join_request.status == 'pending' && <input
                                type="button"
                                value="accept/reject"
                                onClick = {() => this.togglePopup (!this.state.isOpen)}
                                style={{backgroundColor: '#0F3856', color: 'white'}}
                                />} */}

                                {data.join_request.status == 'rejected' && <input
                                type="button"
                                value={data.join_request.status}
                                style={{backgroundColor: 'red', color: 'white'}}
                                />}

                                {data.join_request.status == 'accepted' && <input
                                type="button"
                                value={data.join_request.status}
                                style={{backgroundColor: 'green', color: 'white'}}
                                />}


                                {data.join_request.status == "pending" && 
                                    <div>
                                        <button onClick={() =>this.confirmed (data.join_request.who_sent_id, data.join_request.req_id, "accept")} 
                                        >Accept</button>

                                        <button onClick={() =>this.confirmed (data.join_request.who_sent_id, data.join_request.req_id, "reject")} 
                                        style={{marginLeft: '2%'}}
                                        >Reject</button>
                                    </div>
                                }
                                
                                
                                </td>
                            </tr>  
                            )
                        })
                    }             
                    </tbody>
                </table>
                    </div>
                }
            </div>
        </div>
    )
}
}

export default Requests;

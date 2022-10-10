import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";
import PopUp from '../Utils/PopUp'


class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            currentProjects: null,
            entries: [],
            loaded: false,
            already_teamed: false,
            popup: false,
            sent: false
        }
        this.handleViewProject = this.handleViewProject.bind(this);
        this.handleProjects = this.handleProjects.bind(this);
        this.toggle_loaded = this.toggle_loaded.bind(this);
        this.send_request = this.send_request.bind(this)
        this.togglePopup = this.togglePopup.bind(this)
    }


    // at the beginning, all the projects will be loaded here
    async componentDidMount() {
        console.log("Loading project data")

        const res = await fetch('http://127.0.0.1:8010/proxy/project/dashboard', {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })

        const body = await res.json();
        // console.log (body)

        this.handleProjects(body)
        this.toggle_loaded(true)
    }

    // set the loaded attribute to true if all the data have been loaded
    toggle_loaded = (e) => {
        this.setState({ loaded: e })
        this.state.loaded = e
    }

    // set current projects in the state after loading
    handleProjects = (e) => {
        this.setState({ currentProjects: e })
        this.state.currentProjects = e;
        console.log('Project IDs SET:', this.state.currentProjects)
    }

    // if you click on view details for a project, 
    // this function passes the project id to its parent App.js
    handleViewProject = (e) => {
        this.props.setProjectID(e)
        this.props.onRouteChange("project", e);
    }

    togglePopup = (val) => {
        this.setState({ popup: val });
        this.state.popup = val;
    }

    // if the currently logged in user doesn't have a team, it's possible to send a new request to another team
    // using a project id and team id, a user can submit a join request 
    send_request = async (e) => {

        // check if the user is in already in a team
        const res_1 = await fetch('http://127.0.0.1:8010/proxy/user/' + this.props.user_id, {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })

        const body_1 = await res_1.json();
        console.log("user_id:", this.props.user_id, "reqs:", body_1.user.join_requests, "teams:", body_1.user.teams)

        if (body_1.user.teams.length > 0) {
            this.setState({ already_teamed: true })
            this.state.already_teamed = true

            this.setState({ popup: true })
            this.state.popup = true
        }
        else {
            const res0 = await fetch('http://127.0.0.1:8010/proxy/project/' + String(e), {
                method: 'GET',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            })

            const body0 = await res0.json();
            console.log('sending req for project id:', body0.project.id)

            if (body0.project.teams.length > 0) {
                console.log('sending req for team id:', body0.project.teams[0])

                const res5 = await fetch('http://127.0.0.1:8010/proxy/joinrequest/', {
                    method: 'POST',
                    headers: {
                        Accept: 'application/json',
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    },
                    body: JSON.stringify({
                        creator: this.props.user_id,
                        team: body0.project.teams[0]
                    })
                })

                const body5 = await res5.json();
                console.log(body5)

                this.setState({ sent: true })
                this.state.sent = true
            }
            else {
                console.log("There is no team formed for this project.")
            }
        }
    }

    render() {
        return (
            // this is a table showing all available users, their project name, already teamed up member count
            <table className="table" style={{ marginTop: '5%' }}>
                <thead>
                    <tr>
                        <th>Project Name</th>
                        <th>Team/Project Creator</th>
                        <th>#Existing Team Members</th>
                        <th>Join Team</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.loaded && this.state.currentProjects != null &&
                        this.state.currentProjects.map((data, index) => {
                            return (
                                <tr key={index}>
                                    {/* <td>{index+1}</td> */}
                                    <td>{data.pname}
                                        <br></br>
                                        <Link className="btn btn-primary" style={{ height: '50%', width: '40%', marginTop: '2%' }} to="/project" onClick={() => this.handleViewProject(data.pid)}> View Details </Link> </td>

                                    <td>{data.user_list.map((data2, index2) => {
                                        return (
                                            <div>{data2[1]}</div>
                                        )
                                    })}
                                    </td>

                                    <td>{data.user_list.length} </td>

                                    <td>
                                        {/* <br></br> */}
                                        <Link onClick={() => { this.send_request(data.pid) }} className="btn btn-primary" style={{ width: '60%' }}> Send Request </Link>
                                        {this.state.popup &&


                                            <PopUp
                                                content={<>
                                                    <b style={{
                                                        display: 'flex',
                                                        alignItems: 'center',
                                                        justifyContent: 'center',
                                                    }}>
                                                        You have already teamed up!
                                                    </b>

                                                </>}
                                                handleClose={this.togglePopup}
                                            />}


                                        {this.state.sent &&
                                            <PopUp
                                                content={<>
                                                    <b style={{
                                                        display: 'flex',
                                                        alignItems: 'center',
                                                        justifyContent: 'center',
                                                    }}>
                                                        Your request has been sent!
                                                    </b>

                                                </>}
                                                handleClose={() => {
                                                    this.setState({ sent: false })
                                                    this.state.sent = false
                                                }}
                                            />}

                                    </td>


                                </tr>
                            )
                        })
                    }
                </tbody>
            </table>
        )
    }
}

export default Dashboard;

// https://www.geeksforgeeks.org/how-to-create-popup-box-in-reactjs/
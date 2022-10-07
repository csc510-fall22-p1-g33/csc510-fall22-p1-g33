import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";

class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            currentProjects: null,
            entries: [],
            loaded: false
        }
        this.handleViewProject = this.handleViewProject.bind(this);
        this.handleProjects = this.handleProjects.bind (this);
        this.toggle_loaded = this.toggle_loaded.bind (this);
      }


    async componentDidMount () {
        console.log ("Loading project data")

        const res = await fetch('http://127.0.0.1:8010/proxy/project/dashboard', {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })
        
        const body = await res.json();
        console.log (body)

        this.handleProjects (body)
        
        this.toggle_loaded (true)

    }

    toggle_loaded = (e) => {
        this.setState ({loaded: e})
        this.state.loaded = e
    }

    handleProjects = (e) => {
        this.setState ({currentProjects: e})
        this.state.currentProjects = e;
        console.log ('Project IDs SET:', this.state.currentProjects)
    }

    // if you click on view details for a project, 
    // this function passes the project id to its parent App.js
    handleViewProject = (e) => {
    this.props.setProjectID (e)
    this.props.onRouteChange("project", e);
    }

    render() {
        return (
        // this is a table showing all available users, their project name, already teamed up member count
        <table className="table" style={{marginTop: '5%'}}>
            <thead>
                <tr>  
                    <th>Project Name</th>
                    <th>Member Usernames</th>
                    <th>#Existing Team Members</th>
                    <th>Join Team</th>
                </tr>
            </thead>
            <tbody>
            { this.state.loaded && this.state.currentProjects != null &&
                this.state.currentProjects.map((data, index)=>{
                    return(
                        <tr key={index}>
                            {/* <td>{index+1}</td> */}
                            <td>{data.pname}
                            <br></br>
                            <Link  className="btn btn-primary" style={{height: '50%', width: '40%', marginTop: '2%'}} to="/project" onClick={() => this.handleViewProject(data.pid)}> View Details </Link> </td>

                            <td>{data.user_list.map((data2, index2)=>{
                                return (
                                <div>{data2[1]}</div>
                                )} )}
                            </td>

                            <td>{data.user_list.length} </td>
                        
                            <td>
                            {/* <br></br> */}
                            <Link  className="btn btn-primary" style={{width: '60%'}}> Send Request </Link> </td>
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
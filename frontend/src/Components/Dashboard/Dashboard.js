import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";

// dummy available users data
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

class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            currentProject: ''
        }
        this.handleViewProject = this.handleViewProject.bind(this);
      }

    // if you click on view details for a project, 
    // this function passes the project id to its parent App.js
    handleViewProject = (e) => {
    this.props.onRouteChange("project", e);
    }

    render() {
        return (
        // this is a table showing all available users, their project name, already teamed up member count
        <table className="table" style={{marginTop: '5%'}}>
            <thead>
                <tr>
                    <th>Full Name</th>
                    <th>Email Address</th>
                    <th>Project</th>
                    <th>Team Member Required</th>
                    <th>Add Member</th>
                </tr>
            </thead>
            <tbody>
            {
                tableData.map((data, index)=>{
                    return(
                        <tr key={index}>
                            {/* <td>{index+1}</td> */}
                            <td>{data.fullName}</td>
                            <td>{data.emailAddress}</td>
                            <td>{data.projectName} 
                            <br></br>
                            <Link  className="btn btn-primary" style={{height: '50%', width: '40%', marginTop: '2%'}} to="/project" onClick={() => this.handleViewProject(data.project.id)}> View Details </Link> </td>
                            <td>{data.memberNeeded}</td>
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
import React, { Component } from "react";
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";

// dummy project details for a dummy project id
const projectData = [{
    projectId: 0,
    projectName: "Pokemon",
    members: {
        '0': 'udith',
        '1': 'aneesh',
        '3': 'ryan'
    },
    about: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sollicitudin nisi semper accumsan fermentum. Aenean tristique mauris sit amet nisi dictum, id dapibus nisl tempus. Ut ac tellus eros. Sed eu lacus non diam interdum facilisis. Mauris et dolor porta, facilisis orci sit amet, dapibus ipsum. Fusce vel nisl ac orci vestibulum scelerisque in ut nulla. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed iaculis elit ut aliquam facilisis. Pellentesque sed sodales risus. Nunc nisi enim, fringilla ac libero in, volutpat iaculis ligula. Nulla vel lorem justo. Etiam interdum ante luctus tortor consequat cursus. Fusce nec nibh in augue scelerisque porttitor quis in nulla. Curabitur varius elit lacus, ut bibendum lorem hendrerit vitae. Curabitur hendrerit vestibulum ligula, eu cursus quam interdum quis. Integer turpis erat, aliquam eget venenatis et, gravida sit amet lectus.",
}]
    

class Project extends Component {
    constructor(props) {
        super(props);
        this.state = {
            description: "",
            name: "",
            id: null,
            teams: null,
            users: null
        }
      }

      async componentDidMount () {
        console.log ("Loading a project")

        const res = await fetch('http://127.0.0.1:8010/proxy/project/'+this.props.projectID, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })
        
        const body = await res.json();
        console.log (body.project.about)

        let res2, body2, uname;
        let uname_list = []

        let i;

        for (i=0; i<body.project.users.length; i++){

            res2 = await fetch('http://127.0.0.1:8010/proxy/user/'+body.project.id, {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
            })
        
        try {
            body2 = await res2.json();
            console.log (body2)
        }
        catch (e) {
            console.log (e)
        }
        uname = body2.user.username
        console.log (uname)
        uname_list.push (uname)
        }
        console.log ("uname list:", uname_list)

        this.setState({
            name: body.project.about.name,
            description: body.project.about.description,
            id: body.project.id,
            teams: body.project.teams,
            users: uname_list
        })

        this.state.name = body.project.about.name
        this.state.description = body.project.about.description
        this.state.id = body.project.id
        this.state.teams = body.project.teams
        this.state.users = uname_list

    }


    render() {
        return (
        <div>
           
                    <div style={{marginLeft: '5%', marginTop: '5%'}}>
                        {/* project name and description */}
                        Project Name: {this.state.name}
                        <br></br><br></br>
                        Project Description: {this.state.description}
                        <br></br><br></br>

                        {/* show project member details in a table */}
                        <table className="table">
                            <thead>
                                <tr>
                                    <th>Member No</th>
                                    <th>Name</th>
                                    <th>Details</th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                            {
                                this.state.users == null ? <p>No team formed</p>: 
                                Object.keys(this.state.users).map((key, index) =>{
                                    return(
                                        <tr key={index+1}>
                                            <td>{index+1}</td>
                                            <td>{this.state.users[key]}</td>
                                            <td><Link className="btn btn-primary" style={{height: '50%', width: '20%', marginTop: '-.2%'}}> View Profile </Link></td>
                                            
                                        </tr>
                                    )
                                })
                            }
                            </tbody>
                        </table>

                        {/* click this to go back to the dashboard page */}
                        <Link className="btn btn-primary" to="/dashboard"  style={{width: '15%', float: 'right', marginRight: '5%'}}> Back to Dashboard </Link>
                    </div>
              
           
        </div>
    )
}
}

export default Project;

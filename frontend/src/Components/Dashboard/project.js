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
      }

    render() {
        return (
        <div>
            {projectData.map((data, index)=> {
                return (
                    <div style={{marginLeft: '5%', marginTop: '5%'}}>
                        {/* project name and description */}
                        Project Name: {data.projectName}
                        <br></br><br></br>
                        Project Description: {data.about}
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
                                data.members == ""? <p>No team formed</p>: 
                                Object.keys(data.members).map((key, index) =>{
                                    return(
                                        <tr key={index+1}>
                                            <td>{index+1}</td>
                                            <td>{data.members[key]}</td>
                                            <td><Link className="btn btn-primary"> View Profile </Link></td>
                                            
                                        </tr>
                                    )
                                })
                            }
                            </tbody>
                        </table>

                        {/* click this to go back to the dashboard page */}
                        <Link className="btn btn-primary" to="/dashboard"  style={{marginLeft: '25%'}}> Back to Dashboard </Link>
                    </div>
                )})
            }
        </div>
    )
}
}

export default Project;

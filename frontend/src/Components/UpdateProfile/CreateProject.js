import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";
import { TextField } from '@mui/material';
    

class Project extends Component {
    constructor(props) {
        super(props);
        this.state = {
            p_id: "",
            id: "",
            creator: "",

            projectTitle: "",
            projectDetails: "",

            saved: false,
            project: ""
        }
        this.toggleSaved = this.toggleSaved.bind (this);
        this.submitProject = this.submitProject.bind (this);

        this.setProjectTitle = this.setProjectTitle.bind (this);
        this.setProjectDetails = this.setProjectDetails.bind (this);
    }

    componentDidMount () {
        this.setState ({creator: this.props.user_id})
    }

    
    submitProject = async () => {
        let project = {
            creator: this.state.creator,
            name: this.state.projectTitle,
            description: this.state.projectDetails
        }

        console.log ('Sending POST project:', project)

        const res = await fetch('http://127.0.0.1:8010/proxy/project/', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(project)
        })

        const body = await res.json();
        console.log (body)
        
        this.setState ({p_id: body.id})
        this.state.p_id = body.id


        const res2 = await fetch('http://127.0.0.1:8010/proxy/project/'+body.id, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })

        const body2 = await res2.json();
        console.log (body2)

        this.toggleSaved (true)
    }

    setProjectTitle = (e) => {
        console.log ("project title:", e)
        this.setState ({projectTitle: e})
    }

    setProjectDetails = (e) => {
        console.log ("project description:", e)
        this.setState ({projectDetails: e})
    }

    toggleSaved = (e) => {
        this.setState ({saved: e})
        this.state.saved = e
    }

    render() {
        return (
        <div style={{marginLeft: '10%', marginTop: '5%', marginRight: '10%'}}>

            {!this.state.saved && 
           
            <div>

                <br></br><br></br><br></br><br></br>
                <TextField
                    id="projectTitle"
                    // label="Multiline Placeholder"
                    fullWidth
                    multiline
                    placeholder="Placeholder"
                    variant="standard"

                    value={this.state.projectTitle}
                    label="Project Title"
                    onChange={(e) => {
                    this.setProjectTitle (e.target.value);
                    }}
                />
                <br></br><br></br> 
                
                <TextField
                    id="projectDesc"
                    // label="Multiline Placeholder"
                    fullWidth
                    multiline
                    placeholder="Placeholder"
                    variant="standard"

                    value={this.state.projectDetails}
                    label="Project Description"
                    onChange={(e) => {
                    this.setProjectDetails (e.target.value);
                    }}
                />


                <Link className="btn btn-primary" 
                style={{width: '15%', float: 'right', marginRight: '5%'}}
                onClick = {() => this.submitProject ()}
                > Submit Project </Link>
            </div>
        }


        {
            this.state.saved &&
            <div>
                <p>You have added a project!</p>

                <p>Your Project Details:</p>
                Creator User ID: {this.state.creator} <br></br>
                Project ID: {this.state.p_id} <br></br>
                Title: {this.state.projectTitle} <br></br>
                Description: {this.state.projectDetails} <br></br>

            </div>
        }
            
        </div>
    )
}
}

export default Project;

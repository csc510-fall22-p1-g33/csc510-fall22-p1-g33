import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";
import { TextField } from '@mui/material';
    

class Profile extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bio: "",
            email: "",
            name: "",
            phone: "",
  
            id: "",
            password: "",
            projects: [],
            join_requests: [],
            teams: [],
            username: "",

            saved: true
        }
        this.setName = this.setName.bind(this);
        // this.setName = this.setName.bind(this);
        this.setEmail = this.setEmail.bind(this);
        this.setBio = this.setBio.bind(this);
        this.setPhone = this.setPhone.bind(this);
        this.toggleSaved = this.toggleSaved.bind (this);
        this.setProject = this.setProject.bind (this);

        // this.setProjectTitle = this.setProjectTitle.bind (this);
        // this.setProjectDetails = this.setProjectDetails.bind (this);
    }

    async componentDidMount () {
        console.log ("Loading user data for user id:", this.props.user_id)

        const res = await fetch('http://127.0.0.1:8010/proxy/user/'+this.props.user_id, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })
        
        const body = await res.json();
        console.log (body)
        console.log ('username:', body.user.username)
        console.log ('projects:', body.user.projects)

        this.setName (body.user.about.name)
        this.setEmail (body.user.about.email)
        this.setPhone (body.user.about.phone)
        this.setBio (body.user.about.bio)
        this.setProject (body.user.projects)
    }

    setName = (e) => {
        console.log ("Name:", e)
        this.setState({name: e});
        this.state.name = e;
    }

    setEmail = (e) => {
        console.log ("email:", e)
        this.setState({email: e});
        this.state.email = e;
    }

    setBio = (e) => {
        console.log ("bio:", e)
        this.setState({bio: e});
        this.state.bio = e;
    }

    setPhone = (e) => {
        console.log ("phone:", e)
        this.setState({phone: e});
        this.state.phone = e;
    }

    setProject = (e) => {
        console.log ("Project:", e)
        this.setState({projects: e});
        this.state.projects = e;

        // this.setState ({projects: [...this.state.projects, e]})
    }

    // setProjectTitle = (e, id) => {
    //     console.log ("project title:", e)
        // var someProperty = {...this.state.project[id]}
        // someProperty.projectTitle = e

        // this.setState ({someProperty})
    // }

    // setProjectDetails = (e, id) => {
    //     console.log ("project description:", e)
    //     var someProperty = {...this.state.project[id]}
    //     someProperty.projectDetails = e

    //     this.setState ({someProperty})
    // }

    toggleSaved = (e) => {
        this.setState ({saved: e})
        this.state.saved = e
    }

    render() {
        return (
        <div style={{marginLeft: '10%', marginTop: '5%', marginRight: '10%'}}>

            {!this.state.saved && 
            <div>
                <TextField
                id="name"
                // label="Multiline Placeholder"
                fullWidth
                placeholder="Placeholder"
                variant="standard"

                value={this.state.name}
                label="Name"
                onChange={(e) => {
                this.setName (e.target.value);
                }}
            />
            <br></br><br></br>
            
            <TextField
                id="email"
                fullWidth
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.email}
                label="Email"
                onChange={(e) => {
                this.setEmail (e.target.value);
                }}
            />

            <br></br><br></br>

            <TextField
                id="phone"
                fullWidth
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.phone}
                label="Phone"
                onChange={(e) => {
                this.setPhone (e.target.value);
                }}
            />

            <br></br><br></br>

            <TextField
                id="bio"
                fullWidth
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.bio}
                label="Bio"
                onChange={(e) => {
                this.setBio (e.target.value);
                }}
            />

            

            <br></br><br></br><br></br><br></br>
            {/* <TextField
                id="projectTitle"
                // label="Multiline Placeholder"
                fullWidth
                multiline
                placeholder="Placeholder"
                variant="standard"

                value={this.state.projectTitle}
                label="Project Title"
                onChange={(e) => {
                this.setBio (e.target.value);
                }}
            />
            <br></br><br></br> */}
            {/* {this.state.projects.length == 0 && <p>Add a new project:</p>}
            <div>
            
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
                this.setProject (e.target.value);
                }}
            />
            </div> */}
            

            {/* <br></br><br></br><br></br><br></br> */}

            {/* Team members:<br></br><br></br>
            {
                this.state.teammates.length > 0 &&
                    Object.keys(this.state.teammates).map((key, index) =>{
                        return(
                            <div style={{marginBottom: '1%'}}>
                                {this.state.teammates[key]}<button style={{marginLeft: "2%"}}>Remove</button>
                            </div>
                        )})
                
            } */}
            
            
            {/* <br></br><br></br> */}
            {/* <button onClick={() => this.addFields()}>Add New Project</button> */}
            

            {/* <br></br><br></br> */}

            <Link className="btn btn-primary" 
            style={{width: '15%', float: 'right', marginRight: '5%'}}
            onClick = {() => this.toggleSaved (true)}
            > Save Changes </Link>
            </div>}

            {this.state.saved &&

                <div>
                    <h5>Your Profile</h5>
                    Name: {this.state.name}
                    <br></br>
                    Email: {this.state.email}
                    <br></br>
                    Phone: {this.state.phone}
                    <br></br>
                    Bio: {this.state.bio}
                    <br></br><br></br>
                    
                    {this.state.projects.length == 0 && 
                    <p>Project: You have not yet added any project.
                        <br></br>
                        Teams: You have no team yet.
                    </p>}

                    {this.state.projects.length > 0 && 
                    <p>Projects: 
                        <br></br>
                        You have added {this.state.projects.length} projects!
                        {/* Project Name: {this.state.projects[0].about.name}
                        Project Description: {this.state.projects[0].about.description}
                        Teams: {this.state.projects[0].teams}
                        Users: {this.state.projects[0].users} */}
                        {console.log ("!!!!", this.state.projects.length, this.state.projects[0])}
                    </p>}

                    {/* Team members:<br></br> */}
                    {/* {
                        this.state.teammates.length > 0 &&
                            Object.keys(this.state.teammates).map((key, index) =>{
                                return(
                                    <div>
                                        {this.state.teammates[key]}
                                    </div>
                                )})
                        
                    } */}

                    <Link className="btn btn-primary" 
                    style={{width: '15%', float: 'right', marginRight: '5%'}}
                    onClick = {() => this.toggleSaved (false)}
                    > Update Profile </Link>
                    

                </div>

            }

            

        </div>
    )
}
}

export default Profile;
// https://www.freecodecamp.org/news/build-dynamic-forms-in-react/
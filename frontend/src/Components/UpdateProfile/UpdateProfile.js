import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";
import { TextField } from '@mui/material';
    

class Profile extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            password: '',
            phone: '', 
            bio: '',
            email: '',
            projectTitle: '',
            projectDetails: '',
            project: [{projectTitle: 'Team Formation Tool', 
                        projectDetails: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pharetra lectus nisi, sit amet dapibus velit lacinia ac. Vivamus vel lectus diam. Aliquam in posuere justo. Praesent blandit augue sed erat vestibulum, non fermentum neque pretium. Suspendisse commodo scelerisque magna, sed semper dui lacinia at. Aliquam sit amet facilisis lectus. Morbi volutpat venenatis faucibus.'}]
        }
        this.setName = this.setName.bind(this);
        this.setEmail = this.setEmail.bind(this);
        this.setBio = this.setBio.bind(this);
        this.setPhone = this.setPhone.bind(this);
        this.setProjectTitle = this.setProjectTitle.bind (this);
        this.setProjectDetails = this.setProjectDetails.bind (this);
        this.addFields = this.addFields.bind (this)
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

    setProjectTitle = (e, id) => {
        console.log ("project title:", e)
        var someProperty = {...this.state.project[id]}
        someProperty.projectTitle = e

        this.setState ({someProperty})
    }

    setProjectDetails = (e, id) => {
        console.log ("project description:", e)
        var someProperty = {...this.state.project[id]}
        someProperty.projectDetails = e

        this.setState ({someProperty})
    }



    render() {
        return (
        <div style={{marginLeft: '20%', marginTop: '5%'}}>
            <TextField
                id="name"
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.name}
                label="Name"
                onChange={(e) => {
                this.setName (e.target.value);
                }}
            />
            <br></br>
            
            <TextField
                id="email"
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.email}
                label="Email"
                onChange={(e) => {
                this.setEmail (e.target.value);
                }}
            />

            <br></br>

            <TextField
                id="phone"
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.phone}
                label="Phone"
                onChange={(e) => {
                this.setPhone (e.target.value);
                }}
            />

            <br></br>

            <TextField
                id="bio"
                // label="Multiline Placeholder"
                placeholder="Placeholder"
                variant="standard"

                value={this.state.bio}
                label="Bio"
                onChange={(e) => {
                this.setBio (e.target.value);
                }}
            />

            <br></br>
            {this.state.project.length > 0 &&
            <p>
            Project Name: {this.state.projectTitle}
            <br></br><br></br>
            Project Description: {this.state.projectDetails}
            </p>
            }
            
            
            <br></br><br></br>
            <button onClick={() => this.addFields()}>Add New Project</button>
            

            <br></br><br></br>

            <Link className="btn btn-primary" style={{width: '15%', float: 'right', marginRight: '5%'}}> Save Changes </Link>

        </div>
    )
}
}

export default Profile;
// https://www.freecodecamp.org/news/build-dynamic-forms-in-react/
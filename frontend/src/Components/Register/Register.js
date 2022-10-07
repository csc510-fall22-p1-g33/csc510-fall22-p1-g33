import React from 'react';
import { Component } from 'react';
import { BrowserRouter, Route, Switch, Link } from "react-router-dom";
import './Register.css'

// user can register as a team or an individual user
const register_role = [
    {
        label: "Individual",
        value: "individual",
    },
    {
        label: "Team",
        value: "team",
    }
];


// {
//     "username": "tithi",
//     "password": "sdt",
//     "about": {
//       "name": "Sutapa Dey Tithi",
//       "email": "tithisutapa52@gmail.com",
//       "phone": "123",
//       "bio": "nonee"
//     }
//   }

class Register extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            email:"",
            pass:"",
            fullname: "",
            phone: "",
            bio: "",
            error: false
        };
        this.handleChange_role = this.handleChange_role.bind(this);
        this.handleChange_username = this.handleChange_username.bind(this);
        this.handleChange_fullname = this.handleChange_fullname.bind (this)
        this.handleChange_email = this.handleChange_email.bind(this);
        this.handleChange_pass = this.handleChange_pass.bind(this);
        this.handleChange_phone = this.handleChange_phone.bind (this)
        this.handleChange_bio = this.handleChange_bio.bind (this)
        
        this.setError =  this.setError.bind(this);
        this.clearError =  this.clearError.bind(this);
    }

    // set the error flag if any field entry is invalid
    setError = () => {
        this.setState({error: true});
        this.state.error = true;
    }

    // clear the error flag if all field entries are valid
    clearError = () => {
        this.setState({error: false});
        this.state.error = false;
    }

    // update user's role
    handleChange_role(e) {
        this.setState({ role: e.target.value });
        this.props.setRole(e.target.value);
    }
    // update user's username/handle
    handleChange_username(e) {
        this.setState({ username: e.target.value });
    }
    // update user's email
    handleChange_email(e) {
        this.setState({ email: e.target.value });
    }
    // update user's password
    handleChange_pass(e) {
        this.setState({ pass: e.target.value });
    }

   
    // update user's full name
    handleChange_fullname(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ fullname: e.target.value });
    }
    // update user's contact info
    handleChange_phone(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ phone: e.target.value });
    }
    // update user's short bio
    handleChange_bio(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ bio: e.target.value });
    }

    // after clicking submit, this function sends server the username, password
    // if all credentials are valid, then the user will be logged in
    handleRegister = async () => {
        const user = {
            "username": this.state.username,
            "password": this.state.pass,
            "about": {
                "name": this.state.fullname,
                "email": this.state.email,
                "phone": this.state.phone,
                "bio": this.state.bio
            }
        }

        console.log ("POST req to server:")
        // console.log (user)

          

        const res = await fetch('http://127.0.0.1:8010/proxy/user/reg', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(user)
        })


        const body = await res.json();
        
        if (body.id == -1) {
            console.log (body.error_type)
        }
        else {
            console.log ("Successfully registered!\nid:", body.id)
            this.props.setUserID(body.id);
            this.props.onRouteChange("signedin", null);
        }
    }

    render() {

        return (
            <div id="first">
                <h1>{this.props.text}</h1>
                <div className="card my_card2 border-dark">
                    <div className="card-body">
                        <h3 className="card-title">Register</h3>
                        
                        <input id="Name" name="Name" type="text" placeholder="User name" className="email" onChange={this.handleChange_username} />
                        <input id="fullName" name="fullName" type="text" placeholder="Full Name" className="email" onChange={this.handleChange_fullname} />
                        <input id="Email" name="Email" type="text" placeholder="Email address" className="email"  onChange={this.handleChange_email} />
                        <input id="password" name="password" type="password" placeholder="Password" className="password"  onChange={this.handleChange_pass} />

                        <input id="phone" name="phone" type="text" placeholder="Phone Number" className="email" onChange={this.handleChange_phone} />
                        <input id="bio" name="bio" type="text" placeholder="Bio" className="email" onChange={this.handleChange_bio} />
                        {/* <input id="password" name="password" type="password" placeholder="Password" className="password"  onChange={this.handleChange_pass} /> */}


                        {/* <p style={{ marginTop: 10, textAlign: 'left', marginLeft: 16 }}>Register as
                        <select value={this.state.role} onChange={this.handleChange_role} style={{ marginLeft: 13, borderRadius: 5 }}>
                                {register_role.map((option) => (
                                    <option value={option.value}>{option.label}</option>
                                ))}
                            </select>
                        </p> */}
                        

                        <Link to='/dashboard' className="btn btn-primary " onClick={this.handleRegister}>Submit</Link>
                        <br></br>

                        {/* <input type="submit" id="submit" className="submit" onClick={this.handleRegister}/>  */}
                        <br></br>
                    </div>
                </div>
            </div>
        )
    }
}
export default Register;
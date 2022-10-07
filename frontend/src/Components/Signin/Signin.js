import React from 'react';

import { Component } from 'react';
import { Link } from "react-router-dom";

import './Signin.css'

class first extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            email:"",
            pass:"",
            error: false
          };
      
        this.handleChange_username = this.handleChange_username.bind(this);
        this.handleChange_email = this.handleChange_email.bind(this);
        this.handleChange_pass = this.handleChange_pass.bind(this);

        this.setError =  this.setError.bind(this);
        this.clearError =  this.clearError.bind(this);
    }

    setError = () => {
        this.setState({error: true});
        this.state.error = true;
    }

    clearError = () => {
        this.setState({error: false});
        this.state.error = false;
    }
    
    // after clicking submit, this function sends server the username, password
    // if all credentials are valid, then the user will be logged in
    handleSubmit = async() => {
        console.log ("GET req to server")
        // this.props.onRouteChange("signedin", null);
        
        const params = 'username=' + this.state.username + "&password=" + this.state.pass
        let user_id;

        const res = await fetch('http://127.0.0.1:8010/proxy/user/login?'+params, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        })
        
        const body = await res.json();
        console.log (body.login)
        
        if (body.login == "SUCCESS") {
            this.props.setUserID(body.user_id);
            this.props.onRouteChange("signedin", null);
        }       
    }

    // update the username field in this state
    handleChange_username (e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ username: e.target.value });
    }
   
    // update the email field in this state
    handleChange_email(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ email: e.target.value });
    }
    // update the password field in this state
    handleChange_pass(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ pass: e.target.value });
    }
    
    render() {
        return (
            <div id="first">
                <div className="card signin_card border-dark" >
                    <div className="card-body">
                        <h3 className="card-title">Log In</h3>
                        <input id="username" name="username" type="text" placeholder="Username" className="email" onChange={this.handleChange_username}/> 
                        <input id="Email" name="Email" type="text" placeholder="Email address" className="email" onChange={this.handleChange_email}/> 
                        <input id="password" name="password" type="password" placeholder="Password" className="password" onChange={this.handleChange_pass}/> 
                        <br></br>

                        {
                            this.state.error &&
                            <h7 style={{color: 'red', marginTop: 2}}> Incorrect fields. try Again. </h7>
                        }

                        <Link to="/dashboard" className="btn btn-primary" onClick={this.handleSubmit} 
                        style={{marginTop: '-.0001%'}}>Submit</Link>
                        <br></br> 
                        <p style={{marginTop:10}}>Don't have an account? <Link to="/register">Register</Link></p>
                                                                
                    </div>
                </div>                             
            </div>
        ) 
    }
}

export default first;
import React from 'react';

import { Component } from 'react';
import { Link } from "react-router-dom";

import './Signin.css'
class first extends Component {
    constructor(props) {
        super(props);
        this.state = {
            role: "",
            email:"",
            pass:"",
            error: false
          };
      
        // this.handleChange_role = this.handleChange_role.bind(this);
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


    
    handleSubmit = () => {

        // this.handleChange_role();

        // must delete this line later
        // auto sign up
        console.log ("GET req to server")
        this.props.onRouteChange("signedin");


        // fetch('http://localhost:5000/login', {
        //     method: 'POST',
        //     headers: {
        //       'Accept': 'application/json',
        //       'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({
        //         //   id: this.state.id,
        //         //   item: this.state.item,
        //         //   itemType: this.state.itemType
        //         email:this.state.email,
        //         pass:this.state.pass,
        //         roletype:this.state.role
        //     })
        //   })   
        //   .then((response) => response.json())
        //   .then((data) => {
        //       console.log('This is your data:\n', data);
        //       if(data === "error"){
        //         console.log('Cannot login!\n');
        //         this.setError();
        //       }
        //       else
        //       {
        //         this.props.setUserID(data.user_id);
        //         this.props.onRouteChange("signedin");
        //       }

        //   })
        //   .catch((error) => {
        //       this.setError();
        //   })
        //this.props.onRouteChange("signedin");             
    }

   

    handleChange_email(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ email: e.target.value });
    }
    handleChange_pass(e) {
        this.clearError();
        console.log(e.target.value);
        this.setState({ pass: e.target.value });
    }
    
    
    render() {
        return (
            <div id="first">
                {/* <h1>{this.props.text}</h1> */}
                <div className="card signin_card border-dark" >
                    <div className="card-body">
                        <h3 className="card-title">Log In</h3>
                        <input id="Email" name="Email" type="text" placeholder="Email address" className="email" onChange={this.handleChange_email}/> 
                        <input id="password" name="password" type="password" placeholder="Password" className="password" onChange={this.handleChange_pass}/> 
                        <br></br>
                        
                        {/* <p style={{marginTop:15}}>Login as 
                            <input type="checkbox" id="box1" name="box1" value="individual" className="checkb"
                                defaultChecked={this.state.student}
                                onChange={this.handleChangeStudent}
                            />
                            Individual 
                            <input type="checkbox" id="box2" name="box2" value="team" className="checkb"
                                defaultChecked={this.state.instructor}
                                onChange={this.handleChangeInstructor}
                            />
                            Team
                        </p>  */}

                        {
                            this.state.error &&
                            <h7 style={{color: 'red', marginTop: 2}}> Incorrect fields. try Again. </h7>
                        }
                        <Link to="/authHome" className="btn btn-primary " onClick={this.handleSubmit}>Submit</Link>
                        <br></br> 
                        <p style={{marginTop:10}}>Don't have an account??   <Link to="/register">Register</Link></p>
                        
                    {/* <input type="submit" id="submit" className="submit" onClick={this.handleLangChange}/>  */}
                                        
                    </div>
                </div>                             
            </div>
        ) 
    }
}
export default first;
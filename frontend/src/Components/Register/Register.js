import React from 'react';

import { Component } from 'react';
import { BrowserRouter, Route, Switch, Link } from "react-router-dom";

import './Register.css'
const options_zip = [
    {
        label: "3",
        value: "3",
    },
    {
        label: "4",
        value: "4",
    },
    {
        label: "5",
        value: "5",
    },
    {
        label: "6",
        value: "6",
    },
    {
        label: "7",
        value: "7",
    },
    {
        label: "8",
        value: "8",
    },
    {
        label: "9",
        value: "9",
    },
    {
        label: "10",
        value: "10",
    },

];
const options_zip2 = [
    {
        label: "Individual",
        value: "individual",
    },
    {
        label: "Team",
        value: "team",
    }
];

class first extends Component {
    constructor(props) {
        super(props);
        this.state = {

            class: 3,
            role: "none",
            name:"",
            email:"",
            pass:""

        };
        this.handleChange_class = this.handleChange_class.bind(this);
        this.handleChange_role = this.handleChange_role.bind(this);
        this.handleChange_name = this.handleChange_name.bind(this);
        this.handleChange_email = this.handleChange_email.bind(this);
        this.handleChange_pass = this.handleChange_pass.bind(this);

    }
    handleChange_class(e) {
        this.setState({ class: e.target.value });
    }
    handleChange_role(e) {
        this.setState({ role: e.target.value });
        this.props.setRole(e.target.value);
    }
    handleChange_name(e) {
        this.setState({ name: e.target.value });
    }
    handleChange_email(e) {
        this.setState({ email: e.target.value });
    }
    handleChange_pass(e) {
        this.setState({ pass: e.target.value });
    }

    // INCOMPLETE
    handleLangChange = () => {
        console.log ("POST req to server")
        this.props.onRouteChange("signedin");

        // fetch('http://localhost:5000/signUp', {
        //     method: 'POST',
        //     headers: {
        //       'Accept': 'application/json',
        //       'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({
        //         //   id: this.state.id,
        //         //   item: this.state.item,
        //         //   itemType: this.state.itemType
        //         username:this.state.name,
        //         email:this.state.email,
        //         pass:this.state.pass,
        //         roletype:this.state.role,
        //         class:this.state.class       
        //     })
        //   })    
        //   .then((response) => response.json())
        //   .then((data) => {
        //       console.log('This is your data:\n', data);
        //       if(data === "error")
        //       {
        //         console.log('Cannot register!\n');
        //       }
        //       else
        //       {
        //         this.props.setUserID(data.user_id);
        //         this.props.onRouteChange("signedin"); 
        //       }

        //   });
    }


    render() {

        return (
            <div id="first">
                <h1>{this.props.text}</h1>
                <div className="card my_card2 border-dark">
                    <div className="card-body">
                        <h3 className="card-title">Register</h3>
                        
                        <input id="Name" name="Name" type="text" placeholder="Full name" className="email" onChange={this.handleChange_name} />
                        <input id="Email" name="Email" type="text" placeholder="Email address" className="email"  onChange={this.handleChange_email} />
                        <input id="password" name="password" type="password" placeholder="Password" className="password"  onChange={this.handleChange_pass} />


                        <p style={{ marginTop: 10, textAlign: 'left', marginLeft: 16 }}>Register as
                        <select value={this.state.role} onChange={this.handleChange_role} style={{ marginLeft: 13, borderRadius: 5 }}>
                                {options_zip2.map((option) => (
                                    <option value={option.value}>{option.label}</option>
                                ))}
                            </select>
                        </p>
                        {this.state.role === "student" &&
                            (
                                <p style={{ marginTop: 15, textAlign: 'left', marginLeft: 16 }}>Your class
                                    <select value={this.state.class} onChange={this.handleChange_class} style={{ marginLeft: 20, borderRadius: 5,width:100 }}>
                                        {options_zip.map((option) => (
                                            <option value={option.value}>{option.label}</option>
                                        ))}
                                    </select>
                                </p>

                            )
                        }


                        <Link to="/authHome" className="btn btn-primary " onClick={this.handleLangChange}>Submit</Link>
                        <br></br>

                        {/* <input type="submit" id="submit" className="submit" onClick={this.handleLangChange}/>  */}
                        <br></br>
                    </div>
                </div>




            </div>
        )
    }
}
export default first;
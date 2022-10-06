import React, { Component } from "react";
import { NavLink } from "react-router-dom";

import "./Home.css";
import welcome from "../../Resources/Images/homepage1.jpg";
import { BrowserRouter, Route, Switch, Link } from "react-router-dom";

class Home extends Component {
    constructor(props) {
        super(props);
        
      }
    // componentDidMount(){
    //   this.props.passToParent(0);  
    // }  
    render() {
        return (
            <>
                <main>
                    <section id="home">
                        <div></div>
                       
                        <div className="container-fluid">
                            <h3>Team Formation Tool</h3>
                            <h6>Explore | Be up-to-date about others' availability | Form your team</h6>
                            <img
                                className="welcome-img mx-left"
                                src={welcome}
                            />
                            </div>
                            {/* <button onClick={this.handleLangChange}>
                                Get Started
                            </button> */}
                            {/* <Link to="/first" className="btn btn-primary">Sign up</Link> */}
                        {/* </div>  */}
                    </section>
                </main>
            </>
        );
    }
}

export default Home;


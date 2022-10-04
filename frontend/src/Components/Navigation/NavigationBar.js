import React, { Component } from "react";
import { NavLink, Link } from "react-router-dom";
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem} from 'reactstrap';
import "./NavigationBar.css";
import logo_image from "../../Resources/Images/image 6.png";
import avatar from "../../Resources/Images/image 33.png";

class NavigationBar extends Component {
    constructor(props) {
        super(props);
    }

    state = {
        isOpen: false,
    };

    toggle = () => {
        this.setState({
            isOpen: !this.state.isOpen,
        });
    };

    onSubmitSignOut = () => {
        this.props.onRouteChange("signout");
    }

    render() {
        if(!this.props.isSignedIn) {
            return (
                <>
                    <Navbar className="navbar-expand-lg fixed-top" light>
                        <NavbarBrand href="/">
                            <div className="logo">
                            <img src={logo_image} className="logo_image"/>                                
                            </div>
                            
                        </NavbarBrand>
                        <NavbarToggler onClick={this.toggle} />

                        <Collapse isOpen={this.state.isOpen} navbar>
                            <Nav className="ml-auto" navbar>                            
                                <NavItem className="nav-item">
                                    <NavLink className="nav-links" to="/signin" style={{color:"white"}}>
                                        Log In
                                    </NavLink>
                                </NavItem>

                                {/* <li class="divider-vertical-second-menu2"></li> */}

                                <NavItem className="nav-item">
                                    
                                    <NavLink className="nav-links" to="/register" style={{color:"white"}}>
                                        Register
                                    </NavLink>
                                    
                                </NavItem>
                                
                            </Nav>
                        </Collapse>
                        
                    </Navbar>
                </>
            );
        }
    else {
            return (
                <>
                    <Navbar className="navbar-expand-lg fixed-top " light>
                        <NavbarBrand href="/">
                            <div className="logo">
                                <img src={logo_image} className="logo_image" />
                            </div>

                        </NavbarBrand>
                        <NavbarToggler onClick={this.toggle} />

                        <Collapse isOpen={this.state.isOpen} navbar>
                            <Nav className="ml-auto" navbar>

                                <NavItem>
                                    <NavLink className="nav-links" to="">
                                        Home
                                    </NavLink>
                                </NavItem>


                                <li className="divider-vertical-second-menu"></li>
                                <NavItem>
                                    <NavLink className="nav-links" to="">
                                        View Requests
                                    </NavLink>
                                </NavItem>


                                <li className="divider-vertical-second-menu"></li>
                                <NavItem>
                                    <NavLink className="nav-links" to="/authHome">
                                    Update Profile
                                    </NavLink>
                                </NavItem>
                                
                                <Link to="/profile">
                                <img src={avatar} />
                                </Link>
                                <NavItem style={{ paddingLeft: 10 }}>
                                    <NavLink className="nav-links" to="/" onClick={this.onSubmitSignOut}>
                                    Log Out
                                    </NavLink>
                                </NavItem>
                            </Nav>
                        </Collapse>

                    </Navbar>
                </>
            );
        }
        
    }
}

export default NavigationBar;

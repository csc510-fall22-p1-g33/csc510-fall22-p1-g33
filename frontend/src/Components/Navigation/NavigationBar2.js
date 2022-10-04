import { Link, NavLink } from "react-router-dom"
import styled from "styled-components"
import React from "react";

import logo_image from "../../Resources/Images/logo.png";


const Navigation = styled.div`
    display: flex;
    background-color: #0F3856;
    justify-content: space-between;
    align-items: center;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
    width: 100%;

    & img {
        padding: 0.5em;
        padding-left: 2em;
        width: 4em;
        height: 4em;
    }
`

const Links = styled.div`
    padding-right: 2em;
    width: 40%;
    display: flex;
    justify-content: space-between;

    & a {
        // color: #8C8C8C;
        color: #FFFFFF;
        text-decoration: none;
        font-size: .8em;
        transform: scale(.95, 1.1);
    }

    & a:hover {
        color: #6F6F6F;
    }
`

class NavigationBar extends React.Component {
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
                <Navigation>
                    <Link to="/">
                        <img src={logo_image} alt="logo"/>
                    </Link>
                    <Links>

                        <NavLink to="/faq">
                            <h3>
                                FAQ
                            </h3>
                        </NavLink>
                        <NavLink to="/register">
                            <h3>
                                Register
                            </h3>
                        </NavLink>
                        <NavLink to="/signin">
                            <h3>
                                Log In
                            </h3>
                        </NavLink>
                    </Links>
                </Navigation>
            );
        }
        else {
            return (
                <Navigation>
                    <Link to="/">
                        <img src={logo_image} alt="logo"/>
                    </Link>
                    <Links>

                        <NavLink to="/faq">
                            <h3>
                                FAQ
                            </h3>
                        </NavLink>
                        <NavLink to="/dashboard">
                            <h3>
                                Dashboard
                            </h3>
                        </NavLink>
                        <NavLink to="/requests">
                            <h3>
                                View Requests
                            </h3>
                        </NavLink>
                        <NavLink to="/updateProfile">
                            <h3>
                                Update Profile
                            </h3>
                        </NavLink>
                        <NavLink to="/" onClick={this.onSubmitSignOut}>
                            <h3>
                                Log Out
                            </h3>
                        </NavLink>
                    </Links>
                </Navigation>
            );
        }
    }
}

export default NavigationBar;

import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import {
    Container,
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem } from 'reactstrap';
import i18n from "i18next";
import "./Footer.css";

class Footer extends Component {
    state = {
        isOpen: false,
    };

    toggle = () => {
        this.setState({
            isOpen: !this.state.isOpen,
        });
    };

    render() {
        return(
            <>
                <Navbar className="navbar-expand-lg" light>
                    <NavbarToggler onClick={this.toggle} />
                    
                    <Collapse isOpen={this.state.isOpen} navbar>
                    <Nav className="mr-auto" navbar>
                            <NavItem>
                                <NavLink className="nav-links" to="/about">
                                    { i18n.t("About") }
                                </NavLink>
                            </NavItem>

                            <NavItem>
                                <NavLink className="nav-links" to="/policy">
                                    { i18n.t("Policy") }
                                </NavLink>
                            </NavItem>   
                    </Nav>
                    <Nav className="ml-auto" navbar>
                        <NavItem>
                            <NavLink className="nav-links" to="/contact">
                                { i18n.t("Contact") }
                            </NavLink>
                        </NavItem>
                    </Nav>
                    </Collapse>
                </Navbar>
            </>
        )
    }
}

export default Footer;

// https://6-4-0--reactstrap.netlify.app/components/navbar/
// https://reactjs.org/docs/fragments.html
// className="fixed-bottom"
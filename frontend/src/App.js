import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import React, { Component } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Navigation from "./Components/Navigation/NavigationBar2";
import Signin from "./Components/Signin/Signin";
import Register from "./Components/Register/Register";
import Home from "./Components/Home/Home";
import Dashboard from "./Components/Dashboard/Dashboard";
import Project from "./Components/Dashboard/project";
import Requests from "./Components/JoinRequests/Requests";
import UpdateProfile from "./Components/UpdateProfile/UpdateProfile";
import CreateProject from "./Components/UpdateProfile/CreateProject";
import FAQ from "./Components/FAQ/FAQ.js";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      route: '',
      isSignedIn: false,

      user_id: '',
      username: '',
      password: '',
      teamFormed: false,
      teamName: '',

      view_projectID: '',

      about: {
        name: '',
        email: '',
        phone: '',
        bio: ''
      }
    }
  }

  // utlities for signout/siginin functionality
  onRouteChange = (route, args) => {
    if (route === 'signout') {
      this.setState({ isSignedIn: false })
      this.state.isSignedIn = false;
    } else if (route === 'signedin') {
      this.setState({ isSignedIn: true })
      this.state.isSignedIn = true;
      console.log("signing in")
    }
    console.log(route, args)
    this.setState({ route: route });
  }

  setUserID = (id) => {
    this.setState({ user_id: id });
    this.state.user_id = id;
    console.log("setting user id:", this.state.user_id);
  }

  setUsername = (name) => {
    this.setState({ username: name });
    this.state.username = name;
    console.log("setting username:", this.state.username);
  }

  setProjectID = (pid) => {
    this.setState({ view_projectID: pid });
    this.state.view_projectID = pid;
    console.log("setting view_projectID:", this.state.view_projectID);
  }

  render() {
    return (
      <BrowserRouter>

        {/* navigation bar */}
        <Navigation
          isSignedIn={this.state.isSignedIn}
          role={this.state.role}
          onRouteChange={this.onRouteChange}
          setUserID={this.setUserID}
        />

        <Routes>
          {/* before logging in/being registered, any user view this homepage */}
          <Route exact path="/" element={<Home />} />
          <Route exact path="/FAQ" element={<FAQ />} />

          {/* login/register wizard */}
          <Route exact path="/signin" element={<Signin onRouteChange={this.onRouteChange} setUserID={this.setUserID} setUsername={this.setUsername} />} />
          <Route exact path="/register" element={<Register onRouteChange={this.onRouteChange} setUserID={this.setUserID} setUsername={this.setUsername} />} />


          {this.state.isSignedIn ?
            // if the user is logged in, show the homepage containing available team/user information list
            <>
              <Route exact path="/dashboard" element={<Dashboard onRouteChange={this.onRouteChange} setProjectID={this.setProjectID} user_id={this.state.user_id} />} />
              <Route exact path="/project" element={<Project projectID={this.state.view_projectID} />} />
              <Route exact path="/requests" element={<Requests user_id={this.state.user_id} />} />
              <Route exact path="/updateProfile" element={<UpdateProfile user_id={this.state.user_id} />} />
              <Route exact path="/createproject" element={<CreateProject user_id={this.state.user_id} />} />
            </>

            :
            // if the user cannot login, redirect them to try again
            <Route path="/dashboard" element={
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                height: '100vh',
                fontSize: '1.5rem'
              }}>
                Something went wrong. Please try again!
              </div>
            } />
          }

        </Routes>
      </BrowserRouter>
    );
  }
}

export default App;

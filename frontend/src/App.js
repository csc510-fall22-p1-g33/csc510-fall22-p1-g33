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

          about: {
            name: '',
            email: '',
            phone: '',
            bio: ''
          }
        }
      }


      onRouteChange = (route, args) => {
        if (route === 'signout') {
          this.setState({isSignedIn: false})
          this.state.isSignedIn = false;
        } else if (route === 'signedin') {
          this.setState({isSignedIn: true})
          this.state.isSignedIn = true;
          console.log ("signing in")
        }
        console.log (route, args)
        this.setState({route: route});
      }

      setUserID = (id) => {
        this.setState({user_id: id});
        this.state.user_id = id;
        console.log("setting user id:", this.state.user_id);
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
                <Route exact path="/" element={<Home/>} />
                <Route exact path="/FAQ" element={<FAQ />} />

                {/* login/register wizard */}
                <Route exact path="/signin" element= {<Signin onRouteChange={this.onRouteChange} setUserID={this.setUserID}/> } />
                <Route exact path="/register" element = {<Register onRouteChange={this.onRouteChange}  setUserID={this.setUserID}/> }/>


                {this.state.isSignedIn ?
                  // if the user is logged in, show the homepage containing available team/user information list
                  <>
                    <Route exact path="/dashboard" element={<Dashboard onRouteChange={this.onRouteChange}/> } />
                    <Route exact path="/project" element={<Project />} />
                    <Route exact path="/requests" element={<Requests />} />
                    <Route exact path="/updateProfile" element={<UpdateProfile />} />
                  </>
                  
                :
                  // if the user cannot login, redirect them to try again
                  <Route path="/dashboard" element ={
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    height: '100vh',
                    fontSize: '1.5rem'
                  }}>
                    Something went wrong. Please try again!
                  </div>
                  }/>
                }
              
              </Routes>
            </BrowserRouter>
        );
      }
    }

export default App;

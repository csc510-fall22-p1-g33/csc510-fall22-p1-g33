import React, { Component } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import "./App.css";
import Navigation from "./Components/Navigation/NavigationBar";

import Signin from "./Components/Signin/Signin";
import Register from "./Components/Register/Register";
import Home from "./Components/Home/Home";



class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
          input: '',
          imageUrl: '',
          route: '',
          isSignedIn: false,
          user_id: '',
          teamFormed: false,
          teamName: '',
          user: {
            id: '',
            name: '',
            email: '',
            joined: ''
          }
        }
      }


      onRouteChange = (route) => {
        if (route === 'signout') {
          this.setState({isSignedIn: false})
          this.state.isSignedIn = false;
        } else if (route === 'signedin') {
          this.setState({isSignedIn: true})
          this.state.isSignedIn = true;
          console.log ("signing in")
        }
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

                {/* login/register wizard */}
                <Route exact path="/signin" element= {<Signin onRouteChange={this.onRouteChange} setUserID={this.setUserID}/> } />
                <Route exact path="/register" element = {<Register onRouteChange={this.onRouteChange}  setUserID={this.setUserID}/> }/>


                {this.state.isSignedIn ?
                  // if the user is logged in, show the homepage containing available team/user information list
                  <Route path="/authHome" element ={<div><h1 style={{textAlign: 'center'}}>Here should be the homepage for logged in user</h1></div>}/>
                :
                  // if the user cannot login, redirect them to try again
                  <Route path="/authHome" element ={<div>Unable to login. Try again!</div>}/>
                }
              
              </Routes>

            </BrowserRouter>
        );
      }
    }

export default App;

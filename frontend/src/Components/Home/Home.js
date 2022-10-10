import React, { Component } from "react";
import { NavLink } from "react-router-dom";

import "./Home.css";
import welcome from "../../Resources/Images/homepage1.jpg";

class Home extends Component {
    constructor(props) {
        super(props);
    }

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
                    </section>
                </main>
            </>
        );
    }
}

export default Home;


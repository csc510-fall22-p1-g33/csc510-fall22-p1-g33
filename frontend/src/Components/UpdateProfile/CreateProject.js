import React, { Component } from "react";
import 'reactjs-popup/dist/index.css';
import { Link } from "react-router-dom";
import { TextField } from '@mui/material';


class Project extends Component {
    constructor(props) {
        super(props);
        this.state = {
            p_id: null,
            id: "",
            creator: "",

            projectTitle: "",
            projectDetails: "",

            first_project: null,

            saved: true,
            project: "",
            team_id: null,

            users: null
        }
        this.toggleSaved = this.toggleSaved.bind(this);
        this.submitProject = this.submitProject.bind(this);

        this.setProjectTitle = this.setProjectTitle.bind(this);
        this.setProjectDetails = this.setProjectDetails.bind(this);
        this.deleteProject = this.deleteProject.bind(this)
        // this.remove_from_team = this.remove_from_team.bind (this)
    }


    // if this is the first project for this logged in user, then create a new project and a corresponding team
    // if the user has a project already, then load that, they can update that lateras well
    async componentDidMount() {
        this.setState({ creator: this.props.user_id })

        const res = await fetch('http://127.0.0.1:8010/proxy/user/firstproject?user_id=' + this.props.user_id, {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })

        const body = await res.json();
        console.log(body.first_pid)

        this.setState({ p_id: body.first_pid })
        this.state.p_id = body.first_pid

        if (body.first_pid != -1) {
            this.setState({ project: body.first_project })
            this.state.first_project = body.first_project
            this.state.projectTitle = this.state.first_project.project.about.name
            this.state.projectDetails = this.state.first_project.project.about.description
            console.log(this.state.first_project)
        }


        if (body.first_project.project.teams.length > 0) {
            console.log("project team id:", body.first_project.project.teams[0])

            const res0 = await fetch('http://127.0.0.1:8010/proxy/team/' + String(body.first_project.project.teams[0]), {
                method: 'GET',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            })

            const body0 = await res0.json();
            console.log('user ids in team', body.first_project.project.teams[0], "--", body0.team.users)

            let uname_list = []
            let ui = 0
            for (ui = 0; ui < body0.team.users.length; ui++) {
                const res01 = await fetch('http://127.0.0.1:8010/proxy/user/' + String(body0.team.users[ui]), {
                    method: 'GET',
                    headers: {
                        Accept: 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    }
                })

                const body01 = await res01.json();
                console.log('username', ui, '--', body01.user.username)

                uname_list.push(body01.user.username)

            }

            this.setState({ users: uname_list })
            this.state.users = uname_list
        }
    }


    submitProject = async () => {
        let project = {
            pid: this.state.p_id,
            creator: this.state.creator,
            name: this.state.projectTitle,
            description: this.state.projectDetails
        }

        // console.log ('Sending POST project:', project)

        if (this.state.p_id == -1) {
            const res = await fetch('http://127.0.0.1:8010/proxy/project/', {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify(project)
            })

            const body = await res.json();
            // console.log (body)

            this.setState({ p_id: body.id })
            this.state.p_id = body.id

            const res2 = await fetch('http://127.0.0.1:8010/proxy/project/' + body.id, {
                method: 'GET',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            })

            const body2 = await res2.json();
            // console.log (body2)

            // for this new project, a new team will be generated
            const res3 = await fetch('http://127.0.0.1:8010/proxy/team/', {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify({
                    creator: this.props.user_id,
                    project: this.state.p_id
                })
            })

            const body3 = await res3.json();
            // console.log ("newly created team id", body3)
            this.setState({ team_id: body3.id })
            this.state.team_id = body3.id
        }
        else {
            const res = await fetch('http://127.0.0.1:8010/proxy/project/update', {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify(project)
            })

            const body = await res.json();
            // console.log (body)

            this.setState({ p_id: body.id })
            this.state.p_id = body.id
        }

        this.toggleSaved(true)
    }

    // update project title
    setProjectTitle = (e) => {
        // console.log ("project title:", e)
        this.setState({ projectTitle: e })
    }

    // update project description
    setProjectDetails = (e) => {
        // console.log ("project description:", e)
        this.setState({ projectDetails: e })
    }

    toggleSaved = (e) => {
        this.setState({ saved: e })
        this.state.saved = e
    }

    // delete an entire project
    // the logged in user is the owner of this project/team
    deleteProject = async (e) => {
        if (this.state.p_id != null) {
            const res = await fetch('http://127.0.0.1:8010/proxy/project/' + this.state.p_id, {
                method: 'DELETE',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            })

            const body = await res.text();
            console.log(body)

            // this.setState ({saved: false})
            // this.state.saved = false

            const res2 = await fetch('http://127.0.0.1:8010/proxy/team/' + this.state.team_id, {
                method: 'DELETE',
                headers: {
                    Accept: 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            })

            const body2 = await res2.text();
            console.log(body2)

            this.componentDidMount()
        }

    }


    render() {
        return (
            <div style={{ marginLeft: '10%', marginTop: '5%', marginRight: '10%' }}>

                {!this.state.saved &&

                    <div>

                        <br></br><br></br><br></br><br></br>
                        <TextField
                            id="projectTitle"
                            // label="Multiline Placeholder"
                            fullWidth
                            multiline
                            placeholder="Placeholder"
                            variant="standard"

                            value={this.state.projectTitle}
                            label="Project Title"
                            onChange={(e) => {
                                this.setProjectTitle(e.target.value);
                            }}
                        />
                        <br></br><br></br>

                        <TextField
                            id="projectDesc"
                            // label="Multiline Placeholder"
                            fullWidth
                            multiline
                            placeholder="Placeholder"
                            variant="standard"

                            value={this.state.projectDetails}
                            label="Project Description"
                            onChange={(e) => {
                                this.setProjectDetails(e.target.value);
                            }}
                        />


                        <Link className="btn btn-primary"
                            style={{ width: '15%', float: 'right', marginRight: '5%' }}
                            onClick={() => this.submitProject()}
                        > Save Project </Link>
                    </div>
                }


                {
                    this.state.saved &&
                    <div>

                        {this.state.p_id != -1 &&
                            <div>
                                <p>You have added a project. You have initiated a team for this project as well!</p>

                                <p>Your Project Details:</p>
                                Creator User ID: {this.state.creator} <br></br>
                                Project ID: {this.state.p_id} <br></br>
                                Title: {this.state.projectTitle} <br></br>
                                Description: {this.state.projectDetails} <br></br>

                                <br></br>
                                {
                                    this.state.users != null &&
                                    <div>
                                        Who are in this team/project:
                                        {this.state.users.map((data, index) => {
                                            return (
                                                <p>{data}</p>
                                            )
                                        })}
                                    </div>
                                }

                                <Link className="btn btn-primary"
                                    style={{ width: '15%', float: 'right', marginRight: '5%' }}
                                    onClick={() => {
                                        this.setState({ saved: false })
                                        this.state.saved = false
                                    }}
                                > Update Project </Link>

                                <Link className="btn btn-primary"
                                    style={{ width: '15%', float: 'right', marginRight: '5%' }}
                                    onClick={() => this.deleteProject()}
                                > Delete Project/team </Link>
                            </div>
                        }

                        {this.state.p_id == -1 &&
                            <div>
                                <p>You have no project yet!</p>
                                <Link className="btn btn-primary"
                                    style={{ width: '15%', float: 'right', marginRight: '5%' }}
                                    onClick={() => {
                                        this.setState({ saved: false })
                                        this.state.saved = false
                                    }}
                                > Create your first project </Link>
                            </div>
                        }
                    </div>
                }
            </div>
        )
    }
}

export default Project;

import React from "react";
import logo from './logo.svg';
import './index.css'
import './App.css';
import UserList from "./components/User";
import ProjectList from "./components/Project";
import ToDoList from "./components/ToDo";
import Footer from "./components/Footer";
import axios from "axios";
import Menu from "./components/Menu";
import {BrowserRouter, Link, Route} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'projects': {},
            'users': {},
            'todo': {},
        };
    }

    componentDidMount() {
        axios
            .get('http://localhost:8000/api/projects/?format=json')
            .then(response => {this.setState({'projects': response.data});})
            .catch(error => console.log(error));
        axios
            .get('http://localhost:8000/api/users/?format=json')
            .then(response => {this.setState({'users': response.data});})
            .catch(error => console.log(error));
        axios
            .get('http://localhost:8000/api/todo/?format=json')
            .then(response => {this.setState({'todo': response.data});})
            .catch(error => console.log(error));
    }

    render() {
        return ([
                <BrowserRouter>
                <div className={'App-header'}>
                    <Menu menu={Menu}/>
                        <div>
                            <Route exact path='/projects' component={() => 
                            <ProjectList items={this.state.projects} />} />
                            <Route exact path='/users' component={() => 
                            <UserList users={this.state.users} />} />
                            <Route exact path='/todo' component={() => 
                            <ToDoList items={this.state.todo} />} />
                        </div>
                    <Footer footer={Footer}/>
                </div>
                </BrowserRouter>
            ]
        );
    }
}


export default App;

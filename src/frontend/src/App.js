import React from "react";
import logo from './logo.svg';
import './index.css'
import './App.css';
import UserList from "./components/User";
import Footer from "./components/Footer";
import axios from "axios";
import Menu from "./components/Menu";
import {BrowserRouter, Link, Route} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'count': 0,
            'users': [],
            'usersPgPrev': '',
            'usersPgNext': '',
        };
    }

    componentDidMount() {
        axios
            .get('http://localhost:8000/api/users/?format=json')
            .then(response => {
                this.setState({'count': response['data']['count']});
                this.setState({'users': response['data']['results']});
                this.setState({'usersPgPrev': response['data']['previous']});
                this.setState({'usersPgNext': response['data']['next']});
                this.setState({'footer': Footer});
                this.setState({'menu': Menu});
            })
            .catch(error => console.log(error));
    }

    render() {
        return ([
            <BrowserRouter>
                <div className={'App-header'}>
                    <Menu menu={this.state.menu}/>
                        <div>
                            <UserList
                                users={this.state.users}
                                prev={this.state.usersPgPrev}
                                next={this.state.usersPgNext}
                            />
                        </div>
                    <Footer footer={this.state.footer}/>
                </div>
            </BrowserRouter>
            ]
        );
    }
}


export default App;

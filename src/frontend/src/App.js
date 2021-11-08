import React from "react";
import logo from './logo.svg';
import './index.css'
import './App.css';
import UserList from "./components/User";
import Footer from "./components/Footer";
import axios from "axios";
import Menu from "./components/Menu";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios
            .get('http://localhost:8000/api/users/')
            .then(response => {
                const users = response.data;
                this.setState({'users': users})
                this.setState({'footer': Footer})
                this.setState({'menu': Menu})
            })
            .catch(error => console.log(error))
    }

    render() {
        return ([
                <div className={'App-header'}>
                    <Menu menu={this.state.menu}/>
                    <div>
                        <UserList users={this.state.users}/>
                    </div>
                    <Footer footer={this.state.footer}/>
                </div>
            ]
        )
    }
}


export default App;

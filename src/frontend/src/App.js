import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./User";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
       const users = [
           {
               'first_name': 'Фёдор',
               'last_name': 'Достоевский',
               'email': 'fedor_dostoyevskiy@example.com'
           },
           {
               'first_name': 'Александр',
               'last_name': 'Грин',
               'email': 'alex_green@example.com'
           },
       ]
       this.setState(
           {
               'users': users
           }
       )

    }

    render() {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
    }
}


export default App;

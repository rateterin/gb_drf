import React from "react";
import {BrowserRouter, Link, Route} from 'react-router-dom';


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}


const UserList = (props) => {
    console.log(props)
    const isPrev = Boolean(typeof props.prev)
    const isNext = Boolean(typeof props.next)
    console.log(
        `prev = ${ props.prev }`,
        `next = ${ props.next }`,
        `isNext = ${ isNext }`,
        `isPrev = ${ isPrev }`,
    )

    const isPaginated = isPrev || isNext
    return (
        <>
            <table>
                <tr>
                    <th>
                        First name
                    </th>
                    <th>
                        Last Name
                    </th>
                    <th>
                        eMail
                    </th>
                </tr>
                {props.users.map((user) => <UserItem user={user} />)}
            </table>
        { isPaginated &&
            <table>
                <tr>
                    <td>{isPrev ? <Link to={props.prev}>Prev</Link> : 'Prev' }</td>
                    <td>{isNext ? <Link to={props.next}>Next</Link> : 'Next' }</td>
                </tr>
            </table>
        }
        </>
    )
}


export default UserList

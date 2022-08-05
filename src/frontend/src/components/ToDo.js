import React from "react";


const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.project}</td>
            <td>{item.text}</td>
            <td>{item.created_date}</td>
            <td>{item.updated_date}</td>
            <td>{item.user_created}</td>
            <td>{item.complete}</td>
        </tr>
    )
}


const ToDoList = ({items}) => {
    return (
        <div>
            <table>
                <tr>
                    <th>Project</th>
                    <th>Text</th>
                    <th>Created</th>
                    <th>Updated</th>
                    <th>User created</th>
                    <th>Complete</th>
                </tr>
                {items.map((item) => <ToDoItem item={item} />)}
            </table>
        </div>
    )
}


export default ToDoList

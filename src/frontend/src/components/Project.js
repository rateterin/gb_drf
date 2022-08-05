import React from "react";


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.name}</td>
            <td>{item.link_to_repo}</td>
            <td>{item.users}</td>
        </tr>
    )
}


const ProjectList = ({items}) => {
    return (
        <div>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Link to repo</th>
                    <th>Users</th>
                </tr>
                {items.map((item) => <ProjectItem item={item} />)}
            </table>
        </div>
    )
}


export default ProjectList

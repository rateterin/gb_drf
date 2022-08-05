import React from "react";
import { Link } from "react-router-dom";

const Menu = () => {
    return (
        <nav>
            <Link to='/projects'>Projects</Link>&nbsp;
            <Link to='/users'>Users</Link>&nbsp;
            <Link to='/todo'>ToDo</Link>&nbsp;
        </nav>
    )
}

export default Menu
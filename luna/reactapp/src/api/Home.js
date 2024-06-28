import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
    return (
        <div>
            <h2>Home Page</h2>
            <p>Welcome to the Home Page!</p>
            <Link to="/create-user">Create User</Link>
        </div>
    );
}

export default Home;

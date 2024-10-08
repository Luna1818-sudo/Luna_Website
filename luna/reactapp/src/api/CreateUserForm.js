// src/CreateUserForm.js
import React, { useState } from 'react';
import { Link , useNavigate } from 'react-router-dom';
// import CryptoJS from 'crypto-js';

function CreateUserForm() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [first_name, setfirst_name] = useState('');
    const [last_name, setlast_name] = useState('');
    const [createdUsername, setCreatedUsername] = useState(null);  // State variable to store created username
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        // const hashedPassword = CryptoJS.SHA256(password).toString();

        const response = await fetch('http://127.0.0.1:8000/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                 username,
                 first_name,
                 last_name,
                  email,
                   password,
                }),
        });

        const data = await response.json();
        console.log(response)
        if (response.ok) {
            setCreatedUsername(username);  // Set the created username in state
            alert('User created successfully!');

            const response_get = await fetch(`http://127.0.0.1:8000/api/accountsearch/${username}`)
            const getData = await response_get.json();

            // console.log(getData);

            // console.log(getData.password)

            // const fetched_jwtid = getData.username
            const fetched_password = getData.password

            localStorage.setItem('jwtid', fetched_password)

            navigate(`user/${username}`)

            // if (response_get.ok) {
            // //     console.log(getData); // Process the fetched user data here
            // //     navigate(`/user/${username}`);

          
        } else {
            alert('Error creating user: ' + JSON.stringify(data));
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>First Name:</label>
                    <input
                        type="text"
                        value={first_name}
                        onChange={(e) => setfirst_name(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Last Name:</label>
                    <input
                        type="text"
                        value={last_name}
                        onChange={(e) => setlast_name(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Create User</button>
                <br />
                <Link to="/">Back to Home</Link>
            </form>
            {createdUsername && (  // Conditionally render the created username
                <div>
                    <h3>User Created: {createdUsername}</h3>
                </div>
            )}
        </div>
    );
}

export default CreateUserForm;

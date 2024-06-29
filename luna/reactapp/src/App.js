import React from 'react';
import CreateUserForm from './api/CreateUserForm';
import DashBoard from './api/DashBoard'
import { BrowserRouter as Router, Route, Routes, Switch } from 'react-router-dom';
import Home from './api/Home';

function App() {
    return (
      <Router>
        <div className="App">
            {/* <h1>Create User</h1> */}
            <Routes>
              <Route exact path='/' Component={Home} />
              <Route path="/createuser" Component={CreateUserForm} />
              <Route path="user/<username>/" Component={DashBoard} />
            </Routes>
            <CreateUserForm />
        </div>
      </Router>  
    );
}

export default App;


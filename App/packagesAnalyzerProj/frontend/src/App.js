
import React from 'react';
import SearchPage from './components/SearchPage';
import StatsComponent  from  './components/StatisticsDirectoryComponents/StatsComponent';
import AboutComponent from './components/AboutComponent';
import NpmSecurityToTable from './components/NpmSecurityComponents/NpmSecurityToTable';
import './App.css';
import Home from './components/Home';


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  
} from "react-router-dom";
function App() {

  const BarStyling = {background:"#9aad93", border:"double", padding:"0.6rem", display: 'inline'}
  const Styling = {  margin: '1%'};

  return (
    <div className="App">
      
<Router>
            <div  style={BarStyling} className="row">
             <Link  style={Styling} to="/">Home</Link>  
            
              <Link style={Styling} to="/about">About</Link>
           
            
              <Link style={Styling} to="/search_page">Search Page</Link>
            
            
              <Link style={Styling} to="/stats_page">Stats</Link>
              <Link style={Styling} to="/npm_security_table">Npm Security To Table</Link>

              
              </div>



        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/about">
            <AboutComponent />
          </Route>
          <Route path="/search_page">
          <SearchPage />
          </Route>
          <Route path="/stats_page">
            <StatsComponent />
          </Route>
          <Route path="/npm_security_table">
            <NpmSecurityToTable />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
    </Router>

            </div>


  );

  
  
}

export default App;

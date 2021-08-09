
import SearchPage from './components/SearchPage';
import StatsComponent  from  './components/StatisticsDirectoryComponents/StatsComponent';
import AboutComponent from './components/AboutComponent';
import './App.css';
import Home from './components/Home';


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  
} from "react-router-dom";
function App() {

  const BarStyling = {background:"#9aad93", border:"double", padding:"0.6rem", display: 'inline-block'}
  

  return (
    <div className="App">
      
<Router>
            <div  style={BarStyling} className="row">
             <Link  to="/">Home</Link>  
            
              <Link to="/about">About</Link>
           
            
              <Link to="/search_page">Search Page</Link>
            
            
              <Link to="/stats_page">Stats</Link>
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
          <Route path="/">
            <Home />
          </Route>
        </Switch>
    </Router>

            </div>


  );

  
  
}

export default App;

import React from 'react';
// import '../App.css';
import {
    Card, CardText, CardBody,
    CardTitle, CardSubtitle, ListGroup, ListGroupItem 
  } from 'reactstrap';


class AboutComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {};
    }
  
    render() {
      return (
          <div >
            <h2>  About  : </h2>
           
            <a href="https://github.com/rtgfd157/PackageAnalyzer/" target="_blank">GitHub of Project link </a>  

        <Card>
        <CardBody>
          <CardTitle tag="h5">What this project do?</CardTitle>
          <CardSubtitle tag="h6" className="mb-2 text-muted">The project will search for npm package</CardSubtitle>

            <CardText > Searching by: 
            
                <ListGroup>
      <ListGroupItem style={{textAlign:"left"}}>1) ElasticSearch </ListGroupItem>
      <ListGroupItem style={{textAlign:"left"}}>2)  DB-postgres</ListGroupItem>
      <ListGroupItem style={{textAlign:"left"}}>3) api- https://registry.npmjs.org/package name/latest</ListGroupItem>
    
        </ListGroup>
                
               <u> Each package will show also his dependency</u>.</CardText>
        </CardBody>


        </Card>

          </div>
       
      );
    }
  }
  
  export default AboutComponent  
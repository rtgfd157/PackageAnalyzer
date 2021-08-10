import React from 'react';
import DbComponent from './DbComponent';
import ElasticSearchComponent from './ElasticSearchComponent';
import {
    CardDeck
  } from 'reactstrap';


class StatsComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {};
    }
  
    render() {
      return (
          <div style={{margin: '10px'}}>
            <br/>
       <h2 style={{margin: '10px', padding: '1%'}}> <u>Stats Component : </u> </h2>
       <CardDeck style={{display: 'flex', flexDirection: 'row', justifyContent: 'center'}}>
       <DbComponent></DbComponent>
       <ElasticSearchComponent/>
       </CardDeck>
       </div>
      );
    }
  }
  
  export default StatsComponent  
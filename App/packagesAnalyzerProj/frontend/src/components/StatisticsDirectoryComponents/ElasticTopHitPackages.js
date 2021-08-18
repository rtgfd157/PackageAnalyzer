import React from 'react';
import {
  ListGroup, ListGroupItem 
} from 'reactstrap';

const ElasticTopHitPackages = ({ packages = [] }) => {


  return (
    <>
      <div>
        <ListGroup>
          {packages.map((data, index) => {
            if (data) {

              return (
                <div key={data.id}>
                  
                  <ListGroupItem> {data}</ListGroupItem> 
                </div>
              )
            }
            return null
            
          })}



      </ListGroup>

      </div>
    </>
  );
}

export default ElasticTopHitPackages
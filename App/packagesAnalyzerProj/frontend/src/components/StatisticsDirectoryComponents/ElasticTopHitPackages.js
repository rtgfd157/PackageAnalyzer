import React from 'react';


const ElasticTopHitPackages = ({ packages = [] }) => {


  return (
    <>
      <div>
        <ul>

          {packages.map((data, index) => {
            if (data) {

              return (
                <div key={data.id}>
                  
                  <li> {data}</li> 



                </div>
              )
            }
            return null
            
          })}



        </ul>
      </div>
    </>
  );
}

export default ElasticTopHitPackages
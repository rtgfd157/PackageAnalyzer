import React from 'react';
import PackageComponent from './PackageComponent';


const PackagesDependecies = ({node=[]}) => {
  return (
    <>

    <div>
      <ul>

      { node.map((data,index) => {
        if (data) {
          return (
            <div key={data.id}>
              { data.npm_name  && <PackageComponent packages =  {data} >      
              
              <li>name: {data.npm_name} , Version: {data.version}  </li>
              
              </PackageComponent>
              }
              

              
	        </div>	
    	   )	
    	 }
    	 return null
    }) }
      


      </ul>
    </div>
    </>
  );
}

export default PackagesDependecies
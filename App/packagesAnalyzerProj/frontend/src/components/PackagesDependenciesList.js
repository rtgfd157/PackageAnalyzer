import React from 'react';

const PackagesDependenciesList = ({packagesList=[]}) => {
  return (
    <>

    <div>

    { packagesList.map((data,index) => {
        if (data) {
          return (
            <div key={data.id}>
              <li>name: {data.npm_package_dep_name} , Version: {data.version} </li>
	        </div>	
    	   )	
    	 }
    	 return null
    }) }



    </div>
    </>
  );
}

export default PackagesDependenciesList
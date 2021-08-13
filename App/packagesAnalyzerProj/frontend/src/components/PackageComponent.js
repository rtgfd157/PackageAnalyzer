import React from 'react';
import PackagesDependecies from './PackagesDependecies';

      const PackageComponent = ({packages=[], bg_color}) => {
       // console.log('color: '+ bg_color);
  const BarStyling = {textAlign:"left", width:"20rem",backgroundColor :bg_color , border:"none", padding:"0.5rem"};

  return (
    <>

    <div>

      <ul>
        
      { packages.npm_name  && <li  style={BarStyling}> name: {packages.npm_name} , version: {packages.version} </li>}
      { packages.npm_name  &&   <p style={{textAlign:"left"}}> number of dependecies: {packages.dependencies.length}</p>  }

      <PackagesDependecies node = {packages.dependencies} />
      </ul>

    </div>
    </>
  );
}

export default PackageComponent
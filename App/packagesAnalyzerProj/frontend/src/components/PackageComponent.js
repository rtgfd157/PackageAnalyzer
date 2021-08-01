import React from 'react';
import PackagesDependecies from './PackagesDependecies';

const PackageComponent = ({packages=[]}) => {
  return (
    <>

    <div>

      <ul>
      { packages.npm_name  && <li  style={{textAlign:"left"}}> name: {packages.npm_name} , version: {packages.version} </li>}
      { packages.npm_name  &&   <p style={{textAlign:"left"}}> number of dependecies: {packages.dependencies.length}</p>  }

      <PackagesDependecies node = {packages.dependencies} />
      </ul>

    </div>
    </>
  );
}

export default PackageComponent
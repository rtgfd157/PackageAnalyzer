import React from 'react';
import PackageComponent from './PackageComponent';


const PackagesDependecies = ({ node = [] }) => {



  let randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
  return (
    <>
      <div>
        <ul>

          {node.map((data, index) => {
            if (data) {

              return (
                <div key={data.id}>
                  {data.npm_name && <PackageComponent packages={data} bg_color={randomColor} />


                  }



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

export default PackagesDependecies
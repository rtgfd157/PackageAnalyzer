import React from 'react';



const PackageSearchResult = ({npm_name, version, bad_search_message }) => {
  return (
    <div data-testid="search-res-1">
    <p style={{ color: 'red' }} > {bad_search_message?'search came without results, please try again':''} </p>
    
        {npm_name &&   <h2> Name: {npm_name} version: {version}</h2>}           
    </div>
  );
}

export default PackageSearchResult
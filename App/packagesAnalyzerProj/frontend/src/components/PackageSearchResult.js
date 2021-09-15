import React from 'react';



const PackageSearchResult = ({ bad_search_message }) => {
  return (
    <div data-testid="search-res-1">
    <p style={{ color: 'red' }} > {bad_search_message?'search came without results, please try again':''} </p>
    
    </div>
  );
}

export default PackageSearchResult
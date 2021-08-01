import React from 'react';


const SearchBar = ({handleSubmit , handleChange , search_word }) => {
  const BarStyling = {width:"20rem",background:"#F2F1F9", border:"none", padding:"0.5rem"};
  return (
    
    <form onSubmit={handleSubmit}>
        <label> 
          <input 
          style={BarStyling}
          type="text"
           name="search_word"
            value={search_word}
             onChange={handleChange}
              />
        </label>
        <input type="submit" value="Submit" />
      </form>
  );
}

export default SearchBar
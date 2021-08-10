import React from 'react';


const SearchBar = ({handleSubmit , handleChange , search_word }) => {
  const BarStyling = {width:"20rem",background:"#F2F1F9", border:"groove", padding:"0.5rem" };
  const BarStylingForm = {background:"#F2F1F9", padding:"0.5rem", margin: '1%'};
  const ButtonStyle = {borderRadius: '8px' ,padding:"0.4rem"};
  return (
    
    <form  style={BarStylingForm} onSubmit={handleSubmit}>
        <label> 
          <input 
          style={BarStyling}
          type="text"
           name="search_word"
            value={search_word}
             onChange={handleChange}
              />
        </label>
        <input style={ButtonStyle} type="submit" value="Submit" />
      </form>
  );
}

export default SearchBar
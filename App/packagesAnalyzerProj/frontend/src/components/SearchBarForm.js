import React from 'react';
import {  Form, FormGroup, Label, Input } from 'reactstrap';


const SearchBar = ({handleSubmit , handleChange_search_word, handleChange_search_version , search_version , search_word }) => {
  const BarStyling = {width:"20rem",background:"#F2F1F9", border:"groove", padding:"0.5rem" };
  const BarStylingForm = {background:"#F2F1F9", padding:"0.5rem", margin: '1%'};
  const ButtonStyle = {borderRadius: '8px' ,padding:"0.4rem"};
  return (
    
    <Form data-testid="search-bar-1"  style={BarStylingForm} onSubmit={handleSubmit}>
      <FormGroup>
        <Label> 
          Npm Name: 
          <Input 
          style={BarStyling}
          type="text"
           name="search_word"
            value={search_word}
             onChange={handleChange_search_word}
              />
        </Label>

        </FormGroup>

        <FormGroup>
        <Label> 
          Version: 
          <Input 
          style={BarStyling}
          type="text"
           name="search_version"
            value={search_version}
             onChange={handleChange_search_version}
              />
        </Label>
        </FormGroup>
        <input style={ButtonStyle} type="submit" value="Submit" />
        
      </Form>
  );
}

export default SearchBar
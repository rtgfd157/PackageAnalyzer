import React from 'react';
import {  Form, FormGroup, Label, Input } from 'reactstrap';




const PredictBarForm = ({handleSubmit , handleChange_number_of_maintainers, handleChange_unpackedsize , unpackedsize , number_of_maintainers }) => {
  const BarStyling = {backgroundColor: 'grey' , width:"20rem",background:"#F2F1F9", border:"groove", padding:"0.5rem" };
  const BarStylingForm = {background:"#F2F1F9", padding:"0.5rem", margin: '1%'};
  const ButtonStyle = {borderRadius: '8px' ,padding:"0.4rem"};
 

  return (
    <Form data-testid="search-bar-3"  style={BarStylingForm} onSubmit={handleSubmit}>
        <FormGroup>
        <Label> 
         <b> Number Of maintainers: </b>
         
          <Input 
          style={BarStyling}
          type="number"
           name="number_of_maintainers"
            value={number_of_maintainers}
             onChange={handleChange_number_of_maintainers}
             disabled
              />
              </Label>
        </FormGroup>
        
        <FormGroup>
        <Label> 
         <b>  Package Size: </b>

          <Input 
          style={BarStyling}
          type="number"
           name="unpackedsize"
            value={unpackedsize}
             onChange={handleChange_unpackedsize}
             disabled
              />
        <input style={ButtonStyle} type="submit" value="Post" />
        </Label>
        </FormGroup>
      </Form>
  );
}

export default PredictBarForm
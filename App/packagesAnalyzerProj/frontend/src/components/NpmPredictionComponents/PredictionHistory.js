import React from 'react';
import {
    Card, CardText, CardBody,
    CardTitle, CardSubtitle
  } from 'reactstrap';


class PredictionHistory extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
          data:[],
          counnt_npm_sec : 'didnt fetch successfuly yet',
          is_mount :false
          
      };
      this.fetch_data = this.fetch_data.bind(this);
      
      this.lst_5_predictions = 'http://127.0.0.1:8000/api/mlrequests_last_5/' ; 
      this.Styling = { padding:"0.5rem", margin: '1%'};


      
    }
    

    async componentDidMount() {
        let  data = await  this.fetch_data(this.lst_5_predictions );
        if (data){
            // console.log('data : '+ data);
              this.setState({ data : data});
              //this.setState({ is_mount : true});
            }
       
      }

      async fetch_data(adress){
        return  await  fetch(adress)
       .then(response => response.json())
       .catch(error => {
        console.log('error in fetch');
        throw(error);
        
        })}
  
    render() {
      
      return (
                  <div>
                    <h2> History Prediction: <u></u> </h2>

                    {this.state.data.map((data, index) => {
            if (data) {

              return (
                <div key={data.id}>
              
                   <Card>
                        <CardBody>
                        <CardTitle tag="h5">Input : {data.input_data}. Response: {data.response}</CardTitle>
                        <CardSubtitle tag="h6" className="mb-2 text-muted">{data.created_at} - {data.parent_mlalgorithm} </CardSubtitle>

                        <CardText>{data.feedback} </CardText>
                        <CardText>{data.full_response}</CardText>
                        </CardBody>
                    </Card>


                   



                </div>
              )
            }
            return null
          })}
                   
            
            </div>
            ) 

           
                
                
    }
  }
  
  export default PredictionHistory  

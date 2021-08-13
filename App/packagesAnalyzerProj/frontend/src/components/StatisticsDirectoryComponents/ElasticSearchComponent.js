import React from 'react';
import {
    Card, CardText, CardBody,
    CardTitle, CardSubtitle, ListGroup, ListGroupItem 
  } from 'reactstrap';

  import ElasticTopHitPackages from './ElasticTopHitPackages';

class ElasticSearchComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
          el_pack_count:0,
          top_packages: []
      };
      this.fetch_data = this.fetch_data.bind(this);
      this.adress_search_el_packages_tree_count = 'http://127.0.0.1:8000/api/count_doc_pacakges_elastic/';
      this.Styling = {background:"#F2F1F9", padding:"0.5rem", margin: '1%', flex: 1};
      this.adress_top_packages = 'http://127.0.0.1:8000/api/top_doc_pacakges_elastic/'
    }
    

    async componentDidMount() {
       let  data = await  this.fetch_data(this.adress_search_el_packages_tree_count );
       console.log(' *****1***** ')
       if (data){
        console.log('data : '+ data);
         this.setState({ el_pack_count : data[0]});
       }else{
        this.setState({ el_pack_count : '---'});
       }

       console.log(' *****4***** ')
       let  data_packages = await  this.fetch_data(this.adress_top_packages);
       if (data_packages){
        console.log('data_packages : '+ data_packages);
         this.setState({ top_packages : data_packages['list_r']});
       }else{
         console.log('emptyyy ');
        this.setState({ top_packages : []});
       }

       
      }

      async fetch_data(adress){
        return  await  fetch(adress)
       .then(response => response.json())
       .catch(error => {
        this.setState({ el_pack_count : ' '});
        this.setState({ top_packages : []});
        
        console.log('error in fetch');
        throw(error);
        
        })}
  
    render() {
      return (
          <div>
       <h2> Elastic Stats Component : </h2>
       <Card style={this.Styling}>
       <CardBody>
         <CardTitle tag="h5"><u> Elastic Search  </u></CardTitle>
         <CardSubtitle tag="h6" className="mb-2 text-muted">Number of package Trees in ElasticSearch.</CardSubtitle>

           <CardText > Result: 
           
               <ListGroup>
     <ListGroupItem style={{textAlign:"left"}}> Number of Packages in ElasticSearch Server: {this.state.el_pack_count} </ListGroupItem>
   
       </ListGroup>
               
              <u>  http://localhost:9200/elastic_packages_tree/_mapping/?pretty </u>
              <u>  http://127.0.0.1:8000/api/count_doc_pacakges_elastic/</u></CardText>
              
              
              {  this.state.top_packages.length > 0  &&  <CardTitle tag="h6"><u>  Top Packages:   </u></CardTitle> }    
       <CardText> 

        
       <ElasticTopHitPackages packages = {this.state.top_packages} />
       </CardText>
        
       
       
       </CardBody>


       </Card>
       </div>
      );
    }
  }
  
  export default ElasticSearchComponent  

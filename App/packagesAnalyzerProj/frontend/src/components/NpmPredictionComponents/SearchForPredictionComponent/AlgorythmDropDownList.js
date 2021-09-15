import React from 'react';
import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';

class AlgorythmDropDownList extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
            list_algo:[],
          is_mount :false,
          dropdownOpen: false,
          chosen_algo_for_prediction: props.chosen_algo_for_prediction
          
      };
      this.fetch_data = this.fetch_data.bind(this);
      
      this.get_all_algo = 'http://127.0.0.1:8000/api/mlalgorithms/' ; 
      this.Styling = { padding:"0.5rem", margin: '1%'};


      //this.handle_change_algorythm_list = this.props.handle_change_algorythm_list.bind(this);
      this.toggle = this.toggle.bind(this);

      
    }

   

     toggle(){
        
          this.setState(prevState => ({   dropdownOpen: !prevState.dropdownOpen }));
          console.log(this.state.dropdownOpen )

    }

    async componentDidMount() {
        let d= await this.fetch_data(this.get_all_algo);
        this.setState({ list_algo : d});
       
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
                    <p>  Algo of Prediction:  <u></u> </p>
                   
                   


                        <Dropdown isOpen={this.state.dropdownOpen} toggle={this.toggle}>
                        <DropdownToggle caret>
                        Dropdown -  
                        {     this.props.chosen_algo_for_prediction && this.props.chosen_algo_for_prediction.name }
                        - {     this.props.chosen_algo_for_prediction && this.props.chosen_algo_for_prediction.version }
                        </DropdownToggle>
                        <DropdownMenu container="body">
                        

                        {this.state.list_algo.map(algo => <div key={algo.id}>
                            <DropdownItem 
                            id={algo.id}
                             key={algo.id}
                             version={algo.version}
                             current_status={algo.current_status}
                             name = {algo.name}
                            onClick={this.props.handle_change_algorythm_list}
                            
                            >{algo.name}  {algo.current_status}&{algo.version} </DropdownItem> </div>
                                   ) } 
                            
                        </DropdownMenu>
                        </Dropdown>
            </div>
            ) 

           
                
                
    }
  }
  
  export default AlgorythmDropDownList  

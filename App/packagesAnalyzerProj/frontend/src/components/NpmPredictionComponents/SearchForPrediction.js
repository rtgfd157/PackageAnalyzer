import React from 'react';
import AlgorythmDropDownList from './SearchForPredictionComponent/AlgorythmDropDownList' ;
import PackageSearchForPrediction from './PackageSearchForPrediction';
import PredictionPost from './PredictionPost';

class SearchForPrediction extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
          data:{},
          counnt_npm_sec : 'didnt fetch successfuly yet',
          is_mount :false,
          chosen_algo_for_prediction: null,
          number_of_maintainers: 0 ,
          unpackedsize: 0
          
      };
      this.fetch_data = this.fetch_data.bind(this);
      
   
      this.Styling = { padding:"0.5rem", margin: '1%'};

      this.handle_change_algorythm_list =this.handle_change_algorythm_list.bind(this);
      this.handle_change_number_of_maintainers_unpackedsize =this.handle_change_number_of_maintainers_unpackedsize.bind(this);


    }
    
    async componentDidMount() {
       
       
      }

   async handle_change_number_of_maintainers_unpackedsize(number_of_maintainers, unpackedsize){
     console.log(' handle_change_number_of_maintainers_unpackedsize');
     console.log(number_of_maintainers+ '  $$$ ' + unpackedsize)

     await this.setState({ unpackedsize : unpackedsize,
     number_of_maintainers: number_of_maintainers
        });
   }

   async  handle_change_algorythm_list (event){
    // algo
     // console.log('@@ '+ algo.name)
    //  let d = {}
    //  d['version'] = algo['version']
    //  d['name'] = algo['name']

    //  //let d = {'algo_name':algo.name , 'algo_version':algo.version } ; 
    //  console.log('d '+d);

     //console.log(algo['version']);
    //  console.log(' event '+ event.currentTarget.textContent);
    //  console.log(' event '+ event.currentTarget.getAttribute('current_status'));
    //  console.log(' event '+ event.currentTarget.getAttribute('name'));
    //  console.log(' event '+ event.currentTarget.getAttribute('version'));
    //  console.log(' event '+ event.currentTarget.getAttribute('id'));
    let d = {}

    d['current_status'] = event.currentTarget.getAttribute('current_status'); 
    d['name'] = event.currentTarget.getAttribute('name'); 
    d['version'] = event.currentTarget.getAttribute('version'); 
    d['id'] = event.currentTarget.getAttribute('id'); 


     await this.setState({
      chosen_algo_for_prediction : d 

     })



     //await this.setState({ chosen_algo_for_prediction : event.currentTarget.textContent })
      // await this.setState({ chosen_algo_for_prediction : event.currentTarget.textContent }, () => {
      //   console.log(this.state.chosen_algo_for_prediction, 'event.currentTarget.textContent');
      // });
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
                    <h2> Number Prediction: <u></u> </h2>
                    <AlgorythmDropDownList 
                    handle_change_algorythm_list= {this.handle_change_algorythm_list}
                    chosen_algo_for_prediction ={this.state.chosen_algo_for_prediction}
                    />
                    <PackageSearchForPrediction
                    handle_change_number_of_maintainers_unpackedsize = {this.handle_change_number_of_maintainers_unpackedsize}
                    
                    />
                    <PredictionPost 
                    
                    number_of_maintainers= {this.state.number_of_maintainers}
                    unpackedsize= {this.state.unpackedsize}
                    chosen_algo_for_prediction= {this.state.chosen_algo_for_prediction} />

            </div>
            ) 
        
    }
  }
  
  export default SearchForPrediction  

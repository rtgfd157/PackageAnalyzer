import React from 'react';
import PackageSearchResult from '../PackageSearchResult';
//import Loader from 'react-loader'; // fetch symbol animation
//import Loader from "react-loader-spinner";

import LoaderSpin from '../LoaderSpin';
import SearchBar from '../SearchBarForm';

class PackageSearchForPrediction extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      search_word: '',
      search_version: '',
       pack_data: [],
       dep_data:[],
       bad_search_message: false,
       is_dep : false,
       data_from_res_manipulate: [],
       message_after_search: '',
       is_fetching: false,
       unpackedSize:'',
       number_of_maintainers:''

       };

       // need to add logic to message_not_input


    this.handleChange_search_word = this.handleChange_search_word.bind(this);
    this.handleChange_search_version = this.handleChange_search_version.bind(this);

    this.handleSubmit = this.handleSubmit.bind(this);

      

  }


  async handleChange_search_word(event) {
    // this.setState({[event.target.name]: event.target.value});
    await this.setState({search_word: event.target.value});
  }

  async handleChange_search_version(event) {
    // this.setState({[event.target.name]: event.target.value});
    await this.setState({search_version: event.target.value});
  }




   async handleSubmit(event){
    this.setState({bad_search_message  : false});
     console.log(' ^^^ '+this.state.search_version);
    event.preventDefault();
    if (   this.check_not_empty_search_word() === false  ){
      console.log('check emptyyy');
      return 
    } 


    this.setState({ is_fetching : true});
  

    var k = this.state.search_version
    console.log(' k : '+k);
    

    let send = ''; 
    for (var i = 0; i < k.length; i += 1) {
      if ( k[i] === '.'){
        send += 'qqq';
      }else{
        send+= k[i];
      }
       
      }
    let p= await this.fetch_data('http://127.0.0.1:8000/api/packageSearchForPrediction/'+this.state.search_word+'/'+send+'/');
    //this.setState({ tree_data : p.data});
    
    console.log('p[unpackedSize] '+p['unpackedSize']);



    

    
    this.setState({ is_fetching : false});
 
  
    if (typeof p['unpackedSize'] !== 'undefined'  &&  typeof p['number_of_maintainers'] !== 'undefined' ) {
        
        await this.setState({ unpackedSize : p['unpackedSize'],
        number_of_maintainers: p['number_of_maintainers']

    
    });

    this.props.handle_change_number_of_maintainers_unpackedsize(this.state.number_of_maintainers ,this.state.unpackedSize )


      console.log('good response');
      this.insert_good_return();
    }else{
      console.log('search_no_result');
      this.search_no_result()
    }
  
      }
////////////////////////////////////////////////////

      async fetch_data(adress){
        return  await  fetch(adress)
       .then(response => response.json())
       .catch(error => {
        this.setState({ is_fetching : false});
        this.setState({ pack_data : []});
          this.setState( { dep_data : [] });
          this.setState( { npm_name : '' });
          this.setState( { search_version : '' });
        console.log('error in fetch'+ error);
        throw(error);
        
        })
       
     }
    
///////////////////////////////////////////////////////
        check_not_empty_search_word(){

          if(  !(this.state.search_word) &&   !(this.state.search_version)    ){
            console.log('return false');
            this.setState({ message_after_search : ' Please enter both inputs values'});
            this.setState({ pack_data : []});
          this.setState( { dep_data : [] });
          this.setState( { npm_name : '' });
          this.setState( { search_version : '' });
            //this.empty_search();
          return false
        }
        else{
          console.log('return true');
          return true
        } 
      }
        
///////////////////////////////////////////////////////       
        async insert_good_return(){
          
          this.setState({bad_search_message  : false});
          this.setState({is_dep  : true});
          

        }


/////////////////////////////////////////////////////////
        search_no_result(){
          console.log("empty111")
          this.setState({bad_search_message  : true});
          this.setState({ pack_data : []});
          this.setState( { number_of_maintainers : '-' });
          this.setState( { unpackedSize : '-' });

          this.setState( { npm_name : '' });
          this.setState( { search_version : '' });
          
          this.setState( { message_after_search : 'search came without results, please try again' })


          
        }
//////////////////////////////////////////////////////////
       // <div>{!!(this.state.search_word)?this.state.search_word:"whatever you want"}</div>

       
       

  render() {
    return (
      <div  data-testid="search-page-2" style={{ padding: "left" }}>
      

      <SearchBar handleSubmit= {this.handleSubmit}
       handleChange_search_word= {this.handleChange_search_word}
       handleChange_search_version= {this.handleChange_search_version}
       search_version = {this.state.search_version}
         search_word = {this.state.search_word}
         /> 

      { this.state.is_fetching  && <LoaderSpin/>}

      <PackageSearchResult   
     
      bad_search_message= {this.state.bad_search_message}
      />
    




      </div>
    );
  }
}

export default PackageSearchForPrediction
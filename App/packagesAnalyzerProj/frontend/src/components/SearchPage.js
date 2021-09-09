import React from 'react';
import PackageSearchResult from './PackageSearchResult';
import PackageComponent from './PackageComponent';
//import Loader from 'react-loader'; // fetch symbol animation
//import Loader from "react-loader-spinner";

import LoaderSpin from './LoaderSpin';
import SearchBar from './SearchBarForm';

class SearchPage extends React.Component {
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
       tree_data: [],
       is_fetching: false

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

  /*
    // loop for making tree 
    
      tree_data [   
          npm_name : xxxxx,
          version :  yyyyy,
          dependecies: [
                          npm_name : xxxxx,
                          version :  yyyyy,
                            dependecies: [ ......]
          ] ]

    */
   

    

   async handleSubmit(event){
    this.setState({bad_search_message  : false});
     console.log(' ^^^ '+this.state.search_version);
    event.preventDefault();
    if (   this.check_not_empty_search_word() === false  ){
      console.log('check emptyyy');
      return 
    } 


    this.setState({ is_fetching : true});
    this.setState({ tree_data : []});
  

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
      console.log(' send: '+send);

    let p= await this.fetch_data('http://127.0.0.1:8000/api/packageTreeSearch/'+this.state.search_word+'/'+send+'/');
    this.setState({ tree_data : p});
    this.setState({ is_fetching : false});
 
  
    if (this.state.tree_data.npm_name) {
      console.log('fghfhg');
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
          this.setState( { dep_data : [] });
          this.setState( { npm_name : '' });
          this.setState( { search_version : '' });
          
          this.setState( { message_after_search : 'search came without results, please try again' })


          
        }
//////////////////////////////////////////////////////////
       // <div>{!!(this.state.search_word)?this.state.search_word:"whatever you want"}</div>

       
       

  render() {
    return (
      <div  data-testid="search-page-1" style={{ padding: "left" }}>
      

      <SearchBar handleSubmit= {this.handleSubmit}
       handleChange_search_word= {this.handleChange_search_word}
       handleChange_search_version= {this.handleChange_search_version}
       search_version = {this.state.search_version}
         search_word = {this.state.search_word}
         /> 

      { this.state.is_fetching  && <LoaderSpin/>}

      <PackageSearchResult   
      npm_name={this.state.tree_data.npm_name}
      version={this.state.tree_data.version}
      bad_search_message= {this.state.bad_search_message}
      />
     
      <PackageComponent packages =  {this.state.tree_data} />




      </div>
    );
  }
}

export default SearchPage
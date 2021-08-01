import React from 'react';
import PackageSearchResult from './PackageSearchResult';
import PackageComponent from './PackageComponent';

class SearchPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      search_word: '',
       pack_data: [],
       dep_data:[],
       bad_search_message: false,
       is_dep : false,
       data_from_res_manipulate: [],
       message_after_search: '',
       tree_data: []

       };

       // need to add logic to message_not_input


    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

  }

  async handleChange(event) {
    // this.setState({[event.target.name]: event.target.value});
    await this.setState({search_word: event.target.value});
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
    event.preventDefault();
    if (   this.check_not_empty_search_word() === false  ){
      console.log('check emptyyy');
      return 
    } 

    let p= await this.fetch_data('http://127.0.0.1:8000/api/packageTreeSearch/'+this.state.search_word+'/npmpackage/');
    this.setState({ tree_data : p});
 
  
    if (this.state.tree_data.npm_name) {
      console.log('fghfhg');
      this.insert_good_return();
    }else{
      this.search_no_result()
    }
  
      }
////////////////////////////////////////////////////

      async fetch_data(adress){
        return  await  fetch(adress)
       .then(response => response.json())
       
     }

///////////////////////////////////////////////////////
        check_not_empty_search_word(){

          if(  !(this.state.search_word) ){
            console.log('return false');
            this.setState({ message_after_search : ' Please enter value'});
            this.setState({ pack_data : []});
          this.setState( { dep_data : [] });
          this.setState( { npm_name : '' });
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
          this.setState( { message_after_search : 'search came without results, please try again' })


          
        }
//////////////////////////////////////////////////////////
       // <div>{!!(this.state.search_word)?this.state.search_word:"whatever you want"}</div>

       
       

  render() {
    return (
      <div>
      <form onSubmit={this.handleSubmit}>
        <label> 
          <input type="text" name="search_word" value={this.state.search_word} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>


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
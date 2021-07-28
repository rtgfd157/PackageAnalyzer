import React, { useState, useEffect } from 'react';
import PackagesDependenciesList from './PackagesDependenciesList';
import PackageSearchResult from './PackageSearchResult';

class SearchPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      search_word: '',
       pack_data: [],
       dep_data:[],
       bad_search_message: false,
       is_dep : false
       };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.searchPackageDep = this.searchPackageDep.bind(this);
  }

  handleChange(event) {
    this.setState({[event.target.name]: event.target.value});
  }

  searchPackageDep(search_word){
    let address = 'http://127.0.0.1:8000/api/npm_package_dependecy/?search='+this.state.search_word;
    return fetch(address)
      .then(response => response.json())      
      .then((data) => {

        this.setState({ dep_data : data});
      })
  }

   handleSubmit(event){
    event.preventDefault();
    console.log(" type "+ typeof(this.search_word))
    if(  !(this.state.search_word) ){
        this.state.message = ' Please enter value'
      return
    }

    let address = 'http://127.0.0.1:8000/api/npm_package/?search2='+this.state.search_word;
    console.log('adress: '+address);
    return fetch(address)
      .then(response => response.json())      
      .then((data) => {
       
        if (data.length > 0) {
          console.log(" $$$ -"+ data[0].id);
        let d= data[0];
        this.setState({pack_data : d});
        console.log(" $$$ 2 - "+ this.pack_data);
        this.setState({bad_search_message  : false});
        this.setState({is_dep  : true});
        this.searchPackageDep(this.state.search_word, this.is_dep)
        
        }else{
          console.log("empty")
          this.setState({bad_search_message  : true});
          this.setState({ pack_data : []});
          this.searchPackageDep([], false)
        }

        })

       // <div>{!!(this.state.search_word)?this.state.search_word:"whatever you want"}</div>

       
       ;}

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
      npm_name={this.state.pack_data.npm_name}
      version={this.state.pack_data.version}
      bad_search_message= {this.state.bad_search_message}
      />
     

     { this.state.is_dep  && <h2> Dependecies: </h2>}
     <PackagesDependenciesList packagesList={this.state.dep_data}  />

      </div>
    );
  }
}
export default SearchPage
import React from 'react';
import MaterialTable from 'material-table';
// https://material-table.com/#/docs/features/filtering
// https://www.npmjs.com/package/material-table
class NpmSecurityToTable extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
          data:{},
          is_mount :false
          
      };
      this.fetch_data = this.fetch_data.bind(this);
      
      this.npm_security_packages = 'http://127.0.0.1:8000/api/npm_package_security/' ; 
    }
    

    async componentDidMount() {
       let  data = await  this.fetch_data(this.npm_security_packages );
       //console.log(' *****1***** ')
       if (data){
       // console.log('data : '+ data);
         this.setState({ data : data});
         this.setState({ is_mount : true});
       }

       this.Styling = { padding:"0.5rem", margin: '1%'};

       
      }

      async fetch_data(adress){
        return  await  fetch(adress)
       .then(response => response.json())
       .catch(error => {
        console.log('error in fetch');
        throw(error);
        
        })}
  
    render() {
      if (this.state.is_mount){
      return (
                
                    <MaterialTable style={this.Styling}
                    title="Npm Security  Filtering "
                    columns={[
                        { title: 'Name', field: 'npm_package' },
                        { title: 'Version', field: 'return_version_npm' },
                        
                        //{ title: 'version', field: this.state.data.npm_package.version },
                        { title: 'Number of maintainers', field: 'number_of_maintainers', type: 'numeric' },
                        { title: 'Unpackedsize', field: 'unpackedsize', type: 'numeric' },
        
        
                        { title: 'License', field: 'license' },
                        { title: 'Is exploite ? ', field: 'is_exploite' ,type: 'boolean'},
                        { title: 'Number moderate severity', field: 'num_moderate_severity' },
                        { title: 'Nnumber high severity', field: 'num_high_severity' },
                        { title: 'Number info severity', field: 'num_info_severity' },
                        { title: 'Number low severity', field: 'num_low_severity' },
                        { title: 'Number critical severity', field: 'num_critical_severity' },
                        
                        
                    ]}
                    data = {this.state.data}        
                    options={{
                        filtering: true
                    }}
            />  )} 

            else{
                  return(<h2>loading ... </h2>)
                    
                }
                
                
    }
  }
  
  export default NpmSecurityToTable  

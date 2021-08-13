import React from 'react';
import {
    Card, CardText, CardBody,
    CardTitle, CardSubtitle, ListGroup, ListGroupItem
} from 'reactstrap';

class DbComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            npm_count: '',
            npm_dep_count: ''

        };
        this.fetch_data = this.fetch_data.bind(this);
        this.adress_search_el_packages_tree_count = 'http://127.0.0.1:8000/api/count_npm_pacakges_and_dep_packages/';
        this.Styling = {background:"#F2F1F9", padding:"0.5rem", margin: '1%', flex: 1};

    }

    async componentDidMount() {
        let data = await this.fetch_data(this.adress_search_el_packages_tree_count);
        console.log('data : ' + data);
        this.setState({ npm_count: data.npm_count });
        this.setState({ npm_dep_count: data.npm_dep_count });

    }

    async fetch_data(adress) {
        return await fetch(adress)
            .then(response => response.json())
            .catch(error => {
                this.setState({ npm_count: '' });
                this.setState({ npm_dep_count: '' });

                console.log('error in fetch');
                throw (error);

            })
    }

    render() {
        return (
            <div>
                <h2> DB Stats Component : </h2>
                <Card style={this.Styling}>
                    <CardBody>
                        <CardTitle tag="h5"> <u> DB npm package And npm Dependencies </u></CardTitle>
                        <CardSubtitle tag="h6" className="mb-2 text-muted">Counting of NpmPackage And NpmPackageDependecy Models</CardSubtitle>

                        <CardText > Result:

                            <ListGroup>
                                <ListGroupItem style={{ textAlign: "left" }}> Count of Rows npm: {this.state.npm_count} </ListGroupItem>
                                <ListGroupItem style={{ textAlign: "left" }}> Count of Rows npm Dependecies: {this.state.npm_dep_count}  </ListGroupItem>

                            </ListGroup>

                            <u>  Npm rows & Npm Dep rows </u>
                            <u> http://127.0.0.1:8000/api/count_npm_pacakges_and_dep_packages/</u></CardText>
                    </CardBody>


                </Card>
            </div>
        );
    }
}

export default DbComponent
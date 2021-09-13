import React from 'react';

import PredictionHistory from './PredictionHistory';
import SearchForPrediction from './SearchForPrediction';
import { Container, Row, Col } from 'reactstrap';


class Prediction extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: {},
            counnt_npm_sec: 'didnt fetch successfuly yet',
            is_mount: false

        };
        this.fetch_data = this.fetch_data.bind(this);

        this.npm_security_packages = 'http://127.0.0.1:8000/api/npm_package_security/';
        this.count_npm_security = 'http://127.0.0.1:8000/api/count_npm_security/';
        this.Styling = { padding: "0.5rem", margin: '1%' };



    }


    async componentDidMount() {


    }

    async fetch_data(adress) {
        return await fetch(adress)
            .then(response => response.json())
            .catch(error => {
                console.log('error in fetch');
                throw (error);

            })
    }

    render() {

        return (
            <div>
                <h2>   <u>Prediction:</u> </h2>
                <Container>
                    <Row>
                        <Col> <PredictionHistory /> </Col>
                        <Col><SearchForPrediction /> </Col>
                    </Row>
                </Container>

            </div>
        )




    }
}

export default Prediction

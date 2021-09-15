import React from 'react';
// import '../App.css';
import {
  Card, CardText, CardBody,
  CardTitle, CardSubtitle, ListGroup, ListGroupItem,
  Container, Row, Col , CardLink
} from 'reactstrap';


// document.querySelectorAll(" p  ") in browser console

class AboutComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.Styling = { background: "#F2F1F9", padding: "0.5rem", margin: '1%', flex: 1 };

  }

  render() {
    return (

      <div style={{ margin: '10px' }}>
        <h2 >  About: </h2>

        <a href="https://github.com/rtgfd157/PackageAnalyzer/" target="_blank" rel="noreferrer">Link: Project in GitHub    </a>

        <Container>
          <Row>
            <Col><Card style={this.Styling}>
              <CardBody>
                <CardTitle tag="h5">About Search Page?</CardTitle>
                <CardSubtitle tag="h6" className="mb-2 text-muted">The project will search for npm package</CardSubtitle>
                <CardText > Searching by: </CardText>
                <ListGroup>
                  <ListGroupItem style={{ textAlign: "left" }}>1) ElasticSearch </ListGroupItem>
                  <ListGroupItem style={{ textAlign: "left" }}>2)  DB-postgres</ListGroupItem>
                  <ListGroupItem style={{ textAlign: "left" }}>3) api- https://registry.npmjs.org/package name/latest</ListGroupItem>

                </ListGroup>

                <CardText >  <u> Each package will show also his dependency</u>.</CardText>
              </CardBody>
            </Card></Col>
            <Col><Card style={this.Styling}>
              <CardBody>
                <CardTitle tag="h5">About Npm Security Table</CardTitle>
                <CardSubtitle tag="h6" className="mb-2 text-muted">The page will show table</CardSubtitle>

                <CardText >
                  will show a table of Npm Packages if they:
                </CardText>
                <CardText style={{ textAlign: "left" }} >- exploitable(based on npm_fetch_sec.js that is using npm-registry-fetch).</CardText>
                <CardText style={{ textAlign: "left" }} >- license </CardText>
                <CardText style={{ textAlign: "left" }} >- Number of maintainers </CardText>
                <CardText style={{ textAlign: "left" }}>- Number of low, moderate ... severities ..    </CardText>

              </CardBody>
            </Card> </Col>
          </Row>
        </Container>

        <Card style={this.Styling}>
              <CardBody>
                <CardTitle tag="h5">About Npm Prediction</CardTitle>
                <CardSubtitle tag="h6" className="mb-2 text-muted">The page will show last 5 prediction and making new prediction's </CardSubtitle>

                <CardText style={{ textAlign: "left" }}>
                  will make new prediction based on Ml algorithm in our BE. for example :
                </CardText>
                <CardLink>  http://127.0.0.1:8000/api/predict/linear_regression_classifier/?status=production&version=0.0.1</CardLink>

              </CardBody>
            </Card>






      </div>

    );
  }
}

export default AboutComponent
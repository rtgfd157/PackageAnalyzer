import React from 'react';


const Home = () => {
  return (
    
    <div style={{margin: '10px'}} >
        <h2>Project Npm Packages Analysis: </h2>
        <h3>Links</h3>
        <ul>
            <li style={{ textAlign: "left" }}> https://www.django-rest-framework.org/</li>
            <li style={{ textAlign: "left" }}> https://reactjs.org/</li>
            <li style={{ textAlign: "left" }}> https://www.djangoproject.com/ </li>
            <li style={{ textAlign: "left" }}> https://hub.docker.com/</li>
            <li style={{ textAlign: "left" }}> https://registry.npmjs.org/express/latest</li>
            <li style={{ textAlign: "left" }}>http://localhost:9200/elastic_packages_tree/_mapping/?pretty</li>
            <li style={{ textAlign: "left" }}>http://127.0.0.1:8000/api/</li>
            <li style={{ textAlign: "left" }}>http://127.0.0.1:3000/</li>
            <li style={{ textAlign: "left" }}>http://127.0.0.1:8000/api/predict/linear_regression_classifier/?status=production&version=0.0.1</li>

        </ul>

    </div>
    
  );
}

export default Home
import React from 'react';

import Loader from "react-loader-spinner";
// https://www.npmjs.com/package/react-loader-spinner

class LoaderSpin extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }
    render() {
        return (
          <Loader
            type="Audio"
            color="#00BFFF"
            height={120}
            width={120}
            timeout={360000}  // 360 secondes
            //timeout={3000} //3 secs
          />
        );
      }

}

export default LoaderSpin


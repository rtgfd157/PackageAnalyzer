import React from 'react';
import PackageSearchResult from '../PackageSearchResult';
//import Loader from 'react-loader'; // fetch symbol animation
//import Loader from "react-loader-spinner";

import LoaderSpin from '../LoaderSpin';
import PredictBarForm from './PredictBarForm';

class PredictionPost extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

            pack_data: [],
            dep_data: [],
            bad_search_message: false,
            is_dep: false,
            data_from_res_manipulate: [],
            message_after_search: '',
            is_fetching: false,
            number_of_maintainers: this.props.number_of_maintainers,
            unpackedsize: this.props.unpackedsize,
            chosen_algo_for_prediction: this.props.chosen_algo_for_prediction

        };

        // need to add logic to message_not_input


        this.handleChange_unpackedsize = this.handleChange_unpackedsize.bind(this);
        this.handleChange_number_of_maintainers = this.handleChange_number_of_maintainers.bind(this);

        this.handleSubmit = this.handleSubmit.bind(this);

    }

    // beacuse props rebder one on constructor need this function for updating .. 
    static getDerivedStateFromProps(props, state) {
        return {
            number_of_maintainers: props.number_of_maintainers,
            unpackedsize: props.unpackedsize,
            chosen_algo_for_prediction: props.chosen_algo_for_prediction
        };
    }


    async handleChange_unpackedsize(event) {
        console.log('tryy   ' + event.target.value);
        // this.setState({[event.target.name]: event.target.value});
        await this.setState({ unpackedsize: event.target.value });
        console.log(' --- ' + this.state.unpackedsize)
    }

    async handleChange_number_of_maintainers(event) {
        // this.setState({[event.target.name]: event.target.value});
        await this.setState({ number_of_maintainers: event.target.value });
    }


    async handleSubmit(event) {
        this.setState({ bad_search_message: false });
        console.log(' ^^^ ' + this.state.unpackedsize);
        event.preventDefault();
        if (this.check_not_empty_search_word() === false) {
            console.log('check emptyyy');
            return
        }

        if (!this.state.chosen_algo_for_prediction) {
            console.log('error');
            return
        }


        this.setState({ is_fetching: true });




        // http://127.0.0.1:8000/api/v1/income_classifier/predict?status=testing&version=1.1.1.

        let algo_classifier = this.state.chosen_algo_for_prediction.name
        algo_classifier = algo_classifier.replace(' ', '_');
        // console.log( 'algo_classifier ' + algo_classifier);

        let adress = 'http://127.0.0.1:8000/api/predict/' + algo_classifier +
            '_classifier/?status=' + this.state.chosen_algo_for_prediction.current_status +
            '&version=' + this.state.chosen_algo_for_prediction.version;

        console.log('adress ' + adress)
        // http://127.0.0.1:8000/api/predict/linear_regression_classifier/?status=production&version=0.0.1

        fetch(adress, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'unpackedsize': this.state.unpackedsize,
                'number_of_maintainers': this.state.number_of_maintainers
            })
        })






        this.setState({ is_fetching: false });










    }
    ////////////////////////////////////////////////////

    async fetch_data(adress) {
        return await fetch(adress)
            .then(response => response.json())
            .catch(error => {
                this.setState({ is_fetching: false });
                this.setState({ pack_data: [] });
                this.setState({ dep_data: [] });
                this.setState({ npm_name: '' });
                this.setState({ unpackedsize: '' });
                console.log('error in fetch' + error);
                throw (error);

            })

    }

    ///////////////////////////////////////////////////////
    check_not_empty_search_word() {

        console.log(' @@ ' + this.state.number_of_maintainers + '  - ' + this.state.unpackedsize)
        if ((isNaN(this.state.number_of_maintainers)) && (isNaN(this.state.unpackedsize))) {
            console.log('return false');
            this.setState({ message_after_search: ' Please enter both inputs values' });
            this.setState({ pack_data: [] });
            this.setState({ dep_data: [] });
            this.setState({ npm_name: '' });
            this.setState({ unpackedsize: '' });
            //this.empty_search();
            return false
        }
        else {
            console.log('return true');
            return true
        }
    }

    ///////////////////////////////////////////////////////       
    async insert_good_return() {

        this.setState({ bad_search_message: false });
        this.setState({ is_dep: true });


    }


    /////////////////////////////////////////////////////////
    search_no_result() {
        console.log("empty111")
        this.setState({ bad_search_message: true });
        this.setState({ pack_data: [] });
        this.setState({ number_of_maintainers: '-' });
        this.setState({ unpackedsize: '-' });

        this.setState({ npm_name: '' });
        this.setState({ unpackedSize: '' });

        this.setState({ message_after_search: 'search came without results, please try again' })



    }
    //////////////////////////////////////////////////////////



    render() {
        return (
            <div data-testid="search-page-22" style={{ padding: "left" }}>


                <PredictBarForm handleSubmit={this.handleSubmit}
                    handleChange_unpackedsize={this.handleChange_unpackedsize}
                    handleChange_number_of_maintainers={this.handleChange_number_of_maintainers}
                    unpackedsize={this.state.unpackedsize}
                    number_of_maintainers={this.state.number_of_maintainers}
                />


                {this.state.is_fetching && <LoaderSpin />}

                <PackageSearchResult

                    bad_search_message={this.state.bad_search_message}
                />

                <p> {this.state.chosen_algo_for_prediction && this.state.chosen_algo_for_prediction.name}  </p>

            </div>
        );
    }
}

export default PredictionPost
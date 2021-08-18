
import { render, screen, cleanup} from "@testing-library/react";
import  SearchBarForm from '../SearchBarForm';

// https://www.youtube.com/watch?v=ML5egqL3YFE
test('should render SearchPage component ', () => {

    const handleSubmit = jest.fn();
    const handleChange = jest.fn();
    const search_word = 'search word';


    // handleSubmit= {this.handleSubmit} handleChange= {this.handleChange}  search_word = {this.state.search_word} 
    render(<SearchBarForm handleSubmit = {handleSubmit}  handleChange= {handleChange}  search_word = {search_word}  />);

    const search_bar_formElement = screen.getByTestId('search-bar-1');
    expect(search_bar_formElement).toBeInTheDocument();
    // expect(search_pageElement).toHaveTextContent('Hello');
                               
});


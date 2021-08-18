
import { render, screen, cleanup} from "@testing-library/react";
import  SearchPage from '../SearchPage';

// https://www.youtube.com/watch?v=ML5egqL3YFE
test('should render SearchPage component ', () => {
    render(<SearchPage/>);

    const search_pageElement = screen.getByTestId('search-page-1');
    expect(search_pageElement).toBeInTheDocument();
    // expect(search_pageElement).toHaveTextContent('Hello');
                               
});


test('test ', () => {
    expect(true).toBe(true);

})

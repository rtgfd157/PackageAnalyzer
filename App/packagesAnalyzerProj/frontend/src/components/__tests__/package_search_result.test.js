
import { render, screen, cleanup} from "@testing-library/react";
import  PackageSearchResult from '../PackageSearchResult';
import renderer from 'react-test-renderer';


//  afterEach will run after each test
afterEach(() =>{
    cleanup();
})

// https://www.youtube.com/watch?v=ML5egqL3YFE
test('should render PackageSearchResult component ', () => {

    const version = '1.0.1';
    const true_false_search_message_ = false;
    const npm_name = 'test';
    render(
    <PackageSearchResult   
      npm_name={npm_name}
      version={version}
      bad_search_message = {true_false_search_message_}
      />
    )



    const search_bar_formElement = screen.getByTestId('search-res-1');
    expect(search_bar_formElement).toBeInTheDocument('Name: test version: 1.0.1');
    // expect(search_pageElement).toHaveTextContent('Hello');

    afterEach
                               
});



test('should render PackageSearchResult component search not found message', () => {

    const version = '';
    const true_false_search_message_ = true;
    const npm_name = '';
    render(
    <PackageSearchResult   
      npm_name={npm_name}
      version={version}
      bad_search_message = {true_false_search_message_}
      />
    )

    const search_res_pack = screen.getByTestId('search-res-1');
    expect(search_res_pack).toBeInTheDocument('search came without results, please try again');
    expect(search_res_pack).toHaveTextContent('search came without results, please try again');
    expect(search_res_pack).to
    // toContainHTML('<p style="color: red;">')
                               
});

// will make a snapshot and then will check every time new match snapshot been runing with the exsisting snapshot
test('match snapshot ', () => {
    const version = '1.0.1';
    const true_false_search_message_ = false;
    const npm_name = 'test';
    const result =  renderer.create(
    <PackageSearchResult   
      npm_name={npm_name}
      version={version}
      bad_search_message = {true_false_search_message_}
      />
    ).toJSON();

    expect(result).toMatchSnapshot();

    
})

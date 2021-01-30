import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import MainPage from './components/mainpage.component';
import ResultsPage from './components/resultspage.component';
import NotFound from './components/notfound.component';
import Header from './components/header.component';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recs: []
    };
  }

  componentDidMount() {
    this.setState({ recs: [] });
  }

  handleSubmit = (e, history, searchInput) => {
    e.preventDefault();
    e.currentTarget.reset();
    let url = `/results/${searchInput}`;
    history.push(url);
    this.getRecs();
  };

  getRecs = () => {
    axios.get("http://localhost:8000/api/tools")
      .then(res => this.setState({ recs: res.data }))
      .catch(err => console.log(err));
    
  }

  render() {
    return (
      <div className="container">
        <Router>
          <Route render={props => (
              <Header handleSubmit={this.handleSubmit} history={props.history}/>
            )}
          />
          <Switch>
            <Route
              path="/results/:searchInput"
              render={props => (
                <ResultsPage searchTerm={props.match.params.searchInput} />
              )}
            />
            <Route exact path='/' component={MainPage} />
            <Route component={NotFound} />
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;

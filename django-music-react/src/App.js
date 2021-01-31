import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import MainPage from './components/mainpage.component';
import ResultsPage from './components/resultspage.component';
import NotFound from './components/notfound.component';
import Header from './components/header.component';
import DisplayItem from './components/displayitem.component.js'
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recs: [],
      displayed: []
    };
  }

  componentDidMount() {
    let displayItems = [];
    for(let i = 0; i < this.state.recs.length; i++) {
      let item = {
        album:"",
        image:"",
        artist:"",
        external_url:"",
        name:"",
        preview_url:""
      }
      if (typeof this.state.recs[i] != 'undefined'){
        item.album = this.state.recs[i].album;
        item.image = "https://open.spotify.com/embed/album/".concat(this.state.recs[i].album_id);
        item.artist = this.state.recs[i].artist;
        item.external_url = this.state.recs[i].external_url;
        item.name = this.state.recs[i].name;
        item.preview_url = this.state.recs[i].preview_url;
      }
      displayItems.push(
        <DisplayItem item={item}></DisplayItem>
      );

      this.setState({displayed: displayItems});
    }
  }

  handleSubmit = (e, history, searchInput) => {
    e.preventDefault();
    e.currentTarget.reset();
    let url = `/results/${searchInput}`;
    history.push(url);
    this.getRecs(searchInput);
  };

  getRecs = async(searchInput) => {
    let str1 = "http://localhost:8000/api/songrecs/"
    let str2 = searchInput.split('?')[1];
    console.log(str1.concat(str2))
    await axios.get(str1.concat(str2))
      .then(res => this.setState({ recs: res.data }, () => {
        console.log(this.state.recs);
      }))
      .catch(err => console.log(err));
    
  }

  
  render() {
    const recsNotNull = this.state.recs.length !== 0;
    let songs;
    if (recsNotNull) {
      const styleObj = {
        fontSize: 40,
        color: "white",
        }
      songs = <>
                <div style = {styleObj}>1. {this.state.recs[0].name} by {this.state.recs[0].artist}</div> 
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[0].album_id} width="800" height="200" padding-bottom = "25" />
                <div style = {styleObj}>2. {this.state.recs[1].name} by {this.state.recs[1].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[1].album_id} width="800" height="200"/>
                <div style = {styleObj}>3. {this.state.recs[2].name} by {this.state.recs[2].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[2].album_id} width="800" height="200"/>
                <div style = {styleObj}>4. {this.state.recs[3].name} by {this.state.recs[3].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[3].album_id} width="800" height="200"/>
                <div style = {styleObj}>5. {this.state.recs[4].name} by {this.state.recs[4].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[4].album_id} width="800" height="200"/>
                <div style = {styleObj}>6. {this.state.recs[5].name} by {this.state.recs[5].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[5].album_id} width="800" height="200"/>
                <div style = {styleObj}>7. {this.state.recs[6].name} by {this.state.recs[6].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[6].album_id} width="800" height="200"/>
                <div style = {styleObj}>8. {this.state.recs[7].name} by {this.state.recs[7].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[7].album_id} width="800" height="200"/>
                <div style = {styleObj}>9. {this.state.recs[8].name} by {this.state.recs[8].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[8].album_id} width="800" height="200"/>
                <div style = {styleObj}>10. {this.state.recs[9].name} by {this.state.recs[9].artist}</div>
                <iframe src={"https://open.spotify.com/embed/album/" + this.state.recs[9].album_id} width="800" height="200"/>
              </> 
    }
    else {
      songs = <div></div>
    }

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
                <>
                  <ResultsPage searchTerm={props.match.params.searchInput} />
                  {songs}
                </>
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

import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
  constructor() {
    super();
    this.state = {
      saying: '...'
    }
    this.clickHandler = this.clickHandler.bind(this);
    this.sapHandler = this.sapHandler.bind(this)
    this.setState = this.setState.bind(this)
  }

  clickHandler = () => {
    document.querySelector(".input").click();
  }

  async sapHandler(event) {
    let that = this;
    let files = event.target.files;
    if (files && files.length > 0) {
      let reader = new FileReader();

      await reader.addEventListener("load", async function (event) {
        let result = event.target.result
        that.setState({
          saying: 'Hmm....'
        });
        let name = files[0].name;
        result = result.split(',');

        let { data } = await axios.post('/api/predict', { name: name, data: result[1] });

        if (data === 'recycle') {
          that.setState({
            saying: 'Get outta here!'
          })
        } else {
          that.setState({
            saying: 'Gimmee!'
          })
        }

      });
      reader.readAsDataURL(files[0]);


    }

    // document.querySelector(".imageC").classList.add("imageCScRollIn");
  }



  render() {
    return (
      <div className="App">
        <header className="App-header">
          <div className='circle'>
            <h2 className='text'>{this.state.saying}</h2>
            <div className="upload-btn-wrapper">
              <button onClick={this.clickHandler} className="btn">Hi Oscar</button>
              <input className='input' onChange={this.sapHandler} type="file" name="myfile" accept="image/*" />
            </div>
            <div className='imageC'>
              <img className="image" src='oscar2.png' alt='oscar' />
            </div>
          </div>
        </header>
      </div>
    );
  }
}

export default App;

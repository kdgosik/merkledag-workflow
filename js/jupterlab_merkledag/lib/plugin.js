'use strict';

/* TODO
  1. Fill in cell with code
  2. Push Button to hash current cell
  3. Hash current cell
  4. Add hash to meta data of current cell under "hash" key
  5. Create a new cell next
  6. Add hash to meta data of next cell under "previous_hash" key

*/

import SHA256 from 'crypto-js/sha256'

module.exports = [{
    id: 'jupterlab_merkledag',
    autoStart: true,
    activate: function(app) {
      console.log('JupyterLab extension jupterlab_merkledag is activated!');
      console.log(app.commands);
    }
}];

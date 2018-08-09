# piper

## Installation

1. Install system dependencies:

    ```shell
    sudo apt-get install build-essential curl g++ gcc python-dev
    ```

2. Install NVM and Node 8.x:

    ```shell
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
    source ~/.bashrc
    nvm install v8.9.4
    nvm alias default v8.9.4
    ```

3. Install Node and Python dependencies:

    ```shell
    cd /path/to/piper
    ./install.sh
    ```

## Usage

1. Start the app and open in a browser window:

    ```shell
    cd /path/to/piper
    ./start.sh
    ```

2. If the browser cannot connect to the app within a few seconds, then open http://localhost:8080

## Static site

[netbek.github.io/piper](https://netbek.github.io/piper)

To publish the GitHub Pages static site, run:

```shell
cd /path/to/piper
npm run-script deploy
```

## License

Copyright (c) 2018 Hein Bekker. Licensed under the GNU Affero General Public License, version 3.

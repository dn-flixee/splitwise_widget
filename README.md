# SplitWise Web Widget

A web widget project to view your top 4 friends who owe you the most and see the top 3 activities.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Widget](#running-the-widget)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The SplitWise Web Widget is designed to provide a convenient way to visualize and track your top 4 friends who owe you the most, along with the top 3 activities related to your split expenses.

## Getting Started

Follow these instructions to set up and run the SplitWise Web Widget.

### Prerequisites

Make sure you have the following installed:

- Python (>=3.9)
- Flask
- Other dependencies (check requirements.txt)

### Configuration

1. Create a file named `config.py` in the root directory of the project.

2. Obtain your SplitWise API keys by creating an application at [https://secure.splitwise.com/apps](https://secure.splitwise.com/apps).

3. Add the following lines to `config.py`:

   ```python
   
   import os
   def set_environment_variables():
     os.environ['CONSUMER_KEY'] = 'CONSUMER_KEY'
     os.environ['CONSUMER_SECRET'] = 'CONSUMER_SECRET'
     os.environ['API_KEY'] = 'API_KEY'
    ```

   Replace `your_consumer_key`, `your_consumer_secret`, and `your_api_key` with the keys you obtained from the SplitWise Developer Portal.

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/your-username/splitwise-web-widget.git
cd splitwise-web-widget
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Learn how to run and use the SplitWise Web Widget.


### Development Mode

In development mode, you can use Flask's built-in development server.

Activate the virtual environment and start the Flask app:

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
python app.py
```

Visit `http://localhost:5000` in your web browser to view the widget.

### Production Mode

In production mode, use Gunicorn as the server.

```bash
# Activate the virtual environment if not already activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 your_app:app
```

Visit `http://localhost:5000` in your web browser.

## Contributing

Contributions to this project are welcome. If you have ideas for improvements or new features, please feel free to open an issue or submit a pull request.

## License

This project is open-source and available under the MIT License. You are free to use, modify, and distribute the code as long as you include the appropriate attribution.
```

This README provides clear instructions on how to set up the configuration file and obtain the necessary API keys for the SplitWise Web Widget.

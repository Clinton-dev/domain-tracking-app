# Domain Tracking Application

The Domain Tracking Application is a Python script that allows you to check the status of multiple domain URLs and save the results in an Excel file. It uses multithreading to speed up the process and provides a progress bar to track the progress.

## Getting Started

Before running the application, it's recommended to set up a virtual environment to isolate the application's dependencies from the system-wide Python installation.

### Create Virtual Environment

```
bash
# Replace <version> with the desired Python version, e.g., 3.8
python<version> -m venv <virtual-environment-name>
```


### Activate Environment
```
# In CMD
<virtual-environment-name>\Scripts\activate.bat

# In PowerShell
<virtual-environment-name>\Scripts\Activate.ps1

# In linux
source <virtual-environment-name>/bin/activate

```

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3
- pandas
- requests
- tqdm
- humanize

### Installation
You can install the required dependencies using `pip`:

```
pip install -r requirements.txt
```

1. Clone the repository to your local machine:

```
https://github.com/clinton-dev/domain-tracking-app.git
```

```cd domain-tracking-app```

2. Place your domain tracking data in the `files` folder as an Excel file named `DomainTracking.xlsx`. The Excel file should contain a column named `DOMAIN` with the list of domain URLs to check.

### Usage

To run the application, execute the `main.py` script: `python main.py`


The application will start checking the status of the domains, and a progress bar will indicate the progress. Once the check is complete, the results will be saved in the `previous-runs` folder as an Excel file named `DomainStatus_YYYY-MM-DD_HH-MM-SS.xlsx`, where `YYYY-MM-DD` is the current date and `HH-MM-SS` is the current time.

You can find the list of domains that are not up in the Excel file.

### Customization

If you want to modify the input file or customize the behavior of the application, you can do so in the following files:

- `files/DomainTracking.xlsx`: Replace this file with your own domain tracking data.
- `main.py`: Modify the application behavior, such as the number of threads used or the progress bar description.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The application uses the [pandas](https://pandas.pydata.org/), [requests](https://docs.python-requests.org/), [tqdm](https://github.com/tqdm/tqdm), and [humanize](https://github.com/jmoiron/humanize) libraries. Special thanks to the authors and contributors of these libraries.



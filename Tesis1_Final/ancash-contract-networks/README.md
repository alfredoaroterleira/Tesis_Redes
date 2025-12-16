# Ancash Contract Networks Project

This project aims to model contracting networks for the Ancash region, utilizing data from contracts awarded between 2005 and 2024. The primary focus is on constructing bipartite networks that represent the relationships between the government and contracting companies, analyzing these networks, and visualizing the results.

## Project Structure

- **data/**: Contains raw and processed data files.
  - **raw/**: Holds the original dataset (`contratos_ancash_all.xlsx`).
  - **processed/**: Will contain processed data files after cleaning and transformation.

- **notebooks/**: Jupyter notebooks for various stages of the project.
  - **01-data-cleaning.ipynb**: Data cleaning tasks, including handling missing values and formatting.
  - **02-network-construction.ipynb**: Construction of bipartite networks for each year.
  - **03-metrics-and-analysis.ipynb**: Calculation of network metrics and identification of key nodes.
  - **04-visualization-export.ipynb**: Visualization of networks and exporting results to HTML.

- **src/**: Source code for data processing, network construction, and visualization.
  - **data/**: Functions for loading and processing data.
  - **networks/**: Functions for building networks and calculating metrics.
  - **viz/**: Functions for exporting visualizations.
  - **utils.py**: Utility functions for various tasks.

- **web/**: Contains files for rendering interactive visualizations.
  - **templates/**: HTML templates for network visualizations.
  - **static/**: Static files including JavaScript and CSS for visualizations.

- **reports/**: Contains markdown files summarizing findings from the analysis.

- **tests/**: Unit tests for the project modules.

- **requirements.txt**: Lists Python dependencies required for the project.

- **environment.yml**: Environment setup file specifying packages and dependencies.

- **.gitignore**: Specifies files and directories to be ignored by version control.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ancash-contract-networks
   ```

2. Set up the environment:
   - Using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```
   - Or using `environment.yml`:
     ```
     conda env create -f environment.yml
     ```

3. Open Jupyter Notebook and navigate to the `notebooks` directory to start working on the project.

## Usage Guidelines

- Begin with `01-data-cleaning.ipynb` to prepare the data for analysis.
- Proceed to `02-network-construction.ipynb` to build the bipartite networks.
- Use `03-metrics-and-analysis.ipynb` to calculate network metrics and identify key nodes.
- Finally, visualize the networks and export the results using `04-visualization-export.ipynb`.

## Contributions

Contributions to improve the project are welcome. Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
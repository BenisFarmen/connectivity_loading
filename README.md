# connectivity_loading
This repository contains convenience functions, that allow the user to easily load matlab brain connectivity data into python with the right structure for use with photonai-graph

## Example

Load a matlab file in the right format for use with photonai-graph in one line of code

```python
 from load_functions import load_conn
 
 x = load_conn("/path/to/your/data.mat", mtrx_name='connectivity')
 ```

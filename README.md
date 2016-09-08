# Hungergames, Open Food Facts data in your python script


### install


    git clone https://github.com/frankrousseau/hungergames
    cd hungergames
    sudo python setup.py install


### Data

Data follows OFF API format and are returned as Python dicts

### Docs

*Get all available trace type*

```python
traces = hungergames.get_traces()
```

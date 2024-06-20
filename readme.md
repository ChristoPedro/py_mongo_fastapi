# Rest API for Mongo using Python FastAPI

This is a study about how to connect and query and retrive json data from Mongo Atlas using FastAPI as web framework.

## Routes

```/movies```

Return all movies from MongoDB sample collection *movies*.

```/movie/{movie name}```

Retuen all movies that mach parcially or with the full string.


```/movie/id/{id}```

Return the mobie by given MongoDB *_id*.

## How to use

1. Create a python virtual enviroment.

```bash
python -m venv ./venv
```

2. Activate the virtual enviroment

```bash
source .venv/bin/activate
```

3. Create a Enviroment Variable with Mongo Atlas connection string

``` bash
export MONGO_STRING={You Mongo Atlas Connection String} 
```

4. Install all needed libs using pip

```bash
pip install -r requirementes.txt 
```

5. Execute the webserver using uvicorn

```bash
uvicorn mongo:app --host=0.0.0.0 --port 8080 
```

## Check the FastAPI Generated Documentation

Just access the bellow URL to access the documentation.

0.0.0.0:8080/docs
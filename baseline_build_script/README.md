# Baseline Project Template

Provides a baseline project organization. Includes a `README.md` file and three subdirectories: `src`, `docs`, and `tests`.

## README.md

Edit this file as required to describe your project and provide additional documentation as you see fit. 

## src Directory

The purpose of the `src` directory (src is short for *source* code.) is to house all your project's source code files. Larger projects can group related files into subdirectories. 

## docs Directory

The `docs` directory houses project documentation, includeing automatically-generated documentation from tools like Sphinx.

## tests Directory

Place all unit and integration test file in the `tests` directory. A test file begins with the string "test".

The `context.py` file, located in the `tests` directory, includes code that adds the `src` directory to the Python system path and imports modules required for unit and integration tests. 

---
## Run the Application
To run the main.py module, from the project root directory (the directory this `README.md` file is located) run the following command:
```
python src/main.py

```

## Run the Unit Tests

From the root directory run the following commands: (use python or python3 as required)
```
pushd tests
python3 -m unittest -v
popd
```

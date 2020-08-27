"""
Predict.py has been updated from the base Fast API template. Predict.py now contains the flexible search function from
model_create_for_app.py which can be found in the models_and_data folder of DS. This function allows us to search our 
Csv file for strains of cannabis that a user might be interested in. Predict.py currently accepts two inputs.
The first called 'Symptoms', is a single string containing keywords to be searched on. The second input called 'results',
will accept a positive integer that will determine the number of results outputted. Our output 'strain_recommendations' currently
returns a Json dictionary with the specified number of results. Each result will contain values for name, type, flavor, positive effects,
negative effects, ailment, and search.  
"""

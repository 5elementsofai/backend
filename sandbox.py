import yaml
import mlflow


print(mlflow.models.Model.load)

mlflow.set_experiment('5elementsofai')
with mlflow.start_run(run_name='test_run_name'):
    mlflow.log_param('a', 1)
    for a in range(10):
        mlflow.log_metric('a',a)

    mlflow.log_artifact('requirements.txt')
'''
with open(r'./use-cases/object-detection/MLproject') as file:
    project = yaml.load(file, Loader=yaml.FullLoader)

    print(project['entry_points'])
    
'''
'''
with open(r'E:\data\store_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
'''

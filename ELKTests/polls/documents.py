# documents.py
#################ELASTICSEARCH##################

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Session, Simulation

#################TFG##################DONE

@registry.register_document
class SessionDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'kibotics_session_log'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Session # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'type',
            'date',
            'username',
            'client_ip',
            'user_agent',
        ]

@registry.register_document
class SimulationDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'kibotics_simulation_log'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Simulation # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'type',
            'date',
            'username',
            'client_ip',
            'simulation_type',
            'exercise_id',
            'host_ip',
            'container_id',
            'user_agent',
        ]

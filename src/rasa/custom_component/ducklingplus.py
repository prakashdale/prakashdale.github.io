from rasa.nlu.components import Component

class DucklingPlus(Component):
    """A custom component to handle few cases not supported by duckling entity extractor"""
    name = "ducklingplus"
    provides = ["entities"]
    requires = ['tokens']
    defaults = {}
    language_list = ["en"]

    print("initialized the class")

    def __init__(self, component_config=None):
        super(DucklingPlus, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """ Not neeed. entities will be extracted using pattern matching """
        pass

    def persist(self, file_name, model_dir):
        """ Not needed as we are not generating the model here """
        pass

    def convert_to_rasa(self, value, confidence):
        """ Covert model output to rasa nlu compatible output format """

        entity = {
            "value": value,
            "confidence": confidence,
            "entity": "time",
            "extractor": "ducklingplus_extractor"
        }

        return entity

    def process(self, message, **kwargs):
        """ Retrieve the text message, pass it to the classifier and append the prediction result
        to the message class """

        print(message)

    




# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

airtable_api_key = os.getenv("AIRTABLE_KEY")
base_id = os.getenv("BASE_ID")
table_name = os.getenv("TABLE_NAME")

def create_health_log(confirm_exercise, exercise, sleep, diet, stress, goal):
    

    return ""
    #print(resp.raise_for_status)

class HealthForm(FormAction):
    
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True)
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None")
            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny")
            ],
            "stress": [
                self.from_entity(entity="stress"),
                self.from_intent(intent="deny", value="None")
            ],
            "goal": [
                self.from_text(intent="inform"),
            ]
        }
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSearch(Action):
    def name(self) -> Text:
        return "action_search"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        camera = tracker.get_slot('slot_camera')
        ram = tracker.get_slot('slot_RAM')
        battles = tracker.get_slot('slot_battery')

        dispatcher.utter_message(text="here are your search results")
        dispatcher.utter_message(text="the features you entered: "+ str(camera) + " " + str(ram) + " " + str(battles))

        return []


class ActionShowLatestNews(Action):
    def name(self) -> Text:
        return "action_Show_latest_news"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="here the latest news for your category")
        return []


class Name(Action):
    def name(self) -> Text:
        return "action_name"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")

        msg = f"hello {name}, how can i help you?"
        dispatcher.utter_message(text=msg)

        return []

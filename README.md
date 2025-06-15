Personal experience with Vision AI Classification.
Trained on my two cats, Phineas and Ferb.
Goal is to make an universal package that people can use to train their own model, make a connection with input images (Share, MQTT, Frigate, ??) and classify the feeds.

## Environment Variables

- `MODEL_PATH`: path to the TFLite model (default `model.tflite`)
- `RESULTS_PATH`: path to the JSON file storing predictions (default `results.json`)
- `FLASK_PORT`: port used by the Flask server (default `5000`)
- `FLASK_DEBUG`: set to `true` to enable debug mode


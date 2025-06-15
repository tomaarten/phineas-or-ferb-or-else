Personal experience with Vision AI Classification.
Trained on my two cats, Phineas and Ferb.
Goal is to make an universal package that people can use to train their own model, make a connection with input images (Share, MQTT, Frigate, ??) and classify the feeds.

## Configuration

The application can be tuned through environment variables. These can either be
set in your shell, passed via `docker-compose`, or stored in a `.env` file.

- `MODEL_PATH` - path to the TFLite model (default `model.tflite`)
- `RESULTS_PATH` - path to the JSON file storing predictions (default
  `results.json`)
- `FLASK_PORT` - port used by the Flask server (default `5000`)
- `FLASK_DEBUG` - set to `true` to enable debug mode
- `UPLOADS_PATH` - directory on the host used to persist uploaded files (default
  `/var/lib/phineas/static/uploads`)

### Example

Create a `.env` file in the project root:

```env
FLASK_PORT=5000
FLASK_DEBUG=true
MODEL_PATH=model.tflite
RESULTS_PATH=results.json
UPLOADS_PATH=/tmp/uploads
```

Then start the service with:

```bash
docker-compose up
```


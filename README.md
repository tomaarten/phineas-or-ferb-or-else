Personal experience with Vision AI Classification.
Trained on my two cats, Phineas and Ferb.
Goal is to make an universal package that people can use to train their own model, make a connection with input images (Share, MQTT, Frigate, ??) and classify the feeds.

## Configuration

The application can be tuned through environment variables. These can either be
set in your shell, passed via `docker-compose`, or stored in a `.env` file.

- `MODEL_PATH` - path to the TFLite model inside the container (default `model.tflite`)
- `RESULTS_PATH` - path inside the container storing predictions (default `results.json`)
- `FLASK_PORT` - port used by the Flask server (default `5000`)
- `FLASK_DEBUG` - set to `true` to enable debug mode

Host paths for uploads, the model and results are configured directly in
`docker-compose.yml`.

### Example

Create a `.env` file in the project root:

```env
FLASK_PORT=5000
FLASK_DEBUG=true
MODEL_PATH=model.tflite
RESULTS_PATH=results.json
```

Then start the service with:

```bash
docker-compose up
```

### Startup behavior

The container runs `setup_paths.py` before launching the Flask app. This script
ensures `/app/static/uploads`, `/app/model.tflite` and `/app/results.json`
exist. If the mounted model file is empty, the bundled default model is copied
so the service has a usable model on first start.


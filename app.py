import argparse

from flask import Flask, render_template, Response
from flask_cors import CORS, cross_origin

from src.stage_01_load_save import get_data

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["POST"])
@cross_origin()
def trainRouteClient():
    try:
        get_data()
    except ValueError:
        return Response("Error Occurred! :: " + str(ValueError))
    except KeyError:
        return Response("Error Occurred! :: " + str(KeyError))
    except Exception as e:
        return Response("Error Occurred! :: " + str(e))
    return Response("Training successful")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default='config/config.yaml')

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)
    app.run(debug=True)
import connexion
from connexion import NoContent

def report_server_health_readings(body):
    """ Receives a server health reading batch event """

    print(body)

    return NoContent, 201

def report_player_telemetry_event(body):
    """ Receives a player telemetry event """

    print(body)

    return NoContent, 201

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("game_server_api.yml",
            strict_validation=True,
            validate_responses=True)


if __name__ == "__main__":
    app.run(port=8088)
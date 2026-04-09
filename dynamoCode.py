import boto3
from botocore.exceptions import ClientError

REGION = "us-east-1"
TABLE_NAME = "NBATeamRatings"

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME)

def get_team_rating(Team):
    """Fetch the current fan rating of the given team."""
    response = table.get_item(Key={"Team": Team})
    return response.get("Item")

def add_or_update_team_rating(Team, Rating):
    """Add or overwrite the fan rating for a team."""
    try:
        table.put_item(
            Item={
                "Team": Team,
                "fan_rating": int(Rating)
            }
        )
        return True, "Fan rating added or updated successfully."
    except ClientError as e:
        return False, f"Could not add/update rating: {e.response['Error']['Message']}"
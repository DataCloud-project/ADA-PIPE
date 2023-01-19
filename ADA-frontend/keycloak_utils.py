from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError

import yaml

#import api_config


def __get_secret_key() -> str:
    with open('credentials.yml', 'r') as file:
        yaml_file = yaml.safe_load(file)
        return yaml_file['keycloak']['client_sk']


def _get_keycloak_open_id() -> KeycloakOpenID:
    return KeycloakOpenID(
        server_url='https://datacloud-auth.euprojects.net/auth/',
        client_id='testclient',
        realm_name='user-authentication',
        client_secret_key=__get_secret_key()
    )

__keycloak_open_id = _get_keycloak_open_id()


def _get_keycloak_token(username: str, password: str) -> dict:
    """Get the assigned KeyCloak token for the ADA-PIPE backend to be able to send requests to other DataCloud services.

    Returns:
        dict: the keycloak token for ADA-PIPE
    """
    token = __keycloak_open_id.token(
        username,
        password)
    return token


def verify_keycloak_token(keycloak_token: dict) -> bool:
    """Verify a given KeyCloak token

    Args:
        keycloak_token (dict): a KeyCloak token to be verified

    Returns:
        bool:  returns True if the token could be verified by KeyCloak, else returns False
    """
    if keycloak_token is None or len(keycloak_token) == 0:
        return False
    if 'access_token' not in keycloak_token:
        return False
    try:
        keycloak_response = __keycloak_open_id.userinfo(
            keycloak_token['access_token'])

        if 'email_verified' not in keycloak_response or 'preferred_username' not in keycloak_response:
            return False

        return True

    except KeycloakAuthenticationError as err:
        # Token could not be verified
        print('Invalid Access Token', err)
        return False


def verify_access_token(access_token: str) -> bool:
    """Verify the (KeyCloak) access token of a service request.

    Args:
        access_token (str): the access token to be verified

    Returns:
        bool:  returns True if the token could be verified by KeyCloak, else returns False
    """
    if access_token is None or len(access_token) == 0:
        return False

    try:
        keycloak_response = __keycloak_open_id.userinfo(access_token)

        if 'email_verified' not in keycloak_response or 'preferred_username' not in keycloak_response:
            return False

        return True

    except KeycloakAuthenticationError as err:
        # Token could not be verified
        print('Invalid Access Token', err)
        return False

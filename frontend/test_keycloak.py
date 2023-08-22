from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError
import keycloak_utils
keycloak_open_id = keycloak_utils._get_keycloak_open_id()

keycloak_token = keycloak_utils._get_keycloak_token('testuser','testuser')
access_token = keycloak_token['access_token']
print(access_token)

user_info = keycloak_utils.verify_access_token(access_token)
print(user_info)

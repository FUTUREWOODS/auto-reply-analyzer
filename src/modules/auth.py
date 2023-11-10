from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..constants import constant

security = HTTPBearer()


def verify_token(
    http_auth_credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if http_auth_credentials:
        token = http_auth_credentials.credentials
        if token == constant.API_SECRET_TOKEN:
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token"
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing"
    )

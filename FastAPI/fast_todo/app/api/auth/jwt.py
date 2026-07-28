from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService
from app.core.security import create_access_token, create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserDetails
from app.models.user_model import User
from app.api.dependencies.user_deps import get_current_user

auth_router = APIRouter()


@auth_router.post(
    "/login", summary="Cria Acess Token e Refresh Token", response_model=TokenSchema
)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email=data.username,
        password=data.password,
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail ou senha estão incorretos",
        )
    return {
        "access_token": create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id),
    }


@auth_router.post("/test", summary="Testando Token", response_model=UserDetails)
async def test_token(user: User = Depends(get_current_user)):
    return user

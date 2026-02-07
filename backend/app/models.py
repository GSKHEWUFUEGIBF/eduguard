from pydantic import BaseModel, Field

# Request model for creating a user
class CreateUserRequest(BaseModel):
    username: str = Field(..., description="The user's unique username")
    email: str = Field(..., description="The user's email address")
    password: str = Field(..., description="The user's password")

# Response model for user creation
class CreateUserResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the user creation was successful")
    user_id: int = Field(..., description="The unique id of the created user")

# Request model for authenticating a user
class AuthUserRequest(BaseModel):
    username: str = Field(..., description="The user's username")
    password: str = Field(..., description="The user's password")

# Response model for user authentication
class AuthUserResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the authentication was successful")
    token: str = Field(..., description="JWT token for authenticated user")

# Response model for user information
class UserResponse(BaseModel):
    user_id: int = Field(..., description="The unique id of the user")
    username: str = Field(..., description="The user's username")
    email: str = Field(..., description="The user's email address")
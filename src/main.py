from fastapi import FastAPI, Depends, HTTPException,status
from typing import List
from sqlalchemy.orm.session import Session
from schemas.user import UserCreate, UserDisplay
from db.models.user import DbUser
from db.database import get_db

app = FastAPI()

@app.get("/all", response_model=List[UserDisplay])
def get_users(db:Session=Depends(get_db)):
    return db.query(DbUser).all()

"""
@app.post("/register")
def register_user(user: schemas.UserCreate, session: Session = Depends(get_session)):
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password =get_hashed_password(user.password)

    new_user = models.User(username=user.username, email=user.email, password=encrypted_password )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message":"user created successfully"}
"""

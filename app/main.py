from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# -------- Health --------

@app.get("/health")
def health():
    return {"status": "ok"}


# -------- Users --------

@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        email=user.email,
        hashed_password=user.password  # hashing later
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

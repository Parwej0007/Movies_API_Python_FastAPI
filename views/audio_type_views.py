from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from views.pydantic_view import SongPyd, PodcastPyd, AudioBookPyd
from sqlalchemy.orm import Session
from database import sessionLocal, Base, engine
from models import audio_model




# connecting db and for create table inside database
# Migrating all the table --> models.Base_db.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)


# FastAPi instance
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True,   )



# db connection session
def get_db():
    Db = sessionLocal()
    try:
        yield Db
    except Exception as e:
        print(f"Session Failed: {e}")
    finally:
        Db.close()


#################################### Song API CRUD #############################################
@app.post('/audiofiletype/song/create/', tags=["Song"], status_code=status.HTTP_201_CREATED)
def create_song(request: SongPyd, db: Session = Depends(get_db)):
    db_create_song = audio_model.SongModel(**request.dict())
    db.add(db_create_song)
    db.commit()
    db.refresh(db_create_song)
    return db_create_song




# get all songs
@app.get('/audiofiletype/song/list/', tags=["Song"], status_code=status.HTTP_200_OK)
def list_song(db: Session = Depends(get_db)):
    data = db.query(audio_model.SongModel).all()
    return data



# get specific song by its id
@app.get('/audiofiletype/song/details/{id}/', tags=["Song"], status_code=status.HTTP_202_ACCEPTED)
def details_song(id: int, db: Session = Depends(get_db)):
    get_data = db.query(audio_model.SongModel).filter(audio_model.SongModel.id==id).first()
    if get_data:
        return get_data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")


# update specific song
@app.put('/audiofiletype/song/update/{id}/', tags=["Song"], status_code=status.HTTP_201_CREATED)
def update_song(id: int, request: SongPyd, db: Session = Depends(get_db)):
    get_data = db.query(audio_model.SongModel).filter(audio_model.SongModel.id==id).first()
    if get_data:
        json_supplier = jsonable_encoder(get_data)
        update_data = request.dict(exclude_unset=True)
        for field in json_supplier:
            if field in update_data!=0:
                setattr(get_data, field, update_data[field])
        db.commit()
        db.refresh(get_data)
        return get_data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")


# delete song by it id
@app.delete('/audiofiletype/song/delete/{id}/', tags=["Song"], status_code=status.HTTP_200_OK)
def delete_song(id: int, db: Session = Depends(get_db)):
    get_data = db.query(audio_model.SongModel).filter(audio_model.SongModel.id==id).first()
    if get_data:
        db.delete(get_data)
        db.commit()
        return {"data": f"successfuly remove song by id: {id}"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")




##################################### Podcast API CRUD #################################################


# create podcast
@app.post('/audiofiletype/podcast/create/', tags=["Podcast"], status_code=status.HTTP_201_CREATED)
def create_podcast(request_podcast: PodcastPyd, db: Session = Depends(get_db)):
    data = audio_model.Podcast(**request_podcast.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


# get all podcast
@app.get('/audiofiletype/podcast/list/', tags=["Podcast"], status_code=status.HTTP_200_OK)
def list_podcast(db: Session = Depends(get_db)):
    return db.query(audio_model.Podcast).all()



# get specific podcast
@app.get('/audiofiletype/podcast/detail/{id}', tags=["Podcast"], status_code=status.HTTP_200_OK)
def detail_podcast(id: int, db: Session = Depends(get_db)):
    fetch_data = db.query(audio_model.Podcast).filter(audio_model.Podcast.id == id).first()
    if fetch_data:
        return fetch_data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")


# update data of podcast by its id
@app.put('/audiofiletype/podcast/update/{id}', tags=["Podcast"], status_code=status.HTTP_200_OK)
def update_podcast(id: int, request:PodcastPyd ,db: Session = Depends(get_db)):
    get_data = db.query(audio_model.Podcast).filter(audio_model.Podcast.id == id).first()
    if get_data:
        jsonable_get_data = jsonable_encoder(get_data)
        podcast_update_data = request.dict(exclude_unset=True)
        for field in jsonable_get_data:
            if field in podcast_update_data and podcast_update_data[field]!=0:
                setattr(get_data, field, podcast_update_data[field])
        db.commit()
        db.refresh(get_data)
        return get_data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")


# delete podcast
@app.delete('/audiofiletype/podcast/delete/{id}', tags=["Podcast"], status_code=status.HTTP_200_OK)
def delete_podcast(id: int, db: Session = Depends(get_db)):
    get_data = db.query(audio_model.Podcast).filter(audio_model.Podcast.id == id).first()
    if get_data:
        db.delete(get_data)
        db.commit()
        return {"data": f"successfuly remove podcast by id: {id}"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")




##################################### AudioBook API CRUD ##################################################

# create audiobook
@app.post('/audiofiletype/audiobook/create/', tags=["AudioBook"], status_code=status.HTTP_201_CREATED)
def create_podcast(request_podcast: AudioBookPyd, db: Session = Depends(get_db)):
    data = audio_model.Audiobook(**request_podcast.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


# get all audiobook
@app.get('/audiofiletype/audiobook/list/', tags=["AudioBook"], status_code=status.HTTP_200_OK)
def list_podcast(db: Session = Depends(get_db)):
    return db.query(audio_model.Audiobook).all()


# get specific audiobook
@app.get('/audiofiletype/audiobook/detail/{id}', tags=["AudioBook"], status_code=status.HTTP_200_OK)
def detail_podcast(id: int, db: Session = Depends(get_db)):
    fetch_data = db.query(audio_model.Audiobook).filter(audio_model.Audiobook.id == id).first()
    if fetch_data:
        return fetch_data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")



# update data of audiobook by id
@app.put('/audiofiletype/audiobook/update/{id}', tags=["AudioBook"], status_code=status.HTTP_200_OK)
def update_podcast(id: int, request:AudioBookPyd ,db: Session = Depends(get_db)):
    get_data = db.query(audio_model.Audiobook).filter(audio_model.Audiobook.id == id).first()
    if get_data:
        jsonable_get_data = jsonable_encoder(get_data)
        podcast_update_data = request.dict(exclude_unset=True)
        for field in jsonable_get_data:
            if field in podcast_update_data and podcast_update_data[field]!=0:
                setattr(get_data, field, podcast_update_data[field])
        db.commit()
        db.refresh(get_data)
        return get_data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")


# delete audiobook by id
@app.delete('/audiofiletype/audiobook/delete/{id}', tags=["AudioBook"], status_code=status.HTTP_200_OK)
def delete_podcast(id: int, db: Session = Depends(get_db)):
    get_data = db.query(audio_model.Audiobook).filter(audio_model.Audiobook.id == id).first()
    if get_data:
        db.delete(get_data)
        db.commit()
        return {"data": f"successfuly remove Audiobook by id: {id}"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not found {id}")


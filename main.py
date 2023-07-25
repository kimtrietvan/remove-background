from fastapi import FastAPI, UploadFile
from fastapi.responses import Response
import uvicorn, io
from PIL import Image
from rembg import new_session, remove

model = 'u2net'
app = FastAPI()


@app.post("/")
async def remove_background(file: UploadFile):
    image = Image.open(io.BytesIO(await file.read()))
    session = new_session(model_name=model)
    new_image = remove(session=session, data=image)
    imageByte = io.BytesIO()
    new_image.save(imageByte, format='PNG')
    return Response(imageByte.getvalue())


if __name__ == '__main__':
    uvicorn.run(app="main:app", host='0.0.0.0', port=80, reload=True)
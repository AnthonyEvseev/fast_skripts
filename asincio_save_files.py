from fastapi import UploadFile, File
from aiofile import async_open
import asyncio


async def save_files(img: UploadFile = File(...)):
    async with async_open(img.filename, "wb") as f:
        data = await img.read()
        await f.write(data)


async def download_files(img: list[UploadFile] = File(...)):
    tasks = []
    for i in img:
        task = asyncio.create_task(save_files(i))
        tasks.append(task)
    await asyncio.gather(*tasks)

from .progress import humanbytes
from .formats import yaml_format


async def mediadata(e_media):
    xavier = ""
    if e_media.file.name:
        xavier += f"📍 NAME :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        xavier += f"📍 MIME TYPE :  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        xavier += f"📍 SIZE :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        xavier += f"📍 DATE :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        xavier += f"📍 ID :  {e_media.file.id}<br>"
    if e_media.file.ext:
        xavier += f"📍 EXTENSION :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        xavier += f"📍 EMOJI :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        xavier += f"📍 TITLE :  {e_media.file.title}<br>"
    if e_media.file.performer:
        xavier += f"📍 PERFORMER :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        xavier += f"📍 DURATION :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        xavier += f"📍 HEIGHT :  {e_media.file.height}<br>"
    if e_media.file.width:
        xavier += f"📍 WIDTH :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        xavier += f"📍 STICKER SET :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            xavier += f"📍 Thumb  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return xavier


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None


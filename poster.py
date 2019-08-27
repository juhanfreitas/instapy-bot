from instapy_cli import client

def postBot(image, description):
    
    """A bot that receives images and its descriptions and upload at the
    Instagram account."""

    username = 'instagram account username'
    password = 'instagram account password'

    with client(username, password) as cli:
        cli.upload(image, description)

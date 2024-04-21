from supabase import create_client, Client
from sprite_rendering import wx_sprite
import wx
import random
import datetime

url: str = "https://kjrtaohycygzmncqlffw.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtqcnRhb2h5Y3lnem1uY3FsZmZ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM2MDc5OTQsImV4cCI6MjAyOTE4Mzk5NH0.2lsH0yuwL6-puxJl-YULVzaaHfHtMRvD__xait4iKto"
supabase: Client = create_client(url, key)

wx_app = wx.App()
sprite = wx_sprite.Sprite()
sprite.Show()

def getAppCoords(name):
    response = supabase.table('coordinates').select("*").eq("app_name", name).execute()
    return response

def moveSpriteToApp(name):
    res = getAppCoords(name)
    print(res.data[0]['x'])
    dest = [res.data[0]['x']-50,res.data[0]['y']-230]
    sprite.traverse(dest,7)

if __name__ == '__main__':
    apps = supabase.table('coordinates').select("app_name").execute()
    dest = random.choice(apps.data)
    moveSpriteToApp(dest['app_name'])
    # sprite.traverse([0,100],10)
    wx_app.MainLoop()
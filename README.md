# SnippetHub
Code Snippets that I regularly use.

```python
from myhelper.yt_dlp_helper import Ytube,Ytlist

url="Your YouTube Video Url"

yt=Ytube(url)

list_of_formats=yt.formats

audios=yt.audios
videos=yt.videos 
progressive=yt.progressive

video=yt.download_by_resolution("144p")
audio=yt.download_audio_by_bt_rate(128)
audio=yt.download_audio_by_bt_rate("128kbps")
audio=yt.download_audio_by_bt_rate("128k")

yt_=Ytlist("Your Playlist Url")
lst=yt_.download_all_videos_by_resolution('720p',out_fol="Out_Folder",alt="360p")

#lst: dict containing outputs

lst["output_folder"]
lst["files_list"]
lst["size_downloaded"]
lst["downloaded"]
lst["failed"]
lst["total"]

```



```python
from pdftk import pdftk
# **To Merge Pdf:**
pdftk().merge( input_files=['file1.pdf','file1.pdf'],output='/your path/your pdf.pdf',user_pw='PrinceIsGod',owner_pw='HeIsTheOnlyOwnerOfWorld' )

# **To Burst Pdf:**
pdftk().burst_pdf('file1.pdf',output_folder='pk',input_pw='passwordofyourpdf')

# ** To Remove Password:**
pdftk().decrypt('file1.pdf',input_pw='yourpass',output='pk.pdf')

# ** To encrypt Pdf:**
pdftk().encrypt('file1.pdf',user_pw='pass',owner_pw='pass1',output='output.pdf')

# ** To add background:**
pdftk().add_background(pdf, background_pdf)

```
---
```python
Help on class pdftk in module pdftk:

class pdftk(builtins.object)
 |  pdftk() -> None
 |  
 |  Complete wrapper for pdftk.
 |  
 |  Methods defined here:
 |  
 |  __init__(self) -> None
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  add_background(self, pdf, back_pdf, input_pw=None, multi=False, user_pw=None, owner_pw=None, output=None)
 |      If the input PDF does not have a transparent background (such as a PDF created from page scans) then
 |      the resulting background won't be visible -- use the add_stamp operation instead.
 |  
 |  add_stamp(self, pdf, back_pdf, input_pw=None, multi=False, user_pw=None, owner_pw=None, output=None)
 |  
 |  burst_pdf(self, pdf, output_folder=None, input_pw=None)
 |  
 |  decrypt(self, pdf, input_pw, output=None)
 |  
 |  encrypt(self, pdf, user_pw=None, owner_pw=None, output=None)
 |  
 |  execute(self)
 |  
 |  get_page_count(self, pdf)
 |  
 |  merge(self, input_files: list, output=None, user_pw=None, owner_pw=None)
 |  
 |  rotate_pdf(self, pdf, direction='north', page_ranges='1-end', output=None, input_pw=None, user_pw=None, owner_pw=None)
 |      Each option sets the page rotation as follows (in degrees): north: 0,east: 90, south: 180, west: 270, left: -90,
 |      right: +90, down: +180. left, right, and down make relative adjustments to a page's rotation.
 |  
 |  split_pdf(self, pdf, page_or_range: list, output=None, input_pw=None)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```


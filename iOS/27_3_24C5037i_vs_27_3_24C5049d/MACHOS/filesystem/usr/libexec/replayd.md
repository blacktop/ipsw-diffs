## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-770.2.1.0.0
-  __TEXT.__text: 0xb98b4
-  __TEXT.__auth_stubs: 0x1930
+770.4.1.0.0
+  __TEXT.__text: 0xb9ad4
+  __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0xf340
   __TEXT.__objc_methlist: 0x74b0
   __TEXT.__const: 0x3e4
   __TEXT.__gcc_except_tab: 0xfc8
-  __TEXT.__objc_methname: 0x15fe3
-  __TEXT.__oslogstring: 0x16863
-  __TEXT.__cstring: 0x17d26
+  __TEXT.__objc_methname: 0x15feb
+  __TEXT.__oslogstring: 0x168e3
+  __TEXT.__cstring: 0x17d36
   __TEXT.__objc_classname: 0xa44
-  __TEXT.__objc_methtype: 0x4410
-  __TEXT.__unwind_info: 0x33e8
+  __TEXT.__objc_methtype: 0x43fc
+  __TEXT.__unwind_info: 0x33f0
   __DATA_CONST.__const: 0x2b00
   __DATA_CONST.__cfstring: 0x5d40
   __DATA_CONST.__objc_classlist: 0x278

   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xca8
+  __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x11418

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3683
-  Symbols:   803
+  Functions: 3684
+  Symbols:   802
   CStrings:  7395
 
Symbols:
- _FigCFDictionaryGetNumberValue
CStrings:
+ " [ERROR] %{public}s:%d Rejecting AppsAndWindowsPinnedToDisplay filter with individual window ID"
+ " [INFO] %{public}s:%d %p added video input with resolution %zux%zu transform=[%.0f %.0f %.0f %.0f] and started writing"
+ "-[RPRecordingManager processSaveToPhotos:mixAudioTracks:ignoreDoNotDisturb:isClip:handler:]"
+ "-[RPRecordingManager processSaveToPhotos:mixAudioTracks:ignoreDoNotDisturb:isClip:handler:]_block_invoke"
+ "processSaveToPhotos:mixAudioTracks:ignoreDoNotDisturb:isClip:handler:"
- " [INFO] %{public}s:%d %p added video input with resolution %zux%zu and started writing"
- "-[RPRecordingManager processSaveToPhotos:mixAudioTracks:ignoreDoNotDisturb:isClip:]"
- "-[RPRecordingManager processSaveToPhotos:mixAudioTracks:ignoreDoNotDisturb:isClip:]_block_invoke"
- "processSaveToPhotos:mixAudioTracks:ignoreDoNotDisturb:isClip:"
- "v36@0:8@16B24B28B32"
```

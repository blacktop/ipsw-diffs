## afinfo

> `/usr/bin/afinfo`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-830.0.0.0.0
-  __TEXT.__text: 0x762c
+830.201.0.0.0
+  __TEXT.__text: 0x7568
   __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_stubs: 0x80
-  __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x1dae
+  __TEXT.__gcc_except_tab: 0x634
+  __TEXT.__cstring: 0x1d36
   __TEXT.__const: 0xa8
   __TEXT.__objc_methname: 0x32
   __TEXT.__unwind_info: 0x2c8

   __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0x90
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x388
+  __DATA.__data: 0x380
   __DATA.__common: 0x11
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   Functions: 79
   Symbols:   158
-  CStrings:  348
+  CStrings:  344
 
Functions:
~ sub_100001938 : 10372 -> 10176
CStrings:
- "AudioFileGetProperty kAudioFilePropertyContentType failed"
- "Content Type:"
- "content_type_dict"
- "kAudioFilePropertyContentType"
```

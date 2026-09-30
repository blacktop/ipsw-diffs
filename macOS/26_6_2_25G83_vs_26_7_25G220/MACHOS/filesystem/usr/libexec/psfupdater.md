## psfupdater

> `usr/libexec/psfupdater`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 25.0.0.0.0
-  __TEXT.__text: 0xbff0
+  __TEXT.__text: 0xc348
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__gcc_except_tab: 0x67c
-  __TEXT.__cstring: 0x41c
+  __TEXT.__gcc_except_tab: 0x6fc
+  __TEXT.__cstring: 0x44e
   __TEXT.__const: 0x498
   __TEXT.__objc_methname: 0xdb
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__unwind_info: 0x530
   __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x718
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x50
   __DATA.__objc_classrefs: 0x18

   - /usr/lib/libobjc.A.dylib
   Functions: 245
   Symbols:   108
-  CStrings:  86
+  CStrings:  91
 
Functions:
~ sub_1000014a4 : 60 -> 832
~ sub_1000014e0 -> sub_1000017e4 : 392 -> 376
~ sub_100001fc0 -> sub_1000022b4 : 140 -> 240
CStrings:
+ "-s %i"
+ "Mac-4B6E2C6433455938"
+ "PLDS1"
+ "TYP2S"
+ "signed_MLB"
```

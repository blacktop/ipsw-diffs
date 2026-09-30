## timed

> `/usr/libexec/timed`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-340.0.12.0.0
-  __TEXT.__text: 0x17858
+340.0.14.0.0
+  __TEXT.__text: 0x1796c
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_stubs: 0x26e0
-  __TEXT.__objc_methlist: 0xd6c
+  __TEXT.__objc_stubs: 0x2700
+  __TEXT.__objc_methlist: 0xd7c
   __TEXT.__const: 0x280
-  __TEXT.__objc_methname: 0x255c
-  __TEXT.__cstring: 0x20e7
+  __TEXT.__objc_methname: 0x2593
+  __TEXT.__cstring: 0x20f6
   __TEXT.__objc_classname: 0x111
   __TEXT.__objc_methtype: 0x554
   __TEXT.__oslogstring: 0x2c6c
   __TEXT.__gcc_except_tab: 0x98
   __TEXT.__unwind_info: 0x5f8
   __DATA_CONST.__const: 0xe68
-  __DATA_CONST.__cfstring: 0x2b60
+  __DATA_CONST.__cfstring: 0x2b80
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1d8
-  __DATA.__objc_const: 0x1da0
-  __DATA.__objc_selrefs: 0xb48
+  __DATA.__objc_const: 0x1db0
+  __DATA.__objc_selrefs: 0xb50
   __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x310

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 622
+  Functions: 623
   Symbols:   256
-  CStrings:  1289
+  CStrings:  1293
 
CStrings:
+ "340.0.14"
+ "AudioAccessory"
+ "TB,R,GisAudioAccessory"
+ "audioAccessory"
+ "isAudioAccessory"
- "340.0.12"
```

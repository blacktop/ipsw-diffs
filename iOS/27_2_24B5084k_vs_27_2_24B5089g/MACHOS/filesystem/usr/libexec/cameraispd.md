## cameraispd

> `/usr/libexec/cameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-20.104.4.0.0
-  __TEXT.__text: 0x7e914
+20.105.6.0.0
+  __TEXT.__text: 0x7e918
   __TEXT.__auth_stubs: 0x1f90
   __TEXT.__objc_stubs: 0x11e0
   __TEXT.__objc_methlist: 0x270
   __TEXT.__gcc_except_tab: 0x1a2c
   __TEXT.__const: 0x2c08
-  __TEXT.__cstring: 0x7e7c
+  __TEXT.__cstring: 0x7e62
   __TEXT.__oslogstring: 0x60c1
   __TEXT.__objc_methname: 0x13f2
   __TEXT.__objc_classname: 0x88
   __TEXT.__objc_methtype: 0x1073
   __TEXT.__unwind_info: 0x1c80
   __DATA_CONST.__const: 0x9ae0
-  __DATA_CONST.__cfstring: 0x3060
+  __DATA_CONST.__cfstring: 0x3040
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__auth_got: 0xfd8
-  __DATA_CONST.__got: 0xcd8
+  __DATA_CONST.__got: 0xce0
   __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x5c8
   __DATA.__objc_selrefs: 0x590

   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
   Functions: 1587
-  Symbols:   933
-  CStrings:  1936
+  Symbols:   934
+  CStrings:  1935
 
Symbols:
+ _kFigCaptureStreamMetadata_SmartTapAlgorithmMetadata
Functions:
~ sub_100066d94 : 52776 -> 52780
CStrings:
+ "20.105.6"
- "20.104.4"
- "SmartTapAlgorithmMetadata"
```

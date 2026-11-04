## seld

> `/usr/libexec/seld`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-371.8.0.0.0
-  __TEXT.__text: 0x26d90
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x33a0
+372.4.1.0.0
+  __TEXT.__text: 0x26e8c
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_stubs: 0x3400
   __TEXT.__objc_methlist: 0xef4
   __TEXT.__const: 0x1b0
-  __TEXT.__objc_methname: 0x38b5
-  __TEXT.__cstring: 0x444d
+  __TEXT.__objc_methname: 0x393d
+  __TEXT.__cstring: 0x4478
   __TEXT.__oslogstring: 0x4157
   __TEXT.__objc_classname: 0x234
   __TEXT.__objc_methtype: 0xced
   __TEXT.__unwind_info: 0x558
   __DATA_CONST.__const: 0xa98
-  __DATA_CONST.__cfstring: 0x22e0
+  __DATA_CONST.__cfstring: 0x2340
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x260
   __DATA.__objc_const: 0x1ea0
-  __DATA.__objc_selrefs: 0xf68
+  __DATA.__objc_selrefs: 0xf80
   __DATA.__objc_ivar: 0x1dc
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x4e0

   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 367
-  Symbols:   221
-  CStrings:  1719
+  Symbols:   223
+  CStrings:  1725
 
Symbols:
+ _OBJC_CLASS_$_NFAutoBugCapture
+ _dispatch_get_global_queue
Functions:
~ sub_1000253f4 : 2368 -> 2620
CStrings:
+ "%@:%ld"
+ "No PT key info"
+ "PTKeyInfoUnavailable"
+ "domain"
+ "requestSnapshotWithType:subType:subTypeContext:detectedProcess:attachments:preferencesDomain:queue:completion:"
+ "stringWithFormat:"
```

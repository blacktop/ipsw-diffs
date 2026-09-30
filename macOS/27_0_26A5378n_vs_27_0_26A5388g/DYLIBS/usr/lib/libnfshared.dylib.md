## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-370.38.2.0.0
-  __TEXT.__text: 0x20af0
+370.40.2.0.0
+  __TEXT.__text: 0x20f94
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x1fcc
+  __TEXT.__objc_methlist: 0x1fe4
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x4825
+  __TEXT.__cstring: 0x4859
   __TEXT.__oslogstring: 0x15da
-  __TEXT.__unwind_info: 0x620
+  __TEXT.__unwind_info: 0x630
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1250
+  __DATA_CONST.__objc_selrefs: 0x1260
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x658
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__objc_arraydata: 0x660
+  __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__cfstring: 0x4440
   __AUTH_CONST.__objc_const: 0x3a50
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 693
-  Symbols:   357
-  CStrings:  878
+  Functions: 695
+  Symbols:   358
+  CStrings:  880
 
Symbols:
+ ___NSDictionary0__struct
CStrings:
+ "+[NFHashes validateNFCCHashes:reference:expectedVersion:hashResults:]"
+ "nfcDeviceModeStateChangeCount"
+ "validHash"
- "+[NFHashes validateNFCCHashes:reference:expectedVersion:]"
```

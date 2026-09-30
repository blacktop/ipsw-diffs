## tvremoted

> `/usr/libexec/tvremoted`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-627.0.28.0.0
-  __TEXT.__text: 0xb85c
+627.10.45.0.0
+  __TEXT.__text: 0xba8c
   __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x1680
-  __TEXT.__objc_methlist: 0xb3c
+  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__objc_methlist: 0xb4c
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__objc_methname: 0x22f4
-  __TEXT.__oslogstring: 0x16e7
+  __TEXT.__objc_methname: 0x231d
+  __TEXT.__oslogstring: 0x1726
   __TEXT.__cstring: 0x4c3
   __TEXT.__objc_classname: 0xcc
   __TEXT.__objc_methtype: 0xdc4

   __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x910
-  __DATA.__objc_selrefs: 0x870
+  __DATA.__objc_selrefs: 0x878
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 214
+  Functions: 215
   Symbols:   83
-  CStrings:  592
+  CStrings:  594
 
Functions:
~ sub_100004160 : 476 -> 540
+ sub_10000ae30
CStrings:
+ "Not relinquishing %@ - a client connection is still interested"
+ "_hasInterestedClientConnectionForDevice:"
```

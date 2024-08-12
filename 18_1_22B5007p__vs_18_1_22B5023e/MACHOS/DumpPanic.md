## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-318.0.0.0.0
-  __TEXT.__text: 0x22b68
-  __TEXT.__auth_stubs: 0xcd0
+320.0.0.0.0
+  __TEXT.__text: 0x22c80
+  __TEXT.__auth_stubs: 0xcc0
   __TEXT.__objc_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x600
   __TEXT.__const: 0x38a
-  __TEXT.__cstring: 0x28dd
-  __TEXT.__gcc_except_tab: 0xa88
+  __TEXT.__cstring: 0x2923
+  __TEXT.__gcc_except_tab: 0xae4
   __TEXT.__oslogstring: 0x4578
   __TEXT.__ustring: 0x1c6
   __TEXT.__objc_classname: 0xfa
   __TEXT.__objc_methname: 0x18ca
   __TEXT.__objc_methtype: 0x427
   __TEXT.__unwind_info: 0x540
-  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__auth_got: 0x670
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x28e0
+  __DATA_CONST.__cfstring: 0x2900
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 417
-  Symbols:   289
-  CStrings:  1197
+  Symbols:   288
+  CStrings:  1199
 
Symbols:
- _objc_retain_x9
CStrings:
+ "iBoot panic-save unexpected reset, boot faults: %!@(MISSING)"
+ "invalid reset type"

```

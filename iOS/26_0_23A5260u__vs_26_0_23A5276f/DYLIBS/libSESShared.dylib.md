## libSESShared.dylib

> `/usr/lib/libSESShared.dylib`

```diff

-60.26.1.0.0
-  __TEXT.__text: 0xdfd8
+60.28.0.0.0
+  __TEXT.__text: 0xe174
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x900
-  __TEXT.__const: 0xa68
+  __TEXT.__const: 0xa60
   __TEXT.__cstring: 0xd0a
-  __TEXT.__oslogstring: 0x721
+  __TEXT.__oslogstring: 0x7d6
   __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x151a
+  __TEXT.__objc_methname: 0x1530
   __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__objc_stubs: 0x1080
+  __TEXT.__objc_stubs: 0x10a0
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x728
+  __DATA_CONST.__objc_selrefs: 0x730
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x390

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8CB9865A-EAB4-3EAA-964A-759A10B77AEB
+  UUID: 1CBD9F7B-D06A-3536-A6A3-FC0059C1DC3D
   Functions: 285
-  Symbols:   1057
-  CStrings:  773
+  Symbols:   1058
+  CStrings:  778
 
Symbols:
+ _objc_msgSend$initWithBytes:length:
Functions:
~ +[SESTLV _parseTLVs:end:simple:] : 1240 -> 1652
CStrings:
+ "Failed to recurse children of constructed (?) tag 0x%x, returning as simple"
+ "Tag value overflows"
+ "Underflow: tag=0x%x len=%u have=%lu offset=%lu"
+ "Unexpected %u len on tag 0"
+ "[SESTLV TLVWithTag:children:] failed!"
+ "initWithBytes:length:"
- "Underflow: tag=0x%x len=%u"

```

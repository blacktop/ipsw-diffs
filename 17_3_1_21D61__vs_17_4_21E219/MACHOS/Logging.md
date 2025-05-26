## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Logging`

```diff

-38.2.0.0.0
-  __TEXT.__text: 0xc68
+45.0.0.0.0
+  __TEXT.__text: 0xc8c
   __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x461
+  __TEXT.__cstring: 0x4a5
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methname: 0x49e
   __TEXT.__objc_methtype: 0x1a2

   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x120
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x50
   __DATA.__objc_const: 0x380
   __DATA.__objc_selrefs: 0x148
-  __DATA.__objc_classrefs: 0x50
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libobjc.A.dylib
   Functions: 17
   Symbols:   68
-  CStrings:  108
+  CStrings:  109
 
CStrings:
+ "Missing logarchive path. Use --Logging:archive=[path] to pass it"
+ "Passed logarchive path doesn't exist"
- "Passed logarchive path is invalid"

```

## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-315.0.0.0.1
-  __TEXT.__text: 0x22b70
+318.0.0.0.0
+  __TEXT.__text: 0x22b68
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x600
   __TEXT.__const: 0x38a
-  __TEXT.__cstring: 0x289e
-  __TEXT.__gcc_except_tab: 0xa90
+  __TEXT.__cstring: 0x28dd
+  __TEXT.__gcc_except_tab: 0xa88
   __TEXT.__oslogstring: 0x4578
   __TEXT.__ustring: 0x1c6
   __TEXT.__objc_classname: 0xfa

   __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x28a0
+  __DATA_CONST.__cfstring: 0x28e0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   - /usr/lib/libz.1.dylib
   Functions: 417
   Symbols:   289
-  CStrings:  1195
+  CStrings:  1197
 
CStrings:
+ " after panic save CE trigger"
+ " panic save CE trigger"
+ " panic save chip reset"
- " panic save"

```

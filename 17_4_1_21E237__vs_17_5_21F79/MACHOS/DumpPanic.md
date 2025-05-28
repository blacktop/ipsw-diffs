## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-285.100.1.0.0
-  __TEXT.__text: 0x24dcc
+285.120.1.0.1
+  __TEXT.__text: 0x24e5c
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_stubs: 0x1c20
   __TEXT.__objc_methlist: 0x538
   __TEXT.__const: 0x2ee
-  __TEXT.__cstring: 0x255e
+  __TEXT.__cstring: 0x25bf
   __TEXT.__gcc_except_tab: 0x7fc
-  __TEXT.__oslogstring: 0x3ee1
+  __TEXT.__oslogstring: 0x3f0b
   __TEXT.__ustring: 0x1c6
   __TEXT.__objc_classname: 0xdd
   __TEXT.__objc_methname: 0x15fb

   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x828
-  __DATA_CONST.__cfstring: 0x2520
+  __DATA_CONST.__cfstring: 0x2560
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x188
+  __DATA_CONST.__objc_arraydata: 0x198
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA.__objc_const: 0xc50
   __DATA.__objc_selrefs: 0x760
   __DATA.__objc_ivar: 0x9c

   - /usr/lib/libz.1.dylib
   Functions: 477
   Symbols:   279
-  CStrings:  1085
+  CStrings:  1088
 
CStrings:
+ "DRAM panic log missing; corefile fallback log in use"
+ "embedded_panic_header_corefile_fallback.bin"
+ "failed to write fallback data to file: %@"

```

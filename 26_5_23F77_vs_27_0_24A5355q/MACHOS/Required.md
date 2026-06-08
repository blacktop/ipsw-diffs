## Required

> `/System/Library/Trace/Providers/Required.bundle/Required`

```diff

-134.120.2.0.0
-  __TEXT.__text: 0x90a8
-  __TEXT.__auth_stubs: 0x790
+188.0.0.0.0
+  __TEXT.__text: 0x93bc
+  __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0x2dc
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x9eb
-  __TEXT.__objc_methname: 0x7c7
-  __TEXT.__objc_classname: 0x79
+  __TEXT.__cstring: 0xa46
+  __TEXT.__objc_methname: 0x7c1
+  __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x29a
-  __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__unwind_info: 0x370
-  __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__gcc_except_tab: 0x390
+  __TEXT.__unwind_info: 0x378
   __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__cfstring: 0x5c0
+  __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__got: 0xe0
   __DATA.__objc_const: 0x540
   __DATA.__objc_selrefs: 0x260
   __DATA.__objc_ivar: 0x34

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1EC9DE8-C686-343E-8787-0ED5BB612C4B
+  UUID: 13171EA5-452D-3142-8AE5-09E5D0B212CF
   Functions: 199
-  Symbols:   176
-  CStrings:  263
+  Symbols:   181
+  CStrings:  267
 
Symbols:
+ _ats_postprocessing_complete_write_dscmaps
+ _ats_postprocessing_complete_write_kernelmap
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x8
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "ApplePMPv2"
+ "Failed to serialize IO services metadata dictionary: %@"
+ "Failed to write DSC maps chunk (error %u)"
+ "Failed to write kernel map chunk (error %u)"
+ "_serializeIOServices"
- " SEGMENT"
- "Failed to serialize AGX and IOMFB metadata dictionary: %@"
- "_serializeIOMFBAGXServices"

```

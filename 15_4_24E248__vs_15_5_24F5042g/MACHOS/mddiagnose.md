## mddiagnose

> `/usr/bin/mddiagnose`

```diff

-2333.22.13.7.0
-  __TEXT.__text: 0xfc34
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_stubs: 0x12a0
+2333.41.1.3.0
+  __TEXT.__text: 0xff14
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_stubs: 0x12c0
   __TEXT.__objc_methlist: 0x314
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x4525
-  __TEXT.__objc_methname: 0xd7f
-  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__cstring: 0x4682
+  __TEXT.__objc_methname: 0xd96
+  __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__objc_classname: 0x4b
   __TEXT.__objc_methtype: 0x15d
   __TEXT.__oslogstring: 0x1b
   __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__auth_got: 0x768
+  __DATA_CONST.__auth_got: 0x780
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x518
-  __DATA_CONST.__cfstring: 0x4660
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__cfstring: 0x4860
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x428
-  __DATA_CONST.__objc_arrayobj: 0x450
+  __DATA_CONST.__objc_arraydata: 0x4d0
+  __DATA_CONST.__objc_arrayobj: 0x4e0
   __DATA.__objc_const: 0x360
-  __DATA.__objc_selrefs: 0x4f0
+  __DATA.__objc_selrefs: 0x4f8
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1ae8

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 323
-  Symbols:   302
-  CStrings:  965
+  Functions: 327
+  Symbols:   305
+  CStrings:  984
 
Symbols:
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
CStrings:
+ "\n\n=== Begin piped commands\n\n"
+ "\n'%@' exited with status '%i'\n"
+ "  Executing '%@'..."
+ "-0"
+ "-attr"
+ "/usr/bin/grep"
+ "/usr/bin/tr"
+ "/usr/bin/xargs"
+ "=== (%fsec) End of command '%@'\n"
+ "=== Begin command '%@'\n"
+ "=== Begin final command '%@'\n\n"
+ "=== Timed out waiting for piped commands to complete"
+ "Begin piped commands"
+ "End piped commands"
+ "\\0"
+ "\\n"
+ "com.apple.application-bundle"
+ "com.apple.mdsdiagnostic.piped"
+ "kMDItemContentType"
+ "setTerminationHandler:"
+ "v16@?0@\"NSTask\"8"
- "\n\n=== Begin piped commands\n"
- "\n=== Output of final command '%@'\n"

```

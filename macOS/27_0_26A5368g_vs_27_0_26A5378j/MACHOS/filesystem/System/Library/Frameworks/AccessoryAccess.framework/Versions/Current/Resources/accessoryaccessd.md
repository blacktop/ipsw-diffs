## accessoryaccessd

> `/System/Library/Frameworks/AccessoryAccess.framework/Versions/Current/Resources/accessoryaccessd`

```diff

-  __TEXT.__text: 0x3636c
-  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__text: 0x37424
+  __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_stubs: 0x240
-  __TEXT.__const: 0x3fe0
-  __TEXT.__gcc_except_tab: 0x3fe0
+  __TEXT.__const: 0x3fe8
+  __TEXT.__gcc_except_tab: 0x418c
   __TEXT.__cstring: 0xf5c
-  __TEXT.__oslogstring: 0x98f
+  __TEXT.__oslogstring: 0xa8b
   __TEXT.__objc_methname: 0x15c
-  __TEXT.__unwind_info: 0x1468
+  __TEXT.__unwind_info: 0x14c8
   __DATA_CONST.__const: 0xec8
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x6f8
+  __DATA_CONST.__auth_got: 0x710
   __DATA_CONST.__got: 0x1f0
   __DATA.__objc_selrefs: 0x90
   __DATA.__crash_info: 0x148

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 613
-  Symbols:   297
-  CStrings:  209
+  Functions: 622
+  Symbols:   300
+  CStrings:  214
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ _CFArrayAppendValue
+ _CFArrayCreateCopy
+ _CFArrayCreateMutable
CStrings:
+ "Configuration descriptor is only %zu bytes, expected at least %zu bytes"
+ "Failed to get configuration descriptor data."
+ "Failed to get descriptors from io_service_t."
+ "Failed to initialize USB descriptor parser for device."
+ "Failed to parse device descriptor."

```

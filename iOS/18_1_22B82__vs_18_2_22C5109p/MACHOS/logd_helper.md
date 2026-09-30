## logd_helper

> `/usr/libexec/logd_helper`

```diff

-1612.40.4.0.0
-  __TEXT.__text: 0x5074
+1612.60.25.0.0
+  __TEXT.__text: 0x5ac4
   __TEXT.__auth_stubs: 0x960
   __TEXT.__objc_stubs: 0x240
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xb21
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0xbb1
   __TEXT.__objc_methname: 0x174
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__unwind_info: 0x140
   __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x550
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x90

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 58
-  Symbols:   176
-  CStrings:  129
+  Functions: 62
+  Symbols:   175
+  CStrings:  134
 
Symbols:
+ _CSGetBinaryPathForExclaveWithUUIDBytes
+ __dyld_is_memory_immutable
- __os_trace_get_image_info
- __os_trace_macho_for_each_slice
- __os_trace_sect_names
CStrings:
+ "Harvesting from exclave failed (uuid: %!s(MISSING), err: %!x(MISSING))"
+ "Harvesting from exclave succeded: %!s(MISSING)"
+ "__OS_LOG"
+ "i16@?0r^{load_command=II}8"
+ "i24@?0[16c]8I16I20"

```

## IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

```diff

-399.27.7.0.0
-  __TEXT.__text: 0x24528
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__const: 0x19f8
-  __TEXT.__cstring: 0x4aca
-  __TEXT.__unwind_info: 0x3e8
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0xc0
+524.7.0.0.0
+  __TEXT.__text: 0x28f0c
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__const: 0x1a28
+  __TEXT.__cstring: 0x4be9
+  __TEXT.__unwind_info: 0x3f0
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x1ab0
   __DATA_CONST.__cfstring: 0x360
-  __DATA.__bss: 0x1bd32
+  __DATA.__bss: 0x1bd3a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: AEC622C8-B169-37E4-97D4-874240FDBDD0
-  Functions: 319
-  Symbols:   132
-  CStrings:  692
+  UUID: DD11C18A-CA61-3BF8-BB66-E663258B097E
+  Functions: 313
+  Symbols:   131
+  CStrings:  700
 
Symbols:
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- _wmemchr
CStrings:
+ "%s: Region data data not well-formed."
+ "e:  Invalid prox config encountered."
+ "e: Failed copy for EM LUTS"
+ "e: Invalid IRDC version %d\n"
+ "e: mismatching versions: %u != 1,2,3,6,7\n"
+ "e: mismatching versions: %u != 1,3,6, 7\n"
+ "e: missing gray scales (sync T%d B%d async T%d B%d)\n"
+ "e: too many Brightness tap points %d\n"
+ "e: too many Temp tap points %d\n"
+ "e: unsupported config: 0x%x\n"
- "e: mismatching versions: %u != 1,2,3,6\n"
- "e: mismatching versions: %u != 1,3,6\n"

```

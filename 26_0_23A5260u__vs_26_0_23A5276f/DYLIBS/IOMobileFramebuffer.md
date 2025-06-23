## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-524.7.0.0.0
-  __TEXT.__text: 0xda50
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__cstring: 0x1c6a
+524.18.0.0.0
+  __TEXT.__text: 0xdbc8
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__cstring: 0x1e16
   __TEXT.__const: 0xcc
   __TEXT.__unwind_info: 0x3b0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__cfstring: 0x840
   __DATA.__data: 0x34
   __DATA.__bss: 0x64
   __DATA_DIRTY.__data: 0xf0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: 93641CF8-3FF3-3F9B-917F-31165B5611FA
+  UUID: FD0CFBA3-C5DB-3070-B365-62899D700A24
   Functions: 408
-  Symbols:   818
-  CStrings:  280
+  Symbols:   819
+  CStrings:  289
 
Symbols:
+ _IOServiceGetMatchingServices
Functions:
~ ___iomfb_populate_all_display_infos_block_invoke : 1148 -> 1524
CStrings:
+ "%s: AppleParavirtGPU DisplayPortCount was not a 32 bit number - shouldn't happen - error\n"
+ "%s: AppleParavirtGPU missing DisplayPortCount - shouldn't happen - error\n"
+ "%s: Did not find a AppleParavirtGPU - shouldn't happen - error\n"
+ "%s: Found AppleParavirtGPU with DisplayPortCount %u\n"
+ "%s: IOServiceGetMatchingServices for AppleParavirtGPU failed - shouldn't happen - error\n"
+ "AppleParavirtGPU"
+ "DisplayPortCount"
+ "getParavirtDisplayCount"

```

## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-524.18.0.0.0
-  __TEXT.__text: 0xdbc8
+524.21.0.0.0
+  __TEXT.__text: 0xdc9c
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__cstring: 0x1e16
+  __TEXT.__cstring: 0x1ec8
   __TEXT.__const: 0xcc
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__unwind_info: 0x410
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8
   __AUTH_CONST.__auth_got: 0x3d0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: FD0CFBA3-C5DB-3070-B365-62899D700A24
-  Functions: 408
-  Symbols:   819
-  CStrings:  289
+  UUID: 11D3AFE9-5055-3A71-887C-CDD3BFA6C3A3
+  Functions: 410
+  Symbols:   822
+  CStrings:  292
 
Symbols:
+ _IOMobileFramebufferSwapSetLayerEDRCompensation
+ ___block_descriptor_tmp.226
+ _kern_SwapSetLayerEDRCompensation
- ___block_descriptor_tmp.224
CStrings:
+ "%s - Cannot use zero gamma value for %d layer\n"
+ "%s - Exceeded max number of layers: %d\n"
+ "IOReturn kern_SwapSetLayerEDRCompensation(IOMobileFramebufferRef, uint32_t, double, _Bool)"

```

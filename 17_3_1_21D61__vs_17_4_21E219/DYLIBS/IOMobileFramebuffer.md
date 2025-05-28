## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-336.3.6.0.0
-  __TEXT.__text: 0xc4b8
-  __TEXT.__auth_stubs: 0x750
+337.5.36.0.0
+  __TEXT.__text: 0xc8a0
+  __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x175a
-  __TEXT.__unwind_info: 0x364
+  __TEXT.__cstring: 0x17ef
+  __TEXT.__unwind_info: 0x374
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0xd0
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__cfstring: 0x7e0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x3b0
   __DATA.__data: 0x7c
   __DATA.__bss: 0x4
   __DATA_DIRTY.__const: 0xb0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  Functions: 363
-  Symbols:   733
-  CStrings:  181
+  Functions: 369
+  Symbols:   743
+  CStrings:  184
 
Symbols:
+ _IOMobileFrameBufferGetAutoLuminanceBoost
+ _IOMobileFramebufferAnnounceNextSwapTimestamp
+ _IOMobileFramebufferSetClamshellState
+ ___block_descriptor_tmp.202
+ _iomfb_AnnounceNextSwapTimestamp
+ _isServicingTwoExternalDisplay
+ _kern_SetClamshellState
+ _sleep
- ___block_descriptor_tmp.198
CStrings:
+ "%s: %s service is 0x%x\n"
+ "IOMFBIntDcpUsedForExtWhenLidClose"
+ "Warning: tried to match BC (%p) to IOMFB (%p) disp type (%d) with container ID (%s) - skip"

```

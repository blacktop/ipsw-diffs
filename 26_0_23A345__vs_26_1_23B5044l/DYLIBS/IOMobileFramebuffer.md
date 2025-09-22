## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-524.21.23.0.0
-  __TEXT.__text: 0xde3c
+524.22.6.0.0
+  __TEXT.__text: 0xdf6c
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__cstring: 0x1ee5
-  __TEXT.__const: 0xcc
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__const: 0xbc
+  __TEXT.__unwind_info: 0x420
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8
   __AUTH_CONST.__auth_got: 0x3d0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: 9C8FDB53-7857-3ED0-B86E-226FF4C46CC6
-  Functions: 414
-  Symbols:   828
+  UUID: 359A4FE0-7FF5-37EB-A37F-46B14F2330FE
+  Functions: 416
+  Symbols:   831
   CStrings:  294
 
Symbols:
+ _IOMobileFramebufferSwapSecureLayer
+ _kern_SwapSecureLayer
Functions:
~ _kern_SwapSetLayer : 1416 -> 1420
~ _IOMobileFramebufferOpen : 3296 -> 3316
~ __ioMobileFramebufferAlloc : 644 -> 704
~ _IOMobileFramebufferPowerNotifyFunc : 124 -> 128
+ _IOMobileFramebufferSwapSetEventSignalOnGlass
~ _benchmark_DisableNotifications : 32 -> 36
+ _kern_SwapSecureLayer
~ _kern_SetTVOutMode : 164 -> 168
~ _kern_SetDisplayDevice : 184 -> 188
~ _kern_SetDigitalOutMode : 180 -> 184
~ _virt_SetDigitalOutMode : 140 -> 144
~ _virt_GetDisplaySize : 92 -> 100

```

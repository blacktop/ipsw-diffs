## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-525.21.0.0.0
-  __TEXT.__text: 0xe094
+525.26.0.0.0
+  __TEXT.__text: 0xe178
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__cstring: 0x1f78
-  __TEXT.__const: 0xbc
+  __TEXT.__cstring: 0x1fb6
+  __TEXT.__const: 0xcc
   __TEXT.__unwind_info: 0x430
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: AAB1A23E-F9BA-3E3C-9AEE-7946F57FB1F5
-  Functions: 416
-  Symbols:   831
-  CStrings:  297
+  UUID: 5CDED003-D57B-3FB4-90C3-2A1257F24968
+  Functions: 420
+  Symbols:   837
+  CStrings:  299
 
Symbols:
+ _IOMobileFramebufferSwapSetAppleLook
+ _IOMobileFramebufferSwapSetLFCTimestamps
+ ___block_descriptor_tmp.232
+ _kern_SwapSetExternalAppleLook
+ _kern_SwapSetLFCTimestamps
- ___block_descriptor_tmp.231
Functions:
~ _kern_SwapSetLayer : 1420 -> 1416
~ _IOMobileFramebufferOpen : 3316 -> 3356
~ __ioMobileFramebufferAlloc : 704 -> 648
~ _IOMobileFramebufferPowerNotifyFunc : 128 -> 124
+ _IOMobileFramebufferSwapSetAppleLook
+ _IOMobileFramebufferSwapWorkaroundSettings
~ _IOMobileFramebufferGetBrightnessControlInfo : 72 -> 68
~ _benchmark_DisableNotifications : 36 -> 32
+ _kern_SwapSetExternalAppleLook
+ _kern_SwapSetLFCTimestamps
~ _kern_SetTVOutMode : 168 -> 164
~ _kern_SetDisplayDevice : 188 -> 184
~ _kern_SetDigitalOutMode : 184 -> 180
~ _IOMobileFramebufferOpenByName : 1576 -> 1548
~ _virt_SetDigitalOutMode : 144 -> 140
~ _virt_GetDisplaySize : 100 -> 92
~ _virt_EnableStatistics : 24 -> 20
CStrings:
+ "%s: LFC: NT=%llu EM=%llu lfc_en=%u\n"
+ "kern_SwapSetLFCTimestamps"

```

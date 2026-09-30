## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/Versions/A/IOMobileFramebuffer`

```diff

-525.22.1.0.0
-  __TEXT.__text: 0xe01c
+525.26.0.0.0
+  __TEXT.__text: 0xe100
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__cstring: 0x1f29
-  __TEXT.__const: 0xbc
+  __TEXT.__cstring: 0x1f67
+  __TEXT.__const: 0xcc
   __TEXT.__unwind_info: 0x3a8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: 7439E4E9-3CD0-3D84-8E20-6C6627265AA2
-  Functions: 416
-  Symbols:   611
-  CStrings:  296
+  UUID: 09D1A8C3-CD26-3C19-84CD-CC649B5C3C6C
+  Functions: 420
+  Symbols:   615
+  CStrings:  298
 
Symbols:
+ _IOMobileFramebufferSwapSetAppleLook
+ _IOMobileFramebufferSwapSetLFCTimestamps
+ __block_descriptor_tmp.232
+ _kern_SwapSetExternalAppleLook
+ _kern_SwapSetLFCTimestamps
- __block_descriptor_tmp.231
Functions:
+ _IOMobileFramebufferSwapSetAppleLook
+ _IOMobileFramebufferSwapSetBrightness
~ _IOMobileFramebufferGetBrightnessControlInfo : 72 -> 68
~ _IOMobileFramebufferOpen : 3316 -> 3356
~ __ioMobileFramebufferAlloc : 704 -> 648
~ _benchmark_DisableNotifications : 36 -> 32
~ _kern_SwapSetLayer : 1420 -> 1416
+ _kern_SwapSetExternalAppleLook
+ _kern_SwapSetLFCTimestamps
~ _kern_SetTVOutMode : 168 -> 164
~ _kern_SetDisplayDevice : 188 -> 184
~ _kern_SetDigitalOutMode : 184 -> 180
~ _IOMobileFramebufferOpenByName : 1576 -> 1548
~ _IOMobileFramebufferPowerNotifyFunc : 128 -> 124
~ _virt_SetDigitalOutMode : 144 -> 140
~ _virt_GetDisplaySize : 100 -> 92
~ _virt_EnableStatistics : 24 -> 20
CStrings:
+ "%s: LFC: NT=%llu EM=%llu lfc_en=%u\n"
+ "kern_SwapSetLFCTimestamps"

```

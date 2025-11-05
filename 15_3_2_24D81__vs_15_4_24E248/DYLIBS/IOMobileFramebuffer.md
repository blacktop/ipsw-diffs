## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/Versions/A/IOMobileFramebuffer`

```diff

-398.4.0.0.0
-  __TEXT.__text: 0xd624
+399.26.7.0.0
+  __TEXT.__text: 0xd704
   __TEXT.__auth_stubs: 0x790
   __TEXT.__cstring: 0x1b54
-  __TEXT.__const: 0xdc
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__const: 0xc8
+  __TEXT.__unwind_info: 0x370
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xb8
   __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x118
   __AUTH_CONST.__cfstring: 0x800

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: 2A45A0EA-9C87-3635-B309-0B172D8EEF56
+  UUID: 20755C7E-336A-3D74-96B0-4BCAA95C7CFB
   Functions: 403
-  Symbols:   592
+  Symbols:   597
   CStrings:  273
 
Symbols:
+ _IOMobileFramebufferSwapCancelAllGetCurrent
+ _IOMobileFramebufferSwapGetCurrent
+ _kern_SwapCancelAllGetCurrent
+ _kern_SwapGetCurrent
+ iomfb_populate_all_display_infos.cold.1

```

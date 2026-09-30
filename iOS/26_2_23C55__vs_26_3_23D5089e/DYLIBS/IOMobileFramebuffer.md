## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

```diff

-524.23.9.0.0
-  __TEXT.__text: 0xdf6c
+525.21.0.0.0
+  __TEXT.__text: 0xe094
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__cstring: 0x1ee5
+  __TEXT.__cstring: 0x1f78
   __TEXT.__const: 0xbc
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x430
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8
   __AUTH_CONST.__auth_got: 0x3d0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: 50917594-4173-3F7B-8897-B987D80CFA27
+  UUID: AAB1A23E-F9BA-3E3C-9AEE-7946F57FB1F5
   Functions: 416
   Symbols:   831
-  CStrings:  294
+  CStrings:  297
 
Symbols:
+ ___block_descriptor_tmp.231
- ___block_descriptor_tmp.229
Functions:
~ _iomfb_match_callback : 1060 -> 1180
~ _IOMobileFramebufferSetDigitalOutMode : 28 -> 128
~ _IOMobileFramebufferSetPreset : 48 -> 124
CStrings:
+ "IOMFB: %s: failed to fetch kIOMFBDisplayExternal property to determine index!\n"
+ "IOMobileFramebufferSetDigitalOutMode\n"
+ "IOMobileFramebufferSetPreset\n"

```

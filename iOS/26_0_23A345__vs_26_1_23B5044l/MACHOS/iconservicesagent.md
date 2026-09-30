## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

-729.100.0.0.0
-  __TEXT.__text: 0x4b8c
-  __TEXT.__auth_stubs: 0x580
+732.0.0.0.0
+  __TEXT.__text: 0x4bd0
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0x1220
   __TEXT.__objc_methlist: 0x3f4
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x387
+  __TEXT.__cstring: 0x3b6
   __TEXT.__oslogstring: 0x797
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__objc_methname: 0x11f7
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methtype: 0x3bd
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0x150
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x218
   __DATA_CONST.__cfstring: 0x620
   __DATA_CONST.__objc_classlist: 0x28

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
+  - /System/Library/PrivateFrameworks/IconRendering.framework/IconRendering
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36834285-782B-321D-A4E2-506CBB5388EE
+  UUID: 0B4143FC-D6E5-3795-90A5-15E3D66A33A9
   Functions: 95
-  Symbols:   142
-  CStrings:  449
+  Symbols:   144
+  CStrings:  450
 
Symbols:
+ _OBJC_CLASS_$_ICRTexturePool
+ _notify_post
Functions:
~ sub_100002dc4 -> sub_100002e2c : 20 -> 76
~ sub_100005028 -> sub_1000050c8 : 220 -> 232
CStrings:
+ "com.apple.iconservicesd.clearCache.immediately"

```

## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

```diff

-1027.2.1.0.0
-  __TEXT.__text: 0x15090
+1027.2.3.0.0
+  __TEXT.__text: 0x15638
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0x1e84
-  __TEXT.__const: 0xa8
+  __TEXT.__objc_stubs: 0x2ca0
+  __TEXT.__objc_methlist: 0x1ec4
+  __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x550
   __TEXT.__cstring: 0x4f81
-  __TEXT.__objc_methname: 0x5511
-  __TEXT.__oslogstring: 0x1381
+  __TEXT.__objc_methname: 0x55eb
+  __TEXT.__oslogstring: 0x148e
   __TEXT.__objc_classname: 0xe23
-  __TEXT.__objc_methtype: 0xeb7
+  __TEXT.__objc_methtype: 0xecc
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__unwind_info: 0x710
   __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x10c0
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x10e8
   __DATA_CONST.__cfstring: 0x4a80
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x3f80
-  __DATA.__objc_selrefs: 0x13b0
-  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_const: 0x3fb0
+  __DATA.__objc_selrefs: 0x13f8
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x1d10
   __DATA.__data: 0x188
   __DATA.__bss: 0x82

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5CDE3F5-FEFC-3A4F-84C4-E33FB248D09D
-  Functions: 560
-  Symbols:   549
-  CStrings:  2240
+  UUID: 48B50202-086A-3F61-A808-59C8E6AD5815
+  Functions: 569
+  Symbols:   553
+  CStrings:  2259
 
Symbols:
+ _AVSystemController_EffectiveVolumeDidChangeNotification
+ _AVSystemController_EffectiveVolumeNotificationParameter_Volume
+ _AVSystemController_EffectiveVolumeNotificationParameter_VolumeChangeReason
+ _OBJC_CLASS_$_AVSystemController
CStrings:
+ "Effective volume changed: %f. Reason: %@"
+ "Set volume for category %@ to %f"
+ "Tf,N,V_volume"
+ "Volume buttons are disabled, so undoing effective volume change and putting back old volume: %f"
+ "_effectiveVolumeChanged:"
+ "_updateAVSystemControllerWithVolume:"
+ "_volume"
+ "allowsVolumeButtons"
+ "effectiveVolumeChanged but notification info is nil"
+ "effectiveVolumeChanged but volume value is nil"
+ "f"
+ "f16@0:8"
+ "floatValue"
+ "getActiveCategoryVolume:andName:"
+ "setActiveCategoryVolumeTo:"
+ "setVolume:"
+ "sharedAVSystemController"
+ "v20@0:8f16"
+ "volume"

```

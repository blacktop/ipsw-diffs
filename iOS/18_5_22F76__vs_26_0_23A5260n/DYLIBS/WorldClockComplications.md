## WorldClockComplications

> `/System/Library/NanoTimeKit/ComplicationBundles/WorldClockComplications.bundle/WorldClockComplications`

```diff

-299.3.1.0.0
-  __TEXT.__text: 0x9828
-  __TEXT.__auth_stubs: 0x650
+316.0.0.0.0
+  __TEXT.__text: 0x858c
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__delay_stubs: 0xdc
+  __TEXT.__delay_helper: 0x17c
   __TEXT.__objc_methlist: 0x76c
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__cstring: 0x956
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x839
   __TEXT.__oslogstring: 0x600
   __TEXT.__ustring: 0x14
-  __TEXT.__dlopen_cstrs: 0xcc
-  __TEXT.__unwind_info: 0x340
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__objc_classname: 0x1cc
   __TEXT.__objc_methname: 0x20d6
   __TEXT.__objc_methtype: 0x422
   __TEXT.__objc_stubs: 0x1f40
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x930
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x9e0
   __AUTH_CONST.__objc_const: 0xd90

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x84
-  __DATA.__bss: 0x148
+  __DATA.__data: 0x4
+  __DATA.__bss: 0xe0
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications
   - /System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DA85ECD-1024-3AB2-98DA-8A3801C40889
-  Functions: 220
-  Symbols:   235
-  CStrings:  650
+  UUID: 10B9ADFA-BA56-3067-8AC1-D7BCC82C9757
+  Functions: 195
+  Symbols:   239
+  CStrings:  635
 
Symbols:
+ _NTKComplicationFamilyUtilitarianLargeNarrow
+ _NTKIdealizedDate
+ _NTKLocationComponentLatitudeKey
+ _NTKLocationComponentLongitudeKey
+ _NTKLocationComponentStrings
+ _NTKLocationComponentStringsShowSeconds
+ _NTKRoundDateDownToNearestMinute
+ _NTKShowBlueRidgeUI
+ _OBJC_CLASS_$_NTKLocationManager
+ _OBJC_CLASS_$_NTKOverrideTextProvider
+ _dlopen
- __os_feature_enabled_impl
- __sl_dlopen
- _abort_report_np
- _dlerror
- _dlsym
- _objc_getClass
- _objc_retain_x9
CStrings:
+ "/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit"
- "%s"
- "NTKComplicationFamilyUtilitarianLargeNarrow"
- "NTKIdealizedDate"
- "NTKLocationComponentLatitudeKey"
- "NTKLocationComponentLongitudeKey"
- "NTKLocationComponentStrings"
- "NTKLocationComponentStringsShowSeconds"
- "NTKLocationManager"
- "NTKOverrideTextProvider"
- "NTKRoundDateDownToNearestMinute"
- "NTKShowBlueRidgeUI"
- "Unable to find class %s"
- "WorldClockComplications"
- "snackbar"
- "softlink:r:path:/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion"
- "swiss"

```

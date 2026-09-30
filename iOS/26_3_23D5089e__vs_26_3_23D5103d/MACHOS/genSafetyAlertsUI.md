## genSafetyAlertsUI

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/PlugIns/genSafetyAlertsUI.appex/genSafetyAlertsUI`

```diff

-65.0.1.0.0
-  __TEXT.__text: 0x70c4
+65.0.2.0.0
+  __TEXT.__text: 0x747c
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x1180
+  __TEXT.__objc_stubs: 0x11a0
   __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__const: 0x2a8
+  __TEXT.__const: 0x2c8
   __TEXT.__cstring: 0x2b2
-  __TEXT.__gcc_except_tab: 0xc14
+  __TEXT.__gcc_except_tab: 0xc4c
   __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methname: 0x14c1
+  __TEXT.__objc_methname: 0x14e0
   __TEXT.__objc_methtype: 0x52a
-  __TEXT.__oslogstring: 0x12bf
+  __TEXT.__oslogstring: 0x165f
   __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x730
-  __DATA.__objc_selrefs: 0x6b8
+  __DATA.__objc_selrefs: 0x6c0
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A403946B-5AEA-3414-ADFF-EBF5228A185D
+  UUID: A8014566-3BB8-3AA8-BAA3-E02DBFA0542A
   Functions: 113
-  Symbols:   145
-  CStrings:  436
+  Symbols:   147
+  CStrings:  448
 
Symbols:
+ _OBJC_CLASS_$__MKCartographicMapConfiguration
+ __os_log_default
Functions:
~ sub_100001cc4 : 284 -> 360
~ sub_100001de0 -> sub_100001e2c : 3052 -> 3504
~ sub_1000029cc -> sub_100002bdc : 680 -> 832
~ sub_100002c74 -> sub_100002f1c : 2504 -> 2612
~ sub_100004e48 -> sub_10000515c : 1520 -> 1684
CStrings:
+ "#saGeneralNotificationExtension,didReceiveNotification:%{public}@"
+ "#saGeneralNotificationExtension,invalid or nil instruction"
+ "#saGeneralNotificationExtension,processMapImageInfo,about to request snapshot with options:%{public}@, snapshot:%{public}@"
+ "#saGeneralNotificationExtension,processMapImageInfo,centroidInvalid"
+ "#saGeneralNotificationExtension,processMapImageInfo,noGeometry"
+ "#saGeneralNotificationExtension,processMapImageInfo,regionSpan:%{public}f"
+ "#saGeneralNotificationExtension,processMapImageInfo,snapshotCallback,mapOverlayImage has been set to mapImageView"
+ "#saGeneralNotificationExtension,processMapImageInfo,snapshotCallback,snapshot:%{public}@, error:%{public}@"
+ "#saGeneralNotificationExtension,processMapImageInfo,usingGeometryCentroid, lat:%f, lon:%f"
+ "#saGeneralNotificationExtension,processMapImageInfo,valid polygons with number of polygons:%{public}lu"
+ "#saGeneralNotificationExtension,valid instruction:%{public}@"
+ "initWithCartographicConfiguration:"
+ "setPreferredConfiguration:"
- "_setCartographicConfiguration:"

```

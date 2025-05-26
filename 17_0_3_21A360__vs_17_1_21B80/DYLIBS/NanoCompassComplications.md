## NanoCompassComplications

> `/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications`

```diff

-502.0.0.0.0
-  __TEXT.__text: 0x353cc
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x32f4
-  __TEXT.__const: 0x484
-  __TEXT.__oslogstring: 0x33a3
-  __TEXT.__cstring: 0x3628
+524.2.1.0.0
+  __TEXT.__text: 0x34f84
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x3284
+  __TEXT.__const: 0x444
+  __TEXT.__oslogstring: 0x3362
+  __TEXT.__cstring: 0x35b8
   __TEXT.__ustring: 0xde
-  __TEXT.__gcc_except_tab: 0x930
+  __TEXT.__gcc_except_tab: 0x908
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__constg_swiftt: 0x148
-  __TEXT.__swift5_typeref: 0x5e
-  __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__constg_swiftt: 0x10c
+  __TEXT.__swift5_typeref: 0x58
+  __TEXT.__swift5_fieldmd: 0x64
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_reflstr: 0xf
-  __TEXT.__unwind_info: 0xeb0
-  __TEXT.__objc_classname: 0x8f0
-  __TEXT.__objc_methname: 0x7e9e
+  __TEXT.__unwind_info: 0xe98
+  __TEXT.__objc_classname: 0x909
+  __TEXT.__objc_methname: 0x7dd2
   __TEXT.__objc_methtype: 0x10ca
   __TEXT.__objc_stubs: 0x67a0
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0xcb0
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6370
-  __DATA_CONST.__objc_selrefs: 0x1f00
+  __DATA_CONST.__objc_const: 0x6308
+  __DATA_CONST.__objc_selrefs: 0x1ee8
   __DATA_CONST.__objc_arraydata: 0xa58
   __AUTH_CONST.__objc_doubleobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__cfstring: 0x2a20
-  __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__objc_const: 0x1aa8
+  __AUTH_CONST.__const: 0x5f0
+  __AUTH_CONST.__objc_const: 0x1a60
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x588
-  __AUTH.__objc_data: 0x1988
-  __AUTH.__data: 0x138
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH.__objc_data: 0x18d0
+  __AUTH.__data: 0x110
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x4c0
+  __DATA.__objc_classrefs: 0x4b8
   __DATA.__objc_superrefs: 0x190
-  __DATA.__objc_ivar: 0x490
-  __DATA.__data: 0x658
-  __DATA.__bss: 0x748
-  __DATA.__common: 0x38
+  __DATA.__objc_ivar: 0x488
+  __DATA.__data: 0x650
+  __DATA.__bss: 0x758
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
-  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
-  - /System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync
   - /System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications
   - /System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1405
-  Symbols:   634
-  CStrings:  2446
+  Functions: 1394
+  Symbols:   633
+  CStrings:  2436
 
Symbols:
+ _AccuracyThreshold
+ _IsNanoCompass
- _OBJC_CLASS_$__TtC24NanoCompassComplications21UnitLengthPreferences
- _OBJC_METACLASS_$__TtC24NanoCompassComplications21UnitLengthPreferences
- ___chkstk_darwin
CStrings:
+ "%s: Loaded guides, calling _refreshNonDistanceLimitedWaypoints"
+ "%s: posting notification for GuidesFirstUnlockNotification"
+ "-[NCGuidesManager _handleFirstUnlock]_block_invoke"
+ "-[NCGuidesManager _loadGuides]_block_invoke"
+ "-[NCGuidesManager init]_block_invoke"
+ "CellularWaypointEquality"
+ "Created guide with name %@ and waypoints %@"
+ "_locationPromptShownAction"
+ "isEquivalentCellularWaypoint:"
+ "mainBundle"
+ "performAfterLocationPromptIsShown:"
+ "usesMetricSystem"
- "%s: We can't refresh guides until the store controller has loaded."
- "%s: already waiting for map guides to load."
- "%s: deferring loading of maps guides until device unlock"
- "%s: not loading map guides as the device has not been unlocked"
- "-[NCGuidesManager _loadMapGuides]"
- "-[NCGuidesManager _loadMapGuides]_block_invoke"
- "T@\"_TtC24NanoCompassComplications21UnitLengthPreferences\",N,R"
- "TB,GisInterestAdjustmentNeeded,V_interestAdjustmentNeeded"
- "_TtC24NanoCompassComplications21UnitLengthPreferences"
- "_interestAdjustmentNeeded"
- "_loadMapGuides"
- "_locationPromptCompletionHandler"
- "_reloadGuidesOnFirstUnlock:"
- "_waitingForStoreController"
- "interestAdjustmentNeeded"
- "isInterestAdjustmentNeeded"
- "locationPromptIsShownWithCompletion:"
- "setInterestAdjustmentNeeded:"
- "shared"
- "usesMetric"

```

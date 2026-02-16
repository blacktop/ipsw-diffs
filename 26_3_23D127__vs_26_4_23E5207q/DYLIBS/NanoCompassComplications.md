## NanoCompassComplications

> `/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications`

```diff

-676.2.13.0.0
-  __TEXT.__text: 0x3fc58
-  __TEXT.__auth_stubs: 0xa90
+676.5.6.0.0
+  __TEXT.__text: 0x42d20
+  __TEXT.__auth_stubs: 0xa40
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x3c64
+  __TEXT.__objc_methlist: 0x3cc4
   __TEXT.__const: 0x544
-  __TEXT.__cstring: 0x3e3e
+  __TEXT.__cstring: 0x3bca
   __TEXT.__ustring: 0xd6
-  __TEXT.__oslogstring: 0x3da0
-  __TEXT.__gcc_except_tab: 0xb40
+  __TEXT.__oslogstring: 0x3f5b
+  __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x90
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x25
-  __TEXT.__unwind_info: 0x10e8
-  __TEXT.__objc_classname: 0xa1f
-  __TEXT.__objc_methname: 0x8d71
-  __TEXT.__objc_methtype: 0x137c
-  __TEXT.__objc_stubs: 0x7320
-  __DATA_CONST.__got: 0x680
-  __DATA_CONST.__const: 0xdb0
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __TEXT.__unwind_info: 0x12a0
+  __TEXT.__objc_classname: 0xbb8
+  __TEXT.__objc_methname: 0x8f02
+  __TEXT.__objc_methtype: 0x139a
+  __TEXT.__objc_stubs: 0x7460
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2418
+  __DATA_CONST.__objc_selrefs: 0x2440
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x1140
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH_CONST.__const: 0xa00
+  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__const: 0xa20
   __AUTH_CONST.__cfstring: 0x3080
-  __AUTH_CONST.__objc_const: 0x6fe8
+  __AUTH_CONST.__objc_const: 0x7090
   __AUTH_CONST.__objc_doubleobj: 0x4d0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH.__objc_data: 0x1c38
+  __AUTH.__objc_data: 0x1c88
   __AUTH.__data: 0x160
   __DATA.__objc_ivar: 0x52c
   __DATA.__data: 0x3cc
-  __DATA.__bss: 0x988
+  __DATA.__bss: 0x998
   __DATA.__common: 0x38
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/WatchKit.framework/WatchKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications
   - /System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWatchKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 87BDAEA0-5C4F-39D3-8C55-8976C4F547C6
-  Functions: 1618
-  Symbols:   682
-  CStrings:  3107
+  UUID: 5F0AE1D1-28C7-3B2F-AFCF-11AB02FCF6F7
+  Functions: 1631
+  Symbols:   681
+  CStrings:  3110
 
Symbols:
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_VehicleEventsManager
+ _OBJC_CLASS_$_WKInterfaceDevice
+ _OBJC_METACLASS_$_VehicleEventsManager
+ __swift_FORCE_LOAD_$_swiftWatchKit
- _OBJC_CLASS_$_UIScreen
- __swiftEmptyDictionarySingleton
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%s targetedWaypoint is %@"
+ "-[SmartWaypointComplicationDataSource _fetchTargetedWaypoint]"
+ "4AF61239-332F-481C-B7DE-7E80973B07BF"
+ "@\"NSHashTable\""
+ "FE1BCD7B-332F-481C-B7DE-7E80973B07BF"
+ "NCStyleAttributes"
+ "TB,N,V_hasVehicleEvents"
+ "VehicleEventsManager"
+ "VehicleEventsManager: Cannot start monitoring for nil client"
+ "VehicleEventsManager: Cannot stop monitoring for nil client"
+ "VehicleEventsManager: Client %@ does not support parked car, not monitoring "
+ "VehicleEventsManager: Client %@ started monitoring (total clients: %lu)"
+ "VehicleEventsManager: Client %@ stopped monitoring (remaining clients: %lu)"
+ "VehicleEventsManager: Client %@ supports parked car, start monitoring "
+ "_monitoringClients"
+ "hasVehicleEvents"
+ "setHasVehicleEvents:"
+ "startMonitoringVehicleEventsForClient:"
+ "stopMonitoringVehicleEventsForClient:"
+ "supportsParkedCarComplication"
+ "weakObjectsHashTable"
- "4AF61239-2126-4FD6-8E7A-CDA2D7A0BFE9"
- "FE1BCD7B-63A2-4EB3-9EF5-D6A9E506101E"
- "_disabledGuidesQueue"
- "com.apple.nanocompass.guidesmanager.disabledguides"
- "mainScreen"

```

## EnergyKitService

> `/System/Library/PrivateFrameworks/EnergyKitInternal.framework/XPCServices/EnergyKitService.xpc/EnergyKitService`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0x5c024
-  __TEXT.__auth_stubs: 0x1e40
-  __TEXT.__objc_methlist: 0x998
-  __TEXT.__cstring: 0x1832
-  __TEXT.__objc_methname: 0x1cba
-  __TEXT.__oslogstring: 0x1266
+347.0.0.0.0
+  __TEXT.__text: 0x658e0
+  __TEXT.__auth_stubs: 0x2180
+  __TEXT.__objc_methlist: 0x99c
+  __TEXT.__cstring: 0x18a2
+  __TEXT.__objc_methname: 0x1cd4
+  __TEXT.__oslogstring: 0x1596
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xf08
-  __TEXT.__constg_swiftt: 0x9cc
-  __TEXT.__swift5_types: 0x70
-  __TEXT.__swift5_typeref: 0x6dd
-  __TEXT.__swift_as_entry: 0x15c
-  __TEXT.__swift5_reflstr: 0x452
-  __TEXT.__swift5_fieldmd: 0x4c0
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_capture: 0x7f8
+  __TEXT.__const: 0xfe8
+  __TEXT.__constg_swiftt: 0xa6c
+  __TEXT.__swift5_types: 0x74
+  __TEXT.__swift5_typeref: 0x763
+  __TEXT.__swift_as_entry: 0x174
+  __TEXT.__swift5_reflstr: 0x492
+  __TEXT.__swift5_fieldmd: 0x4f4
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_capture: 0x82c
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methtype: 0x695
-  __TEXT.__swift_as_ret: 0x228
+  __TEXT.__swift_as_ret: 0x250
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x1498
-  __TEXT.__eh_frame: 0x4c1c
-  __DATA_CONST.__auth_got: 0xf20
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__auth_ptr: 0x2a8
-  __DATA_CONST.__const: 0x1608
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x1600
+  __TEXT.__eh_frame: 0x537c
+  __DATA_CONST.__auth_got: 0x10c0
+  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__auth_ptr: 0x2d0
+  __DATA_CONST.__const: 0x1680
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA.__objc_const: 0x2178
+  __DATA.__objc_const: 0x2228
   __DATA.__objc_selrefs: 0x7d8
-  __DATA.__objc_data: 0x318
-  __DATA.__data: 0x18f8
-  __DATA.__common: 0xd8
-  __DATA.__bss: 0x780
+  __DATA.__objc_data: 0x368
+  __DATA.__data: 0x1a90
+  __DATA.__common: 0xe0
+  __DATA.__bss: 0x800
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation
   - /System/Library/PrivateFrameworks/EnergyKitInternal.framework/EnergyKitInternal
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents
   - /System/Library/PrivateFrameworks/HomeServices.framework/HomeServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 24F86CE2-5680-3AEA-8A13-091CB40A5078
-  Functions: 1125
-  Symbols:   191
-  CStrings:  571
+  UUID: 77332A58-76D0-3CDB-AAF9-AF5A3A2FE0FE
+  Functions: 1186
+  Symbols:   192
+  CStrings:  589
 
Symbols:
+ _swift_allocBox
CStrings:
+ "Corrected historical interval from %s to %s"
+ "Skip interval"
+ "[LoadEventManager] Cached GridID is %s"
+ "[LoadEventManager] Cached Home is %s"
+ "[LoadEventManager] Failed to process %ld events"
+ "[LoadEventManager] Failed to process event %@"
+ "[LoadEventManager] Feature Disabled. Skip submission"
+ "[LoadEventManager] Mocking enabled. Skip submission"
+ "[LoadEventManager] Processing Load %s from %s"
+ "[LoadEventManager] Retrieved GridID is %s"
+ "[LoadEventManager] Retrieved Home is %s"
+ "[LoadEventManager] Uploading %ld Load Events"
+ "[LoadEventOperations] Event submission failed: %@"
+ "[LoadEventOperations] Invalid application-identifier"
+ "[LoadEventOperations] Submitted %ld load event records"
+ "[LoadEventOperations] Unauthorized"
+ "_TtC16EnergyKitService16LoadEventManager"
+ "lastFetchedGridID"
+ "lastFetchedHome"
+ "submitLoadEventsWithEvents:sandboxExtension:completionHandler:"
+ "v40@0:8@\"_TtC9EnergyKit31XPCElectricalLoadEventContainer\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?q>32"
- "com.apple.EnergyKitService.Load"
- "receiveLoadEvents:completionHandler:"
- "v32@0:8@\"_TtC17EnergyKitInternal21XPCLoadEventContainer\"16@?<v@?q@\"NSError\">24"

```

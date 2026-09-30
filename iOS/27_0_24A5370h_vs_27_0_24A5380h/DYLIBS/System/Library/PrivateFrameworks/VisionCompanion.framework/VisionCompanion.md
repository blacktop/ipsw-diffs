## VisionCompanion

> `/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion`

```diff

-  __TEXT.__text: 0x74230
+  __TEXT.__text: 0x76ea4
   __TEXT.__objc_methlist: 0x3f8
-  __TEXT.__const: 0x3cbc
-  __TEXT.__swift5_typeref: 0x1592
-  __TEXT.__swift5_capture: 0xa04
-  __TEXT.__cstring: 0x17af
-  __TEXT.__constg_swiftt: 0x1004
+  __TEXT.__const: 0x3d3c
+  __TEXT.__swift5_typeref: 0x15da
+  __TEXT.__swift5_capture: 0xa28
+  __TEXT.__cstring: 0x18ef
+  __TEXT.__constg_swiftt: 0x1048
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x740
-  __TEXT.__swift5_fieldmd: 0xa70
+  __TEXT.__swift5_reflstr: 0x7a0
+  __TEXT.__swift5_fieldmd: 0xac0
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__oslogstring: 0x1dc4
+  __TEXT.__oslogstring: 0x1f94
   __TEXT.__swift5_proto: 0x22c
-  __TEXT.__swift5_types: 0x110
-  __TEXT.__swift_as_entry: 0x334
-  __TEXT.__swift_as_ret: 0x3fc
-  __TEXT.__swift_as_cont: 0x650
+  __TEXT.__swift5_types: 0x118
+  __TEXT.__swift_as_entry: 0x338
+  __TEXT.__swift_as_ret: 0x400
+  __TEXT.__swift_as_cont: 0x65c
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x1dc0
-  __TEXT.__eh_frame: 0x6028
+  __TEXT.__unwind_info: 0x1e28
+  __TEXT.__eh_frame: 0x60e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3850
+  __AUTH_CONST.__const: 0x3988
   __AUTH_CONST.__objc_const: 0xc28
-  __AUTH_CONST.__auth_got: 0xea0
+  __AUTH_CONST.__auth_got: 0xed8
   __AUTH.__objc_data: 0x90
-  __AUTH.__data: 0x358
-  __DATA.__data: 0xa78
+  __AUTH.__data: 0x3d8
+  __DATA.__data: 0xab8
   __DATA.__bss: 0x2f50
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x220

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1961
-  Symbols:   1471
-  CStrings:  295
+  Functions: 1993
+  Symbols:   1499
+  CStrings:  313
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _MCFeatureDiagnosticsSubmissionAllowed
+ _OBJC_CLASS_$_MCProfileConnection
+ _objc_msgSend$effectiveBoolValueForSetting:
+ _objc_msgSend$initWithLongLong:
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$synchronize
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic SS_So8NSObjectCt
+ _symbolic _____ 15VisionCompanion0B7SessionV
+ _symbolic _____ 15VisionCompanion19DiagnosticUtilitiesO
+ _symbolic _____ s5Int64V
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
CStrings:
+ "%s DNU isAllowed: %{bool}d"
+ "%s cross device analytics task completed"
+ "%s fetched session: sessionCount=%lld, lastSessionDate=%s"
+ "%s fetching CompanionSession for cross-device analytics"
+ "%s received unexpected cross device analytics task %s"
+ "%s reset session"
+ "%s wipe skipped: KVS already empty"
+ "%s wipe sync failed: %@"
+ "%s wipe sync succeeded"
+ "%s wiping session keys (DNU disabled)"
+ "AnalyticsCoordinator"
+ "CompanionToDeviceActivation"
+ "CompanionToDeviceActivationThreeDays"
+ "recentlyOpenedSession_one_day"
+ "recentlyOpenedSession_seven_days"
+ "recentlyOpenedSession_thirty_days"
+ "recentlyOpenedSession_three_days"
+ "sessionsSinceLastDeviceUse"

```

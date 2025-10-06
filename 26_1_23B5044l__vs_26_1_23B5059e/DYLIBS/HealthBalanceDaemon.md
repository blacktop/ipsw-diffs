## HealthBalanceDaemon

> `/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon`

```diff

-6200.2.7.2.1
-  __TEXT.__text: 0x76b10
-  __TEXT.__auth_stubs: 0x2300
+6200.2.11.2.0
+  __TEXT.__text: 0x7a34c
+  __TEXT.__auth_stubs: 0x2500
   __TEXT.__objc_methlist: 0x834
-  __TEXT.__const: 0x2584
-  __TEXT.__cstring: 0x251f
-  __TEXT.__constg_swiftt: 0x125c
-  __TEXT.__swift5_typeref: 0xfe4
-  __TEXT.__swift5_reflstr: 0x153d
-  __TEXT.__swift5_fieldmd: 0x10a4
+  __TEXT.__const: 0x25d4
+  __TEXT.__cstring: 0x257f
+  __TEXT.__constg_swiftt: 0x128c
+  __TEXT.__swift5_typeref: 0x1016
+  __TEXT.__swift5_reflstr: 0x15b3
+  __TEXT.__swift5_fieldmd: 0x10e4
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_proto: 0x130
-  __TEXT.__swift5_types: 0x118
-  __TEXT.__oslogstring: 0x1f2e
+  __TEXT.__swift5_types: 0x11c
+  __TEXT.__oslogstring: 0x1fd3
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_capture: 0x388
-  __TEXT.__unwind_info: 0xfa0
-  __TEXT.__eh_frame: 0xe20
+  __TEXT.__unwind_info: 0x1000
+  __TEXT.__eh_frame: 0xec8
   __TEXT.__objc_classname: 0x272
-  __TEXT.__objc_methname: 0x2455
+  __TEXT.__objc_methname: 0x24de
   __TEXT.__objc_methtype: 0x68f
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x888
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xa48
   __DATA_CONST.__objc_protorefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x1188
-  __AUTH_CONST.__const: 0x2088
+  __AUTH_CONST.__auth_got: 0x1288
+  __AUTH_CONST.__const: 0x2090
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x2258
+  __AUTH_CONST.__objc_const: 0x2298
   __AUTH.__objc_data: 0x400
-  __AUTH.__data: 0x850
-  __DATA.__data: 0x10f8
-  __DATA.__bss: 0x1490
+  __AUTH.__data: 0x8d0
+  __DATA.__data: 0x11b0
+  __DATA.__bss: 0x14a0
   __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x748
+  __DATA_DIRTY.__objc_data: 0x758
   __DATA_DIRTY.__data: 0x17b8
   __DATA_DIRTY.__common: 0x80
   __DATA_DIRTY.__bss: 0x980

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B607DCC4-90DE-37F2-A2CE-AA7B7704F374
-  Functions: 1518
-  Symbols:   1054
-  CStrings:  802
+  UUID: D9D57FF4-18D3-3230-BB1F-08338718321B
+  Functions: 1553
+  Symbols:   1057
+  CStrings:  811
 
Symbols:
+ _symbolic So26HDContentProtectionManagerCSg
+ _symbolic Ss_SiSgt
+ _symbolic _____ 11SleepHealth0aB28NotificationSettingsProviderC
+ _symbolic _____ 19HealthBalanceDaemon39VitalsOutlierNotificationHoldIdentifierV
+ _symbolic _____Sg 11SleepHealth0aB28NotificationSettingsProviderC
- _symbolic _____ 13HealthBalance48SleepingSampleChangeNotificationSettingsProviderC
- _symbolic _____Sg 13HealthBalance48SleepingSampleChangeNotificationSettingsProviderC
CStrings:
+ "[%{public}s] Error issuing hold instruction for vitals outliers notification (%s): %{public}@"
+ "[%{public}s] Error issuing send instruction for vitals outliers notification (%s): %{public}@"
+ "[%{public}s] Error reading sleep event record: %{public}@"
+ "[%{public}s] Notification is held"
+ "[%{public}s] Posting notification (%s)"
+ "[%{public}s] Skipping hold instruction for %s due to no protected data"
+ "contentProtectionManager"
+ "currentSleepEventRecordWithError:"
+ "isProtectedDataAvailable"
+ "lastWakeUpResultsIntroductionNotificationVersionSent"
+ "shouldIssueSendInstructionsWhenFiringVitalsOutlierNotification"
- "[%{public}s] Error sending instruction for vitals change notification (%s): %{public}@"
- "[%{public}s] Posting notification (%s) and syncing a hold instruction"
- "[%{public}s] Skipping Sleep Score notification because we notified on Vitals."

```

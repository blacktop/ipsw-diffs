## HealthMedicationsExperience

> `/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0x8c124
-  __TEXT.__auth_stubs: 0x22d0
-  __TEXT.__objc_methlist: 0x244
-  __TEXT.__const: 0x4814
-  __TEXT.__cstring: 0x3bfb
-  __TEXT.__swift5_typeref: 0x157e
-  __TEXT.__swift5_reflstr: 0x167a
-  __TEXT.__swift5_assocty: 0x340
-  __TEXT.__constg_swiftt: 0x192c
-  __TEXT.__swift5_fieldmd: 0x135c
+5200.2.4.1.5
+  __TEXT.__text: 0x95710
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__objc_methlist: 0x280
+  __TEXT.__const: 0x4914
+  __TEXT.__cstring: 0x3ceb
+  __TEXT.__swift5_typeref: 0x169e
+  __TEXT.__swift5_reflstr: 0x177a
+  __TEXT.__swift5_assocty: 0x358
+  __TEXT.__constg_swiftt: 0x199c
+  __TEXT.__swift5_fieldmd: 0x141c
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_proto: 0x244
-  __TEXT.__swift5_types: 0x180
-  __TEXT.__swift5_capture: 0x694
-  __TEXT.__oslogstring: 0xea2
-  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift5_proto: 0x248
+  __TEXT.__swift5_types: 0x188
+  __TEXT.__swift5_capture: 0x6ec
+  __TEXT.__oslogstring: 0xeb2
+  __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x22b8
-  __TEXT.__eh_frame: 0x2ab8
+  __TEXT.__unwind_info: 0x24f0
+  __TEXT.__eh_frame: 0x30e0
   __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methname: 0x1c9c
+  __TEXT.__objc_methname: 0x1e4d
   __TEXT.__objc_methtype: 0x17e
-  __DATA_CONST.__got: 0x9f8
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8a0
+  __DATA_CONST.__objc_selrefs: 0x928
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1168
-  __AUTH_CONST.__auth_ptr: 0x6e0
-  __AUTH_CONST.__const: 0x2aa0
-  __AUTH_CONST.__objc_const: 0x2708
-  __AUTH.__objc_data: 0x2c8
-  __AUTH.__data: 0x12b0
-  __DATA.__data: 0xf28
-  __DATA.__bss: 0x2c18
+  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH_CONST.__auth_ptr: 0x708
+  __AUTH_CONST.__const: 0x2d48
+  __AUTH_CONST.__objc_const: 0x2778
+  __AUTH.__objc_data: 0x360
+  __AUTH.__data: 0x1230
+  __DATA.__data: 0x1040
+  __DATA.__bss: 0x2c28
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x7d8
-  __DATA_DIRTY.__data: 0x14e8
+  __DATA_DIRTY.__data: 0x1508
   __DATA_DIRTY.__bss: 0x1a80
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform
   - /System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2956
-  Symbols:   458
-  CStrings:  812
+  Functions: 3104
+  Symbols:   475
+  CStrings:  834
 
Symbols:
+ _OBJC_CLASS_$_HKDismissedRemoteScheduleUnavailableRecord
+ _OBJC_CLASS_$_HKRemoteScheduleUnavailableRecord
+ _OBJC_CLASS_$_NRPairedDeviceRegistry
+ _OBJC_CLASS_$__TtC27HealthMedicationsExperience39MedicationsScheduleIncompatibilityCache
+ _OBJC_METACLASS_$__TtC27HealthMedicationsExperience39MedicationsScheduleIncompatibilityCache
CStrings:
+ "%!s(MISSING) Failed to get the incompatibility result back from cache, getter returned nil."
+ "HealthMedicationsExperience.MedicationsScheduleIncompatibilityCache"
+ "[%!s(MISSING)] IncompatibilityResult is nil. Error: '%!@(MISSING)'"
+ "_TtC27HealthMedicationsExperience39LocalScheduleUnavailableAlertDeterminer"
+ "_scheduleIncompatibilityCache"
+ "allDismissedRemoteScheduleUnavailableRecordsWithCompletion:"
+ "deviceForIdentifier:"
+ "deviceIdentifiers"
+ "devices"
+ "getActivePairedDevice"
+ "getDismissedRemoteRecords()"
+ "getResolvedIncompatibilityResults()"
+ "hardwareIdentifier"
+ "initWithLocalPairedDevice:"
+ "initWithMedication:schedule:devices:"
+ "isCompatibleWithSchedule:"
+ "isCompatibleWithScheduleCompatibilityVersion:"
+ "localDeviceInfo"
+ "markRemoteScheduleUnavailableRecordsAsDismissed:completion:"
+ "medication"
+ "medication schedule "
+ "medicationFeatureDevicesInfo"
+ "model"
+ "saveRemoteRecords(_:)"
+ "scheduleCompatibilityVersion"
+ "sharedInstance"
+ "unitTestingCacheUpdateHandler"
- "%!s(MISSING) Failed to get the incompatibility result cache back, getter returned nil."
- "[%!s(MISSING)] IncompatibilityResult is nil"
- "_TtC27HealthMedicationsExperience34ScheduleUnavailableAlertDeterminer"
- "filterOutCompatibleSchedules:"
- "incompatibilityCacheKVDKey"
- "medications schedules devices "

```

## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x56f1c
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x454c
-  __TEXT.__const: 0x198
+6200.5.77.2.6
+  __TEXT.__text: 0x594cc
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_methlist: 0x4584
+  __TEXT.__const: 0x18a
   __TEXT.__cstring: 0x6569
-  __TEXT.__gcc_except_tab: 0xaa4
-  __TEXT.__oslogstring: 0x626b
+  __TEXT.__gcc_except_tab: 0xb1c
+  __TEXT.__oslogstring: 0x6464
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x13f0
+  __TEXT.__unwind_info: 0x1550
   __TEXT.__objc_classname: 0x1209
-  __TEXT.__objc_methname: 0xf1d6
-  __TEXT.__objc_methtype: 0x264e
-  __TEXT.__objc_stubs: 0x8b80
+  __TEXT.__objc_methname: 0xf2a0
+  __TEXT.__objc_methtype: 0x26d7
+  __TEXT.__objc_stubs: 0x8be0
   __DATA_CONST.__got: 0x820
-  __DATA_CONST.__const: 0x1c60
+  __DATA_CONST.__const: 0x1cf8
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f68
+  __DATA_CONST.__objc_selrefs: 0x2f90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x2d8
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x78f8
+  __AUTH_CONST.__objc_const: 0x7908
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
-  - /System/Library/PrivateFrameworks/HealthContentDaemon.framework/HealthContentDaemon
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications
   - /System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles
+  - /System/Library/PrivateFrameworks/HealthOntologyDaemon.framework/HealthOntologyDaemon
+  - /System/Library/PrivateFrameworks/HealthTopics.framework/HealthTopics
+  - /System/Library/PrivateFrameworks/HealthTopicsCore.framework/HealthTopicsCore
   - /System/Library/PrivateFrameworks/Koa.framework/Koa
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 81CD5699-B0D1-3DD9-942D-859CBBF97738
-  Functions: 1911
-  Symbols:   6799
-  CStrings:  3535
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 4146C02A-B948-3790-B6CC-8F7999181663
+  Functions: 1934
+  Symbols:   6945
+  CStrings:  3550
 
Symbols:
+ -[HDMedicationCountProvider userDomainConceptManager:didAddUserDomainConcepts:maxAnchor:]
+ -[HDMedicationCountProvider userDomainConceptManager:didDeleteUserDomainConcepts:maxAnchor:]
+ -[HDMedicationCountProvider userDomainConceptManager:didUpdateUserDomainConcepts:maxAnchor:]
+ -[HDMedicationDataDonator userDomainConceptManager:didAddUserDomainConcepts:maxAnchor:]
+ -[HDMedicationDataDonator userDomainConceptManager:didDeleteUserDomainConcepts:maxAnchor:]
+ -[HDMedicationDataDonator userDomainConceptManager:didUpdateUserDomainConcepts:maxAnchor:]
+ -[HDMedicationScheduleManager userDomainConceptManager:didAddUserDomainConcepts:maxAnchor:]
+ -[HDMedicationScheduleManager userDomainConceptManager:didDeleteUserDomainConcepts:maxAnchor:]
+ -[HDMedicationScheduleManager userDomainConceptManager:didUpdateUserDomainConcepts:maxAnchor:]
+ -[HDMedicationsWidgetSchedulingManager isMedicationFeatureAvailable:]
+ -[HDMedicationsWidgetSchedulingManager shouldRefreshWidget:]
+ -[HDMedicationsWidgetSchedulingManager shouldRefreshWidget:].cold.1
+ GCC_except_table13
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.421
+ __OBJC_$_PROP_LIST_HDMedicationCountProvider.434
+ ___60-[HDMedicationsWidgetSchedulingManager shouldRefreshWidget:]_block_invoke
+ ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.362
+ ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.387
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40r48r56r_e40_16?0"HKMedicationExposableDoseEvent"8lr40l8s32l8r48l8r56l8
+ ___block_literal_global.392
+ ___block_literal_global.408
+ ___block_literal_global.413
+ ___block_literal_global.425
+ ___block_literal_global.427
+ ___block_literal_global.428
+ ___block_literal_global.430
+ ___block_literal_global.436
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.442
+ ___block_literal_global.480
+ ___block_literal_global.518
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_HealthMedicationsDaemonPlugin
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_HealthMedicationsDaemonPlugin
+ _objc_msgSend$enqueueMaintenanceOperation:withPeriodicActivity:
+ _objc_msgSend$isMedicationFeatureAvailable:
+ _objc_msgSend$shouldRefreshWidget:
- -[HDMedicationCountProvider userDomainConceptManager:didAddUserDomainConcepts:]
- -[HDMedicationCountProvider userDomainConceptManager:didDeleteUserDomainConcepts:]
- -[HDMedicationCountProvider userDomainConceptManager:didUpdateUserDomainConcepts:]
- -[HDMedicationDataDonator userDomainConceptManager:didAddUserDomainConcepts:]
- -[HDMedicationDataDonator userDomainConceptManager:didDeleteUserDomainConcepts:]
- -[HDMedicationDataDonator userDomainConceptManager:didUpdateUserDomainConcepts:]
- -[HDMedicationScheduleManager userDomainConceptManager:didAddUserDomainConcepts:]
- -[HDMedicationScheduleManager userDomainConceptManager:didDeleteUserDomainConcepts:]
- -[HDMedicationScheduleManager userDomainConceptManager:didUpdateUserDomainConcepts:]
- __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.382
- __OBJC_$_PROP_LIST_HDMedicationCountProvider.393
- ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.323
- ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.348
- ___block_descriptor_72_e8_32s40r48r_e40_16?0"HKMedicationExposableDoseEvent"8lr40l8s32l8r48l8
- ___block_literal_global.352
- ___block_literal_global.353
- ___block_literal_global.369
- ___block_literal_global.374
- ___block_literal_global.386
- ___block_literal_global.388
- ___block_literal_global.389
- ___block_literal_global.397
- ___block_literal_global.398
- ___block_literal_global.400
- ___block_literal_global.403
- ___block_literal_global.441
- ___block_literal_global.479
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "B32@0:8@\"NSString\"16@?<v@?>24"
+ "B32@0:8@16@?24"
+ "[%{public}@] Database not accessible yet, assuming active medications exist and proceeding with widget setup"
+ "[%{public}@] Failed to check active medications: %{public}@, skipping widget operations"
+ "[%{public}@] Found active medications, will refresh widget"
+ "[%{public}@] Health Medications Profile Extension not found"
+ "[%{public}@] No active medications found, skipping widget operations to avoid unnecessary widget process spawning"
+ "[%{public}@] Skipping medication widget operations - feature not available"
+ "daemonDidReceiveRapportEvent:completion:"
+ "enqueueMaintenanceOperation:withPeriodicActivity:"
+ "isMedicationFeatureAvailable:"
+ "samplesMapWereRemoved:anchor:"
+ "shouldRefreshWidget:"
+ "userDomainConceptManager:didAddUserDomainConcepts:maxAnchor:"
+ "userDomainConceptManager:didDeleteUserDomainConcepts:maxAnchor:"
+ "userDomainConceptManager:didUpdateUserDomainConcepts:maxAnchor:"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
+ "v40@0:8@\"HDUserDomainConceptManager\"16@\"NSArray\"24q32"
- "userDomainConceptManager:didAddUserDomainConcepts:"
- "userDomainConceptManager:didDeleteUserDomainConcepts:"
- "userDomainConceptManager:didUpdateUserDomainConcepts:"

```

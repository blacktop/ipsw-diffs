## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.2.7.2.1
-  __TEXT.__text: 0x791648
+6200.2.11.2.0
+  __TEXT.__text: 0x7920f8
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43ab4
+  __TEXT.__objc_methlist: 0x43afc
   __TEXT.__const: 0x1df7c
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7d07f
+  __TEXT.__cstring: 0x7d12f
   __TEXT.__constg_swiftt: 0x14dc
   __TEXT.__swift5_typeref: 0xd9d
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x5c4
-  __TEXT.__oslogstring: 0x41a07
+  __TEXT.__oslogstring: 0x41aee
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__gcc_except_tab: 0x38348
+  __TEXT.__gcc_except_tab: 0x383b4
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1ccf8
+  __TEXT.__unwind_info: 0x1cd28
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0xc5c3
-  __TEXT.__objc_methname: 0x8eb18
+  __TEXT.__objc_methname: 0x8ebec
   __TEXT.__objc_methtype: 0x16b0a
-  __TEXT.__objc_stubs: 0x504e0
-  __DATA_CONST.__got: 0x5660
-  __DATA_CONST.__const: 0x1d250
+  __TEXT.__objc_stubs: 0x50520
+  __DATA_CONST.__got: 0x5668
+  __DATA_CONST.__const: 0x1d2a0
   __DATA_CONST.__objc_classlist: 0x29d8
   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19eb0
+  __DATA_CONST.__objc_selrefs: 0x19ed8
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
-  __DATA_CONST.__objc_arraydata: 0x8498
+  __DATA_CONST.__objc_arraydata: 0x84a0
   __AUTH_CONST.__auth_got: 0x2428
-  __AUTH_CONST.__const: 0xffe0
-  __AUTH_CONST.__cfstring: 0x3d5c0
-  __AUTH_CONST.__objc_const: 0x7d940
-  __AUTH_CONST.__objc_arrayobj: 0x1ec0
+  __AUTH_CONST.__const: 0x10018
+  __AUTH_CONST.__cfstring: 0x3d5e0
+  __AUTH_CONST.__objc_const: 0x7d960
+  __AUTH_CONST.__objc_arrayobj: 0x1ed8
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0xd438
-  __AUTH.__data: 0x7e0
-  __DATA.__objc_ivar: 0x43b4
+  __AUTH.__objc_data: 0xd120
+  __AUTH.__data: 0x760
+  __DATA.__objc_ivar: 0x43b8
   __DATA.__data: 0x81c8
   __DATA.__common: 0x64
-  __DATA.__bss: 0x18c8
+  __DATA.__bss: 0x18c0
   __DATA_DIRTY.__objc_ivar: 0xe80
-  __DATA_DIRTY.__objc_data: 0xdfc8
-  __DATA_DIRTY.__data: 0x1a0
-  __DATA_DIRTY.__bss: 0x3c8
+  __DATA_DIRTY.__objc_data: 0xe2e0
+  __DATA_DIRTY.__data: 0x210
+  __DATA_DIRTY.__bss: 0x3d0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/AddressBook.framework/AddressBook

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 06AD7B45-E726-3C72-A85C-FEEBB5799387
-  Functions: 34751
-  Symbols:   103866
-  CStrings:  44249
+  UUID: CDC5C05D-D0A4-3374-B824-8E1ECAAA3885
+  Functions: 34762
+  Symbols:   103898
+  CStrings:  44260
 
Symbols:
+ +[HDAuthorizationEntity _shouldSkipAuthorizationInsertionForBloodPressureMismatch:sourceEntity:]
+ +[HDSyncAnchorEntity unitTest_predicateForReceived:]
+ +[HDSyncAnchorEntity unitTest_predicateForStoreType:]
+ +[HDSyncAnchorEntity unitTest_predicateForType:]
+ +[HDSyncAnchorEntity unitTest_predicateForValidated:]
+ -[HDAnchoredObjectQueryServer _supportsBackgroundDataCollection]
+ -[HDQueryServer _supportsBackgroundDataCollection]
+ _HKWatchECGSampleAvailabilityDays
+ _OBJC_IVAR_$_HDSmoothingTask._previousSmoothingError
+ __HDResetECGNanoSyncAnchorsOnWatch
+ ___108-[HDWorkoutBuilderEntity pruneAssociatedSamplesToDateInterval:transaction:error:zonesHandler:sampleHandler:]_block_invoke_2
+ ___52-[HDWorkoutLocationSmoother _queue_smoothNextSample]_block_invoke.393
+ ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.401
+ ___91-[HDWorkoutBuilderEntity _createTemporaryProtectedAssociatedSampleListInTransaction:error:]_block_invoke_5
+ ___block_descriptor_186_ea8_32s40s48s56bs64bs112c97_ZTSNSt3__113unordered_setI15_HKDataTypeCodeNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEE152c23_ZTS14HKIntervalMaskIdE_e9_B16?0^8l
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_72_ea8_32s40bs48r56r_e9_B16?0^8lr48l8s32l8r56l8s40l8
+ ___block_literal_global.410
+ ___copy_helper_block_ea8_112c97_ZTSNSt3__113unordered_setI15_HKDataTypeCodeNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEE152c23_ZTS14HKIntervalMaskIdE
+ ___destroy_helper_block_ea8_112c97_ZTSNSt3__113unordered_setI15_HKDataTypeCodeNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEE152c23_ZTS14HKIntervalMaskIdE
+ _objc_msgSend$_shouldSkipAuthorizationInsertionForBloodPressureMismatch:sourceEntity:
+ _objc_msgSend$_supportsBackgroundDataCollection
+ _objc_msgSend$isCondenserVersionLessThan:transaction:
- -[HDCarouselServicesManager takeSessionAssertionForOwnerIdentifier:]
- ___52-[HDWorkoutLocationSmoother _queue_smoothNextSample]_block_invoke.392
- ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.399
- ___block_literal_global.409
- _objc_msgSend$takeSessionAssertionForOwnerIdentifier:
CStrings:
+ "<Workout UUID=%@ \ntotalLocations=%tu \nTask Creation Date=%@ \nTask Start Date=%@ \nAttempts=%lu \nPrevious Attempts Error=%@ \nError=%@>"
+ "Creating tempory table for association sample list"
+ "Skipping authorization insertion: systolic (%ld) and diastolic (%ld) authorization statuses don't match for source %@"
+ "UPDATE sync_anchors SET received=0, validated=0 WHERE sync_anchors.type = 53 AND store IN (SELECT ROWID FROM sync_stores WHERE sync_stores.type=1);"
+ "Will freeze %lu quantity sample series for post journal merge"
+ "_previousSmoothingError"
+ "_shouldSkipAuthorizationInsertionForBloodPressureMismatch:sourceEntity:"
+ "_supportsBackgroundDataCollection"
+ "unitTest_predicateForReceived:"
+ "unitTest_predicateForStoreType:"
+ "unitTest_predicateForType:"
+ "unitTest_predicateForValidated:"
- "<Workout UUID=%@ \ntotalLocations=%tu \nTask Creation Date=%@ \nTask Start Date=%@ \nAttempts=%lu \nError=%@>"
- "takeSessionAssertionForOwnerIdentifier:"

```

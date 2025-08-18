## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6106.1.2.5.0
-  __TEXT.__text: 0x78c90c
+6106.1.2.9.0
+  __TEXT.__text: 0x78cf48
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x435bc
+  __TEXT.__objc_methlist: 0x43614
   __TEXT.__const: 0x1dd74
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7c1c7
+  __TEXT.__cstring: 0x7c209
   __TEXT.__constg_swiftt: 0x14a4
   __TEXT.__swift5_typeref: 0xd25
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__unwind_info: 0x1cc00
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0xc522
-  __TEXT.__objc_methname: 0x8e504
+  __TEXT.__objc_methname: 0x8e5d0
   __TEXT.__objc_methtype: 0x16a85
-  __TEXT.__objc_stubs: 0x50300
-  __DATA_CONST.__got: 0x5628
+  __TEXT.__objc_stubs: 0x50340
+  __DATA_CONST.__got: 0x5630
   __DATA_CONST.__const: 0x1d2d0
   __DATA_CONST.__objc_classlist: 0x29b0
-  __DATA_CONST.__objc_catlist: 0x4b8
+  __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19d40
+  __DATA_CONST.__objc_selrefs: 0x19d50
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __DATA_CONST.__objc_superrefs: 0x1d60
+  __DATA_CONST.__objc_superrefs: 0x1d70
   __DATA_CONST.__objc_arraydata: 0x8478
   __AUTH_CONST.__auth_got: 0x2428
   __AUTH_CONST.__const: 0xfde8
-  __AUTH_CONST.__cfstring: 0x3d1e0
-  __AUTH_CONST.__objc_const: 0x7d258
+  __AUTH_CONST.__cfstring: 0x3d220
+  __AUTH_CONST.__objc_const: 0x7d2c8
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xd2a8
   __AUTH.__data: 0x7e0
-  __DATA.__objc_ivar: 0x4374
+  __DATA.__objc_ivar: 0x4378
   __DATA.__data: 0x8188
   __DATA.__common: 0x64
   __DATA.__bss: 0x14c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4A1F2225-EE30-389C-BD2F-81C2DC30077D
-  Functions: 34609
-  Symbols:   103573
-  CStrings:  44115
+  UUID: CF8FCCC4-B923-3C21-93F1-46C439E4350B
+  Functions: 34615
+  Symbols:   103593
+  CStrings:  44123
 
Symbols:
+ +[HDBinarySampleSyncEntity _predicateForSyncSession:]
+ +[HDQuantitySampleSyncEntity _predicateForSyncSession:]
+ +[HKUnprocessedBloodOxygenDataSample(HDExtensions) hd_dataEntityClass]
+ -[HDNanoSyncStore remoteDeviceSupportsUSLegallyCompliantOxygenSaturation]
+ -[HKUnprocessedBloodOxygenDataSample(HDCodingSupport) codableRepresentationForSync]
+ _HKCategoryTypeIdentifierUnsuccessfulBloodOxygenSaturationAnalysisEvent
+ _OBJC_CLASS_$_HKUnprocessedBloodOxygenDataSample
+ _OBJC_IVAR_$_HDNanoSyncStore._remoteDeviceSupportsUSLegallyCompliantOxygenSaturation
+ __OBJC_$_CATEGORY_HKUnprocessedBloodOxygenDataSample_$_HDCodingSupport
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HKUnprocessedBloodOxygenDataSample_$_HDCodingSupport
+ __OBJC_$_CLASS_METHODS_HKUnprocessedBloodOxygenDataSample(HDCodingSupport|HDExtensions)
+ ___block_descriptor_56_e8_32s40s_e40_v16?0"HDMirroredWorkoutSessionServer"8ls32l8s40l8
+ ___block_literal_global.495
+ __isCompanionSyncToUSLegallyCompliantOxygenSaturationDeviceForSyncSession
+ _objc_msgSend$remoteDeviceSupportsUSLegallyCompliantOxygenSaturation
+ _objc_msgSend$unprocessedBloodOxygenDataType
- ___block_descriptor_48_e8_32s_e40_v16?0"HDMirroredWorkoutSessionServer"8ls32l8
- ___block_literal_global.481
- ___block_literal_global.490
- ___block_literal_global.494
Functions:
+ -[HKUnprocessedBloodOxygenDataSample(HDCodingSupport) codableRepresentationForSync]
~ ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke : 568 -> 572
~ ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.327 : 144 -> 160
~ -[HDNanoSyncStore _initWithIdentityServicesDevice:nanoRegistryDevice:pairingEntity:obliteratedDatabaseUUIDs:protocolVersion:delegate:profile:tinkerPairing:] : 724 -> 804
+ -[HDNanoSyncStore remoteDeviceSupportsUSLegallyCompliantOxygenSaturation]
~ +[HDCategorySampleSyncEntity _predicateForSyncSession:] : 160 -> 320
+ __isCompanionSyncToUSLegallyCompliantOxygenSaturationDeviceForSyncSession
+ +[HDQuantitySampleSyncEntity _predicateForSyncSession:]
~ +[HDDeletedSampleSyncEntity _predicateForSyncSession:] : 1420 -> 1656
+ +[HDBinarySampleSyncEntity _predicateForSyncSession:]
+ +[HDQuantitySampleStatisticsEntity databaseTable]
CStrings:
+ "2D6D2220-64DB-408A-89ED-ED05391073E8"
+ "TB,R,V_remoteDeviceSupportsUSLegallyCompliantOxygenSaturation"
+ "_remoteDeviceSupportsUSLegallyCompliantOxygenSaturation"
+ "oxygen_saturation_phone_only"
+ "remoteDeviceSupportsUSLegallyCompliantOxygenSaturation"
+ "unprocessedBloodOxygenDataType"

```

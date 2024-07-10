## MicroLocationDaemon

> `/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/Versions/A/MicroLocationDaemon`

```diff

-27.0.26.0.0
-  __TEXT.__text: 0x1cccb8
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x441c
-  __TEXT.__gcc_except_tab: 0x20ae4
-  __TEXT.__cstring: 0xcc90
+27.0.24.0.0
+  __TEXT.__text: 0x1cc7a0
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_methlist: 0x43ac
+  __TEXT.__gcc_except_tab: 0x20bdc
+  __TEXT.__cstring: 0xcd50
   __TEXT.__const: 0x962e
-  __TEXT.__oslogstring: 0x259ee
+  __TEXT.__oslogstring: 0x25c2e
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_typeref: 0xad
   __TEXT.__swift5_fieldmd: 0x30

   __TEXT.__unwind_info: 0xa020
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xb6d
-  __TEXT.__objc_methname: 0xb6d2
-  __TEXT.__objc_methtype: 0xaa33
-  __TEXT.__objc_stubs: 0x9b20
-  __DATA_CONST.__got: 0x5c8
+  __TEXT.__objc_methname: 0xb626
+  __TEXT.__objc_methtype: 0xaa24
+  __TEXT.__objc_stubs: 0x9a00
+  __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29f8
+  __DATA_CONST.__objc_selrefs: 0x29b0
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc40
   __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x9980
   __AUTH_CONST.__cfstring: 0x43c0

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7419
-  Symbols:   14638
-  CStrings:  1674
+  Functions: 7409
+  Symbols:   14624
+  CStrings:  1679
 
Symbols:
+ -[ULPersistenceStore loadWithCoordinator:]
+ -[ULStore _openRadarOnDatabaseAccessError]
+ GCC_except_table391
+ _ZN20CLMiLoServiceManager33migrateLegacyServiceIdToServiceIdEN5boost5uuids4uuidENSt3__18optionalIS2_EE.cold.1
+ _ZN20CLMiLoServiceManager33migrateLegacyServiceIdToServiceIdEN5boost5uuids4uuidENSt3__18optionalIS2_EE.cold.2
+ _ZN20CLMiLoServiceManager33migrateLegacyServiceIdToServiceIdEN5boost5uuids4uuidENSt3__18optionalIS2_EE.cold.3
+ _ZN20CLMiLoServiceManager33migrateLegacyServiceIdToServiceIdEN5boost5uuids4uuidENSt3__18optionalIS2_EE.cold.4
+ _ZN20CLMiLoServiceManager37findOrCreateServiceEntryWithServiceIdEN5boost5uuids4uuidERKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS3_8optionalI13ULServiceTypeEEb.cold.1
+ ___42-[ULPersistenceStore loadWithCoordinator:]_block_invoke
+ ___block_descriptor_40_e8_32r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
+ __block_literal_global.400
+ __block_literal_global.407
+ __block_literal_global.411
+ __block_literal_global.416
+ __block_literal_global.426
+ __block_literal_global.435
+ __block_literal_global.454
+ __block_literal_global.523
+ __block_literal_global.743
+ __block_literal_global.869
+ _objc_msgSend$_openRadarOnDatabaseAccessError
+ _objc_msgSend$loadWithCoordinator:
- -[ULPersistenceManager _deleteDatabaseFilesAtPath:]
- -[ULPersistenceManager _destroyStore]
- -[ULPersistenceManager _disconnectFromStore]
- -[ULPersistenceManager _exitProcessWithFailureCode]
- -[ULPersistenceManager _handleCorruptedDatabase:]
- -[ULPersistenceManager _handleDatabaseError:]
- -[ULPersistenceManager _isMainDatabase]
- -[ULPersistenceManager destroyStore]
- -[ULPersistenceManager handleDatabaseError:]
- -[ULPersistenceStore loadWithCoordinator:error:]
- -[ULStore _handleDatabaseError:]
- _NSSQLiteErrorDomain
- ___36-[ULPersistenceManager destroyStore]_block_invoke
- ___44-[ULPersistenceManager handleDatabaseError:]_block_invoke
- ___48-[ULPersistenceStore loadWithCoordinator:error:]_block_invoke
- ___block_descriptor_48_e8_32r40r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
- ___copy_helper_block_e8_32r40r
- ___destroy_helper_block_e8_32r40r
- __block_literal_global.402
- __block_literal_global.409
- __block_literal_global.413
- __block_literal_global.418
- __block_literal_global.428
- __block_literal_global.437
- __block_literal_global.456
- __block_literal_global.525
- __block_literal_global.745
- __block_literal_global.871
- _exit
- _objc_msgSend$_deleteDatabaseFilesAtPath:
- _objc_msgSend$_destroyStore
- _objc_msgSend$_disconnectFromStore
- _objc_msgSend$_exitProcessWithFailureCode
- _objc_msgSend$_handleCorruptedDatabase:
- _objc_msgSend$_handleDatabaseError:
- _objc_msgSend$_isMainDatabase
- _objc_msgSend$destroyStore
- _objc_msgSend$handleDatabaseError:
- _objc_msgSend$loadWithCoordinator:error:
- _objc_msgSend$userInfo
CStrings:
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationDaemon/Utilities/ULTimerFactory.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationAlgorithms.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationAlgorithms.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBinaryRoiNullSpaceAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBlueAtlasAlgorithms.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBlueAtlasAlgorithms.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBlueAtlasLocalize.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationCosineSimilarityLocalize.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationDendrogramAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprint.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprintDataSources.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprintDistanceFunction.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprintVector.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationLearner.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationLocalizationController.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationLogic.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationModel.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationNearestNeighborAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationNullSpaceAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationPublishHelper.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationRecorder.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationSemiSupervisedAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationSingleClusterNullSpaceAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationStateMachine.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationTimeUtils.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationTriggerManager.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationUtils.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationWiFiChannelHistogramAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/LogicAdapter/ULLogicAdapter.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/LogicAdapter/ULLogicAdapterHelper.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/MachineLearning/CLHierarchicalClustering.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLMicroLocationDatabaseColumns.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLSqlite/CLSqliteDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLSqlite/CLSqliteDatabaseManager.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLSqlite/Utilities/CLMachThreadSupport.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Sensors/CLMicroLocationSensorsDriver.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/ServiceManager/CLMiLoService.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/ServiceManager/CLMiLoServiceManager.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Settings/ULSettings.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/proto/microlocation.pb.cc"
+ "createResult.errorId == ULConnectionErrorCode::ULConnectionErrorNoError"
+ "findOrCreateServiceEntryWithServiceId"
+ "migrateLegacyClientIdToClientIdIfNecessary"
+ "migrateLegacyServiceIdToServiceId"
+ "res"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationDaemon/Utilities/ULTimerFactory.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationAlgorithms.h"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationAlgorithms.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBinaryRoiNullSpaceAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBlueAtlasAlgorithms.h"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBlueAtlasAlgorithms.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationBlueAtlasLocalize.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationCosineSimilarityLocalize.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationDendrogramAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprint.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprintDataSources.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprintDistanceFunction.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationFingerprintVector.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationLearner.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationLocalizationController.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationLogic.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationModel.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationNearestNeighborAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationNullSpaceAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationPublishHelper.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationRecorder.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationSemiSupervisedAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationSingleClusterNullSpaceAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationStateMachine.h"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationTimeUtils.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationTriggerManager.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationUtils.h"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/CLMicroLocationWiFiChannelHistogramAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/LogicAdapter/ULLogicAdapter.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/LogicAdapter/ULLogicAdapterHelper.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/MachineLearning/CLHierarchicalClustering.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLMicroLocationDatabaseColumns.h"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLSqlite/CLSqliteDatabase.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLSqlite/CLSqliteDatabaseManager.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Persistence/DataMigration/CLSqlite/Utilities/CLMachThreadSupport.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Sensors/CLMicroLocationSensorsDriver.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/ServiceManager/CLMiLoService.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/ServiceManager/CLMiLoServiceManager.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/Settings/ULSettings.mm"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationLogic/proto/microlocation.pb.cc"

```

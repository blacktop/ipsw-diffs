## TimeMachine

> `/System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine`

```diff

-2427.0.0.0.0
-  __TEXT.__text: 0xe06bc
-  __TEXT.__auth_stubs: 0x26b0
-  __TEXT.__objc_methlist: 0x5014
-  __TEXT.__const: 0x27a4
-  __TEXT.__cstring: 0xb4cc
-  __TEXT.__gcc_except_tab: 0x1e74
+2430.0.0.0.0
+  __TEXT.__text: 0xd8ac4
+  __TEXT.__auth_stubs: 0x26a0
+  __TEXT.__objc_methlist: 0x5808
+  __TEXT.__const: 0x27c4
+  __TEXT.__cstring: 0xb52c
+  __TEXT.__gcc_except_tab: 0x1e8c
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__swift5_typeref: 0x1330
+  __TEXT.__swift5_typeref: 0x131a
   __TEXT.__swift5_reflstr: 0xf5a
   __TEXT.__swift5_assocty: 0x420
   __TEXT.__constg_swiftt: 0x1a58
   __TEXT.__swift5_fieldmd: 0x12c0
   __TEXT.__swift5_proto: 0xfc
   __TEXT.__swift5_types: 0x17c
+  __TEXT.__swift_as_entry: 0x140
+  __TEXT.__swift_as_ret: 0x148
   __TEXT.__swift5_capture: 0x5f4
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0xd8
-  __TEXT.__unwind_info: 0x3540
-  __TEXT.__eh_frame: 0x3548
+  __TEXT.__unwind_info: 0x31f0
+  __TEXT.__eh_frame: 0x3538
   __TEXT.__objc_classname: 0x8ce
-  __TEXT.__objc_methname: 0xcb50
+  __TEXT.__objc_methname: 0xcbe1
   __TEXT.__objc_methtype: 0x25f9
-  __TEXT.__objc_stubs: 0x9600
-  __DATA_CONST.__got: 0xb10
-  __DATA_CONST.__const: 0xa50
+  __TEXT.__objc_stubs: 0x9620
+  __DATA_CONST.__got: 0xaf0
+  __DATA_CONST.__const: 0xa70
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3190
+  __DATA_CONST.__objc_selrefs: 0x3248
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x1370
+  __AUTH_CONST.__auth_got: 0x1368
   __AUTH_CONST.__const: 0x5470
-  __AUTH_CONST.__cfstring: 0x7e60
-  __AUTH_CONST.__objc_const: 0x9720
+  __AUTH_CONST.__cfstring: 0x7f00
+  __AUTH_CONST.__objc_const: 0x8958
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x15f8
   __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0x474
-  __DATA.__data: 0x95e8
+  __DATA.__objc_ivar: 0x478
+  __DATA.__data: 0x95e0
   __DATA.__bss: 0x3e30
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4FC494A9-E9DE-3E9B-BE62-546E864FE7D1
-  Functions: 4106
-  Symbols:   5932
-  CStrings:  4914
+  UUID: 8FDC142F-AFF8-3187-864B-6070BEC81017
+  Functions: 3883
+  Symbols:   5974
+  CStrings:  4929
 
Symbols:
+ +[NSDate(TMAdditions) _tm_dateFormatter].cold.1
+ +[NSURL(TMAdditions) tm_rospDataVolumeURL].cold.1
+ +[TMAPFSMachineStore addMachineStoreRootACLsToURL:error:].cold.1
+ +[TMBackupDeleter defaultDeleter].cold.1
+ +[TMFirmLinkMap currentRootFirmLinkMap].cold.1
+ +[TMIOKitDisk startupVolumeGroupUUID].cold.1
+ +[TMLogging countDictionary].cold.1
+ +[TMLoggingFormatter standardFormatter].cold.1
+ +[TMMailPersistenceInfo currentMailVersionDirectoryName].cold.1
+ +[TMSession sessionTable].cold.1
+ +[TMSession(Finder) ROSPVolumeStoreInfoCache].cold.1
+ +[TMSession(Finder) cache].cold.1
+ +[TMSession(Finder) currentSystemVolume].cold.1
+ +[TMSession(Finder) inheritanceHistoryCache].cold.1
+ +[TMSession(Finder) remappingCache].cold.1
+ +[TMSystemInformation hasInternalBattery].cold.1
+ +[TMSystemInformation isAppleInternal].cold.1
+ +[TMSystemInformation isNetBooted].cold.1
+ +[TMSystemInformation macAddress].cold.1
+ +[TMSystemPathsOracle _knownSystemInstalledBundleExtensions].cold.1
+ +[TMTarget rootTarget].cold.1
+ -[NSURL _tm_extendedAttributeKeysWithError:including:].cold.2
+ -[TMBackup setUuidToVolumeStoresLock:]
+ -[TMBackup uuidToVolumeStoresLock]
+ -[TMDiskImage backupDiskRawDevicePath]
+ DeleteSnapshotNow.cold.1
+ OBJC_IVAR_$_TMBackup._uuidToVolumeStoresLock
+ __ZNKSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI14NodeCacheEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPKS1_S7_EEvT_T0_l
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne190102Em
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.289
+ _objc_msgSend$backupDiskRawDevicePath
- GCC_except_table67
- __ZNKSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI14NodeCacheEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI14NodeCacheEntryNS_9allocatorIS1_EEE18__assign_with_sizeB8ne180100IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2Em
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __block_literal_global.281
- _fmod
- _symbolic Si3key______5valuetSg 11TimeMachine12XPCTaskGroupC9TaskEntryV
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMAPFSBackupListener.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMBackupDataSource.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMHFSBackupListener.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Configuration/TMConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrList.swift"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrListDisk.swift"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMAPFSDisk.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDADisk.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDisk.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDiskImage.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMFSUtilities.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMOtherIODisk.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMSnapshot.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMVolumeUtilities.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/DMManager+TMExtensions.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/Locks.swift"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/NSURL+TMAdditions.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMLocalSnapshotMessenger.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMXPCListener.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/XPC.swift"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Logging/TMLog.swift"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/BackupCompareInternal.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMMessageSerializer.mm"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMSystemInformation.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMThinningAlgorithm.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/NodeCache/TMNodeCache.mm"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMDeviceRulesEngine.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngine.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngineBuilder.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMBackupProxy.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession+Finder.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMTargetCache.mm"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMMonoStructure.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure+CoreStructures.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructureMetadata.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSBackup.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSMachineStore.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackup.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackupStorage.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMInProgressContainer.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMMachineStore.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMReadOnlyBackup.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMVolumeStore.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMImageDisk.m"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMTestDisk.m"
+ "/dev/r%@"
+ "Attached as %@ to '%@' using mode '%@'"
+ "Backup volume device entry did not appear in IOKit registry in a timely manner!"
+ "Failed to attach to '%@' using mode '%@', error: %@"
+ "Failed to find backup disk device name for '%@'"
+ "Failed to find backup disk raw device name for '%@'"
+ "T{os_unfair_lock_s=I},V_uuidToVolumeStoresLock"
+ "_uuidToVolumeStoresLock"
+ "backupDiskRawDevicePath"
+ "read only"
+ "read/write"
+ "setUuidToVolumeStoresLock:"
+ "uuidToVolumeStoresLock"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMAPFSBackupListener.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMBackupDataSource.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMHFSBackupListener.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Configuration/TMConfiguration.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrList.swift"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrListDisk.swift"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMAPFSDisk.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDADisk.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDisk.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDiskImage.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMFSUtilities.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMOtherIODisk.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMSnapshot.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMVolumeUtilities.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/DMManager+TMExtensions.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/Locks.swift"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/NSURL+TMAdditions.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMLocalSnapshotMessenger.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMXPCListener.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/XPC.swift"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Logging/TMLog.swift"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/BackupCompareInternal.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMMessageSerializer.mm"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMSystemInformation.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMThinningAlgorithm.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/NodeCache/TMNodeCache.mm"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMDeviceRulesEngine.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngine.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngineBuilder.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMBackupProxy.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession+Finder.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMTargetCache.mm"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMMonoStructure.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure+CoreStructures.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructureMetadata.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSBackup.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSMachineStore.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackup.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackupStorage.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMInProgressContainer.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMMachineStore.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMReadOnlyBackup.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMVolumeStore.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMImageDisk.m"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMTestDisk.m"
- "Diskimage '%@' was attached but did not appear in IOKit registry in a timely manner!"
- "Failed to attach using DiskImages2 to url '%@', error: %@"
- "Successfully attached using DiskImages2 as '%@' from URL '%@'"

```

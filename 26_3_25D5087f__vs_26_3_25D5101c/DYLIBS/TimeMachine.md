## TimeMachine

> `/System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine`

```diff

-2520.0.0.0.0
-  __TEXT.__text: 0xbd344
-  __TEXT.__auth_stubs: 0x2750
+2523.0.0.0.0
+  __TEXT.__text: 0xbd3dc
+  __TEXT.__auth_stubs: 0x2760
   __TEXT.__objc_methlist: 0x57e8
   __TEXT.__const: 0x3640
   __TEXT.__gcc_except_tab: 0x1fc4
-  __TEXT.__cstring: 0xc583
+  __TEXT.__cstring: 0xc5c3
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0xb0

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x13c0
+  __AUTH_CONST.__auth_got: 0x13c8
   __AUTH_CONST.__const: 0x5840
-  __AUTH_CONST.__cfstring: 0x85a0
+  __AUTH_CONST.__cfstring: 0x85c0
   __AUTH_CONST.__objc_const: 0x8908
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B8425DBA-8D88-30D0-81B2-4500619313C7
+  UUID: 4ED081F7-15D4-37D0-95A5-AA461A2164A6
   Functions: 3653
-  Symbols:   6041
-  CStrings:  5053
+  Symbols:   6042
+  CStrings:  5055
 
Symbols:
+ _CFPreferencesCopyAppValue
Functions:
~ -[TMConfiguration rawValueForKey:] : 76 -> 148
~ -[TMDisk(NetworkOperations) configureReconnectTimeoutsDisablePrimaryReconnect:disableNetworkQoS:] : 1740 -> 1720
~ +[TMStructure annotatedStateAtURL:] : 696 -> 796
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMAPFSBackupListener.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMBackupDataSource.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMHFSBackupListener.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Configuration/TMConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrList.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrListDisk.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMAPFSDisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDADisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDiskImage.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMFSUtilities.h"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMFSUtilities.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMOtherIODisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMSnapshot.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMStatFSDisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMVolumeUtilities.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/DMManager+TMExtensions.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/Locks.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/NSFileManager+TMAdditions.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/NSURL+TMAdditions.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMLocalSnapshotMessenger.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMXPCListener.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMXPCUtilities.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/XPC.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Logging/TMLog.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/BackupCompareInternal.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/BackupDeletion.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMFirmLinkMap.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMMessageSerializer.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMSystemInformation.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMThinningAlgorithm.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/NodeCache/TMNodeCache.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMDeviceRulesEngine.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngine.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngineBuilder.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMSpotlightOracle.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMSystemPathsOracle.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMBackupProxy.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession+Finder.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMTargetCache.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMMonoStructure.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure+CoreStructures.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructureMetadata.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSBackup.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSMachineStore.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackup.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackupStorage.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMInProgressContainer.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMMachineStore.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMReadOnlyBackup.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMVolumeStore.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMDiskArbiter.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMImageDisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMRAMDisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMSubdirectorySourceDisk.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC5ugB7LHaqLuhDnKTz6f3OaF4P0PIsnCY4z5Y/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMTestDisk.m"
+ "Expected %@ metadata type but found %@ metadata type at URL '%@'"
+ "Preparing to reuse structure at '%@'"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMAPFSBackupListener.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMBackupDataSource.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/BackupDataSource/TMHFSBackupListener.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Configuration/TMConfiguration.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrList.swift"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/AttrListDisk.swift"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMAPFSDisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDADisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMDiskImage.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMFSUtilities.h"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMFSUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMOtherIODisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMSnapshot.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMStatFSDisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/DisksAndFilesystems/TMVolumeUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/DMManager+TMExtensions.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/Locks.swift"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/NSFileManager+TMAdditions.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Extensions/NSURL+TMAdditions.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMLocalSnapshotMessenger.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMXPCListener.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/TMXPCUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/IPC/XPC.swift"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Logging/TMLog.swift"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/BackupCompareInternal.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/BackupDeletion.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMFirmLinkMap.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMMessageSerializer.mm"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMSystemInformation.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Misc/TMThinningAlgorithm.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/NodeCache/TMNodeCache.mm"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMDeviceRulesEngine.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngine.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMRulesEngineBuilder.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMSpotlightOracle.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/RulesEngine/TMSystemPathsOracle.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMBackupProxy.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession+Finder.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMSession.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Session/TMTargetCache.mm"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMMonoStructure.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure+CoreStructures.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructure.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/Structure/TMStructureMetadata.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSBackup.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMAPFSMachineStore.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackup.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMBackupStorage.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMInProgressContainer.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMMachineStore.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMReadOnlyBackup.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/StructureModels/TMVolumeStore.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMDiskArbiter.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMImageDisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMRAMDisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMSubdirectorySourceDisk.m"
- "/AppleInternal/Library/BuildRoots/4~CD2-ugBigd1t7S2XJt2BbzJifUhlZ9ZkPNayrhw/Library/Caches/com.apple.xbs/Sources/backupd/TimeMachine-Framework/TestingSupport/TMTestDisk.m"
- "Preparing to resuse structure at '%@'"

```

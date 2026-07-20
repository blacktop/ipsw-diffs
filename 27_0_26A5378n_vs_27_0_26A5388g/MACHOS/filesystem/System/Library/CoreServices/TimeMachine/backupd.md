## backupd

> `/System/Library/CoreServices/TimeMachine/backupd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-2608.2.0.0.0
-  __TEXT.__text: 0x14d110
+2609.3.0.0.0
+  __TEXT.__text: 0x14d650
   __TEXT.__auth_stubs: 0x3fd0
-  __TEXT.__objc_stubs: 0x8740
-  __TEXT.__objc_methlist: 0x2fd8
+  __TEXT.__objc_stubs: 0x8780
+  __TEXT.__objc_methlist: 0x2ff0
   __TEXT.__const: 0x8770
-  __TEXT.__gcc_except_tab: 0xc44
-  __TEXT.__cstring: 0x116ba
-  __TEXT.__objc_methname: 0xac09
+  __TEXT.__gcc_except_tab: 0xc38
+  __TEXT.__cstring: 0x1173a
+  __TEXT.__objc_methname: 0xac59
   __TEXT.__objc_classname: 0x101c
   __TEXT.__objc_methtype: 0x2ab1
   __TEXT.__swift5_typeref: 0x3621

   __TEXT.__unwind_info: 0x4900
   __TEXT.__eh_frame: 0xa028
   __DATA_CONST.__const: 0x8740
-  __DATA_CONST.__cfstring: 0x5340
+  __DATA_CONST.__cfstring: 0x5360
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2b0

   __DATA_CONST.__got: 0xeb8
   __DATA_CONST.__auth_ptr: 0xa70
   __DATA.__objc_const: 0x7918
-  __DATA.__objc_selrefs: 0x2648
+  __DATA.__objc_selrefs: 0x2658
   __DATA.__objc_ivar: 0x2bc
   __DATA.__objc_data: 0x28d8
   __DATA.__data: 0x4c00

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5198
+  Functions: 5201
   Symbols:   1716
-  CStrings:  3616
+  CStrings:  3619
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/TimeMachinePrivate-Framework/Configuration/BackupDestination+Resolution.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/TimeMachinePrivate-Framework/FSTestToolsExtras/ParallelEnumerator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/TimeMachinePrivate-Framework/IPC/BackupDaemonMessenger.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/TimeMachinePrivate-Framework/IPC/TMHelperAgentProxy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Backup Engine/BackupEngine.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Backup Engine/BackupPhaseReporter.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Backup Engine/LocalSnapshotManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/BackupDaemon.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Checkpointing/APFSCheckpoint.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Checkpointing/BaseCheckpoint.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Checkpointing/HFSCheckpoint.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/BackupCopierTypes.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/BackupCopierTypes.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/BootableBackup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/CopyEstimate.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/CopyObservers.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/CopyProgress.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/DeviceUnlockedAssertion.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/ErrorRemapper.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/ProgressViewpoints.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/ScreenLockMonitor.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Copying/SpotlightInhibitor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/AsyncFSEventStream.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/AttemptMapper.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/EventCollection.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/EventDatabase.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/EventPipes.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/EventProgressObserver.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/EventStrategy.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Event Collection/TMSnapshotDiffer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Health Check/TMDiskImage+BackupExtensions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Health Check/TMDiskImage+HealthCheck.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/IPC/BackupClientManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/IPC/MessagePortIPCDispatcher.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/IPC/RawXPCDispatcher.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Job Management/BackupJob.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Job Management/DestinationChooser.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Job Management/JobDispatcher.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Logging and Analytics/Analytics.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Logging and Analytics/DestinationIOChecker.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Mounting/BackupDestination+Mounting.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Mounting/LightlyHeldVolumes.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Mounting/MountedDestination.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Mounting/MountedDestinationManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Sizing/DeferredSizingQueue.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Sizing/PropagationLookAheadScanner.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Thinning/TMConcurrentDeleter.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Controllers/Thinning/ThinningManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMAPFSMachineStore+BackupAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMBackup+BackupAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMBackupStorage+BackupAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMInProgressContainer+BackupAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMMachineStore+BackupAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMVolumeStore+BackupAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Backup Structure Tree/TMWorkingSet.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Clone Tracking/CloneFamilyAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Clone Tracking/CloneInfo.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Clone Tracking/RangeMapAlgorithm.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Destinations/BackupDestination+ConsistencyScanRequirements.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Destinations/BackupDestination+Inheritance.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Destinations/OptimizedMove.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Destinations/SpotlightIndexer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Inclusions and Exclusions/ExclusionsCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Inclusions and Exclusions/InclusionArbiter.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Sources/BackupSource+Lookup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Sources/BackupSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Volumes/BackupVolume.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CI4J5L/Sources/backupd/backupd/Models/Volumes/VolumeInfo2.swift"
+ "Disk %@ does not have an expected snapshot for timestamp %@ (it may have been deleted or reaped by concurrent thinning/purging)"
+ "createLocalSnapshotsForDisks:withSnapshotDate:error:"
+ "generateLocalSnapshotDate"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/TimeMachinePrivate-Framework/Configuration/BackupDestination+Resolution.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/TimeMachinePrivate-Framework/FSTestToolsExtras/ParallelEnumerator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/TimeMachinePrivate-Framework/IPC/BackupDaemonMessenger.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/TimeMachinePrivate-Framework/IPC/TMHelperAgentProxy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Backup Engine/BackupEngine.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Backup Engine/BackupPhaseReporter.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Backup Engine/LocalSnapshotManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/BackupDaemon.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Checkpointing/APFSCheckpoint.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Checkpointing/BaseCheckpoint.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Checkpointing/HFSCheckpoint.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/BackupCopierTypes.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/BackupCopierTypes.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/BootableBackup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/CopyEstimate.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/CopyObservers.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/CopyProgress.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/DeviceUnlockedAssertion.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/ErrorRemapper.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/ProgressViewpoints.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/ScreenLockMonitor.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Copying/SpotlightInhibitor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/AsyncFSEventStream.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/AttemptMapper.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/EventCollection.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/EventDatabase.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/EventPipes.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/EventProgressObserver.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/EventStrategy.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Event Collection/TMSnapshotDiffer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Health Check/TMDiskImage+BackupExtensions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Health Check/TMDiskImage+HealthCheck.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/IPC/BackupClientManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/IPC/MessagePortIPCDispatcher.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/IPC/RawXPCDispatcher.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Job Management/BackupJob.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Job Management/DestinationChooser.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Job Management/JobDispatcher.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Logging and Analytics/Analytics.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Logging and Analytics/DestinationIOChecker.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Mounting/BackupDestination+Mounting.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Mounting/LightlyHeldVolumes.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Mounting/MountedDestination.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Mounting/MountedDestinationManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Sizing/DeferredSizingQueue.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Sizing/PropagationLookAheadScanner.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Thinning/TMConcurrentDeleter.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Controllers/Thinning/ThinningManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMAPFSMachineStore+BackupAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMBackup+BackupAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMBackupStorage+BackupAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMInProgressContainer+BackupAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMMachineStore+BackupAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMVolumeStore+BackupAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Backup Structure Tree/TMWorkingSet.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Clone Tracking/CloneFamilyAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Clone Tracking/CloneInfo.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Clone Tracking/RangeMapAlgorithm.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Destinations/BackupDestination+ConsistencyScanRequirements.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Destinations/BackupDestination+Inheritance.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Destinations/OptimizedMove.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Destinations/SpotlightIndexer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Inclusions and Exclusions/ExclusionsCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Inclusions and Exclusions/InclusionArbiter.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Sources/BackupSource+Lookup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Sources/BackupSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Volumes/BackupVolume.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KIx4rG/Sources/backupd/backupd/Models/Volumes/VolumeInfo2.swift"
```

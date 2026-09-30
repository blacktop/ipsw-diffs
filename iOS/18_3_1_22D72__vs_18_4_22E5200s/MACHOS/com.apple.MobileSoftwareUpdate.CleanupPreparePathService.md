## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x34404
-  __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_stubs: 0x3e80
-  __TEXT.__objc_methlist: 0x1980
-  __TEXT.__cstring: 0x11091
-  __TEXT.__const: 0x1358
-  __TEXT.__oslogstring: 0x13c8
-  __TEXT.__gcc_except_tab: 0x4a8
-  __TEXT.__objc_classname: 0x219
-  __TEXT.__objc_methname: 0x420e
-  __TEXT.__objc_methtype: 0xe54
-  __TEXT.__unwind_info: 0xa38
-  __DATA_CONST.__auth_got: 0xc38
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1888
-  __DATA_CONST.__cfstring: 0xa600
-  __DATA_CONST.__objc_classlist: 0xd8
+2171.100.125.0.3
+  __TEXT.__text: 0x29088
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_stubs: 0x3740
+  __TEXT.__objc_methlist: 0x165c
+  __TEXT.__cstring: 0x106bd
+  __TEXT.__const: 0x1220
+  __TEXT.__oslogstring: 0x1c6
+  __TEXT.__gcc_except_tab: 0x474
+  __TEXT.__objc_classname: 0x1c7
+  __TEXT.__objc_methname: 0x3a33
+  __TEXT.__objc_methtype: 0xdef
+  __TEXT.__unwind_info: 0x8f8
+  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x1460
+  __DATA_CONST.__cfstring: 0x9ea0
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x25e8
-  __DATA.__objc_selrefs: 0x12f0
-  __DATA.__objc_ivar: 0x160
-  __DATA.__objc_data: 0x870
-  __DATA.__data: 0x588
-  __DATA.__bss: 0x6b8
+  __DATA.__objc_const: 0x1f50
+  __DATA.__objc_selrefs: 0x10d8
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_data: 0x6e0
+  __DATA.__data: 0x4d8
+  __DATA.__bss: 0x670
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 857
-  Symbols:   6396
-  CStrings:  3177
+  - /usr/lib/libpartition2_dynamic.dylib
+  Functions: 779
+  Symbols:   5714
+  CStrings:  2852
 
Symbols:
+ +[MSUFreeSpaceManager sharedInstance].cold.1
+ +[UMEventRecorder submitQueue].cold.1
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.1
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.2
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.3
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.4
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.5
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.6
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.7
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.8
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.9
+ -[UMEventRecorder _currentEAPFSMode].cold.1
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ AMRestorePartitionFWCopyTagData.cold.1
+ AMRestorePartitionFWCopyTagData.cold.10
+ AMRestorePartitionFWCopyTagData.cold.2
+ AMRestorePartitionFWCopyTagData.cold.3
+ AMRestorePartitionFWCopyTagData.cold.4
+ AMRestorePartitionFWCopyTagData.cold.5
+ AMRestorePartitionFWCopyTagData.cold.6
+ AMRestorePartitionFWCopyTagData.cold.7
+ AMRestorePartitionFWCopyTagData.cold.8
+ AMRestorePartitionFWCopyTagData.cold.9
+ CleanupPreparePathService_event_handler.cold.1
+ _AMRestorePartitionOpenFileWithURL.cold.1
+ _AMRestorePartitionOpenFileWithURL.cold.2
+ _MSUPreferencesCopyValueForDomain.cold.1
+ _objc_release_x25
+ booted_from_recoveryos.cold.1
+ logfunctionv.cold.1
+ msuSharedLogger.cold.1
+ ramrod_probe_media_internal.cold.1
+ ramrod_probe_media_internal.cold.2
+ wait_for_device.cold.1
+ wait_for_device.cold.2
+ wait_for_device.cold.3
+ wait_for_device.cold.4
- +[LPAPFSContainer allAPFSContainers]
- +[LPAPFSContainer diagsContainer]
- +[LPAPFSContainer supportedContentTypes]
- +[LPAPFSPhysicalStore supportedContentTypes]
- +[LPAPFSVolume _loadMountPointTableForMode:]
- +[LPAPFSVolume defaultMountPointGivenRole:]
- +[LPAPFSVolume defaultVolumeNameGivenRole:]
- +[LPAPFSVolume initialize]
- +[LPAPFSVolume supportedContentTypes]
- +[LPMedia _copyIOMediaForDiskWithPath:]
- +[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot]
- +[LPMedia allMedia]
- +[LPMedia hasEmbeddedDeviceTypeRoot]
- +[LPMedia liveMediaForSnapshotAtPath:]
- +[LPMedia mediaForBSDNameOrDeviceNode:]
- +[LPMedia mediaForPath:]
- +[LPMedia mediaForPath:isSnapshot:]
- +[LPMedia mediaForPath:snapshotName:]
- +[LPMedia mediaForUUID:]
- +[LPMedia snapshotNameForMediaForPath:]
- +[LPMedia supportedContentTypes]
- +[LPMedia(Private) contentTypeToSubclassMap]
- +[LPMedia(Private) mediaOfCorrectTypeGivenIOMedia:]
- +[LPMedia(Private) waitForBlockStorage]
- +[LPMedia(Private) waitForIOMediaWithDevNode:]
- +[LPPartitionMedia contentTypesForPartitionMedia]
- +[LPPartitionMedia primaryMedia]
- +[LPPartitionMedia supportedContentTypes]
- -[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]
- -[LPAPFSContainer physicalStores]
- -[LPAPFSContainer prebootVolume]
- -[LPAPFSContainer recoveryVolume]
- -[LPAPFSContainer updateVolume]
- -[LPAPFSContainer volumesWithRole:]
- -[LPAPFSContainer volumes]
- -[LPAPFSPhysicalStore container]
- -[LPAPFSPhysicalStore parent]
- -[LPAPFSPhysicalStore role]
- -[LPAPFSVolume _createTemporaryMountPointWithError:]
- -[LPAPFSVolume container]
- -[LPAPFSVolume createSnapshot:error:]
- -[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:]
- -[LPAPFSVolume deleteVolumeWithError:]
- -[LPAPFSVolume eraseVolumeWithError:]
- -[LPAPFSVolume isCaseSenstive]
- -[LPAPFSVolume isEncrypted]
- -[LPAPFSVolume isFilevaultEncrypted]
- -[LPAPFSVolume isMounted]
- -[LPAPFSVolume mountAtPath:error:]
- -[LPAPFSVolume mountAtPath:options:error:]
- -[LPAPFSVolume mountAtTemporaryPathWithError:]
- -[LPAPFSVolume mountAtTemporaryPathWithOptions:error:]
- -[LPAPFSVolume mountWithError:]
- -[LPAPFSVolume pairedVolume]
- -[LPAPFSVolume renameSnapshot:to:error:]
- -[LPAPFSVolume revertToSnapshot:error:]
- -[LPAPFSVolume revertToSnapshot:options:error:]
- -[LPAPFSVolume role]
- -[LPAPFSVolume rootToSnapshot:error:]
- -[LPAPFSVolume setRole:withError:]
- -[LPAPFSVolume snapshotInfoWithError:]
- -[LPAPFSVolume snapshotMountPoints]
- -[LPAPFSVolume snapshotsWithError:]
- -[LPAPFSVolume unmountAllWithError:]
- -[LPAPFSVolume unmountWithError:]
- -[LPAPFSVolume unmountWithOptions:error:]
- -[LPAPFSVolume volumeGroupUUID]
- -[LPMedia BSDName]
- -[LPMedia _deviceCharacteristicStringForKey:]
- -[LPMedia content]
- -[LPMedia dealloc]
- -[LPMedia description]
- -[LPMedia devNodePath]
- -[LPMedia deviceModel]
- -[LPMedia initWithIOMediaObject:]
- -[LPMedia ioMedia]
- -[LPMedia isEmbeddedDeviceTypeRoot]
- -[LPMedia isEqual:]
- -[LPMedia isInternal]
- -[LPMedia isJournaled]
- -[LPMedia isPrimaryMedia]
- -[LPMedia isReadOnly]
- -[LPMedia isWhole]
- -[LPMedia mediaUUID]
- -[LPMedia mountPoint]
- -[LPMedia name]
- -[LPMedia setIoMedia:]
- -[LPMedia setName:withError:]
- -[LPMedia storageMedium]
- -[LPMedia vendorName]
- -[LPMedia wholeMediaForMedia]
- -[LPMedia(Private) getBoolPropertyWithName:]
- -[LPMedia(Private) getPropertyWithName:]
- -[LPMedia(Private) getStringPropertyWithName:]
- -[LPPartitionMedia children]
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
- /Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/libpartition2/
- LPAPFSContainer.m
- LPAPFSContainer_Private.m
- LPAPFSPhyscialStore_Private.m
- LPAPFSPhysicalStore.m
- LPAPFSVolume.m
- LPAPFSVolume_Private.m
- LPIOKitHelper.m
- LPLog.m
- LPMedia.m
- LPPartitionMedia.m
- OBJC_IVAR_$_LPMedia._ioMedia
- _APFSVolumeCreate
- _APFSVolumeCreateForMSU
- _APFSVolumeGetVEKState
- _APFSVolumeRole
- _IOIteratorReset
- _IOObjectIsEqualTo
- _IORegistryEntryGetParentEntry
- _IORegistryIteratorExitEntry
- _IOServiceGetMatchingServices
- _LPAPFSContainerMediaTypeUUID
- _LPAPFSPhysicalStoreDiagsMediaUUID
- _LPAPFSPhysicalStoreMediaUUID
- _LPAPFSPhysicalStoreRecoveryMediaUUID
- _LPAPFSSnapshotPropertyKeyMarkedForRevert
- _LPAPFSSnapshotPropertyKeyMarkedForRoot
- _LPAPFSSnapshotPropertyKeyName
- _LPAPFSSnapshotPropertyKeyXID
- _LPAPFSVolumeMediaTypeUUID
- _LPAPFSVolumeMountOptionNoBrowse
- _LPAPFSVolumeMountOptionNoFirmlinks
- _LPAPFSVolumeMountOptionReadOnly
- _LPAPFSVolumeMountOptionSnapshotName
- _LPAPFSVolumeRevertOptionSkipRemount
- _LPAPFSVolumeSnapshotMountPointKeyMountPoint
- _LPAPFSVolumeSnapshotMountPointKeyName
- _LPAPFSVolumeUnmountOptionAll
- _LPAPFSVolumeUnmountOptionDoNotLock
- _LPAPFSVolumeUnmountOptionForce
- _LPAPFSVolumeUnmountOptionSnapshotName
- _LPLogObject.obj
- _LPLogObject.onceToken
- _NSFilePathErrorKey
- _NSLocalizedFailureReasonErrorKey
- _NSOSStatusErrorDomain
- _OBJC_CLASS_$_LPAPFSContainer
- _OBJC_CLASS_$_LPAPFSPhysicalStore
- _OBJC_CLASS_$_LPAPFSVolume
- _OBJC_CLASS_$_LPMedia
- _OBJC_CLASS_$_LPPartitionMedia
- _OBJC_METACLASS_$_LPAPFSContainer
- _OBJC_METACLASS_$_LPAPFSPhysicalStore
- _OBJC_METACLASS_$_LPAPFSVolume
- _OBJC_METACLASS_$_LPMedia
- _OBJC_METACLASS_$_LPPartitionMedia
- __26-[LPAPFSContainer volumes]_block_invoke.20
- __28-[LPPartitionMedia children]_block_invoke.13
- __LPLogObject
- __LPLogPack
- __OBJC_$_CLASS_METHODS_LPAPFSContainer
- __OBJC_$_CLASS_METHODS_LPAPFSPhysicalStore
- __OBJC_$_CLASS_METHODS_LPAPFSVolume
- __OBJC_$_CLASS_METHODS_LPMedia(Private)
- __OBJC_$_CLASS_METHODS_LPPartitionMedia
- __OBJC_$_INSTANCE_METHODS_LPAPFSContainer
- __OBJC_$_INSTANCE_METHODS_LPAPFSPhysicalStore
- __OBJC_$_INSTANCE_METHODS_LPAPFSVolume
- __OBJC_$_INSTANCE_METHODS_LPMedia(Private)
- __OBJC_$_INSTANCE_METHODS_LPPartitionMedia
- __OBJC_$_INSTANCE_VARIABLES_LPMedia
- __OBJC_$_PROP_LIST_LPMedia
- __OBJC_CLASS_RO_$_LPAPFSContainer
- __OBJC_CLASS_RO_$_LPAPFSPhysicalStore
- __OBJC_CLASS_RO_$_LPAPFSVolume
- __OBJC_CLASS_RO_$_LPMedia
- __OBJC_CLASS_RO_$_LPPartitionMedia
- __OBJC_METACLASS_RO_$_LPAPFSContainer
- __OBJC_METACLASS_RO_$_LPAPFSPhysicalStore
- __OBJC_METACLASS_RO_$_LPAPFSVolume
- __OBJC_METACLASS_RO_$_LPMedia
- __OBJC_METACLASS_RO_$_LPPartitionMedia
- ___26-[LPAPFSContainer volumes]_block_invoke
- ___28-[LPPartitionMedia children]_block_invoke
- ___39+[LPMedia snapshotNameForMediaForPath:]_block_invoke
- ___41-[LPAPFSVolume unmountWithOptions:error:]_block_invoke
- ___44+[LPMedia(Private) contentTypeToSubclassMap]_block_invoke
- ____LPLogObject_block_invoke
- ____is_running_in_ramdisk_block_invoke
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___block_descriptor_40_e8_32s_e5_v8?0l
- ___block_descriptor_44_e8_32r_e8_v12?0I8l
- ___block_descriptor_44_e8_32s_e8_v12?0I8l
- ___chkstk_darwin
- ___copy_helper_block_e8_32s
- ___destroy_helper_block_e8_32s
- __block_literal_global.164
- __block_literal_global.186
- __execForLibpartition
- __lp2_delete_directory_contents
- __lp2_delete_directory_contents_confirm
- __lp2_delete_directory_contents_error
- __os_log_pack_fill
- __os_log_pack_size
- _dprintf
- _execlogfunction
- _fcopyfile
- _fs_snapshot_create
- _fs_snapshot_rename
- _fs_snapshot_root
- _is_running_in_ramdisk.is_ramdisk
- _is_running_in_ramdisk.onceToken
- _iterateSafely
- _kAPFSVolumeCaseSensitiveKey
- _kAPFSVolumeFSIndexKey
- _kAPFSVolumeGroupSiblingFSIndexKey
- _kAPFSVolumeNameKey
- _kAPFSVolumeNoAutomountAtCreateKey
- _kAPFSVolumeQuotaSizeKey
- _kAPFSVolumeReserveSizeKey
- _kAPFSVolumeRoleKey
- _kLPDefaultLiveOSMountPointTable
- _kLPDefaultMountPointTable
- _kLPDefaultRAMDiskMountPointTable
- _mkstempsat_np
- _objc_autoreleaseReturnValue
- _objc_msgSend$BSDName
- _objc_msgSend$_copyIOMediaForDiskWithPath:
- _objc_msgSend$_copyLiveFilesystemIOMediaForRootedSnapshot
- _objc_msgSend$_createTemporaryMountPointWithError:
- _objc_msgSend$_deviceCharacteristicStringForKey:
- _objc_msgSend$_loadMountPointTableForMode:
- _objc_msgSend$allMedia
- _objc_msgSend$children
- _objc_msgSend$compare:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$container
- _objc_msgSend$content
- _objc_msgSend$contentTypeToSubclassMap
- _objc_msgSend$contentTypesForPartitionMedia
- _objc_msgSend$defaultMountPointGivenRole:
- _objc_msgSend$devNodePath
- _objc_msgSend$getBoolPropertyWithName:
- _objc_msgSend$getCString:maxLength:encoding:
- _objc_msgSend$getPropertyWithName:
- _objc_msgSend$getStringPropertyWithName:
- _objc_msgSend$initWithIOMediaObject:
- _objc_msgSend$ioMedia
- _objc_msgSend$isEmbeddedDeviceTypeRoot
- _objc_msgSend$isPrimaryMedia
- _objc_msgSend$isWhole
- _objc_msgSend$lastObject
- _objc_msgSend$liveMediaForSnapshotAtPath:
- _objc_msgSend$mediaForBSDNameOrDeviceNode:
- _objc_msgSend$mediaForPath:
- _objc_msgSend$mediaForPath:snapshotName:
- _objc_msgSend$mediaOfCorrectTypeGivenIOMedia:
- _objc_msgSend$mediaUUID
- _objc_msgSend$mountAtPath:error:
- _objc_msgSend$mountAtPath:options:error:
- _objc_msgSend$mountAtTemporaryPathWithError:
- _objc_msgSend$mountAtTemporaryPathWithOptions:error:
- _objc_msgSend$mountPoint
- _objc_msgSend$name
- _objc_msgSend$numberWithUnsignedShort:
- _objc_msgSend$primaryMedia
- _objc_msgSend$rangeOfString:options:
- _objc_msgSend$revertToSnapshot:options:error:
- _objc_msgSend$role
- _objc_msgSend$setIoMedia:
- _objc_msgSend$snapshotInfoWithError:
- _objc_msgSend$snapshotMountPoints
- _objc_msgSend$sortUsingComparator:
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$substringToIndex:
- _objc_msgSend$supportedContentTypes
- _objc_msgSend$unmountWithError:
- _objc_msgSend$unmountWithOptions:error:
- _objc_msgSend$volumeGroupUUID
- _objc_msgSend$volumes
- _objc_msgSend$volumesWithRole:
- _objc_msgSend$waitForBlockStorage
- _objc_msgSend$waitForIOMediaWithDevNode:
- _objc_release_x26
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _os_log_pack_compose
- _os_log_pack_send
- _posix_spawn_file_actions_addclose
- _removefile_state_alloc
- _removefile_state_free
- _removefile_state_set
- _sConsoleFD
- _sLegacyVolumeNameMapping
- _sLogLevel
- _sLogToConsole
- _sLogToOSLog
- _sLogToStandardOut
- _sMountPointLookupTable
- _sRoleEncodingMapping
- _sRoleLookupTable
- _unlinkat
- _uuid_is_null
- _uuid_parse
- contentTypeToSubclassMap.once
- contentTypeToSubclassMap.sharedMap
CStrings:
+ "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
+ "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
- "%@: %@"
- "%@: %@, Mount: %@"
- "%@: %@, UUID: %@"
- "%@s%d"
- "%s : APFSVolumeCreateForMSU exists and we're creating a System volume. Preferring it to APFSVolumeCreate."
- "%s : Add volume failed with error: %d."
- "%s : Can not iterate over physical store services."
- "%s : Container is missing UUID?"
- "%s : Container is somehow missing a BSD name."
- "%s : Container isn't a container?!"
- "%s : Could not open device is not mounted."
- "%s : Could not open device mount %{private}@."
- "%s : Could not set root from snapshot. Errno: %d"
- "%s : Creating APFS volume %s with options: %@"
- "%s : Failed because target volume is not mounted"
- "%s : Failed to delete snapshot: %{private}@, %d"
- "%s : Failed to encode snapshot name %{private}s for some reason."
- "%s : Failed to get content type."
- "%s : Failed to open media for snapshot delete: %d"
- "%s : IOIterator was still invalid after attempting %d times"
- "%s : Need a valid new snapshot name."
- "%s : Need a valid snapshot name."
- "%s : Need a valid snapshot names."
- "%s : Paired volume is not valid if role is not system."
- "%s : Paired volume must be in the same container"
- "%s : Requested system volume with sibling but the key is not supported."
- "%s : Unable to get parent iterator"
- "%s : Unable to get the iterator for entry."
- "%s : Unable to open mount point %{private}@: %d"
- "%s : Volume name is invalid"
- "%s : Waiting for snapshots to delete timed out"
- "%s : You need to specify a volume name."
- "%s : failed to read value for property named: %@"
- "%s : failed with iokit error: %d"
- "%s : failed with posix error: %d"
- "%s : failed with unknown kern_return_t error: %d"
- "%s : going to delete apfs volume ( %@ )"
- "%s : volume is missing a dev node somehow"
- "%s called but %{private}@ is not mounted."
- "%s called on device with no dev node"
- "%s was stopped by signal %d"
- "%s was terminated by signal %d"
- "%s: %@ isn't an APFS volume"
- "%s: Error getting snapshot info for %@: %@"
- "%s: Failed to find primary media"
- "%s: Failed to get IOMedia objects"
- "%s: Failed to obtain parent IOMedia for disk at path %{private}@"
- "%s: Failed to remount volume with error: %d"
- "%s: Failed to set name for volume: %s\n"
- "%s: Failed to unmount volume with error: %d"
- "%s: Mount point is %{private}@\n"
- "%s: No disk for %{private}@"
- "%s: No media found for path: %{private}@"
- "%s: No snapshot is tagged for boot and none match the naming scheme"
- "%s: Not on a rooted snapshot disk, will return self: %{private}@"
- "%s: Parent of disk backing %{private}@ is not an APFS volume"
- "%s: Skipping unmount/remount of %@"
- "%s: Successfully set volume name to %{private}@\n"
- "%s: Trying to determine mount point\n"
- "%s: Volume is not mounted. Unable to set name\n"
- "%s: could not look up snapshot by UUID: %d (%s)"
- "%s: could not parse %s %{private}s: %{private}@"
- "%s: failed to get journaled status for %@\n"
- "%s: failed to get read-only status for %@\n"
- "%s: failed to get role. Error: %d"
- "%s: no IOMedia for %@ (device 0x%lx)"
- "%s: no filesystem for %@ (%d): %s"
- "%s: path is a snapshot, but has no name: %{private}@"
- "%s: statfs failed: %d (%s)"
- "+[LPAPFSContainer diagsContainer]"
- "+[LPMedia _copyIOMediaForDiskWithPath:]"
- "+[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot]"
- "+[LPMedia allMedia]"
- "+[LPMedia liveMediaForSnapshotAtPath:]"
- "+[LPMedia mediaForPath:snapshotName:]"
- "+[LPMedia snapshotNameForMediaForPath:]"
- "-[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]"
- "-[LPAPFSContainer physicalStores]"
- "-[LPAPFSPhysicalStore container]"
- "-[LPAPFSPhysicalStore parent]"
- "-[LPAPFSPhysicalStore role]"
- "-[LPAPFSVolume createSnapshot:error:]"
- "-[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:]"
- "-[LPAPFSVolume deleteVolumeWithError:]"
- "-[LPAPFSVolume eraseVolumeWithError:]"
- "-[LPAPFSVolume renameSnapshot:to:error:]"
- "-[LPAPFSVolume revertToSnapshot:options:error:]"
- "-[LPAPFSVolume role]"
- "-[LPAPFSVolume rootToSnapshot:error:]"
- "-[LPAPFSVolume snapshotInfoWithError:]"
- "-[LPAPFSVolume snapshotMountPoints]"
- "-[LPMedia isJournaled]"
- "-[LPMedia isReadOnly]"
- "-[LPMedia setName:withError:]"
- "-[LPMedia wholeMediaForMedia]"
- "-[LPMedia(Private) getPropertyWithName:]"
- "-n"
- "-restore"
- ".XXXXXXXX"
- "/System/Volumes/Update"
- "/dev/%@"
- "/mnt1"
- "/mnt10"
- "/mnt11"
- "/mnt2"
- "/mnt3"
- "/mnt4"
- "/mnt5/tmp-mount-XXXXXX"
- "/mnt6"
- "/mnt7"
- "/mnt8"
- "/private/var/"
- "/private/var/hardware"
- "/private/var/internal"
- "/private/var/recovery/"
- "/private/var/vm"
- "/private/var/wireless/baseband_data"
- "/private/xarts"
- "/tmp//tmp-mount-XXXXXX"
- "@"
- "@%@"
- "@20@0:8i16"
- "@24@0:8^@16"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@64@0:8@16i24B28q32q40@48^@56"
- "AppleAPFSMedia"
- "AppleAPFSVolume"
- "Apple_partition_scheme"
- "B28@0:8i16^@20"
- "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=i^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}^vCC^v^{__CFDictionary}C}24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16d24^@32"
- "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=i^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}^vCC^v^{__CFDictionary}C}24^@32"
- "BSD Major"
- "BSD Minor"
- "BSDName"
- "Call to APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ returned EEXIST\n"
- "Can not mount (%@) because mount returned %d."
- "Can not mount (%s) because it does not appear to have a device node."
- "Can not mount (%{private}s) because we could not create its mount folder (%{private}s)."
- "CaseSensitive"
- "Content"
- "Could not removefile(3) path %{private}s: %s"
- "Could not reset metadata on %{private}s: %s"
- "Couldn't create a temporary mount point %s"
- "Deleting contents of %{private}s %s (result: %d)."
- "Deleting contents of %{private}s..."
- "Device Characteristics"
- "Error: More than one preboot volume found: %{private}@"
- "Error: More than one recovery volume found: %{private}@"
- "Error: More than one update volume found: %{private}@"
- "FDisk_partition_scheme"
- "Failed to call APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ with errno %d\n"
- "Failed to create container volumes iterator"
- "Failed to create partition media iterator."
- "Failed to find media for %@"
- "Failed to unmount %@ **FORCING UNMOUNT** error: %d"
- "Failed to unmount %@ retry: %s error: %d"
- "FireWire Vendor Name"
- "GUID_partition_scheme"
- "I24@0:8@16"
- "IOBlockStorageDevice"
- "IOKit service wait timed out, volumes may be stale."
- "IOKit wait timed out, volume for media may be stale."
- "Internal"
- "LPAPFSContainer"
- "LPAPFSPhysicalStore"
- "LPAPFSSnapshotPropertyKeyMarkedForRevert"
- "LPAPFSSnapshotPropertyKeyMarkedForRoot"
- "LPAPFSSnapshotPropertyKeyName"
- "LPAPFSSnapshotPropertyKeyXID"
- "LPAPFSVolume"
- "LPAPFSVolumeMountOptionNoBrowse"
- "LPAPFSVolumeMountOptionNoFirmlinks"
- "LPAPFSVolumeMountOptionReadOnly"
- "LPAPFSVolumeMountOptionSnapshotName"
- "LPAPFSVolumeRevertOptionSkipRemount"
- "LPAPFSVolumeSnapshotMountPointKeyMountPoint"
- "LPAPFSVolumeSnapshotMountPointKeyName"
- "LPAPFSVolumeUnmountOptionAll"
- "LPAPFSVolumeUnmountOptionDoNotLock"
- "LPAPFSVolumeUnmountOptionForce"
- "LPAPFSVolumeUnmountOptionSnapshotName"
- "LPMedia"
- "LPPartitionMedia"
- "Medium Type"
- "Model"
- "Model Number"
- "Mount failed"
- "Mounted %@ at %{private}@"
- "Mounted %@, Snapshot( %{private}@ ) at %{private}@"
- "Physical Interconnect Location"
- "Private"
- "Protocol Characteristics"
- "Rotational"
- "Solid State"
- "T@\"NSArray\",R"
- "T@\"NSDictionary\",R"
- "TI,V_ioMedia"
- "Timed out waiting for: %@"
- "Unmount failed with EINVAL, will assume race. Ignoring error."
- "Unmounted %@ ( %{private}@ )"
- "Vendor Name"
- "VolGroupUUID"
- "Volume is already mounted at %@, attempting to re-mount at %@"
- "Volume is already mounted at %@, skipping re-mount"
- "Was asked asked to unmount (%@) but is not mounted."
- "_Bool iterateSafely(io_iterator_t, int, void (^__strong)(io_object_t), void (^__strong)(void))"
- "_copyIOMediaForDiskWithPath:"
- "_copyLiveFilesystemIOMediaForRootedSnapshot"
- "_createTemporaryMountPointWithError:"
- "_deviceCharacteristicStringForKey:"
- "_ioMedia"
- "_loadMountPointTableForMode:"
- "addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:"
- "allAPFSContainers"
- "allMedia"
- "children"
- "com.apple.IOKit"
- "compare:"
- "componentsSeparatedByString:"
- "container"
- "content"
- "contentTypeToSubclassMap"
- "contentTypesForPartitionMedia"
- "create snapshot operation failed: %d %s"
- "createSnapshot:error:"
- "defaultMountPointGivenRole:"
- "defaultVolumeNameGivenRole:"
- "deleteSnapshots:waitForDeletionFor:error:"
- "deleteVolumeWithError:"
- "devNodePath"
- "diagsContainer"
- "eraseVolumeWithError:"
- "failed"
- "getBoolPropertyWithName:"
- "getCString:maxLength:encoding:"
- "getPropertyWithName:"
- "getStringPropertyWithName:"
- "hasEmbeddedDeviceTypeRoot"
- "initWithIOMediaObject:"
- "initialize"
- "ioMedia"
- "isCaseSenstive"
- "isEmbeddedDeviceTypeRoot"
- "isEncrypted"
- "isFilevaultEncrypted"
- "isInternal"
- "isJournaled"
- "isMounted"
- "isPrimaryMedia"
- "isReadOnly"
- "isWhole"
- "lastObject"
- "libpartition2"
- "liveMediaForSnapshotAtPath:"
- "mediaForBSDNameOrDeviceNode:"
- "mediaForPath:"
- "mediaForPath:isSnapshot:"
- "mediaForPath:snapshotName:"
- "mediaForUUID:"
- "mediaOfCorrectTypeGivenIOMedia:"
- "mediaUUID"
- "mountAtPath:error:"
- "mountAtPath:options:error:"
- "mountAtTemporaryPathWithError:"
- "mountAtTemporaryPathWithOptions:error:"
- "mountPoint"
- "mountWithError:"
- "mount_apfs %@ returned %d, retrying (%d)"
- "mount_apfs returned : %d"
- "no"
- "numberWithUnsignedShort:"
- "pairedVolume"
- "parent"
- "physicalStores"
- "pipe failed while preparing to execute %s: %s"
- "posix_spawn %s failed: %s"
- "prebootVolume"
- "primaryMedia"
- "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
- "q24@?0@8@16"
- "rangeOfString:options:"
- "recoveryVolume"
- "rename snapshot operation failed: %d %s"
- "renameSnapshot:to:error:"
- "revertToSnapshot:error:"
- "revertToSnapshot:options:error:"
- "role"
- "rootToSnapshot:error:"
- "s"
- "setIoMedia:"
- "setName:withError:"
- "setRole:withError:"
- "snapshotInfoWithError:"
- "snapshotMountPoints"
- "snapshotNameForMediaForPath:"
- "snapshotsWithError:"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "storageMedium"
- "substringFromIndex:"
- "substringToIndex:"
- "succeeded"
- "supportedContentTypes"
- "unmountAllWithError:"
- "unmountWithError:"
- "unmountWithOptions:error:"
- "updateVolume"
- "v12@?0I8"
- "vendorName"
- "volumeGroupUUID"
- "volumes"
- "volumesWithRole:"
- "waitForBlockStorage"
- "waitForIOMediaWithDevNode:"
- "waitpid failed for %s: %s"
- "wholeMediaForMedia"
- "yes"
- "{}"

```

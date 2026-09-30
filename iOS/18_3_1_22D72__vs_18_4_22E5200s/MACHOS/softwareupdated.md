## softwareupdated

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x35dc0
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x3fe0
+2171.100.125.0.3
+  __TEXT.__text: 0x2a828
+  __TEXT.__auth_stubs: 0x1480
+  __TEXT.__objc_stubs: 0x3980
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x13f0
-  __TEXT.__const: 0x618
-  __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__cstring: 0xbc3d
-  __TEXT.__objc_classname: 0x34e
-  __TEXT.__objc_methname: 0x427d
-  __TEXT.__objc_methtype: 0x110d
-  __TEXT.__oslogstring: 0x44d8
-  __TEXT.__unwind_info: 0xac0
-  __DATA_CONST.__auth_got: 0xbd0
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1c40
-  __DATA_CONST.__cfstring: 0x9ba0
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__objc_methlist: 0x150c
+  __TEXT.__const: 0x500
+  __TEXT.__gcc_except_tab: 0x6a8
+  __TEXT.__cstring: 0xb181
+  __TEXT.__objc_classname: 0x2fc
+  __TEXT.__objc_methname: 0x3b0d
+  __TEXT.__objc_methtype: 0x1084
+  __TEXT.__oslogstring: 0x32d6
+  __TEXT.__unwind_info: 0x960
+  __DATA_CONST.__auth_got: 0xa50
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x1818
+  __DATA_CONST.__cfstring: 0x93c0
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x2a50
-  __DATA.__objc_selrefs: 0x12a8
-  __DATA.__objc_ivar: 0x11c
-  __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0x7e1
-  __DATA.__bss: 0x3a8
+  __DATA.__objc_const: 0x1bf8
+  __DATA.__objc_selrefs: 0x1168
+  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_data: 0x460
+  __DATA.__data: 0x731
+  __DATA.__bss: 0x360
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 874
-  Symbols:   6711
-  CStrings:  2876
+  - /usr/lib/libpartition2_dynamic.dylib
+  Functions: 772
+  Symbols:   5879
+  CStrings:  2536
 
Symbols:
+ +[MSUBrainDelegateImpl_softwareupdated sharedInstance].cold.1
+ +[MSUNRDUpdateBrainController sharedInstance].cold.1
+ +[MSUSupport sharedSupport].cold.1
+ +[MSUUpdateBrainLocator locatorsDictionary].cold.1
+ +[MSUUpdateBrainLocator locatorsStateQueue].cold.1
+ +[UMEventRecorder submitQueue].cold.1
+ -[UMEventRecorder _currentEAPFSMode].cold.1
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/librestorecommon.a(RestoreCommon.o)
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(NRDRemoteableBlock.o)
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(NRDUpdateBrainClientImpl.o)
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(NRDUpdateDaemonClientImpl.o)
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(nrd_log.o)
+ _MSUPreferencesCopyValueForDomain.cold.1
+ _OBJC_CLASS_$_LPStaticMedia
+ __44-[MSUNRDUpdateBrainController cancelAndLock]_block_invoke.399
+ __84-[MSUNRDUpdateBrainController waitWithTimeout:progressCallback:context:releaseLock:]_block_invoke.420
+ __Block_byref_object_copy_.293
+ __Block_byref_object_dispose_.294
+ __NRDInstallRecoveryOS_block_invoke.442
+ __copy_shared_cleanup_service_connection_block_invoke.cold.1
+ __copy_shared_cryptegraft_service_connection_block_invoke.cold.1
+ __handle_ma_load_brain_block_invoke.cold.1
+ __main_block_invoke.15.cold.1
+ __main_block_invoke_2.cold.2
+ __main_block_invoke_3.cold.3
+ __main_block_invoke_4.cold.1
+ __perform_self_destruct_block_invoke.cold.1
+ copy_shared_cleanup_service_connection.cold.1
+ copy_shared_cryptegraft_service_connection.cold.1
+ copy_underlying_error_description.cold.1
+ get_peer_connections_queue.cold.1
+ handle_create_update_brain_connection.cold.1
+ handle_mark_self_dirty.cold.1
+ logfunctionv.cold.1
+ msuSharedLogger.cold.1
+ nrdSharedLogger.cold.1
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
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
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
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/librestorecommon.a(RestoreCommon.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Root/usr/local/lib/libNRDUpdateClient_static.a(NRDRemoteableBlock.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Root/usr/local/lib/libNRDUpdateClient_static.a(NRDUpdateBrainClientImpl.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Root/usr/local/lib/libNRDUpdateClient_static.a(NRDUpdateDaemonClientImpl.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Root/usr/local/lib/libNRDUpdateClient_static.a(nrd_log.o)
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
- _APFSVolumeDelete
- _APFSVolumeGetVEKState
- _APFSVolumeRole
- _IOIteratorReset
- _IOObjectIsEqualTo
- _IORegistryEntryGetParentEntry
- _IORegistryEntrySearchCFProperty
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
- _NSLocalizedDescriptionKey
- _NSLocalizedFailureReasonErrorKey
- _NSOSStatusErrorDomain
- _NSStringFromClass
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
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- __26-[LPAPFSContainer volumes]_block_invoke.20
- __28-[LPPartitionMedia children]_block_invoke.13
- __44-[MSUNRDUpdateBrainController cancelAndLock]_block_invoke.396
- __84-[MSUNRDUpdateBrainController waitWithTimeout:progressCallback:context:releaseLock:]_block_invoke.417
- __Block_byref_object_copy_.290
- __Block_byref_object_dispose_.291
- __LPLogObject
- __LPLogPack
- __NRDInstallRecoveryOS_block_invoke.439
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
- ___NSArray0__
- ____LPLogObject_block_invoke
- ____is_running_in_ramdisk_block_invoke
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___block_descriptor_40_e8_32s_e5_v8?0l
- ___block_descriptor_44_e8_32r_e8_v12?0I8l
- ___block_descriptor_44_e8_32s_e8_v12?0I8l
- ___chkstk_darwin
- ___copy_helper_block_e8_32r
- ___copy_helper_block_e8_32s
- ___destroy_helper_block_e8_32r
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
- _fs_snapshot_delete
- _fs_snapshot_list
- _fs_snapshot_rename
- _fs_snapshot_revert
- _fs_snapshot_root
- _fsctl
- _getmntinfo_r_np
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
- _mkdtemp
- _mkpath_np
- _mkstempsat_np
- _objc_msgSend$BSDName
- _objc_msgSend$_copyIOMediaForDiskWithPath:
- _objc_msgSend$_copyLiveFilesystemIOMediaForRootedSnapshot
- _objc_msgSend$_createTemporaryMountPointWithError:
- _objc_msgSend$_deviceCharacteristicStringForKey:
- _objc_msgSend$_loadMountPointTableForMode:
- _objc_msgSend$allMedia
- _objc_msgSend$children
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$content
- _objc_msgSend$contentTypeToSubclassMap
- _objc_msgSend$contentTypesForPartitionMedia
- _objc_msgSend$defaultMountPointGivenRole:
- _objc_msgSend$getBoolPropertyWithName:
- _objc_msgSend$getCString:maxLength:encoding:
- _objc_msgSend$getPropertyWithName:
- _objc_msgSend$getStringPropertyWithName:
- _objc_msgSend$hasSuffix:
- _objc_msgSend$initWithIOMediaObject:
- _objc_msgSend$ioMedia
- _objc_msgSend$isEmbeddedDeviceTypeRoot
- _objc_msgSend$isPrimaryMedia
- _objc_msgSend$isWhole
- _objc_msgSend$liveMediaForSnapshotAtPath:
- _objc_msgSend$mediaForBSDNameOrDeviceNode:
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
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$supportedContentTypes
- _objc_msgSend$unmountWithError:
- _objc_msgSend$unmountWithOptions:error:
- _objc_msgSend$volumeGroupUUID
- _objc_msgSend$volumes
- _objc_msgSend$volumesWithRole:
- _objc_msgSend$waitForBlockStorage
- _objc_msgSend$waitForIOMediaWithDevNode:
- _os_log_pack_compose
- _os_log_pack_send
- _pipe
- _posix_spawn
- _posix_spawn_file_actions_addclose
- _posix_spawn_file_actions_adddup2
- _posix_spawn_file_actions_destroy
- _posix_spawn_file_actions_init
- _posix_spawnattr_destroy
- _posix_spawnattr_init
- _posix_spawnattr_setflags
- _removefile
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
- _setattrlist
- _unlinkat
- _unmount
- _uuid_is_null
- _uuid_parse
- _waitpid
- contentTypeToSubclassMap.once
- contentTypeToSubclassMap.sharedMap
CStrings:
- "%.*s"
- "%@: %@"
- "%@: %@, Mount: %@"
- "%@: %@, UUID: %@"
- "%@s%d"
- "%s\n"
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
- "%s : Error in reading attributes for directory entry %d"
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
- "%s : fs_snapshot_list failed with error %d"
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
- "-o"
- "-restore"
- "-s"
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
- "/private/var/logs"
- "/private/var/recovery/"
- "/private/var/vm"
- "/private/var/wireless/baseband_data"
- "/private/xarts"
- "/sbin/mount_apfs"
- "/tmp//tmp-mount-XXXXXX"
- "41504653-0000-11AA-AA11-00306543ECAC"
- "@%@"
- "@20@0:8I16"
- "@32@0:8@16^B24"
- "@64@0:8@16i24B28q32q40@48^@56"
- "AppleAPFSMedia"
- "AppleAPFSSnapshot"
- "AppleAPFSVolume"
- "Apple_partition_scheme"
- "B28@0:8i16^@20"
- "B40@0:8@16@24^@32"
- "B40@0:8@16d24^@32"
- "BSD Major"
- "BSD Minor"
- "BSDName"
- "Baseband Data"
- "Call to APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ returned EEXIST\n"
- "Can not mount (%@) because mount returned %d."
- "Can not mount (%s) because it does not appear to have a device node."
- "Can not mount (%{private}s) because we could not create its mount folder (%{private}s)."
- "CaseSensitive"
- "Content"
- "Could not removefile(3) path %{private}s: %s"
- "Could not reset metadata on %{private}s: %s"
- "Couldn't create a temporary mount point %s"
- "Data"
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
- "Hardware"
- "I16@0:8"
- "I24@0:8@16"
- "IOBlockStorageDevice"
- "IOKit service wait timed out, volumes may be stale."
- "IOKit wait timed out, volume for media may be stale."
- "IOProviderClass"
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
- "Logs"
- "Medium Type"
- "Model"
- "Model Number"
- "Mount failed"
- "Mounted %@ at %{private}@"
- "Mounted %@, Snapshot( %{private}@ ) at %{private}@"
- "Physical Interconnect Location"
- "Preboot"
- "Private"
- "Protocol Characteristics"
- "Recovery"
- "Rotational"
- "Scratch"
- "Solid State"
- "System"
- "T@\"NSArray\",R"
- "T@\"NSDictionary\",R"
- "TB,R"
- "TI,V_ioMedia"
- "Timed out waiting for: %@"
- "Unmount failed with EINVAL, will assume race. Ignoring error."
- "Unmounted %@ ( %{private}@ )"
- "Update"
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
- "com.apple.os.update-"
- "componentsSeparatedByString:"
- "content"
- "contentTypeToSubclassMap"
- "contentTypesForPartitionMedia"
- "create snapshot operation failed: %d %s"
- "createSnapshot:error:"
- "defaultMountPointGivenRole:"
- "defaultVolumeNameGivenRole:"
- "deleteSnapshots:waitForDeletionFor:error:"
- "deleteVolumeWithError:"
- "diagsContainer"
- "eraseVolumeWithError:"
- "failed"
- "getBoolPropertyWithName:"
- "getCString:maxLength:encoding:"
- "getPropertyWithName:"
- "getStringPropertyWithName:"
- "hasEmbeddedDeviceTypeRoot"
- "hasSuffix:"
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
- "libpartition2"
- "liveMediaForSnapshotAtPath:"
- "mediaForBSDNameOrDeviceNode:"
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
- "nobrowse"
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
- "rdonly"
- "recoveryVolume"
- "rename snapshot operation failed: %d %s"
- "renameSnapshot:to:error:"
- "revert snapshot operation failed: %d %s"
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
- "storageMedium"
- "substringFromIndex:"
- "succeeded"
- "supportedContentTypes"
- "unmountAllWithError:"
- "unmountWithError:"
- "unmountWithOptions:error:"
- "updateVolume"
- "v12@?0I8"
- "v20@0:8I16"
- "vendorName"
- "volumeGroupUUID"
- "volumes"
- "volumesWithRole:"
- "waitForBlockStorage"
- "waitForIOMediaWithDevNode:"
- "waitpid failed for %s: %s"
- "wholeMediaForMedia"
- "xART"
- "yes"

```

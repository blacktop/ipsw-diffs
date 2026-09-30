## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x5c0
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0xe0
-  __TEXT.__cstring: 0x163
-  __TEXT.__const: 0x24
-  __TEXT.__objc_methname: 0x85
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__cfstring: 0x60
+2171.101.1.0.0
+  __TEXT.__text: 0xc480
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x4e4
+  __TEXT.__cstring: 0x1217
+  __TEXT.__const: 0x180
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__oslogstring: 0x12a4
+  __TEXT.__objc_classname: 0x70
+  __TEXT.__objc_methname: 0xb3a
+  __TEXT.__objc_methtype: 0x118
+  __TEXT.__unwind_info: 0x228
+  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x38
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0x348
+  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0xac
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/MobileSoftwareUpdate
   - /usr/lib/libMobileGestalt.dylib
+  - /usr/lib/libSecureMAHelper.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D64F5CD8-11E2-3DA6-A50E-71E61E096DCB
-  Functions: 6
-  Symbols:   79
-  CStrings:  25
+  UUID: F8C58D56-29C8-3FE7-A9CD-748D191759B9
+  Functions: 136
+  Symbols:   1161
+  CStrings:  549
 
Symbols:
+ +[LPStaticAPFSContainer allAPFSContainers]
+ +[LPStaticAPFSContainer diagsContainer]
+ +[LPStaticAPFSContainer supportedContentTypes]
+ +[LPStaticAPFSPhysicalStore supportedContentTypes]
+ +[LPStaticAPFSVolume _loadMountPointTableForMode:]
+ +[LPStaticAPFSVolume defaultMountPointGivenRole:]
+ +[LPStaticAPFSVolume defaultVolumeNameGivenRole:]
+ +[LPStaticAPFSVolume initialize]
+ +[LPStaticAPFSVolume initialize].cold.1
+ +[LPStaticAPFSVolume supportedContentTypes]
+ +[LPStaticMedia _copyIOMediaForDiskWithPath:]
+ +[LPStaticMedia _copyLiveFilesystemIOMediaForRootedSnapshot]
+ +[LPStaticMedia allMedia]
+ +[LPStaticMedia hasEmbeddedDeviceTypeRoot]
+ +[LPStaticMedia liveMediaForSnapshotAtPath:]
+ +[LPStaticMedia mediaForBSDNameOrDeviceNode:]
+ +[LPStaticMedia mediaForPath:]
+ +[LPStaticMedia mediaForPath:isSnapshot:]
+ +[LPStaticMedia mediaForPath:snapshotName:]
+ +[LPStaticMedia mediaForUUID:]
+ +[LPStaticMedia snapshotNameForMediaForPath:]
+ +[LPStaticMedia supportedContentTypes]
+ +[LPStaticMedia(Private) contentTypeToSubclassMap]
+ +[LPStaticMedia(Private) contentTypeToSubclassMap].cold.1
+ +[LPStaticMedia(Private) mediaOfCorrectTypeGivenIOMedia:]
+ +[LPStaticMedia(Private) waitForBlockStorage]
+ +[LPStaticMedia(Private) waitForIOMediaWithDevNode:]
+ +[LPStaticPartitionMedia contentTypesForPartitionMedia]
+ +[LPStaticPartitionMedia primaryMedia]
+ +[LPStaticPartitionMedia supportedContentTypes]
+ -[LPStaticAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]
+ -[LPStaticAPFSContainer physicalStores]
+ -[LPStaticAPFSContainer prebootVolume]
+ -[LPStaticAPFSContainer recoveryVolume]
+ -[LPStaticAPFSContainer updateVolume]
+ -[LPStaticAPFSContainer volumesWithRole:]
+ -[LPStaticAPFSContainer volumes]
+ -[LPStaticAPFSPhysicalStore container]
+ -[LPStaticAPFSPhysicalStore parent]
+ -[LPStaticAPFSPhysicalStore role]
+ -[LPStaticAPFSVolume _createTemporaryMountPointWithError:]
+ -[LPStaticAPFSVolume _createTemporaryMountPointWithError:].cold.1
+ -[LPStaticAPFSVolume container]
+ -[LPStaticAPFSVolume createSnapshot:error:]
+ -[LPStaticAPFSVolume deleteSnapshots:waitForDeletionFor:error:]
+ -[LPStaticAPFSVolume deleteVolumeWithError:]
+ -[LPStaticAPFSVolume eraseVolumeWithError:]
+ -[LPStaticAPFSVolume isCaseSenstive]
+ -[LPStaticAPFSVolume isEncrypted]
+ -[LPStaticAPFSVolume isFilevaultEncrypted]
+ -[LPStaticAPFSVolume isMounted]
+ -[LPStaticAPFSVolume mountAtPath:error:]
+ -[LPStaticAPFSVolume mountAtPath:options:error:]
+ -[LPStaticAPFSVolume mountAtTemporaryPathWithError:]
+ -[LPStaticAPFSVolume mountAtTemporaryPathWithOptions:error:]
+ -[LPStaticAPFSVolume mountWithError:]
+ -[LPStaticAPFSVolume pairedVolume]
+ -[LPStaticAPFSVolume renameSnapshot:to:error:]
+ -[LPStaticAPFSVolume revertToSnapshot:error:]
+ -[LPStaticAPFSVolume revertToSnapshot:options:error:]
+ -[LPStaticAPFSVolume role]
+ -[LPStaticAPFSVolume rootToSnapshot:error:]
+ -[LPStaticAPFSVolume setRole:withError:]
+ -[LPStaticAPFSVolume snapshotInfoWithError:]
+ -[LPStaticAPFSVolume snapshotMountPoints]
+ -[LPStaticAPFSVolume snapshotsWithError:]
+ -[LPStaticAPFSVolume unmountAllWithError:]
+ -[LPStaticAPFSVolume unmountWithError:]
+ -[LPStaticAPFSVolume unmountWithOptions:error:]
+ -[LPStaticAPFSVolume volumeGroupUUID]
+ -[LPStaticMedia BSDName]
+ -[LPStaticMedia _deviceCharacteristicStringForKey:]
+ -[LPStaticMedia content]
+ -[LPStaticMedia dealloc]
+ -[LPStaticMedia description]
+ -[LPStaticMedia devNodePath]
+ -[LPStaticMedia deviceModel]
+ -[LPStaticMedia initWithIOMediaObject:]
+ -[LPStaticMedia ioMedia]
+ -[LPStaticMedia isEmbeddedDeviceTypeRoot]
+ -[LPStaticMedia isEqual:]
+ -[LPStaticMedia isInternal]
+ -[LPStaticMedia isJournaled]
+ -[LPStaticMedia isPrimaryMedia]
+ -[LPStaticMedia isReadOnly]
+ -[LPStaticMedia isWhole]
+ -[LPStaticMedia mediaUUID]
+ -[LPStaticMedia mountPoint]
+ -[LPStaticMedia name]
+ -[LPStaticMedia setIoMedia:]
+ -[LPStaticMedia setName:withError:]
+ -[LPStaticMedia storageMedium]
+ -[LPStaticMedia vendorName]
+ -[LPStaticMedia wholeMediaForMedia]
+ -[LPStaticMedia(Private) getBoolPropertyWithName:]
+ -[LPStaticMedia(Private) getPropertyWithName:]
+ -[LPStaticMedia(Private) getStringPropertyWithName:]
+ -[LPStaticPartitionMedia children]
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/libpartition2/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/boot_policy_support.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
+ GCC_except_table4
+ LPAPFSContainer.m
+ LPAPFSContainer_Private.m
+ LPAPFSPhyscialStore_Private.m
+ LPAPFSPhysicalStore.m
+ LPAPFSVolume.m
+ LPAPFSVolume_Private.m
+ LPIOKitHelper.m
+ LPLog.m
+ LPMedia.m
+ LPPartitionMedia.m
+ OBJC_IVAR_$_LPStaticMedia._ioMedia
+ _APFSVolumeCreate
+ _APFSVolumeCreateForMSU
+ _APFSVolumeDelete
+ _APFSVolumeGetVEKState
+ _APFSVolumeRole
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDataCreate
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _CFEqual
+ _CFGetTypeID
+ _CFRelease
+ _CFRetain
+ _CFStringCompare
+ _CFStringGetTypeID
+ _IOBSDNameMatching
+ _IOIteratorIsValid
+ _IOIteratorNext
+ _IOIteratorReset
+ _IOObjectConformsTo
+ _IOObjectIsEqualTo
+ _IOObjectRelease
+ _IOObjectRetain
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryFromPath
+ _IORegistryEntryGetName
+ _IORegistryEntryGetParentEntry
+ _IORegistryEntrySearchCFProperty
+ _IORegistryIteratorExitEntry
+ _IOServiceGetMatchingService
+ _IOServiceGetMatchingServices
+ _IOServiceMatching
+ _IOServiceWaitQuiet
+ _LPAPFSContainerMediaTypeUUID
+ _LPAPFSPhysicalStoreDiagsMediaUUID
+ _LPAPFSPhysicalStoreMediaUUID
+ _LPAPFSPhysicalStoreRecoveryMediaUUID
+ _LPAPFSSnapshotPropertyKeyMarkedForRevert
+ _LPAPFSSnapshotPropertyKeyMarkedForRoot
+ _LPAPFSSnapshotPropertyKeyName
+ _LPAPFSSnapshotPropertyKeyXID
+ _LPAPFSVolumeMediaTypeUUID
+ _LPAPFSVolumeMountOptionNoBrowse
+ _LPAPFSVolumeMountOptionNoFirmlinks
+ _LPAPFSVolumeMountOptionReadOnly
+ _LPAPFSVolumeMountOptionSnapshotName
+ _LPAPFSVolumeRevertOptionSkipRemount
+ _LPAPFSVolumeSnapshotMountPointKeyMountPoint
+ _LPAPFSVolumeSnapshotMountPointKeyName
+ _LPAPFSVolumeUnmountOptionAll
+ _LPAPFSVolumeUnmountOptionDoNotLock
+ _LPAPFSVolumeUnmountOptionForce
+ _LPAPFSVolumeUnmountOptionSnapshotName
+ _LPLogObject.cold.1
+ _LPLogObject.obj
+ _LPLogObject.onceToken
+ _NSFilePathErrorKey
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _NSOSStatusErrorDomain
+ _NSPOSIXErrorDomain
+ _NSStringFromClass
+ _OBJC_CLASS_$_LPStaticAPFSContainer
+ _OBJC_CLASS_$_LPStaticAPFSPhysicalStore
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OBJC_CLASS_$_LPStaticPartitionMedia
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_SecureMAHelper
+ _OBJC_METACLASS_$_LPStaticAPFSContainer
+ _OBJC_METACLASS_$_LPStaticAPFSPhysicalStore
+ _OBJC_METACLASS_$_LPStaticAPFSVolume
+ _OBJC_METACLASS_$_LPStaticMedia
+ _OBJC_METACLASS_$_LPStaticPartitionMedia
+ _OBJC_METACLASS_$_NSObject
+ __32-[LPStaticAPFSContainer volumes]_block_invoke.20
+ __34-[LPStaticPartitionMedia children]_block_invoke.13
+ __Block_object_assign
+ __Block_object_dispose
+ __LPLogObject
+ __LPLogPack
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_LPStaticAPFSContainer
+ __OBJC_$_CLASS_METHODS_LPStaticAPFSPhysicalStore
+ __OBJC_$_CLASS_METHODS_LPStaticAPFSVolume
+ __OBJC_$_CLASS_METHODS_LPStaticMedia(Private)
+ __OBJC_$_CLASS_METHODS_LPStaticPartitionMedia
+ __OBJC_$_INSTANCE_METHODS_LPStaticAPFSContainer
+ __OBJC_$_INSTANCE_METHODS_LPStaticAPFSPhysicalStore
+ __OBJC_$_INSTANCE_METHODS_LPStaticAPFSVolume
+ __OBJC_$_INSTANCE_METHODS_LPStaticMedia(Private)
+ __OBJC_$_INSTANCE_METHODS_LPStaticPartitionMedia
+ __OBJC_$_INSTANCE_VARIABLES_LPStaticMedia
+ __OBJC_$_PROP_LIST_LPStaticMedia
+ __OBJC_CLASS_RO_$_LPStaticAPFSContainer
+ __OBJC_CLASS_RO_$_LPStaticAPFSPhysicalStore
+ __OBJC_CLASS_RO_$_LPStaticAPFSVolume
+ __OBJC_CLASS_RO_$_LPStaticMedia
+ __OBJC_CLASS_RO_$_LPStaticPartitionMedia
+ __OBJC_METACLASS_RO_$_LPStaticAPFSContainer
+ __OBJC_METACLASS_RO_$_LPStaticAPFSPhysicalStore
+ __OBJC_METACLASS_RO_$_LPStaticAPFSVolume
+ __OBJC_METACLASS_RO_$_LPStaticMedia
+ __OBJC_METACLASS_RO_$_LPStaticPartitionMedia
+ __Unwind_Resume
+ ___32-[LPStaticAPFSContainer volumes]_block_invoke
+ ___34-[LPStaticPartitionMedia children]_block_invoke
+ ___45+[LPStaticMedia snapshotNameForMediaForPath:]_block_invoke
+ ___47-[LPStaticAPFSVolume unmountWithOptions:error:]_block_invoke
+ ___50+[LPStaticMedia(Private) contentTypeToSubclassMap]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___NSArray0__
+ ____LPLogObject_block_invoke
+ ____is_running_in_ramdisk_block_invoke
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_44_e8_32r_e8_v12?0I8l
+ ___block_descriptor_44_e8_32s_e8_v12?0I8l
+ ___block_literal_global
+ ___chkstk_darwin
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32s
+ ___objc_personality_v0
+ ___stdoutp
+ ___strlcpy_chk
+ __block_literal_global.164
+ __block_literal_global.186
+ __execForLibpartition
+ __lp2_delete_directory_contents
+ __lp2_delete_directory_contents_confirm
+ __lp2_delete_directory_contents_error
+ __objc_empty_cache
+ __os_log_pack_fill
+ __os_log_pack_size
+ _bootpolicy_get_proposed_local_policy_nonce_digest
+ _bootpolicy_get_proposed_recoveryos_policy_nonce_digest
+ _bootpolicy_update_local_policy_nonce_end
+ _commit_local_bootpolicy_nonce_if_booted
+ _dispatch_once
+ _dprintf
+ _fcopyfile
+ _fetch_bootpolicy_nonces
+ _ffsctl
+ _fopen
+ _fprintf
+ _free
+ _fs_snapshot_create
+ _fs_snapshot_delete
+ _fs_snapshot_list
+ _fs_snapshot_rename
+ _fs_snapshot_revert
+ _fs_snapshot_root
+ _fsctl
+ _get_isc_preboot_volume_mountpoint
+ _getattrlist
+ _getmntinfo_r_np
+ _init_log
+ _is_running_in_ramdisk.is_ramdisk
+ _is_running_in_ramdisk.onceToken
+ _iterateSafely
+ _kAPFSVolumeCaseSensitiveKey
+ _kAPFSVolumeFSIndexKey
+ _kAPFSVolumeGroupSiblingFSIndexKey
+ _kAPFSVolumeNameKey
+ _kAPFSVolumeNoAutomountAtCreateKey
+ _kAPFSVolumeQuotaSizeKey
+ _kAPFSVolumeReserveSizeKey
+ _kAPFSVolumeRoleKey
+ _kCFAllocatorDefault
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kIOMasterPortDefault
+ _kLPDefaultLiveOSMountPointTable
+ _kLPDefaultMountPointTable
+ _kLPDefaultRAMDiskMountPointTable
+ _lchflags
+ _logString
+ _logfunction
+ _logfunctionv
+ _lstat
+ _mkdir
+ _mkdtemp
+ _mkpath_np
+ _mkstempsat_np
+ _objc_autorelease
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$BSDName
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_copyIOMediaForDiskWithPath:
+ _objc_msgSend$_copyLiveFilesystemIOMediaForRootedSnapshot
+ _objc_msgSend$_createTemporaryMountPointWithError:
+ _objc_msgSend$_deviceCharacteristicStringForKey:
+ _objc_msgSend$_loadMountPointTableForMode:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allMedia
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$boolValue
+ _objc_msgSend$children
+ _objc_msgSend$class
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$container
+ _objc_msgSend$content
+ _objc_msgSend$contentTypeToSubclassMap
+ _objc_msgSend$contentTypesForPartitionMedia
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$defaultMountPointGivenRole:
+ _objc_msgSend$description
+ _objc_msgSend$devNodePath
+ _objc_msgSend$diagsContainer
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$firstObject
+ _objc_msgSend$getBoolPropertyWithName:
+ _objc_msgSend$getPropertyWithName:
+ _objc_msgSend$getStringPropertyWithName:
+ _objc_msgSend$graftSecureAssetsFromLastBootSession
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithIOMediaObject:
+ _objc_msgSend$initWithLogger:
+ _objc_msgSend$intValue
+ _objc_msgSend$ioMedia
+ _objc_msgSend$isEmbeddedDeviceTypeRoot
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isKindOfClass:
+ _objc_msgSend$isPrimaryMedia
+ _objc_msgSend$isWhole
+ _objc_msgSend$lastObject
+ _objc_msgSend$length
+ _objc_msgSend$liveMediaForSnapshotAtPath:
+ _objc_msgSend$mediaForBSDNameOrDeviceNode:
+ _objc_msgSend$mediaForPath:
+ _objc_msgSend$mediaForPath:snapshotName:
+ _objc_msgSend$mediaOfCorrectTypeGivenIOMedia:
+ _objc_msgSend$mediaUUID
+ _objc_msgSend$mountAtPath:error:
+ _objc_msgSend$mountAtPath:options:error:
+ _objc_msgSend$mountAtTemporaryPathWithError:
+ _objc_msgSend$mountAtTemporaryPathWithOptions:error:
+ _objc_msgSend$mountPoint
+ _objc_msgSend$name
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$primaryMedia
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$revertToSnapshot:options:error:
+ _objc_msgSend$role
+ _objc_msgSend$setIoMedia:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$snapshotInfoWithError:
+ _objc_msgSend$snapshotMountPoints
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$supportedContentTypes
+ _objc_msgSend$unmountWithError:
+ _objc_msgSend$unmountWithOptions:error:
+ _objc_msgSend$volumeGroupUUID
+ _objc_msgSend$volumes
+ _objc_msgSend$volumesWithRole:
+ _objc_msgSend$waitForBlockStorage
+ _objc_msgSend$waitForIOMediaWithDevNode:
+ _objc_msgSendSuper2
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _open
+ _os_log_create
+ _os_log_pack_compose
+ _os_log_pack_send
+ _os_variant_is_basesystem
+ _posix_spawnattr_destroy
+ _posix_spawnattr_init
+ _posix_spawnattr_setflags
+ _removefile
+ _removefile_state_alloc
+ _removefile_state_free
+ _removefile_state_set
+ _sConsoleFD
+ _sLegacyVolumeNameMapping
+ _sLogLevel
+ _sLogToConsole
+ _sLogToOSLog
+ _sLogToStandardOut
+ _sMountPointLookupTable
+ _sRoleEncodingMapping
+ _sRoleLookupTable
+ _setattrlist
+ _sleep
+ _stat
+ _strcmp
+ _strlen
+ _strnlen
+ _strrchr
+ _strstr
+ _sysctlbyname
+ _unlinkat
+ _unmount
+ _uuid_is_null
+ _uuid_parse
+ boot_policy_support.m
+ commit_local_bootpolicy_nonce_if_booted.cold.1
+ contentTypeToSubclassMap.once
+ contentTypeToSubclassMap.sharedMap
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
CStrings:
+ "%@"
+ "%@: %@, Mount: %@"
+ "%@: %@, UUID: %@"
+ "%@s%d"
+ "%s\n"
+ "%s : APFSVolumeCreateForMSU exists and we're creating a System volume. Preferring it to APFSVolumeCreate."
+ "%s : Add volume failed with error: %d."
+ "%s : Can not iterate over physical store services."
+ "%s : Container is missing UUID?"
+ "%s : Container is somehow missing a BSD name."
+ "%s : Container isn't a container?!"
+ "%s : Could not open device is not mounted."
+ "%s : Could not open device mount %{private}@."
+ "%s : Could not set root from snapshot. Errno: %d"
+ "%s : Creating APFS volume %s with options: %@"
+ "%s : Error in reading attributes for directory entry %d"
+ "%s : Failed because target volume is not mounted"
+ "%s : Failed to delete snapshot: %{private}@, %d"
+ "%s : Failed to encode snapshot name %{private}s for some reason."
+ "%s : Failed to get content type."
+ "%s : Failed to open media for snapshot delete: %d"
+ "%s : IOIterator was still invalid after attempting %d times"
+ "%s : Need a valid new snapshot name."
+ "%s : Need a valid snapshot name."
+ "%s : Need a valid snapshot names."
+ "%s : Paired volume is not valid if role is not system."
+ "%s : Paired volume must be in the same container"
+ "%s : Requested system volume with sibling but the key is not supported."
+ "%s : Unable to get parent iterator"
+ "%s : Unable to get the iterator for entry."
+ "%s : Unable to open mount point %{private}@: %d"
+ "%s : Volume name is invalid"
+ "%s : Waiting for snapshots to delete timed out"
+ "%s : You need to specify a volume name."
+ "%s : failed to read value for property named: %@"
+ "%s : failed with iokit error: %d"
+ "%s : failed with posix error: %d"
+ "%s : failed with unknown kern_return_t error: %d"
+ "%s : fs_snapshot_list failed with error %d"
+ "%s : going to delete apfs volume ( %@ )"
+ "%s : volume is missing a dev node somehow"
+ "%s called but %{private}@ is not mounted."
+ "%s called on device with no dev node"
+ "%s was stopped by signal %d"
+ "%s was terminated by signal %d"
+ "%s: %@ isn't an APFS volume"
+ "%s: Error getting snapshot info for %@: %@"
+ "%s: Failed to find primary media"
+ "%s: Failed to get IOMedia objects"
+ "%s: Failed to obtain parent IOMedia for disk at path %{private}@"
+ "%s: Failed to remount volume with error: %d"
+ "%s: Failed to set name for volume: %s\n"
+ "%s: Failed to unmount volume with error: %d"
+ "%s: Mount point is %{private}@\n"
+ "%s: No disk for %{private}@"
+ "%s: No media found for path: %{private}@"
+ "%s: No snapshot is tagged for boot and none match the naming scheme"
+ "%s: Not on a rooted snapshot disk, will return self: %{private}@"
+ "%s: Parent of disk backing %{private}@ is not an APFS volume"
+ "%s: Skipping unmount/remount of %@"
+ "%s: Successfully set volume name to %{private}@\n"
+ "%s: Trying to determine mount point\n"
+ "%s: Volume is not mounted. Unable to set name\n"
+ "%s: could not look up snapshot by UUID: %d (%s)"
+ "%s: could not parse %s %{private}s: %{private}@"
+ "%s: failed to get journaled status for %@\n"
+ "%s: failed to get read-only status for %@\n"
+ "%s: failed to get role. Error: %d"
+ "%s: no IOMedia for %@ (device 0x%lx)"
+ "%s: no filesystem for %@ (%d): %s"
+ "%s: path is a snapshot, but has no name: %{private}@"
+ "%s: statfs failed: %d (%s)"
+ "%{private}s is a firmlink. Clearing firmlink."
+ "+[LPStaticAPFSContainer diagsContainer]"
+ "+[LPStaticMedia _copyIOMediaForDiskWithPath:]"
+ "+[LPStaticMedia _copyLiveFilesystemIOMediaForRootedSnapshot]"
+ "+[LPStaticMedia allMedia]"
+ "+[LPStaticMedia liveMediaForSnapshotAtPath:]"
+ "+[LPStaticMedia mediaForPath:snapshotName:]"
+ "+[LPStaticMedia snapshotNameForMediaForPath:]"
+ "-[LPStaticAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]"
+ "-[LPStaticAPFSContainer physicalStores]"
+ "-[LPStaticAPFSPhysicalStore container]"
+ "-[LPStaticAPFSPhysicalStore parent]"
+ "-[LPStaticAPFSPhysicalStore role]"
+ "-[LPStaticAPFSVolume createSnapshot:error:]"
+ "-[LPStaticAPFSVolume deleteSnapshots:waitForDeletionFor:error:]"
+ "-[LPStaticAPFSVolume deleteVolumeWithError:]"
+ "-[LPStaticAPFSVolume eraseVolumeWithError:]"
+ "-[LPStaticAPFSVolume renameSnapshot:to:error:]"
+ "-[LPStaticAPFSVolume revertToSnapshot:options:error:]"
+ "-[LPStaticAPFSVolume role]"
+ "-[LPStaticAPFSVolume rootToSnapshot:error:]"
+ "-[LPStaticAPFSVolume snapshotInfoWithError:]"
+ "-[LPStaticAPFSVolume snapshotMountPoints]"
+ "-[LPStaticMedia isJournaled]"
+ "-[LPStaticMedia isReadOnly]"
+ "-[LPStaticMedia setName:withError:]"
+ "-[LPStaticMedia wholeMediaForMedia]"
+ "-[LPStaticMedia(Private) getPropertyWithName:]"
+ "-n"
+ "-o"
+ "-restore"
+ "-s"
+ ".XXXXXXXX"
+ "/System/Volumes/Update"
+ "/System/Volumes/Update/Controller/MSUEarlyBootTask"
+ "/System/Volumes/Update/Controller/MSUEarlyBootTask/MSUEarlyBootTask.log"
+ "/dev/"
+ "/dev/%@"
+ "/mnt1"
+ "/mnt10"
+ "/mnt11"
+ "/mnt2"
+ "/mnt3"
+ "/mnt4"
+ "/mnt5/tmp-mount-XXXXXX"
+ "/mnt6"
+ "/mnt7"
+ "/mnt8"
+ "/private/var/"
+ "/private/var/hardware"
+ "/private/var/internal"
+ "/private/var/logs"
+ "/private/var/mobile"
+ "/private/var/recovery/"
+ "/private/var/vm"
+ "/private/var/wireless/baseband_data"
+ "/private/xarts"
+ "/sbin/mount_apfs"
+ "/tmp//tmp-mount-XXXXXX"
+ "/tmp/preboot-isc.XXXXXX"
+ "41504653-0000-11AA-AA11-00306543ECAC"
+ "52637672-7900-11AA-AA11-00306543ECAC"
+ "69646961-6700-11AA-AA11-00306543ECAC"
+ "7C3457EF-0000-11AA-AA11-00306543ECAC"
+ "=========================MSUEarlyBootTask: Done grafting assets==========================\n"
+ "=========================MSUEarlyBootTask: Running on reboot==========================\n"
+ "@"
+ "@%@"
+ "@16@0:8"
+ "@20@0:8I16"
+ "@20@0:8i16"
+ "@24@0:8@16"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@32@0:8@16^B24"
+ "@64@0:8@16i24B28q32q40@48^@56"
+ "AppleAPFSMedia"
+ "AppleAPFSSnapshot"
+ "AppleAPFSVolume"
+ "Apple_partition_scheme"
+ "B16@0:8"
+ "B24@0:8@16"
+ "B24@0:8^@16"
+ "B28@0:8i16^@20"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16d24^@32"
+ "BSD Major"
+ "BSD Minor"
+ "BSD Name"
+ "BSDName"
+ "Baseband Data"
+ "Booted into proposed bootpolicy nonce; committing now\n"
+ "Call to APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ returned EEXIST\n"
+ "Can not mount (%@) because mount returned %d."
+ "Can not mount (%s) because it does not appear to have a device node."
+ "Can not mount (%{private}s) because we could not create its mount folder (%{private}s)."
+ "CaseSensitive"
+ "Content"
+ "Could not find preboot volume in the ISC container when trying to mount it.\n"
+ "Could not find the ISC container!\n"
+ "Could not find the preboot volume within the ISC container.\n"
+ "Could not removefile(3) path %{private}s: %s"
+ "Could not reset metadata on %{private}s: %s"
+ "Couldn't create a temporary mount point %s"
+ "Data"
+ "Deleting contents of %{private}s %s (result: %d)."
+ "Deleting contents of %{private}s..."
+ "Device Characteristics"
+ "EF57347C-0000-11AA-AA11-00306543ECAC"
+ "EmbeddedDeviceTypeRoot"
+ "Error: More than one preboot volume found: %{private}@"
+ "Error: More than one recovery volume found: %{private}@"
+ "Error: More than one update volume found: %{private}@"
+ "FDisk_partition_scheme"
+ "Failed to call APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ with errno %d\n"
+ "Failed to clear the firmlink on %s with error: %{private}s"
+ "Failed to commit() local bootpolicy nonce\n"
+ "Failed to create container volumes iterator"
+ "Failed to create partition media iterator."
+ "Failed to find media for %@"
+ "Failed to gather local policy nonce digest with error: %d\n"
+ "Failed to gather recoveryOS policy nonce digest with error: %d\n"
+ "Failed to graft"
+ "Failed to mount the ISC preboot volume.\n"
+ "Failed to read firm link information for %{private}s: %s"
+ "Failed to unmount %@ **FORCING UNMOUNT** error: %d"
+ "Failed to unmount %@ retry: %s error: %d"
+ "FireWire Vendor Name"
+ "GUID_partition_scheme"
+ "Hardware"
+ "I"
+ "I16@0:8"
+ "I24@0:8@16"
+ "IOBlockStorageDevice"
+ "IODeviceTree:/chosen/asmb"
+ "IOKit service wait timed out, volumes may be stale."
+ "IOKit wait timed out, volume for media may be stale."
+ "IOMedia"
+ "IOPropertyMatch"
+ "IOProviderClass"
+ "IOService"
+ "Internal"
+ "LPAPFSSnapshotPropertyKeyMarkedForRevert"
+ "LPAPFSSnapshotPropertyKeyMarkedForRoot"
+ "LPAPFSSnapshotPropertyKeyName"
+ "LPAPFSSnapshotPropertyKeyXID"
+ "LPAPFSVolumeMountOptionNoBrowse"
+ "LPAPFSVolumeMountOptionNoFirmlinks"
+ "LPAPFSVolumeMountOptionReadOnly"
+ "LPAPFSVolumeMountOptionSnapshotName"
+ "LPAPFSVolumeRevertOptionSkipRemount"
+ "LPAPFSVolumeSnapshotMountPointKeyMountPoint"
+ "LPAPFSVolumeSnapshotMountPointKeyName"
+ "LPAPFSVolumeUnmountOptionAll"
+ "LPAPFSVolumeUnmountOptionDoNotLock"
+ "LPAPFSVolumeUnmountOptionForce"
+ "LPAPFSVolumeUnmountOptionSnapshotName"
+ "LPStaticAPFSContainer"
+ "LPStaticAPFSPhysicalStore"
+ "LPStaticAPFSVolume"
+ "LPStaticMedia"
+ "LPStaticPartitionMedia"
+ "Logs"
+ "MSUEarlyBootTask: %s secure assets from previous boot session\n"
+ "MSUEarlyBootTask: Attempting to determine secure assets grafted during previous boot\n"
+ "MSUEarlyBootTask: Failed to allocate secureAssetHelper to graft SMA's\n"
+ "Medium Type"
+ "Model"
+ "Model Number"
+ "Mount failed"
+ "Mounted %@ at %{private}@"
+ "Mounted %@, Snapshot( %{private}@ ) at %{private}@"
+ "Physical Interconnect Location"
+ "Preboot"
+ "Private"
+ "Protocol Characteristics"
+ "Recovery"
+ "Rotational"
+ "Scratch"
+ "Solid State"
+ "Successfully grafted"
+ "System"
+ "T@\"NSArray\",R"
+ "T@\"NSDictionary\",R"
+ "TB,R"
+ "TI,V_ioMedia"
+ "Timed out waiting for: %@"
+ "UTF8String"
+ "UUID"
+ "Unmount failed with EINVAL, will assume race. Ignoring error."
+ "Unmounted %@ ( %{private}@ )"
+ "Update"
+ "User"
+ "Vendor Name"
+ "VolGroupUUID"
+ "Volume is already mounted at %@, attempting to re-mount at %@"
+ "Volume is already mounted at %@, skipping re-mount"
+ "Was asked asked to unmount (%@) but is not mounted."
+ "Whole"
+ "_Bool iterateSafely(io_iterator_t, int, void (^__strong)(io_object_t), void (^__strong)(void))"
+ "_copyIOMediaForDiskWithPath:"
+ "_copyLiveFilesystemIOMediaForRootedSnapshot"
+ "_createTemporaryMountPointWithError:"
+ "_deviceCharacteristicStringForKey:"
+ "_ioMedia"
+ "_loadMountPointTableForMode:"
+ "a+"
+ "addObject:"
+ "addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:"
+ "allAPFSContainers"
+ "allMedia"
+ "arrayWithArray:"
+ "arrayWithCapacity:"
+ "arrayWithObjects:count:"
+ "boolValue"
+ "children"
+ "class"
+ "com.apple.IOKit"
+ "com.apple.MobileSoftwareUpdate"
+ "com.apple.os.update-"
+ "compare:"
+ "componentsSeparatedByString:"
+ "container"
+ "content"
+ "contentTypeToSubclassMap"
+ "contentTypesForPartitionMedia"
+ "copy"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "create snapshot operation failed: %d %s"
+ "createSnapshot:error:"
+ "dealloc"
+ "defaultMountPointGivenRole:"
+ "defaultVolumeNameGivenRole:"
+ "deleteSnapshots:waitForDeletionFor:error:"
+ "deleteVolumeWithError:"
+ "description"
+ "devNodePath"
+ "deviceModel"
+ "diagsContainer"
+ "dictionary"
+ "dictionaryWithCapacity:"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObjects:forKeys:count:"
+ "eraseVolumeWithError:"
+ "errorWithDomain:code:userInfo:"
+ "failed"
+ "fileSystemRepresentation"
+ "firstObject"
+ "getBoolPropertyWithName:"
+ "getPropertyWithName:"
+ "getStringPropertyWithName:"
+ "graftSecureAssetsFromLastBootSession"
+ "hasEmbeddedDeviceTypeRoot"
+ "hasPrefix:"
+ "hasSuffix:"
+ "i16@0:8"
+ "init"
+ "initWithBytes:length:encoding:"
+ "initWithIOMediaObject:"
+ "initWithLogger:"
+ "initialize"
+ "intValue"
+ "ioMedia"
+ "isCaseSenstive"
+ "isEmbeddedDeviceTypeRoot"
+ "isEncrypted"
+ "isEqual:"
+ "isEqualToString:"
+ "isFilevaultEncrypted"
+ "isInternal"
+ "isJournaled"
+ "isKindOfClass:"
+ "isMounted"
+ "isPrimaryMedia"
+ "isReadOnly"
+ "isWhole"
+ "kern.bootargs"
+ "lastObject"
+ "length"
+ "libpartition2"
+ "liveMediaForSnapshotAtPath:"
+ "lp-lpnh"
+ "mediaForBSDNameOrDeviceNode:"
+ "mediaForPath:"
+ "mediaForPath:isSnapshot:"
+ "mediaForPath:snapshotName:"
+ "mediaForUUID:"
+ "mediaOfCorrectTypeGivenIOMedia:"
+ "mediaUUID"
+ "mountAtPath:error:"
+ "mountAtPath:options:error:"
+ "mountAtTemporaryPathWithError:"
+ "mountAtTemporaryPathWithOptions:error:"
+ "mountPoint"
+ "mountWithError:"
+ "mount_apfs %@ returned %d, retrying (%d)"
+ "mount_apfs returned : %d"
+ "name"
+ "no"
+ "nobrowse"
+ "numberWithBool:"
+ "numberWithInt:"
+ "numberWithLongLong:"
+ "numberWithUnsignedLongLong:"
+ "numberWithUnsignedShort:"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "pairedVolume"
+ "parent"
+ "physicalStores"
+ "pipe failed while preparing to execute %s: %s"
+ "posix_spawn %s failed: %s"
+ "prebootVolume"
+ "primaryMedia"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "q24@?0@8@16"
+ "rangeOfString:options:"
+ "rdonly"
+ "recoveryVolume"
+ "removeAllObjects"
+ "rename snapshot operation failed: %d %s"
+ "renameSnapshot:to:error:"
+ "revert snapshot operation failed: %d %s"
+ "revertToSnapshot:error:"
+ "revertToSnapshot:options:error:"
+ "role"
+ "rootToSnapshot:error:"
+ "s"
+ "setIoMedia:"
+ "setName:withError:"
+ "setObject:forKey:"
+ "setObject:forKeyedSubscript:"
+ "setRole:withError:"
+ "snapshotInfoWithError:"
+ "snapshotMountPoints"
+ "snapshotNameForMediaForPath:"
+ "snapshotsWithError:"
+ "sortUsingComparator:"
+ "sortedArrayUsingComparator:"
+ "storageMedium"
+ "stringWithCString:encoding:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "succeeded"
+ "supportedContentTypes"
+ "unmountAllWithError:"
+ "unmountWithError:"
+ "unmountWithOptions:error:"
+ "updateVolume"
+ "v12@?0I8"
+ "v16@0:8"
+ "v20@0:8I16"
+ "v20@0:8i16"
+ "v24@0:8@16"
+ "v8@?0"
+ "vendorName"
+ "volumeGroupUUID"
+ "volumes"
+ "volumesWithRole:"
+ "w+"
+ "waitForBlockStorage"
+ "waitForIOMediaWithDevNode:"
+ "waitpid failed for %s: %s"
+ "wholeMediaForMedia"
+ "xART"
+ "yes"

```

## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`

```diff

-737.80.2.0.0
-  __TEXT.__text: 0x1cbc8
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x1f64
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0xf87
-  __TEXT.__oslogstring: 0x1415
-  __TEXT.__gcc_except_tab: 0xcf4
-  __TEXT.__unwind_info: 0x9e0
-  __TEXT.__objc_classname: 0x31c
-  __TEXT.__objc_methname: 0x4261
-  __TEXT.__objc_methtype: 0x2a22
-  __TEXT.__objc_stubs: 0x27a0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0xda8
-  __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x88
+737.100.107.0.0
+  __TEXT.__text: 0x1b270
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x1bb4
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0xdf7
+  __TEXT.__oslogstring: 0x1433
+  __TEXT.__gcc_except_tab: 0xe30
+  __TEXT.__unwind_info: 0x910
+  __TEXT.__objc_classname: 0x2ee
+  __TEXT.__objc_methname: 0x3f9e
+  __TEXT.__objc_methtype: 0x2861
+  __TEXT.__objc_stubs: 0x2940
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1028
+  __DATA_CONST.__objc_selrefs: 0xf58
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x2a20
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0x720
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x780
+  __AUTH_CONST.__objc_const: 0x24c0
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x1a4
+  __DATA.__data: 0x6b8
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BA42D3D-9594-31EB-ADCF-D2D5297DA851
-  Functions: 771
-  Symbols:   2633
-  CStrings:  1340
+  UUID: CF3A0D2D-38E7-3D7B-B111-09EDC1DF442B
+  Functions: 687
+  Symbols:   2419
+  CStrings:  1247
 
Symbols:
+ +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]
+ +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:].cold.1
+ +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]
+ +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:].cold.1
+ +[FSKitDiskArbHelper DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:]
+ +[FSKitDiskArbHelper getFileProviderID]
+ +[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]
+ +[stolenUSBLocalStorageClient newManager]
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.1
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.10
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.11
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.12
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.13
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.14
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.15
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.16
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.17
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.18
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.2
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.3
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.4
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.5
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.6
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.7
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.8
+ -[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:].cold.9
+ -[LiveFSAppleDouble reclaimAndRemoveFromCache]
+ -[LiveFSAppleDoubleManager AppleDoubleForPurpose:withBaseFile:named:inDirectory:].cold.1
+ -[LiveFSAppleDoubleManager AppleDoubleForPurpose:withBaseFile:named:inDirectory:].cold.2
+ -[LiveFSAppleDoubleManager addToCache:forKey:]
+ -[LiveFSAppleDoubleManager appleDoubleCacheLRUOrder]
+ -[LiveFSAppleDoubleManager appleDoubleCache]
+ -[LiveFSAppleDoubleManager cacheKeyForBaseFile:named:inDirectory:]
+ -[LiveFSAppleDoubleManager clearCache]
+ -[LiveFSAppleDoubleManager clearCache].cold.1
+ -[LiveFSAppleDoubleManager evictLRUIfNeeded]
+ -[LiveFSAppleDoubleManager getAppleDoubleFromCacheWithBaseFile:named:inDirectory:]
+ -[LiveFSAppleDoubleManager getFromCache:]
+ -[LiveFSAppleDoubleManager maxCacheSize]
+ -[LiveFSAppleDoubleManager removeFromCache:]
+ -[LiveFSAppleDoubleManager setAppleDoubleCache:]
+ -[LiveFSAppleDoubleManager setAppleDoubleCacheLRUOrder:]
+ -[LiveFSAppleDoubleManager setMaxCacheSize:]
+ -[LiveFSAppleDoubleManager updateLRUOrder:]
+ -[LiveFSClient setConnection:]
+ -[LiveFSMountClient setConnection:]
+ -[LiveFSServiceConnection connectedToFSKitd]
+ -[LiveFSServiceConnection setConnectedToFSKitd:]
+ -[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]
+ -[stolenUSBLocalStorageClient loadVolumes:ofType:withError:].cold.1
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table127
+ GCC_except_table169
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table75
+ GCC_except_table86
+ GCC_except_table94
+ _FSTaskParameterConstantOptionReadOnly
+ _NSLog
+ _OBJC_CLASS_$_FSAuditToken
+ _OBJC_CLASS_$_FSBlockDeviceResource
+ _OBJC_CLASS_$_FSClient
+ _OBJC_CLASS_$_FSKitConstants
+ _OBJC_CLASS_$_FSKitDiskArbHelper
+ _OBJC_CLASS_$_FSModuleExtension
+ _OBJC_CLASS_$_FSPathURLResource
+ _OBJC_CLASS_$_FSServiceUserClient
+ _OBJC_CLASS_$_FSTaskOption
+ _OBJC_CLASS_$_FSTaskOptionsBundle
+ _OBJC_CLASS_$_FSUserClient
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_stolenUSBLocalStorageClient
+ _OBJC_IVAR_$_LiveFSAppleDouble._emptyResourceFork
+ _OBJC_IVAR_$_LiveFSAppleDoubleManager._appleDoubleCache
+ _OBJC_IVAR_$_LiveFSAppleDoubleManager._appleDoubleCacheLRUOrder
+ _OBJC_IVAR_$_LiveFSAppleDoubleManager._maxCacheSize
+ _OBJC_IVAR_$_LiveFSServiceConnection._connectedToFSKitd
+ _OBJC_METACLASS_$_FSKitDiskArbHelper
+ _OBJC_METACLASS_$_FSServiceUserClient
+ _OBJC_METACLASS_$_FSUserClient
+ _OBJC_METACLASS_$_stolenUSBLocalStorageClient
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ __OBJC_$_CLASS_METHODS_FSKitDiskArbHelper
+ __OBJC_$_CLASS_METHODS_stolenUSBLocalStorageClient
+ __OBJC_$_INSTANCE_METHODS_stolenUSBLocalStorageClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSMounter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LiveFSConnectionCoordination
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FSMounter
+ __OBJC_$_PROTOCOL_REFS_LiveFSMounter
+ __OBJC_CLASS_RO_$_FSKitDiskArbHelper
+ __OBJC_CLASS_RO_$_stolenUSBLocalStorageClient
+ __OBJC_LABEL_PROTOCOL_$_FSMounter
+ __OBJC_METACLASS_RO_$_FSKitDiskArbHelper
+ __OBJC_METACLASS_RO_$_stolenUSBLocalStorageClient
+ __OBJC_PROTOCOL_$_FSMounter
+ ___31-[LiveFSAppleDouble createFile]_block_invoke.105
+ ___31-[LiveFSAppleDouble createFile]_block_invoke_2.107
+ ___33-[LiveFSAppleDouble loadADHeader]_block_invoke.116
+ ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_2.117
+ ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_3.118
+ ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_4.119
+ ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.76
+ ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.76.cold.1
+ ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.78
+ ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.78.cold.1
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke.127
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke.129
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke.131
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_2.128
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_2.130
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_2.132
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_3.133
+ ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_4.134
+ ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.9
+ ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.9.cold.1
+ ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.9.cold.2
+ ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.9.cold.3
+ ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.9.cold.4
+ ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.9.cold.5
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke.135
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke.137
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke_2
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke_2.136
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke_2.138
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke_3
+ ___58-[LiveFSAppleDouble _removeXattrNamed:allowADFileRemoval:]_block_invoke_4
+ ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke
+ ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_2
+ ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_3
+ ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_4
+ ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_5
+ ___60+[FSKitDiskArbHelper waitForPreviousTasksToComplete:client:]_block_invoke_6
+ ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.12
+ ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.17
+ ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.17.cold.1
+ ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.18
+ ___60-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]_block_invoke
+ ___60-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]_block_invoke_2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.148
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.148.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.148.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.148.cold.3
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.153
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.153.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.153.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.154
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.154.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.154.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.156
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.156.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.cold.1
+ ___block_descriptor_148_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
+ ___block_descriptor_40_e8_32r_e33_v36?0i8Q12"NSData"20"NSData"28lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e33_v36?0i8Q12"NSData"20"NSData"28lr40l8s32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSError"8"NSArray"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e109_v108?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60"NSData"64Q72"NSString"80B88"NSData"92"NSData"100lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e30_v28?0i8"NSData"12"NSData"20ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e33_v36?0i8Q12"NSData"20"NSData"28lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e34_v32?0"FSTaskDescription"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40r_e33_v36?0i8Q12"NSData"20"NSData"28lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e30_v28?0i8"NSData"12"NSData"20lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e33_v36?0i8Q12"NSData"20"NSData"28lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r_e33_v36?0i8Q12"NSData"20"NSData"28lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e30_v28?0i8"NSData"12"NSData"20lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e30_v28?0i8"NSData"12"NSData"20lr48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e39_v24?0"FSTaskDescription"8"NSError"16ls32l8r48l8r56l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e109_v108?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60"NSData"64Q72"NSString"80B88"NSData"92"NSData"100ls72l8s32l8s40l8s48l8s56l8s64l8
+ _fs_errorForPOSIXError
+ _fskit_std_log
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$AppleDoubleForPurpose:withBaseFile:named:inDirectory:
+ _objc_msgSend$DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:
+ _objc_msgSend$DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:
+ _objc_msgSend$_removeXattrNamed:allowADFileRemoval:
+ _objc_msgSend$activateVolume:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$addDisk:fileSystemType:reply:
+ _objc_msgSend$addOption:
+ _objc_msgSend$addToCache:forKey:
+ _objc_msgSend$audit_token
+ _objc_msgSend$cacheKeyForBaseFile:named:inDirectory:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$clearCache
+ _objc_msgSend$containsString:
+ _objc_msgSend$currentTasksSync:
+ _objc_msgSend$deactivateVolume:shortName:numericOptions:auditToken:replyHandler:
+ _objc_msgSend$description
+ _objc_msgSend$evictLRUIfNeeded
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$firstObject
+ _objc_msgSend$forgetVolume:withFlags:
+ _objc_msgSend$fskitdIsClient:
+ _objc_msgSend$fskitdLiveFSMachServiceName
+ _objc_msgSend$getFileProviderID
+ _objc_msgSend$getFromCache:
+ _objc_msgSend$getResourceID
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$invalidateFileNodesForConnection:terminateVolume:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$loadResource:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$loadVolumes:ofType:withError:
+ _objc_msgSend$maxCacheSize
+ _objc_msgSend$mountVolume:fileSystem:displayName:provider:domainError:on:how:options:auditToken:
+ _objc_msgSend$newClientForProvider:
+ _objc_msgSend$newConnectionForService:
+ _objc_msgSend$newManager
+ _objc_msgSend$option:value:
+ _objc_msgSend$orderedSet
+ _objc_msgSend$proxyResourceForBSDName:isWritable:
+ _objc_msgSend$purpose
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$reclaimAndRemoveFromCache
+ _objc_msgSend$reclaimFile
+ _objc_msgSend$removeFromCache:
+ _objc_msgSend$secureResourceWithURL:readonly:
+ _objc_msgSend$setMaxCacheSize:
+ _objc_msgSend$setTaskUpdateHandler:replyHandler:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$string
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$taskID
+ _objc_msgSend$taskResource
+ _objc_msgSend$taskState
+ _objc_msgSend$token
+ _objc_msgSend$unloadResource:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$updateLRUOrder:
+ _objc_msgSend$volumeID
+ _objc_msgSend$volumeName
+ _objc_msgSend$waitForPreviousTasksToComplete:client:
- +[LiveFSMachPort newByCopyingPort:]
- +[LiveFSMachPort supportsSecureCoding]
- +[LiveFSMemoryMap newWithPort:address:andSize:]
- +[LiveFSPathHelper helperWithMount:andPath:]
- +[LiveFSSharedMutableBuffer bufferWithCapacity:]
- +[LiveFSSharedMutableBuffer bufferWithLength:]
- +[LiveFSSharedMutableBuffer dataWithCapacity:]
- +[LiveFSSharedMutableBuffer dataWithLength:]
- +[LiveFSSharedMutableBuffer newByCopyingPort:]
- +[LiveFSSharedMutableBuffer supportsSecureCoding]
- +[LiveFSUserClient defaultClient]
- -[LiveFSAppleDouble removeXattrNamed:].cold.1
- -[LiveFSAppleDouble removeXattrNamed:].cold.10
- -[LiveFSAppleDouble removeXattrNamed:].cold.11
- -[LiveFSAppleDouble removeXattrNamed:].cold.12
- -[LiveFSAppleDouble removeXattrNamed:].cold.13
- -[LiveFSAppleDouble removeXattrNamed:].cold.14
- -[LiveFSAppleDouble removeXattrNamed:].cold.15
- -[LiveFSAppleDouble removeXattrNamed:].cold.16
- -[LiveFSAppleDouble removeXattrNamed:].cold.17
- -[LiveFSAppleDouble removeXattrNamed:].cold.18
- -[LiveFSAppleDouble removeXattrNamed:].cold.2
- -[LiveFSAppleDouble removeXattrNamed:].cold.3
- -[LiveFSAppleDouble removeXattrNamed:].cold.4
- -[LiveFSAppleDouble removeXattrNamed:].cold.5
- -[LiveFSAppleDouble removeXattrNamed:].cold.6
- -[LiveFSAppleDouble removeXattrNamed:].cold.7
- -[LiveFSAppleDouble removeXattrNamed:].cold.8
- -[LiveFSAppleDouble removeXattrNamed:].cold.9
- -[LiveFSMachPort classForCoder]
- -[LiveFSMachPort dealloc]
- -[LiveFSMachPort dealloc].cold.1
- -[LiveFSMachPort encodeWithCoder:]
- -[LiveFSMachPort initWithCoder:]
- -[LiveFSMachPort initWithCoder:].cold.1
- -[LiveFSMachPort initWithPort:]
- -[LiveFSMachPort init]
- -[LiveFSMachPort machPort]
- -[LiveFSMemoryMap address]
- -[LiveFSMemoryMap dealloc]
- -[LiveFSMemoryMap dealloc].cold.1
- -[LiveFSMemoryMap initWithPort:address:andSize:]
- -[LiveFSMemoryMap port]
- -[LiveFSMemoryMap setPort:]
- -[LiveFSMemoryMap size]
- -[LiveFSPathHelper .cxx_destruct]
- -[LiveFSPathHelper attributes]
- -[LiveFSPathHelper currentFileHandle]
- -[LiveFSPathHelper dealloc]
- -[LiveFSPathHelper error]
- -[LiveFSPathHelper fileHandle]
- -[LiveFSPathHelper finalizeWithErrno:]
- -[LiveFSPathHelper finalizeWithError:]
- -[LiveFSPathHelper initWithMount:andPath:]
- -[LiveFSPathHelper lookupNextComponent]
- -[LiveFSPathHelper lookupWithCompletionHandler:]
- -[LiveFSPathHelper peekFileHandle]
- -[LiveFSPathHelper popFileHandle]
- -[LiveFSPathHelper processLookupReplyWithResult:item:andAttributes:]
- -[LiveFSPathHelper processReadLinkReplyForLink:withResult:linkString:andAttributes:]
- -[LiveFSPathHelper pushFileHandle:attributes:]
- -[LiveFSPathHelper reclaimItem:withContinuation:]
- -[LiveFSPathHelper resolveSymlink:]
- -[LiveFSPathHelper resolveTrailingSymlink]
- -[LiveFSPathHelper setResolveTrailingSymlink:]
- -[LiveFSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:]
- -[LiveFSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:].cold.1
- -[LiveFSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:].cold.2
- -[LiveFSServiceUserClient closeFileDescriptorForKernel:]
- -[LiveFSServiceUserClient createVolumePort]
- -[LiveFSServiceUserClient flushMeta:wait:]
- -[LiveFSServiceUserClient flushMeta:wait:].cold.1
- -[LiveFSServiceUserClient flushMeta:wait:].cold.2
- -[LiveFSServiceUserClient getVolumePort]
- -[LiveFSServiceUserClient init]
- -[LiveFSServiceUserClient openFileDescriptorForKernel:flags:]
- -[LiveFSServiceUserClient purgeMetaBlocks:ranges:rangesCount:]
- -[LiveFSServiceUserClient purgeMetaBlocks:ranges:rangesCount:].cold.1
- -[LiveFSServiceUserClient purgeMetaBlocks:ranges:rangesCount:].cold.2
- -[LiveFSServiceUserClient readMeta:buffer:offset:length:]
- -[LiveFSServiceUserClient readMeta:buffer:offset:length:].cold.1
- -[LiveFSServiceUserClient readMeta:buffer:offset:length:].cold.2
- -[LiveFSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:]
- -[LiveFSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:].cold.1
- -[LiveFSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:].cold.2
- -[LiveFSServiceUserClient writeMeta:buffer:offset:length:]
- -[LiveFSServiceUserClient writeMeta:buffer:offset:length:].cold.1
- -[LiveFSServiceUserClient writeMeta:buffer:offset:length:].cold.2
- -[LiveFSServiceUserClient writeMetaDelayed:buffer:offset:length:]
- -[LiveFSServiceUserClient writeMetaDelayed:buffer:offset:length:].cold.1
- -[LiveFSServiceUserClient writeMetaDelayed:buffer:offset:length:].cold.2
- -[LiveFSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:]
- -[LiveFSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:].cold.1
- -[LiveFSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:].cold.2
- -[LiveFSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:].cold.3
- -[LiveFSSharedMutableBuffer .cxx_destruct]
- -[LiveFSSharedMutableBuffer bytes]
- -[LiveFSSharedMutableBuffer capacity]
- -[LiveFSSharedMutableBuffer classForCoder]
- -[LiveFSSharedMutableBuffer createDispatchData]
- -[LiveFSSharedMutableBuffer createMappingAt:options:startingAtOffset:forLength:completionHandler:]
- -[LiveFSSharedMutableBuffer createMappingForVMAAt:options:startingAtOffset:forLength:completionHandler:]
- -[LiveFSSharedMutableBuffer dealloc]
- -[LiveFSSharedMutableBuffer dealloc].cold.1
- -[LiveFSSharedMutableBuffer detachBytes]
- -[LiveFSSharedMutableBuffer detachBytes].cold.1
- -[LiveFSSharedMutableBuffer encodeWithCoder:]
- -[LiveFSSharedMutableBuffer ensureMappedIOMD]
- -[LiveFSSharedMutableBuffer ensureMappedMB:]
- -[LiveFSSharedMutableBuffer ensureMappedMB:].cold.1
- -[LiveFSSharedMutableBuffer ensureMapped]
- -[LiveFSSharedMutableBuffer initWithCapacity:]
- -[LiveFSSharedMutableBuffer initWithCapacity:andLength:]
- -[LiveFSSharedMutableBuffer initWithCapacity:andLength:].cold.1
- -[LiveFSSharedMutableBuffer initWithCapacity:andLength:].cold.2
- -[LiveFSSharedMutableBuffer initWithCapacity:andLength:].cold.3
- -[LiveFSSharedMutableBuffer initWithCoder:]
- -[LiveFSSharedMutableBuffer initWithCoder:].cold.1
- -[LiveFSSharedMutableBuffer initWithCoder:].cold.2
- -[LiveFSSharedMutableBuffer initWithLength:]
- -[LiveFSSharedMutableBuffer initWithMachPort:capacity:length:wrapsIOWMD:]
- -[LiveFSSharedMutableBuffer isIOWMD]
- -[LiveFSSharedMutableBuffer length]
- -[LiveFSSharedMutableBuffer memMap]
- -[LiveFSSharedMutableBuffer mp]
- -[LiveFSSharedMutableBuffer mutableBytes]
- -[LiveFSSharedMutableBuffer setCapacity:]
- -[LiveFSSharedMutableBuffer setIsIOWMD:]
- -[LiveFSSharedMutableBuffer setLength:]
- -[LiveFSSharedMutableBuffer setMemMap:]
- -[LiveFSSharedMutableBuffer setMp:]
- -[LiveFSSharedMutableBuffer setVma:]
- -[LiveFSSharedMutableBuffer vma]
- -[LiveFSUserClient callStructMethod:inStruct:inSize:outStruct:outStructSize:]
- -[LiveFSUserClient checkUserClientPort]
- -[LiveFSUserClient configureUserClient:pid:pidversion:supportBlockResource:]
- -[LiveFSUserClient configureUserClient:pid:pidversion:supportBlockResource:].cold.1
- -[LiveFSUserClient dealloc]
- -[LiveFSUserClient getConnPort]
- -[LiveFSUserClient getUserClientPortForService:]
- -[LiveFSUserClient getUserClientPort]
- -[LiveFSUserClient init]
- -[LiveFSUserClient setMainMachPort:forDomain:]
- GCC_except_table102
- GCC_except_table105
- GCC_except_table108
- GCC_except_table152
- GCC_except_table26
- GCC_except_table33
- GCC_except_table37
- GCC_except_table45
- GCC_except_table50
- GCC_except_table53
- GCC_except_table73
- GCC_except_table76
- GCC_except_table81
- GCC_except_table84
- GCC_except_table90
- GCC_except_table99
- _IOConnectCallStructMethod
- _IOConnectSetNotificationPort
- _IOServiceClose
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOServiceOpen
- _NSInvalidArgumentException
- _OBJC_CLASS_$_LiveFSMachPort
- _OBJC_CLASS_$_LiveFSMemoryMap
- _OBJC_CLASS_$_LiveFSPathHelper
- _OBJC_CLASS_$_LiveFSSharedMutableBuffer
- _OBJC_CLASS_$_NSXPCCoder
- _OBJC_IVAR_$_LiveFSMachPort._machPort
- _OBJC_IVAR_$_LiveFSMemoryMap._address
- _OBJC_IVAR_$_LiveFSMemoryMap._port
- _OBJC_IVAR_$_LiveFSMemoryMap._size
- _OBJC_IVAR_$_LiveFSPathHelper._attributes
- _OBJC_IVAR_$_LiveFSPathHelper._error
- _OBJC_IVAR_$_LiveFSPathHelper.attributeStack
- _OBJC_IVAR_$_LiveFSPathHelper.completionHandler
- _OBJC_IVAR_$_LiveFSPathHelper.currentPathComponent
- _OBJC_IVAR_$_LiveFSPathHelper.fileHandleStack
- _OBJC_IVAR_$_LiveFSPathHelper.fileHandleStackCount
- _OBJC_IVAR_$_LiveFSPathHelper.lookupCompleted
- _OBJC_IVAR_$_LiveFSPathHelper.lookupInProgress
- _OBJC_IVAR_$_LiveFSPathHelper.numberOfSymlinks
- _OBJC_IVAR_$_LiveFSPathHelper.ourMount
- _OBJC_IVAR_$_LiveFSPathHelper.ourQueue
- _OBJC_IVAR_$_LiveFSPathHelper.pathComponents
- _OBJC_IVAR_$_LiveFSPathHelper.resolveTrailingSymlink
- _OBJC_IVAR_$_LiveFSPathHelper.rootFileHandle
- _OBJC_IVAR_$_LiveFSServiceUserClient.volumePort
- _OBJC_IVAR_$_LiveFSSharedMutableBuffer._capacity
- _OBJC_IVAR_$_LiveFSSharedMutableBuffer._isIOWMD
- _OBJC_IVAR_$_LiveFSSharedMutableBuffer._length
- _OBJC_IVAR_$_LiveFSSharedMutableBuffer._memMap
- _OBJC_IVAR_$_LiveFSSharedMutableBuffer._mp
- _OBJC_IVAR_$_LiveFSSharedMutableBuffer._vma
- _OBJC_IVAR_$_LiveFSUserClient.ourPort
- _OBJC_METACLASS_$_LiveFSMachPort
- _OBJC_METACLASS_$_LiveFSMemoryMap
- _OBJC_METACLASS_$_LiveFSPathHelper
- _OBJC_METACLASS_$_LiveFSSharedMutableBuffer
- __OBJC_$_CLASS_METHODS_LiveFSMachPort
- __OBJC_$_CLASS_METHODS_LiveFSMemoryMap
- __OBJC_$_CLASS_METHODS_LiveFSPathHelper
- __OBJC_$_CLASS_METHODS_LiveFSSharedMutableBuffer
- __OBJC_$_CLASS_METHODS_LiveFSUserClient
- __OBJC_$_CLASS_PROP_LIST_LiveFSMachPort
- __OBJC_$_CLASS_PROP_LIST_LiveFSSharedMutableBuffer
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
- __OBJC_$_INSTANCE_METHODS_LiveFSMachPort
- __OBJC_$_INSTANCE_METHODS_LiveFSMemoryMap
- __OBJC_$_INSTANCE_METHODS_LiveFSPathHelper
- __OBJC_$_INSTANCE_METHODS_LiveFSServiceUserClient
- __OBJC_$_INSTANCE_METHODS_LiveFSSharedMutableBuffer
- __OBJC_$_INSTANCE_METHODS_LiveFSUserClient
- __OBJC_$_INSTANCE_VARIABLES_LiveFSMachPort
- __OBJC_$_INSTANCE_VARIABLES_LiveFSMemoryMap
- __OBJC_$_INSTANCE_VARIABLES_LiveFSPathHelper
- __OBJC_$_INSTANCE_VARIABLES_LiveFSServiceUserClient
- __OBJC_$_INSTANCE_VARIABLES_LiveFSSharedMutableBuffer
- __OBJC_$_INSTANCE_VARIABLES_LiveFSUserClient
- __OBJC_$_PROP_LIST_LiveFSMachPort
- __OBJC_$_PROP_LIST_LiveFSMemoryMap
- __OBJC_$_PROP_LIST_LiveFSPathHelper
- __OBJC_$_PROP_LIST_LiveFSSharedMutableBuffer
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LiveFSMounter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_LiveFSMounter
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding
- __OBJC_CLASS_PROTOCOLS_$_LiveFSMachPort
- __OBJC_CLASS_PROTOCOLS_$_LiveFSSharedMutableBuffer
- __OBJC_CLASS_RO_$_LiveFSMachPort
- __OBJC_CLASS_RO_$_LiveFSMemoryMap
- __OBJC_CLASS_RO_$_LiveFSPathHelper
- __OBJC_CLASS_RO_$_LiveFSSharedMutableBuffer
- __OBJC_LABEL_PROTOCOL_$_NSCoding
- __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
- __OBJC_METACLASS_RO_$_LiveFSMachPort
- __OBJC_METACLASS_RO_$_LiveFSMemoryMap
- __OBJC_METACLASS_RO_$_LiveFSPathHelper
- __OBJC_METACLASS_RO_$_LiveFSSharedMutableBuffer
- __OBJC_PROTOCOL_$_NSCoding
- __OBJC_PROTOCOL_$_NSSecureCoding
- ___27-[LiveFSPathHelper dealloc]_block_invoke
- ___30-[LiveFSPathHelper attributes]_block_invoke
- ___30-[LiveFSPathHelper attributes]_block_invoke_2
- ___31-[LiveFSAppleDouble createFile]_block_invoke.74
- ___31-[LiveFSAppleDouble createFile]_block_invoke_2.76
- ___33-[LiveFSAppleDouble loadADHeader]_block_invoke.84
- ___33-[LiveFSAppleDouble loadADHeader]_block_invoke.86
- ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_2.85
- ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_2.87
- ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_3.88
- ___33-[LiveFSAppleDouble loadADHeader]_block_invoke_4.89
- ___35-[LiveFSPathHelper resolveSymlink:]_block_invoke
- ___35-[LiveFSPathHelper resolveSymlink:]_block_invoke_2
- ___37-[LiveFSVolumeClient updatesDoneFor:]_block_invoke
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke.105
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke.107
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke_2
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke_2.106
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke_2.108
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke_3
- ___38-[LiveFSAppleDouble removeXattrNamed:]_block_invoke_4
- ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.75
- ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.75.cold.1
- ___39-[LiveFSPathHelper lookupNextComponent]_block_invoke
- ___39-[LiveFSPathHelper lookupNextComponent]_block_invoke_2
- ___39-[LiveFSPathHelper lookupNextComponent]_block_invoke_3
- ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.77
- ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.77.cold.1
- ___45-[LiveFSSharedMutableBuffer ensureMappedIOMD]_block_invoke
- ___47-[LiveFSSharedMutableBuffer createDispatchData]_block_invoke
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke.101
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke.97
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke.99
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_2.100
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_2.102
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_2.98
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_3.103
- ___48-[LiveFSAppleDouble setValue:forXattrNamed:how:]_block_invoke_4.104
- ___48-[LiveFSPathHelper lookupWithCompletionHandler:]_block_invoke
- ___48-[LiveFSPathHelper lookupWithCompletionHandler:]_block_invoke_2
- ___49-[LiveFSPathHelper reclaimItem:withContinuation:]_block_invoke
- ___49-[LiveFSPathHelper reclaimItem:withContinuation:]_block_invoke_2
- ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.7
- ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.7.cold.1
- ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.7.cold.2
- ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.7.cold.3
- ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.7.cold.4
- ___57-[LiveFSAppleDoubleManager enumerateDirectory:intoArray:]_block_invoke.7.cold.5
- ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.10
- ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.13
- ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.15.cold.1
- ___60-[LiveFSAppleDoubleManager scrubDirectoryNamed:inDirectory:]_block_invoke.16
- ___68-[LiveFSPathHelper processLookupReplyWithResult:item:andAttributes:]_block_invoke
- ___84-[LiveFSPathHelper processReadLinkReplyForLink:withResult:linkString:andAttributes:]_block_invoke
- ___block_descriptor_32_e19_v20?0i8"NSData"12l
- ___block_descriptor_32_e53_v32?0"NSString"8"<LiveFSVolumeClientUpdate>"16^B24l
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32r_e22_v28?0i8Q12"NSData"20lr32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e94_v72?0i8i12"NSString"16"NSData"24"NSString"32"NSData"40"NSString"48"NSData"56"NSData"64ls32l8
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32bs40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e19_v20?0i8"NSData"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e28_v20?0i8"LiveFSMemoryMap"12lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e85_v92?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60Q64"NSString"72B80"NSData"84lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e32_v28?0i8"NSString"12"NSData"20ls32l8s40l8
- ___block_descriptor_52_e8_32s40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e22_v28?0i8Q12"NSData"20lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e19_v20?0i8"NSData"12lr48l8s32l8s40l8
- ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e19_v20?0i8"NSData"12lr48l8r56l8s32l8s40l8
- ___block_descriptor_68_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e85_v92?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60Q64"NSString"72B80"NSData"84ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.69
- ___memcpy_chk
- ___strlcpy_chk
- __xpc_type_mach_send
- _dispatch_data_create
- _gDefaultClient
- _kIOMasterPortDefault
- _mach_make_memory_entry_64
- _mach_port_deallocate
- _mach_port_mod_refs
- _mach_task_self_
- _mach_vm_map
- _objc_alloc_init
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$address
- _objc_msgSend$callStructMethod:inStruct:inSize:outStruct:outStructSize:
- _objc_msgSend$checkUserClientPort
- _objc_msgSend$createMappingAt:options:startingAtOffset:forLength:completionHandler:
- _objc_msgSend$createMappingForVMAAt:options:startingAtOffset:forLength:completionHandler:
- _objc_msgSend$createVolumePort
- _objc_msgSend$currentFileHandle
- _objc_msgSend$decodeBoolForKey:
- _objc_msgSend$decodeIntegerForKey:
- _objc_msgSend$decodeXPCObjectOfType:forKey:
- _objc_msgSend$defaultClient
- _objc_msgSend$encodeBool:forKey:
- _objc_msgSend$encodeInteger:forKey:
- _objc_msgSend$encodeXPCObject:forKey:
- _objc_msgSend$ensureMapped
- _objc_msgSend$ensureMappedIOMD
- _objc_msgSend$ensureMappedMB:
- _objc_msgSend$finalizeWithErrno:
- _objc_msgSend$finalizeWithError:
- _objc_msgSend$getConnPort
- _objc_msgSend$getRootFileHandleWithError:
- _objc_msgSend$getUserClientPort
- _objc_msgSend$getUserClientPortForService:
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$initWithCapacity:andLength:
- _objc_msgSend$initWithLength:
- _objc_msgSend$initWithMachPort:capacity:length:wrapsIOWMD:
- _objc_msgSend$initWithMount:andPath:
- _objc_msgSend$initWithPort:
- _objc_msgSend$initWithPort:address:andSize:
- _objc_msgSend$lengthOfBytesUsingEncoding:
- _objc_msgSend$lookupIn:name:usingFlags:requestID:reply:
- _objc_msgSend$lookupNextComponent
- _objc_msgSend$newWithPort:address:andSize:
- _objc_msgSend$orderedSetWithCapacity:
- _objc_msgSend$pathComponents
- _objc_msgSend$peekFileHandle
- _objc_msgSend$popFileHandle
- _objc_msgSend$processLookupReplyWithResult:item:andAttributes:
- _objc_msgSend$processReadLinkReplyForLink:withResult:linkString:andAttributes:
- _objc_msgSend$pushFileHandle:attributes:
- _objc_msgSend$reclaim:requestID:reply:
- _objc_msgSend$reclaimItem:withContinuation:
- _objc_msgSend$removeXattrNamed:
- _objc_msgSend$resolveSymlink:
- _objc_msgSend$size
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x9
- _vm_allocate
- _vm_deallocate
- _xpc_mach_send_copy_right
- _xpc_mach_send_create
CStrings:
+ "%@ loadVolumes failed with %@"
+ "%@ mount failed with %@"
+ "%@ mounting with name %@, error %@, and how 0x%x."
+ "%@-%@-%@"
+ "%@: got 2 different names from probe and userfs: p->%@  u->%@"
+ "%s: %@ failed to activate volume (%@)"
+ "%s: %@ failed to deactivateVolume (%@) error (%@)"
+ "%s: %@ failed to load resource (%@)"
+ "%s: %@ failed to unloadResource (%@) error (%@)"
+ "%s: %@ mount failed with %@"
+ "%s: Activating volumeName (%@) volumeID (%@) with activateOptions (%@)"
+ "%s: Mounted %@ successfully."
+ "%s: connection id (%llu) %s from fskitd"
+ "%s:done activating volume (%@)"
+ "%s:done deactivating volume (%@)"
+ "%s:error:%@"
+ "%s:finish:%@:%@:%@"
+ "%s:start:%@:%@"
+ "%s:start:fsShortName(%@):deviceName(%@):mountPoint(%@):volumeName(%@):mountOptionString(%@)"
+ "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]"
+ "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke"
+ "-[LiveFSServiceConnection initForMount:connection:error:]"
+ "-[stolenUSBLocalStorageClient loadVolumes:ofType:withError:]"
+ "<LIFSAD:%p>: [[%@]:[%@][%@]]: ok:%d, err:%d, open:%d, p:%d, ro:%d, emptyfi:%d, emptyrsrc:%d, wcf:%d"
+ "ADM: Cache cleared"
+ "ADM: init: AD file is cached but it was reclaimed (fileHandle = nil)"
+ "ADM: init: AD file is cached but new purpose (%u) != old purpose (%u)"
+ "DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
+ "DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
+ "DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:"
+ "Error setting up update handler: '%s'"
+ "FSKitDiskArbHelper"
+ "FSMounter"
+ "Invalidating file nodes for connection with terminate volume as (%d)"
+ "Mounted %@ successfully."
+ "T@\"NSMutableDictionary\",&,V_appleDoubleCache"
+ "T@\"NSMutableOrderedSet\",&,V_appleDoubleCacheLRUOrder"
+ "TB,V_connectedToFSKitd"
+ "TQ,V_maxCacheSize"
+ "UUID"
+ "Untitled"
+ "_"
+ "_appleDoubleCache"
+ "_appleDoubleCacheLRUOrder"
+ "_connectedToFSKitd"
+ "_emptyResourceFork"
+ "_fskit"
+ "_maxCacheSize"
+ "_removeXattrNamed:allowADFileRemoval:"
+ "activateVolume:shortName:options:auditToken:replyHandler:"
+ "addOption:"
+ "addToCache:forKey:"
+ "appleDoubleCache"
+ "appleDoubleCacheLRUOrder"
+ "audit_token"
+ "cacheKeyForBaseFile:named:inDirectory:"
+ "characterSetWithCharactersInString:"
+ "clearCache"
+ "connectedToFSKitd"
+ "containsString:"
+ "currentTasksSync:"
+ "deactivateVolume:shortName:numericOptions:auditToken:replyHandler:"
+ "errorForDomain"
+ "evictLRUIfNeeded"
+ "fileURLWithPath:"
+ "firstObject"
+ "fskitdIsClient:"
+ "fskitdLiveFSMachServiceName"
+ "getAppleDoubleFromCacheWithBaseFile:named:inDirectory:"
+ "getFileProviderID"
+ "getFromCache:"
+ "getResourceID"
+ "hasSuffix:"
+ "how"
+ "i28@0:8@16B24"
+ "i56@0:8@16@24@32@40@48"
+ "i88@0:8@16@24@32@40{?=[8I]}48@80"
+ "intValue"
+ "integerValue"
+ "invalidateFileNodesForConnection:terminateVolume:"
+ "is"
+ "isn't"
+ "loadResource:shortName:options:auditToken:replyHandler:"
+ "loadVolumes:ofType:withError:"
+ "machp://%@"
+ "machp://com.apple.filesystems.localLiveFiles"
+ "maxCacheSize"
+ "newManager"
+ "o"
+ "option:value:"
+ "orderedSet"
+ "passthroughfs"
+ "proxyResourceForBSDName:isWritable:"
+ "rangeOfCharacterFromSet:"
+ "reclaimAndRemoveFromCache"
+ "removeFromCache:"
+ "secureResourceWithURL:readonly:"
+ "setAppleDoubleCache:"
+ "setAppleDoubleCacheLRUOrder:"
+ "setConnectedToFSKitd:"
+ "setConnection:"
+ "setMaxCacheSize:"
+ "setTaskUpdateHandler:replyHandler:"
+ "sharedInstance"
+ "stolenUSBLocalStorageClient"
+ "string"
+ "substringToIndex:"
+ "taskID"
+ "taskResource"
+ "taskState"
+ "token"
+ "unload for volume %@ failed with %@"
+ "unloadResource:shortName:options:auditToken:replyHandler:"
+ "unsupported error code for domain: %ld"
+ "updateLRUOrder:"
+ "v108@?0i8@\"NSData\"12Q20@\"NSData\"28Q36Q44@\"NSString\"52B60@\"NSData\"64Q72@\"NSString\"80B88@\"NSData\"92@\"NSData\"100"
+ "v24@?0@\"FSTaskDescription\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v28@0:8Q16B24"
+ "v28@?0i8@\"NSData\"12@\"NSData\"20"
+ "v32@?0@\"FSTaskDescription\"8Q16^B24"
+ "v32@?0@\"FSVolumeDescription\"8Q16^B24"
+ "v36@?0i8Q12@\"NSData\"20@\"NSData\"28"
+ "v40@0:8@\"NSString\"16Q24@?<v@?i@\"FSMachPort\">32"
+ "v44@0:8@\"NSString\"16^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}24I32@\"NSDictionary\"36"
+ "v44@0:8@16^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}24I32@36"
+ "v48@0:8@\"NSString\"16Q24Q32@?<v@?i@\"FSMachPort\">40"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"FSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"FSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24Q32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
+ "v64@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
+ "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\">56"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40I48Q52@?<v@?i@\"NSData\"Q@\"NSData\"QQ@\"NSString\"B@\"NSData\"Q@\"NSString\"B@\"NSData\"@\"NSData\">60"
+ "v72@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48Q56@?<v@?iqQ>64"
+ "v84@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">76"
+ "volumeID"
+ "waitForPreviousTasksToComplete:client:"
+ "{_FSFileAttributes=\"__fa_rsvd0\"Q\"fa_validmask\"Q\"fa_seqno\"Q\"fa_type\"I\"fa_mode\"I\"fa_nlink\"I\"fa_uid\"I\"fa_gid\"I\"fa_bsd_flags\"I\"fa_size\"Q\"fa_allocsize\"Q\"fa_fileid\"Q\"fa_parentid\"Q\"fa_atime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_mtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_ctime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_birthtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_backuptime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_addedtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_int_flags\"I\"_pad0\"I}"
- "%s: didn't get the wrapper"
- "%s: failed with error %x"
- "%s: invalid argument given"
- "%s: invalid subblock range"
- "%s: mach_make_memory_entry_64 gave us size %lu instead of %lu"
- "%s: mach_make_memory_entry_64 returned %x"
- "%s: supplied length is greater than supplied capacity"
- "%s: vm_allocate returned %x"
- "-[LiveFSMachPort initWithCoder:]"
- "-[LiveFSServiceUserClient clearMetaBlocks:ranges:rangesCount:wait:]"
- "-[LiveFSServiceUserClient flushMeta:wait:]"
- "-[LiveFSServiceUserClient purgeMetaBlocks:ranges:rangesCount:]"
- "-[LiveFSServiceUserClient readMeta:buffer:offset:length:]"
- "-[LiveFSServiceUserClient readMetaWithRA:buffer:offset:length:raList:raListCount:]"
- "-[LiveFSServiceUserClient writeMeta:buffer:offset:length:]"
- "-[LiveFSServiceUserClient writeMetaDelayed:buffer:offset:length:]"
- "-[LiveFSServiceUserClient writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:]"
- "-[LiveFSSharedMutableBuffer ensureMappedMB:]"
- "-[LiveFSSharedMutableBuffer initWithCapacity:andLength:]"
- "-[LiveFSSharedMutableBuffer initWithCoder:]"
- ".."
- "/"
- "<LIFSAD:%p>: [[%@]:[%@][%@]]: ok:%d, err:%d, open:%d, p:%d, ro:%d, emptyfi:%d, wcf:%d"
- "@\"<LiveFSVolumeCore>\""
- "@\"LiveFSMemoryMap\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSError\""
- "@20@0:8I16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8Q16"
- "@36@0:8I16Q20Q28"
- "@40@0:8I16Q20Q28B36"
- "A"
- "B24@0:8Q16"
- "Didn't find matching client"
- "LiveFSMachPort"
- "LiveFSMachPort: dealloc: error %d"
- "LiveFSMemoryMap"
- "LiveFSMemoryMap: dealloc: error %d"
- "LiveFSPathHelper"
- "LiveFSSMBuff.cap"
- "LiveFSSMBuff.isIOWMD"
- "LiveFSSMBuff.len"
- "LiveFSSMBuff.mp"
- "LiveFSSharedMutableBuffer"
- "LiveFSSharedMutableBuffer: dealloc: error %d"
- "LiveFSmp.mp"
- "NSCoding"
- "NSSecureCoding"
- "No matching dict"
- "T@\"LiveFSMemoryMap\",&,V_memMap"
- "T@\"NSData\",R"
- "T@\"NSError\",R,V_error"
- "T@\"NSString\",R"
- "TB,R"
- "TB,V_isIOWMD"
- "TI,R,V_machPort"
- "TI,V_mp"
- "TI,V_port"
- "TQ"
- "TQ,R,V_address"
- "TQ,R,V_size"
- "TQ,V_capacity"
- "TQ,V_vma"
- "This object may only be decoded by an NSXPCCoder."
- "This object may only be encoded by an NSXPCCoder."
- "_address"
- "_attributes"
- "_capacity"
- "_error"
- "_isIOWMD"
- "_length"
- "_machPort"
- "_memMap"
- "_mp"
- "_port"
- "_size"
- "_vma"
- "addObjectsFromArray:"
- "address"
- "attributeStack"
- "bufferWithCapacity:"
- "bufferWithLength:"
- "callStructMethod:inStruct:inSize:outStruct:outStructSize:"
- "capacity"
- "checkUserClientPort"
- "classForCoder"
- "clearMetaBlocks:ranges:rangesCount:wait:"
- "clear_meta_blocks returned %d"
- "closeFileDescriptorForKernel:"
- "close_kernel_fd returned %d"
- "com.apple.LiveFSPathHelper.lookup"
- "com_apple_filesystems_lifs"
- "completionHandler"
- "configureUserClient returned %d"
- "configureUserClient:pid:pidversion:supportBlockResource:"
- "createMappingAt:options:startingAtOffset:forLength:completionHandler:"
- "createMappingForVMAAt:options:startingAtOffset:forLength:completionHandler:"
- "createVolumePort"
- "create_volume_port returned %d"
- "currentFileHandle"
- "currentPathComponent"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeXPCObjectOfType:forKey:"
- "defaultClient"
- "detachBytes"
- "detatchBytes called on LiveFSSharedMutableBuffer wrapping an IOMD, which won't work well"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeWithCoder:"
- "encodeXPCObject:forKey:"
- "ensureMapped"
- "ensureMappedIOMD"
- "ensureMappedMB:"
- "error"
- "fileHandleStack"
- "fileHandleStackCount"
- "finalizeWithErrno:"
- "finalizeWithError:"
- "flushMeta:wait:"
- "flush_meta returned %d"
- "get client returned %x"
- "getConnPort"
- "getUserClientPort"
- "getUserClientPortForService:"
- "getVolumePort"
- "helperWithMount:andPath:"
- "i20@0:8i16"
- "i24@0:8i16i20"
- "i24@0:8r*16"
- "i28@0:8I16@20"
- "i32@0:8I16i20i24i28"
- "i32@0:8i16^{FSKit_Meta_BlockRange_s=qII}20i28"
- "i36@0:8i16^{FSKit_Meta_BlockRange_s=qII}20i28i32"
- "i44@0:8i16^v20q28Q36"
- "i44@0:8i16r^v20q28Q36"
- "i52@0:8I16r^v20Q28^v36^Q44"
- "i56@0:8i16^v20q28Q36^{FSKit_Meta_Readahead_s=qQ}44i52"
- "i60@0:8i16q20Q28r^v36q44Q52"
- "initWithCapacity:"
- "initWithCapacity:andLength:"
- "initWithCoder:"
- "initWithLength:"
- "initWithMachPort:capacity:length:wrapsIOWMD:"
- "initWithMount:andPath:"
- "initWithPort:"
- "initWithPort:address:andSize:"
- "isIOWMD"
- "lengthOfBytesUsingEncoding:"
- "lookupCompleted"
- "lookupInProgress"
- "lookupNextComponent"
- "lookupWithCompletionHandler:"
- "machPort"
- "machPortForKernelMountUse"
- "mach_port_mod_refs failed, returned %d"
- "machp://com.apple.filesystems.fskitd"
- "memMap"
- "mp"
- "newByCopyingPort:"
- "newWithPort:address:andSize:"
- "numberOfSymlinks"
- "openFileDescriptorForKernel:flags:"
- "open_kernel_fd returned %d"
- "orderedSetWithCapacity:"
- "ourMount"
- "ourPort"
- "ourQueue"
- "pathComponents"
- "peekFileHandle"
- "popFileHandle"
- "port"
- "processLookupReplyWithResult:item:andAttributes:"
- "processReadLinkReplyForLink:withResult:linkString:andAttributes:"
- "purgeMetaBlocks:ranges:rangesCount:"
- "purge_meta_blocks returned %d"
- "pushFileHandle:attributes:"
- "r^v16@0:8"
- "readMeta:buffer:offset:length:"
- "readMetaWithRA:buffer:offset:length:raList:raListCount:"
- "read_meta returned %d"
- "read_meta_with_ra returned %d"
- "reclaimItem:withContinuation:"
- "resolveSymlink:"
- "resolveTrailingSymlink"
- "rootFileHandle"
- "set client domain returned %x"
- "set notification port returned %x"
- "setCapacity:"
- "setIsIOWMD:"
- "setLength:"
- "setMainMachPort:forDomain:"
- "setMemMap:"
- "setMp:"
- "setPort:"
- "setResolveTrailingSymlink:"
- "setVma:"
- "size"
- "supportsSecureCoding"
- "switchToFSKit:"
- "v20@?0i8@\"LiveFSMemoryMap\"12"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v28@?0i8@\"NSString\"12@\"NSData\"20"
- "v28@?0i8Q12@\"NSData\"20"
- "v32@?0@\"NSString\"8@\"<LiveFSVolumeClientUpdate>\"16^B24"
- "v36@0:8i16@20@28"
- "v40@0:8@\"NSString\"16Q24@?<v@?i@\"LiveFSMachPort\">32"
- "v44@0:8@\"NSString\"16^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}24I32@\"NSDictionary\"36"
- "v44@0:8@16^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}24I32@36"
- "v44@0:8@16i24@28@36"
- "v48@0:8@\"NSString\"16Q24Q32@?<v@?i@\"LiveFSMachPort\">40"
- "v52@0:8Q16I24Q28Q36@?44"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ>48"
- "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24Q32Q40@?<v@?i@\"NSData\">48"
- "v64@0:8@\"NSString\"16@\"LiveFSSharedMutableBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i>56"
- "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40I48Q52@?<v@?i@\"NSData\"Q@\"NSData\"QQ@\"NSString\"BQ@\"NSString\"B@\"NSData\">60"
- "v72@0:8@\"NSString\"16@\"LiveFSSharedMutableBuffer\"24Q32Q40Q48Q56@?<v@?iqQ>64"
- "v84@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">76"
- "v92@?0i8@\"NSData\"12Q20@\"NSData\"28Q36Q44@\"NSString\"52B60Q64@\"NSString\"72B80@\"NSData\"84"
- "vma"
- "volumePort"
- "writeMeta:buffer:offset:length:"
- "writeMetaDelayed:buffer:offset:length:"
- "writeMetaSubBlock:offset:length:subBlockBuffer:subBlockOffset:subBlockLength:"
- "write_meta returned %d"
- "write_meta_delayed returned %d"
- "write_meta_subblock returned %d"
- "{_LIFileAttributes=\"__fa_rsvd0\"Q\"fa_validmask\"Q\"fa_seqno\"Q\"fa_type\"I\"fa_mode\"I\"fa_nlink\"I\"fa_uid\"I\"fa_gid\"I\"fa_bsd_flags\"I\"fa_size\"Q\"fa_allocsize\"Q\"fa_fileid\"Q\"fa_parentid\"Q\"fa_atime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_mtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_ctime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_birthtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_backuptime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_addedtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_int_flags\"I\"_pad0\"I}"

```

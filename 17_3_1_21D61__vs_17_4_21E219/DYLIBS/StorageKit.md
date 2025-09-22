## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-851.40.2.0.0
-  __TEXT.__text: 0x255f4
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x26d4
-  __TEXT.__cstring: 0x26e3
-  __TEXT.__oslogstring: 0xfd6
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xf54
-  __TEXT.__unwind_info: 0x9f0
-  __TEXT.__objc_classname: 0x4c9
-  __TEXT.__objc_methname: 0x56c4
-  __TEXT.__objc_methtype: 0xd0d
-  __TEXT.__objc_stubs: 0x5240
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x778
-  __DATA_CONST.__objc_classlist: 0x188
+854.100.13.0.0
+  __TEXT.__text: 0x28610
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x2870
+  __TEXT.__oslogstring: 0x1093
+  __TEXT.__cstring: 0x299c
+  __TEXT.__const: 0xaa
+  __TEXT.__gcc_except_tab: 0xf34
+  __TEXT.__swift5_typeref: 0x82
+  __TEXT.__swift5_fieldmd: 0x30
+  __TEXT.__constg_swiftt: 0x74
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xac8
+  __TEXT.__objc_classname: 0x505
+  __TEXT.__objc_methname: 0x5c02
+  __TEXT.__objc_methtype: 0xded
+  __TEXT.__objc_stubs: 0x55a0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5b20
-  __DATA_CONST.__objc_selrefs: 0x1830
+  __DATA_CONST.__objc_const: 0x58d8
+  __DATA_CONST.__objc_selrefs: 0x1938
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__cfstring: 0x2d80
-  __AUTH_CONST.__objc_const: 0x1368
-  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__objc_const: 0x13f8
+  __AUTH_CONST.__cfstring: 0x2de0
+  __AUTH_CONST.__const: 0x750
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH.__objc_data: 0xc08
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x260
-  __DATA.__objc_superrefs: 0x100
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH.__objc_data: 0xce8
   __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0xa20
-  __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x348
-  __DATA_DIRTY.__bss: 0x18
+  __DATA.__objc_data: 0x20
+  __DATA.__data: 0xa88
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0x420
+  __DATA_DIRTY.__data: 0x60
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration
   - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: B2B4F1E2-46AA-38E2-94BF-E7BF91EBA957
-  Functions: 946
-  Symbols:   3729
-  CStrings:  2297
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  UUID: 8EECAC3A-4FEE-305B-AB9D-17824C2DE316
+  Functions: 1033
+  Symbols:   3959
+  CStrings:  2383
 
Symbols:
+ -[SKBaseManager logEvent:eventPayloadBuilder:]
+ -[SKCompletionHandler .cxx_destruct]
+ -[SKCompletionHandler completionBlock]
+ -[SKCompletionHandler errorBlock]
+ -[SKCompletionHandler functionName]
+ -[SKCompletionHandler initWithCompletionBlock:progressBlock:function:]
+ -[SKCompletionHandler progressBlock]
+ -[SKCompletionHandler semaphore]
+ -[SKCompletionHandler setErrorBlock:]
+ -[SKCompletionHandler setProgressBlock:]
+ -[SKCompletionHandler setSemaphore:]
+ -[SKHelperClient _scheduleCompletionUUID:forFunction:blocking:withBlock:]
+ -[SKHelperClient _scheduleCompletionUUID:progress:forFunction:withBlock:]
+ -[SKHelperClient _scheduleSyncCompletionUUID:forFunction:withBlock:]
+ -[SKHelperClient callbackQueue]
+ -[SKHelperClient childDisksForWholeDisk:blocking:withCallbackBlock:]
+ -[SKHelperClient completionHandlers]
+ -[SKHelperClient createXPCConnection]
+ -[SKHelperClient diskForPath:blocking:withCallbackBlock:]
+ -[SKHelperClient ejectDisk:blocking:withCompletionBlock:]
+ -[SKHelperClient filesystemsWithBlocking:callbackBlock:]
+ -[SKHelperClient isBusyWithBlocking:completionBlock:]
+ -[SKHelperClient isInvalidated]
+ -[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]
+ -[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]
+ -[SKHelperClient queueWithBlocking:]
+ -[SKHelperClient recacheDisk:options:blocking:callbackBlock:]
+ -[SKHelperClient setCallbackQueue:]
+ -[SKHelperClient setIsInvalidated:]
+ -[SKHelperClient syncAllDisksWithBlocking:completionBlock:]
+ -[SKHelperClient unmountDisk:options:blocking:withCompletionBlock:]
+ -[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]
+ -[SKHelperClient wholeDiskForDisk:blocking:withCallbackBlock:]
+ -[SKHelperClient xpcConnection]
+ -[SKHelperClient xpcQueue]
+ -[SKLogAnalyticsSink sendEventWithName:eventPayloadBuilder:]
+ -[SKManager callbackQueue]
+ -[SKManager setCallbackQueue:]
+ -[SKSyncCommand returnWithError:]
+ GCC_except_table21
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table83
+ GCC_except_table9
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_DICommonAttach
+ _OBJC_CLASS_$_DIDeviceHandle
+ _OBJC_CLASS_$_SKCompletionHandler
+ _OBJC_CLASS_$_SKLogAnalyticsSink
+ _OBJC_CLASS_$__TtC10StorageKit14SKAnalyticsHub
+ _OBJC_CLASS_$__TtC10StorageKit19SKCoreAnalyticsSink
+ _OBJC_IVAR_$_SKCompletionHandler._completionBlock
+ _OBJC_IVAR_$_SKCompletionHandler._errorBlock
+ _OBJC_IVAR_$_SKCompletionHandler._functionName
+ _OBJC_IVAR_$_SKCompletionHandler._progressBlock
+ _OBJC_IVAR_$_SKCompletionHandler._semaphore
+ _OBJC_IVAR_$_SKHelperClient._callbackQueue
+ _OBJC_IVAR_$_SKHelperClient._completionHandlers
+ _OBJC_IVAR_$_SKHelperClient._isInvalidated
+ _OBJC_IVAR_$_SKHelperClient._xpcConnection
+ _OBJC_IVAR_$_SKHelperClient._xpcQueue
+ _OBJC_METACLASS_$_SKCompletionHandler
+ _OBJC_METACLASS_$_SKLogAnalyticsSink
+ _OBJC_METACLASS_$__TtC10StorageKit14SKAnalyticsHub
+ _OBJC_METACLASS_$__TtC10StorageKit19SKCoreAnalyticsSink
+ __Block_copy
+ __Block_release
+ __DATA__TtC10StorageKit14SKAnalyticsHub
+ __DATA__TtC10StorageKit19SKCoreAnalyticsSink
+ __METACLASS_DATA__TtC10StorageKit14SKAnalyticsHub
+ __METACLASS_DATA__TtC10StorageKit19SKCoreAnalyticsSink
+ __OBJC_$_CLASS_METHODS__TtC10StorageKit14SKAnalyticsHub
+ __OBJC_$_INSTANCE_METHODS_SKCompletionHandler
+ __OBJC_$_INSTANCE_METHODS_SKLogAnalyticsSink
+ __OBJC_$_INSTANCE_METHODS__TtC10StorageKit14SKAnalyticsHub
+ __OBJC_$_INSTANCE_METHODS__TtC10StorageKit19SKCoreAnalyticsSink
+ __OBJC_$_INSTANCE_VARIABLES_SKCompletionHandler
+ __OBJC_$_PROP_LIST_SKCompletionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP10StorageKit15SKAnalyticsSink_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP10StorageKit15SKAnalyticsSink_
+ __OBJC_CLASS_PROTOCOLS_$_SKLogAnalyticsSink
+ __OBJC_CLASS_RO_$_SKCompletionHandler
+ __OBJC_CLASS_RO_$_SKLogAnalyticsSink
+ __OBJC_LABEL_PROTOCOL_$__TtP10StorageKit15SKAnalyticsSink_
+ __OBJC_METACLASS_RO_$_SKCompletionHandler
+ __OBJC_METACLASS_RO_$_SKLogAnalyticsSink
+ __OBJC_PROTOCOL_$__TtP10StorageKit15SKAnalyticsSink_
+ __PROTOCOLS__TtC10StorageKit19SKCoreAnalyticsSink
+ __PROTOCOLS__TtC10StorageKit19SKCoreAnalyticsSink.2
+ __PROTOCOL_INSTANCE_METHODS__TtP10StorageKit15SKAnalyticsSink_
+ __PROTOCOL_METHOD_TYPES__TtP10StorageKit15SKAnalyticsSink_
+ __PROTOCOL__TtP10StorageKit15SKAnalyticsSink_
+ ___22-[SKHelperClient init]_block_invoke.63
+ ___26+[SKError frameworkBundle]_block_invoke_2
+ ___35-[SKDiskImage deduceDiskWithError:]_block_invoke
+ ___36+[SKFilesystem extensionFilesystems]_block_invoke_2
+ ___37-[SKHelperClient createXPCConnection]_block_invoke
+ ___37-[SKHelperClient createXPCConnection]_block_invoke.101
+ ___38-[SKDiskImage attachWithParams:error:]_block_invoke
+ ___42+[SKPartitionTable getSectorSizeWithDisk:]_block_invoke
+ ___42+[SKPartitionTable getSectorSizeWithDisk:]_block_invoke.39
+ ___42-[SKPartition buildWithScheme:sectorSize:]_block_invoke
+ ___45+[SKDiskImage diskImageWithURL:params:error:]_block_invoke
+ ___45-[SKPartitionTable fitToContainerSize:error:]_block_invoke
+ ___45-[SKPartitionTable fitToContainerSize:error:]_block_invoke.134
+ ___47-[SKPartitionTable writePartitionScheme:error:]_block_invoke
+ ___49+[SKPartitionTable createMediaRefWithDisk:error:]_block_invoke
+ ___49-[SKManager _initialPopulateCompleteForListener:]_block_invoke
+ ___49-[SKPartitionTable resizePartitionID:size:error:]_block_invoke
+ ___49-[SKPartitionTable resizePartitionID:size:error:]_block_invoke.150
+ ___50-[SKHelperClient eraseWithEraser:completionBlock:]_block_invoke_4
+ ___53-[SKHelperClient isBusyWithBlocking:completionBlock:]_block_invoke
+ ___53-[SKHelperClient isBusyWithBlocking:completionBlock:]_block_invoke_2
+ ___56-[SKHelperClient filesystemsWithBlocking:callbackBlock:]_block_invoke
+ ___56-[SKHelperClient filesystemsWithBlocking:callbackBlock:]_block_invoke_2
+ ___56-[SKPartitionTable writeNewMediaLayout:partitionScheme:]_block_invoke
+ ___56-[SKPartitionTable writeNewMediaLayout:partitionScheme:]_block_invoke.64
+ ___56-[SKPartitionTable writeNewMediaLayout:partitionScheme:]_block_invoke.67
+ ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke
+ ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_2
+ ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_3
+ ___57-[SKHelperClient ejectDisk:blocking:withCompletionBlock:]_block_invoke
+ ___57-[SKHelperClient ejectDisk:blocking:withCompletionBlock:]_block_invoke_2
+ ___57-[SKPartitionTable overwritePartitionAt:partition:error:]_block_invoke
+ ___57-[SKPartitionTable overwritePartitionAt:partition:error:]_block_invoke.118
+ ___59-[SKHelperClient syncAllDisksWithBlocking:completionBlock:]_block_invoke
+ ___59-[SKHelperClient syncAllDisksWithBlocking:completionBlock:]_block_invoke_2
+ ___60-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke
+ ___60-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke_2
+ ___60-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke_3
+ ___60-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke_4
+ ___60-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke_5
+ ___60-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke_6
+ ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke
+ ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke.80
+ ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke_2
+ ___61-[SKManager knownDiskForDictionary:waitingForDaemon:fromSet:]_block_invoke_3
+ ___62-[SKHelperClient wholeDiskForDisk:blocking:withCallbackBlock:]_block_invoke
+ ___62-[SKHelperClient wholeDiskForDisk:blocking:withCallbackBlock:]_block_invoke_2
+ ___62-[SKHelperClient wholeDiskForDisk:blocking:withCallbackBlock:]_block_invoke_3
+ ___64-[SKManager knownDisksForDictionaries:waitingForDaemon:fromSet:]_block_invoke
+ ___67-[SKHelperClient unmountDisk:options:blocking:withCompletionBlock:]_block_invoke
+ ___67-[SKHelperClient unmountDisk:options:blocking:withCompletionBlock:]_block_invoke_2
+ ___68-[SKHelperClient _scheduleSyncCompletionUUID:forFunction:withBlock:]_block_invoke
+ ___68-[SKHelperClient childDisksForWholeDisk:blocking:withCallbackBlock:]_block_invoke
+ ___68-[SKHelperClient childDisksForWholeDisk:blocking:withCallbackBlock:]_block_invoke_2
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke.89
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_2
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_3
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_4
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_5
+ ___72-[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]_block_invoke
+ ___72-[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]_block_invoke_2
+ ___73-[SKDiskImage(Resize) resizeLimitsShallowInternalWithLimitsParams:error:]_block_invoke
+ ___73-[SKDiskImage(Resize) resizeLimitsShallowInternalWithLimitsParams:error:]_block_invoke.18
+ ___73-[SKHelperClient _scheduleCompletionUUID:progress:forFunction:withBlock:]_block_invoke
+ ___75-[SKPartitionTable overwriteExistingMediaLayout:opts:partitionScheme:size:]_block_invoke
+ ___75-[SKPartitionTable overwriteExistingMediaLayout:opts:partitionScheme:size:]_block_invoke.82
+ ___75-[SKPartitionTable overwriteExistingMediaLayout:opts:partitionScheme:size:]_block_invoke.85
+ ___75-[SKPartitionTable overwriteExistingMediaLayout:opts:partitionScheme:size:]_block_invoke.88
+ ___block_descriptor_32_e19_"NSDictionary"8?0l
+ ___block_descriptor_40_e8_32r_e16_v16?0"SKDisk"8lr32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56r_e5_v8?0ls32l8s48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s56l8r64l8s48l8
+ ___block_literal_global.106
+ ___block_literal_global.12
+ ___block_literal_global.120
+ ___block_literal_global.126
+ ___block_literal_global.136
+ ___block_literal_global.142
+ ___block_literal_global.152
+ ___block_literal_global.166
+ ___block_literal_global.170
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.189
+ ___block_literal_global.20
+ ___block_literal_global.27
+ ___block_literal_global.28
+ ___block_literal_global.38
+ ___block_literal_global.41
+ ___block_literal_global.44
+ ___block_literal_global.49
+ ___block_literal_global.59
+ ___block_literal_global.66
+ ___block_literal_global.69
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___block_literal_global.79
+ ___block_literal_global.81
+ ___block_literal_global.84
+ ___block_literal_global.87
+ ___block_literal_global.90
+ ___block_literal_global.95
+ ___eraseDisk_block_invoke.10
+ ___eraseDisk_block_invoke.15
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_StorageKit
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_StorageKit
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_StorageKit
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_StorageKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_StorageKit
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_StorageKit
+ __swift_stdlib_malloc_size
+ __unnamed_array_storage.102
+ __unnamed_array_storage.103
+ __unnamed_array_storage.115
+ __unnamed_array_storage.116
+ __unnamed_array_storage.122
+ __unnamed_array_storage.123
+ __unnamed_array_storage.131
+ __unnamed_array_storage.132
+ __unnamed_array_storage.138
+ __unnamed_array_storage.139
+ __unnamed_array_storage.147
+ __unnamed_array_storage.148
+ __unnamed_array_storage.63
+ __unnamed_array_storage.74
+ __unnamed_array_storage.75
+ __unnamed_array_storage.85
+ __unnamed_array_storage.94
+ _base64Encode
+ _block_copy_helper
+ _block_copy_helper.12
+ _block_copy_helper.15
+ _block_descriptor
+ _block_descriptor.14
+ _block_descriptor.17
+ _block_destroy_helper
+ _block_destroy_helper.13
+ _block_destroy_helper.16
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_queue
+ _objc_msgSend$_scheduleCompletionUUID:forFunction:blocking:withBlock:
+ _objc_msgSend$_scheduleCompletionUUID:progress:forFunction:withBlock:
+ _objc_msgSend$_scheduleSyncCompletionUUID:forFunction:withBlock:
+ _objc_msgSend$addSink:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$callbackQueue
+ _objc_msgSend$childDisksForWholeDisk:blocking:withCallbackBlock:
+ _objc_msgSend$completionBlock
+ _objc_msgSend$completionHandlers
+ _objc_msgSend$createXPCConnection
+ _objc_msgSend$diskForPath:blocking:withCallbackBlock:
+ _objc_msgSend$diskImageAttach:BSDName:error:
+ _objc_msgSend$diskImageAttach:readOnly:autoMount:BSDName:error:
+ _objc_msgSend$ejectDisk:blocking:withCompletionBlock:
+ _objc_msgSend$errorBlock
+ _objc_msgSend$filesystemsWithBlocking:callbackBlock:
+ _objc_msgSend$functionName
+ _objc_msgSend$initWithCompletionBlock:progressBlock:function:
+ _objc_msgSend$isBusyWithBlocking:completionBlock:
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$logEvent:eventPayloadBuilder:
+ _objc_msgSend$mountDisk:options:connection:blocking:completionBlock:
+ _objc_msgSend$physicalStoresForAPFSVolume:blocking:completionBlock:
+ _objc_msgSend$progressBlock
+ _objc_msgSend$queueWithBlocking:
+ _objc_msgSend$recacheDisk:options:blocking:callbackBlock:
+ _objc_msgSend$returnWithError:
+ _objc_msgSend$sendEventWithName:eventPayloadBuilder:
+ _objc_msgSend$setBSDName:
+ _objc_msgSend$setCallbackQueue:
+ _objc_msgSend$setErrorBlock:
+ _objc_msgSend$setIsInvalidated:
+ _objc_msgSend$setProgressBlock:
+ _objc_msgSend$setSemaphore:
+ _objc_msgSend$setUniqueDevice:
+ _objc_msgSend$syncAllDisksWithBlocking:completionBlock:
+ _objc_msgSend$unmountDisk:options:blocking:withCompletionBlock:
+ _objc_msgSend$volumesForAPFSPS:blocking:completionBlock:
+ _objc_msgSend$wholeDiskForDisk:blocking:withCallbackBlock:
+ _objc_msgSend$xpcConnection
+ _objc_msgSend$xpcQueue
+ _objc_opt_self
+ _objc_retain_x6
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_endAccess
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic $s10StorageKit15SKAnalyticsSinkP
+ _symbolic 10StorageKit15SKAnalyticsSink_p
+ _symbolic So12NSDictionaryCSgIeyBa_
+ _symbolic So8NSObjectC
+ _symbolic _____ 10StorageKit14SKAnalyticsHubC
+ _symbolic _____ 10StorageKit19SKCoreAnalyticsSinkC
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
- -[SKHelperClient _setProgressHandler:forUUID:]
- -[SKHelperClient _xpcConnection]
- -[SKHelperClient diskNotificationQueue]
- -[SKHelperClient synchronousRemoteObjecUUID:tWithErrorHandler:]
- -[SKIdleWaiter .cxx_destruct]
- -[SKIdleWaiter init]
- -[SKIdleWaiter initialPopulateComplete]
- -[SKIdleWaiter semaphore]
- -[SKIdleWaiter setSemaphore:]
- -[SKIdleWaiter waitForIdle]
- -[SKSyncCommand init]
- -[SKSyncCommand semaphore]
- -[SKSyncCommand setSemaphore:]
- -[SKSyncCommand waitAndReturnWithError:]
- GCC_except_table13
- GCC_except_table29
- GCC_except_table36
- GCC_except_table40
- GCC_except_table45
- GCC_except_table47
- GCC_except_table50
- GCC_except_table57
- GCC_except_table61
- GCC_except_table65
- GCC_except_table69
- GCC_except_table74
- GCC_except_table76
- OBJC_IVAR_$_SKHelperClient._callbackQueue
- OBJC_IVAR_$_SKHelperClient._completionBlockDictionary
- OBJC_IVAR_$_SKHelperClient._connection
- OBJC_IVAR_$_SKHelperClient._errorBlockDictionary
- OBJC_IVAR_$_SKHelperClient._isInvalidated
- OBJC_IVAR_$_SKHelperClient._progressBlock
- OBJC_IVAR_$_SKHelperClient._progressBlockDictionary
- OBJC_IVAR_$_SKManager._diskNotificationQueue
- _OBJC_CLASS_$_SKIdleWaiter
- _OBJC_IVAR_$_SKIdleWaiter._semaphore
- _OBJC_IVAR_$_SKSyncCommand._semaphore
- _OBJC_METACLASS_$_SKIdleWaiter
- __OBJC_$_INSTANCE_METHODS_SKIdleWaiter
- __OBJC_$_INSTANCE_VARIABLES_SKIdleWaiter
- __OBJC_$_PROP_LIST_SKIdleWaiter
- __OBJC_CLASS_PROTOCOLS_$_SKIdleWaiter
- __OBJC_CLASS_RO_$_SKIdleWaiter
- __OBJC_METACLASS_RO_$_SKIdleWaiter
- ___25-[SKHelperClient isBusy:]_block_invoke
- ___25-[SKHelperClient isBusy:]_block_invoke_2
- ___25-[SKManager syncAllDisks]_block_invoke
- ___29-[SKDisk recacheWithOptions:]_block_invoke
- ___30+[SKManager syncSharedManager]_block_invoke
- ___31-[SKHelperClient disksChanged:]_block_invoke
- ___32-[SKHelperClient _xpcConnection]_block_invoke
- ___32-[SKHelperClient _xpcConnection]_block_invoke.58
- ___32-[SKHelperClient _xpcConnection]_block_invoke_2
- ___32-[SKHelperClient disksAppeared:]_block_invoke
- ___32-[SKHelperClient managerResumed]_block_invoke
- ___32-[SKHelperClient managerStalled]_block_invoke
- ___35-[SKHelperClient disksDisappeared:]_block_invoke
- ___41-[SKHelperClient initialPopulateComplete]_block_invoke
- ___46-[SKHelperClient _setProgressHandler:forUUID:]_block_invoke
- ___47-[SKHelperClient filesystemsWithCallbackBlock:]_block_invoke
- ___47-[SKHelperClient filesystemsWithCallbackBlock:]_block_invoke_2
- ___48-[SKHelperClient diskForPath:withCallbackBlock:]_block_invoke
- ___48-[SKHelperClient diskForPath:withCallbackBlock:]_block_invoke_2
- ___48-[SKHelperClient diskForPath:withCallbackBlock:]_block_invoke_3
- ___48-[SKHelperClient ejectDisk:withCompletionBlock:]_block_invoke
- ___48-[SKHelperClient ejectDisk:withCompletionBlock:]_block_invoke_2
- ___50-[SKHelperClient syncAllDisksWithCompletionBlock:]_block_invoke
- ___50-[SKHelperClient syncAllDisksWithCompletionBlock:]_block_invoke_2
- ___50-[SKHelperClient unmountDisk:withCompletionBlock:]_block_invoke
- ___50-[SKHelperClient unmountDisk:withCompletionBlock:]_block_invoke_2
- ___51-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke
- ___51-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke_2
- ___51-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke_3
- ___51-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke_4
- ___51-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke_5
- ___51-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke_6
- ___52-[SKHelperClient recacheDisk:options:callbackBlock:]_block_invoke
- ___52-[SKHelperClient recacheDisk:options:callbackBlock:]_block_invoke.31
- ___52-[SKHelperClient recacheDisk:options:callbackBlock:]_block_invoke_2
- ___53-[SKHelperClient wholeDiskForDisk:withCallbackBlock:]_block_invoke
- ___53-[SKHelperClient wholeDiskForDisk:withCallbackBlock:]_block_invoke_2
- ___53-[SKHelperClient wholeDiskForDisk:withCallbackBlock:]_block_invoke_3
- ___58-[SKHelperClient unmountDisk:options:withCompletionBlock:]_block_invoke
- ___58-[SKHelperClient unmountDisk:options:withCompletionBlock:]_block_invoke_2
- ___59-[SKHelperClient _markConnectionInvalidAndCallAllCallbacks]_block_invoke
- ___59-[SKHelperClient childDisksForWholeDisk:withCallbackBlock:]_block_invoke
- ___59-[SKHelperClient childDisksForWholeDisk:withCallbackBlock:]_block_invoke_2
- ___62-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke
- ___62-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke.40
- ___62-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke_2
- ___62-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke_3
- ___62-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke_4
- ___62-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke_5
- ___63-[SKHelperClient mountDisk:options:connection:completionBlock:]_block_invoke
- ___63-[SKHelperClient mountDisk:options:connection:completionBlock:]_block_invoke_2
- ___63-[SKHelperClient synchronousRemoteObjecUUID:tWithErrorHandler:]_block_invoke
- ___64-[SKHelperClient _scheduleCompletionUUID:forFunction:withBlock:]_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e16_v16?0"SKDisk"8ls32l8
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_literal_global.165
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.173
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.48
- ___block_literal_global.52
- ___block_literal_global.75
- ___block_literal_global.80
- __unnamed_array_storage.28
- __unnamed_array_storage.36
- __unnamed_array_storage.42
- __unnamed_array_storage.45
- __unnamed_array_storage.50
- __unnamed_array_storage.51
- __unnamed_array_storage.65
- __unnamed_array_storage.66
- __unnamed_array_storage.76
- __unnamed_array_storage.80
- __unnamed_array_storage.81
- __unnamed_array_storage.87
- __unnamed_array_storage.88
- __unnamed_array_storage.92
- __unnamed_array_storage.98
- __unnamed_array_storage.99
- __xpcConnection.onceToken
- _objc_msgSend$_xpcConnection
- _objc_msgSend$addListener:
- _objc_msgSend$attachWithParams:handle:error:
- _objc_msgSend$childDisksForWholeDisk:withCallbackBlock:
- _objc_msgSend$diskForPath:withCallbackBlock:
- _objc_msgSend$diskNotificationQueue
- _objc_msgSend$ejectWithCompletionBlock:
- _objc_msgSend$filesystemsWithCallbackBlock:
- _objc_msgSend$isBusy:
- _objc_msgSend$physicalStoresForAPFSVolume:completionBlock:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_msgSend$volumesForAPFSPS:completionBlock:
- _objc_msgSend$waitAndReturnWithError:
- _objc_msgSend$waitForIdle
- _objc_msgSend$wholeDiskForDisk:withCallbackBlock:
- _syncSharedManager.once
CStrings:
+ "\x15"
+ "\x18"
+ "%s: No completion handler set for %{public}@, cannot set error block"
+ "%s:%d"
+ "-[SKHelperClient childDisksForWholeDisk:blocking:withCallbackBlock:]"
+ "-[SKHelperClient childDisksForWholeDisk:blocking:withCallbackBlock:]_block_invoke_2"
+ "-[SKHelperClient diskForPath:blocking:withCallbackBlock:]"
+ "-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_3"
+ "-[SKHelperClient ejectDisk:blocking:withCompletionBlock:]"
+ "-[SKHelperClient filesystemsWithBlocking:callbackBlock:]"
+ "-[SKHelperClient filesystemsWithBlocking:callbackBlock:]_block_invoke_2"
+ "-[SKHelperClient isBusyWithBlocking:completionBlock:]"
+ "-[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]"
+ "-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]"
+ "-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_5"
+ "-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]"
+ "-[SKHelperClient remoteObjectWithUUID:errorHandler:]_block_invoke"
+ "-[SKHelperClient syncAllDisksWithBlocking:completionBlock:]"
+ "-[SKHelperClient unmountDisk:options:blocking:withCompletionBlock:]"
+ "-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]"
+ "-[SKHelperClient volumesForAPFSPS:blocking:completionBlock:]_block_invoke_6"
+ "-[SKHelperClient wholeDiskForDisk:blocking:withCallbackBlock:]"
+ "-[SKHelperClient wholeDiskForDisk:blocking:withCallbackBlock:]_block_invoke_3"
+ "@\"NSDictionary\"8@?0"
+ "@40@0:8@16r*24@?32"
+ "@40@0:8@?16@?24r*32"
+ "@44@0:8@16r*24B32@?36"
+ "CLIENT - Initial Populate Complete"
+ "Completion block directly executed for: %{public}@"
+ "Completion callback for: %{public}@ - end"
+ "Completion callback for: %{public}@ - start"
+ "Down-casted Array element failed to match the target type\nExpected "
+ "Error: no completion handler for %{public}@"
+ "Fallback attaching %@ with %@"
+ "Fatal error"
+ "NSArray element failed to match the Swift Array Element type\nExpected "
+ "Reached XPC reply for %{public}@ %{public}s"
+ "SKCompletionHandler"
+ "SKDiskImage+Resize.m"
+ "SKDiskImage.m"
+ "SKError.m"
+ "SKFilesystem.m"
+ "SKHelperClient.m"
+ "SKLogAnalyticsSink"
+ "SKPartitionTable.m"
+ "Sending event %@ with payload %@"
+ "Setting sync completion callback for ( %s ) to: %{public}@"
+ "T@\"NSMutableDictionary\",R,N,V_completionHandlers"
+ "T@\"NSObject<OS_dispatch_queue>\",&"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_callbackQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_xpcQueue"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSXPCConnection\",R,N,V_xpcConnection"
+ "T@?,C,N,V_errorBlock"
+ "T@?,C,N,V_progressBlock"
+ "T@?,R,N,V_completionBlock"
+ "TB,V_isInvalidated"
+ "Tr*,R,N,V_functionName"
+ "_TtC10StorageKit14SKAnalyticsHub"
+ "_TtC10StorageKit19SKCoreAnalyticsSink"
+ "_TtP10StorageKit15SKAnalyticsSink_"
+ "_completionBlock"
+ "_completionHandlers"
+ "_errorBlock"
+ "_functionName"
+ "_queue"
+ "_scheduleCompletionUUID:forFunction:blocking:withBlock:"
+ "_scheduleCompletionUUID:progress:forFunction:withBlock:"
+ "_scheduleSyncCompletionUUID:forFunction:withBlock:"
+ "_xpcQueue"
+ "addSink:"
+ "base64EncodedStringWithOptions:"
+ "callbackQueue"
+ "childDisksForWholeDisk:blocking:withCallbackBlock:"
+ "com.apple.StorageKit.Callbacks"
+ "com.apple.StorageKit.log.fault"
+ "completionBlock"
+ "completionHandlers"
+ "createXPCConnection"
+ "diskForPath:blocking:withCallbackBlock:"
+ "diskImageAttach:BSDName:error:"
+ "diskImageAttach:readOnly:autoMount:BSDName:error:"
+ "ejectDisk:blocking:withCompletionBlock:"
+ "errorBlock"
+ "faultCode"
+ "filesystemsWithBlocking:callbackBlock:"
+ "functionName"
+ "initWithCompletionBlock:progressBlock:function:"
+ "isBusyWithBlocking:completionBlock:"
+ "isInvalidated"
+ "logEvent:eventPayloadBuilder:"
+ "mountDisk:options:connection:blocking:completionBlock:"
+ "physicalStoresForAPFSVolume:blocking:completionBlock:"
+ "progressBlock"
+ "queueWithBlocking:"
+ "r*"
+ "r*16@0:8"
+ "recacheDisk:options:blocking:callbackBlock:"
+ "returnWithError:"
+ "sendEventWithName:eventPayloadBuilder:"
+ "setBSDName:"
+ "setCallbackQueue:"
+ "setErrorBlock:"
+ "setIsInvalidated:"
+ "setProgressBlock:"
+ "setUniqueDevice:"
+ "syncAllDisksWithBlocking:completionBlock:"
+ "unmountDisk:options:blocking:withCompletionBlock:"
+ "v28@0:8B16@?20"
+ "v32@0:8@\"NSString\"16@?<@\"NSDictionary\"@?>24"
+ "v36@0:8@16B24@?28"
+ "v44@0:8@16@24B32@?36"
+ "v44@0:8@16Q24B32@?36"
+ "v48@0:8@16@?24r*32@?40"
+ "v52@0:8@16@24@32B40@?44"
+ "volumesForAPFSPS:blocking:completionBlock:"
+ "wholeDiskForDisk:blocking:withCallbackBlock:"
+ "xpcConnection"
+ "xpcQueue"
- "\x06\x11"
- "\x19"
- "%s: fatal - SKIdleWaiter init failed"
- "+[SKManager syncSharedManager]_block_invoke"
- "-[SKHelperClient childDisksForWholeDisk:withCallbackBlock:]"
- "-[SKHelperClient childDisksForWholeDisk:withCallbackBlock:]_block_invoke_2"
- "-[SKHelperClient diskForPath:withCallbackBlock:]"
- "-[SKHelperClient diskForPath:withCallbackBlock:]_block_invoke_3"
- "-[SKHelperClient ejectDisk:withCompletionBlock:]"
- "-[SKHelperClient filesystemsWithCallbackBlock:]"
- "-[SKHelperClient filesystemsWithCallbackBlock:]_block_invoke_2"
- "-[SKHelperClient isBusy:]"
- "-[SKHelperClient mountDisk:options:connection:completionBlock:]"
- "-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]"
- "-[SKHelperClient physicalStoresForAPFSVolume:completionBlock:]_block_invoke_5"
- "-[SKHelperClient recacheDisk:options:callbackBlock:]"
- "-[SKHelperClient syncAllDisksWithCompletionBlock:]"
- "-[SKHelperClient unmountDisk:options:withCompletionBlock:]"
- "-[SKHelperClient unmountDisk:withCompletionBlock:]"
- "-[SKHelperClient volumesForAPFSPS:completionBlock:]"
- "-[SKHelperClient volumesForAPFSPS:completionBlock:]_block_invoke_6"
- "-[SKHelperClient wholeDiskForDisk:withCallbackBlock:]"
- "-[SKHelperClient wholeDiskForDisk:withCallbackBlock:]_block_invoke_3"
- "CLIENT - Initial Populate Compelete"
- "Called, clearing completion callback for: %{public}@"
- "Calling completion callback for: %{public}@"
- "Clearing completion callback for: %{public}@"
- "Error: no callback block found for: %{public}@"
- "SKIdleWaiter"
- "_completionBlockDictionary"
- "_diskNotificationQueue"
- "_errorBlockDictionary"
- "_progressBlockDictionary"
- "_setProgressHandler:forUUID:"
- "attachWithParams:handle:error:"
- "com.apple.SKHelperClient.disknotification"
- "diskNotificationQueue"
- "synchronousRemoteObjecUUID:tWithErrorHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v32@0:8@?16@24"
- "waitAndReturnWithError:"
- "waitForIdle"

```

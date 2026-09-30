## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-192.0.0.0.0
-  __TEXT.__text: 0x4f4fc
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x4694
-  __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x1110
-  __TEXT.__cstring: 0x3ab6
-  __TEXT.__oslogstring: 0x4983
+195.0.0.0.0
+  __TEXT.__text: 0x55c0c
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_methlist: 0x48a4
+  __TEXT.__const: 0x3a4
+  __TEXT.__gcc_except_tab: 0x10ac
+  __TEXT.__cstring: 0x3ef2
+  __TEXT.__oslogstring: 0x4d24
   __TEXT.__dlopen_cstrs: 0x278
-  __TEXT.__unwind_info: 0x1358
-  __TEXT.__objc_classname: 0xade
-  __TEXT.__objc_methname: 0xa0f8
-  __TEXT.__objc_methtype: 0x1e4b
-  __TEXT.__objc_stubs: 0x6ce0
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1228
-  __DATA_CONST.__objc_classlist: 0x340
+  __TEXT.__swift5_typeref: 0x168
+  __TEXT.__swift5_fieldmd: 0xd4
+  __TEXT.__constg_swiftt: 0x15c
+  __TEXT.__swift5_reflstr: 0x40
+  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__unwind_info: 0x15a8
+  __TEXT.__eh_frame: 0x2f8
+  __TEXT.__objc_classname: 0xb3f
+  __TEXT.__objc_methname: 0xa4ce
+  __TEXT.__objc_methtype: 0x1f7e
+  __TEXT.__objc_stubs: 0x6da0
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x1318
+  __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23f0
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x2c0
+  __DATA_CONST.__objc_selrefs: 0x24c0
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x508
-  __AUTH_CONST.__const: 0x190
-  __AUTH_CONST.__cfstring: 0x3400
-  __AUTH_CONST.__objc_const: 0xae38
-  __AUTH_CONST.__objc_intobj: 0x3f0
+  __AUTH_CONST.__auth_got: 0x6b0
+  __AUTH_CONST.__const: 0x488
+  __AUTH_CONST.__cfstring: 0x3480
+  __AUTH_CONST.__objc_const: 0xaeb0
+  __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x4d0
-  __DATA.__data: 0xaf8
+  __AUTH.__objc_data: 0x3e8
+  __AUTH.__data: 0x78
+  __DATA.__objc_ivar: 0x4e0
+  __DATA.__data: 0xcac
   __DATA.__bss: 0x48
-  __DATA_DIRTY.__objc_data: 0x1f90
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x1ef0
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: BFBB2A57-2631-3DFF-863E-880B2E0E121B
-  Functions: 1817
-  Symbols:   6408
-  CStrings:  3302
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 41B6F6E7-B5FE-3865-8937-61025C6A9E4A
+  Functions: 2024
+  Symbols:   6675
+  CStrings:  3409
 
Symbols:
+ +[CCMaintenanceClient sharedInstance]
+ +[CCSetStoreAdminXPCClient performMaintenanceOnAllSets:clientId:shouldDeferBlock:]
+ +[CCSetStoreAdminXPCClient removeAllSets:completion:]
+ +[CCSetStoreAdminXPCClient wrappedCompletion:retainingClient:]
+ -[CCDaemon initWithQueue:setBookkeeping:]
+ -[CCDaemon start]
+ -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]
+ -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:].cold.1
+ -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:usingBlock:].cold.1
+ -[CCDatabaseSetStateReader checkForLocalSourceDonation:error:]
+ -[CCDatabaseSetStateReader checkForPresentContent:filterByDeviceRowId:error:]
+ -[CCDatabaseUpdater expireRemoteDeviceUUID:]
+ -[CCDatabaseUpdater registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:]
+ -[CCDonateXPCClient remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]
+ -[CCMaintenanceClient .cxx_destruct]
+ -[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:]
+ -[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:].cold.1
+ -[CCMaintenanceClient client]
+ -[CCMaintenanceClient init]
+ -[CCMaintenanceClient performNightlyMaintenanceWithCompletion:]
+ -[CCMaintenanceClient performNightlyMaintenanceWithError:]
+ -[CCRemoteCRDTSetDonation remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:]
+ -[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:]
+ -[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.1
+ -[CCSetStoreAdminXPCClient .cxx_destruct]
+ -[CCSetStoreAdminXPCClient initWithClientId:shouldDeferBlock:]
+ -[CCSetStoreAdminXPCClient shouldDeferCurrentActivity:]
+ -[CCSetStoreAdminXPCClient shouldDeferCurrentActivity:].cold.1
+ -[CCSetsAccessDaemonDelegate lastMaintenanceDateForResourceContainer:]
+ -[CCSetsAccessDaemonDelegate lastMaintenanceDateForResourceContainer:].cold.1
+ -[CCSetsAccessDaemonDelegate setLastMaintenanceDateForResourceContainer:date:error:]
+ -[CCSetsAccessDaemonDelegate setLastMaintenanceDateForResourceContainer:date:error:].cold.1
+ -[CCXPCClient serviceThrowingRequest:completion:usingBlock:]
+ GCC_except_table145
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table61
+ _CCRemoteUpdateTypeDescription
+ _CCSetStoreAdminServiceResultDescription
+ _NSStringFromProtocol
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_CCMaintenanceClient
+ _OBJC_CLASS_$_CCMaintenanceServer
+ _OBJC_CLASS_$_CCScheduledTaskState
+ _OBJC_CLASS_$_CCScheduledTasks
+ _OBJC_CLASS_$_CCSetStoreAdminXPCClient
+ _OBJC_CLASS_$__PASLock
+ _OBJC_IVAR_$_CCDaemon._maintenanceServer
+ _OBJC_IVAR_$_CCDaemon._scheduledTasks
+ _OBJC_IVAR_$_CCDaemon._setBookkeeping
+ _OBJC_IVAR_$_CCMaintenanceClient._queue
+ _OBJC_IVAR_$_CCSetStoreAdminXPCClient._shouldDeferBlock
+ _OBJC_METACLASS_$_CCMaintenanceClient
+ _OBJC_METACLASS_$_CCMaintenanceServer
+ _OBJC_METACLASS_$_CCScheduledTaskState
+ _OBJC_METACLASS_$_CCScheduledTasks
+ _OBJC_METACLASS_$_CCSetStoreAdminXPCClient
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_CCMaintenanceServer
+ __CLASS_PROPERTIES_CCMaintenanceServer
+ __DATA_CCMaintenanceServer
+ __DATA_CCScheduledTaskState
+ __DATA_CCScheduledTasks
+ __INSTANCE_METHODS_CCMaintenanceServer
+ __INSTANCE_METHODS_CCScheduledTaskState
+ __IVARS_CCMaintenanceServer
+ __IVARS_CCScheduledTaskState
+ __IVARS_CCScheduledTasks
+ __METACLASS_DATA_CCMaintenanceServer
+ __METACLASS_DATA_CCScheduledTaskState
+ __METACLASS_DATA_CCScheduledTasks
+ __OBJC_$_CLASS_METHODS_CCMaintenanceClient
+ __OBJC_$_CLASS_METHODS_CCSetStoreAdminXPCClient
+ __OBJC_$_INSTANCE_METHODS_CCMaintenanceClient
+ __OBJC_$_INSTANCE_METHODS_CCScheduledTasks(CascadeSets)
+ __OBJC_$_INSTANCE_METHODS_CCSetStoreAdminXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_CCMaintenanceClient
+ __OBJC_$_INSTANCE_VARIABLES_CCSetStoreAdminXPCClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCMaintenanceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCMaintenanceServerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCSetBookkeeping
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCSetStoreAdminService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCSetStoreAdminServiceClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCMaintenanceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCMaintenanceServerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCSetBookkeeping
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCSetStoreAdminService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCSetStoreAdminServiceClient
+ __OBJC_$_PROTOCOL_REFS_CCSetStoreAdminServiceClient
+ __OBJC_$_PROTOCOL_REFS_CCSetStoreAdminServiceServer
+ __OBJC_CLASS_PROTOCOLS_$_CCMaintenanceClient
+ __OBJC_CLASS_PROTOCOLS_$_CCSetStoreAdminXPCClient
+ __OBJC_CLASS_RO_$_CCMaintenanceClient
+ __OBJC_CLASS_RO_$_CCSetStoreAdminXPCClient
+ __OBJC_LABEL_PROTOCOL_$_CCMaintenanceProtocol
+ __OBJC_LABEL_PROTOCOL_$_CCMaintenanceServerProtocol
+ __OBJC_LABEL_PROTOCOL_$_CCSetBookkeeping
+ __OBJC_LABEL_PROTOCOL_$_CCSetStoreAdminService
+ __OBJC_LABEL_PROTOCOL_$_CCSetStoreAdminServiceClient
+ __OBJC_LABEL_PROTOCOL_$_CCSetStoreAdminServiceServer
+ __OBJC_METACLASS_RO_$_CCMaintenanceClient
+ __OBJC_METACLASS_RO_$_CCSetStoreAdminXPCClient
+ __OBJC_PROTOCOL_$_CCMaintenanceProtocol
+ __OBJC_PROTOCOL_$_CCMaintenanceServerProtocol
+ __OBJC_PROTOCOL_$_CCSetBookkeeping
+ __OBJC_PROTOCOL_$_CCSetStoreAdminService
+ __OBJC_PROTOCOL_$_CCSetStoreAdminServiceClient
+ __OBJC_PROTOCOL_$_CCSetStoreAdminServiceServer
+ __OBJC_PROTOCOL_REFERENCE_$_CCMaintenanceServerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CCSetStoreAdminServiceClient
+ __OBJC_PROTOCOL_REFERENCE_$_CCSetStoreAdminServiceServer
+ __PROPERTIES_CCMaintenanceServer
+ __PROPERTIES_CCScheduledTaskState
+ __PROPERTIES_CCScheduledTasks
+ __PROTOCOLS_CCMaintenanceServer
+ __PROTOCOLS_CCMaintenanceServer.4
+ __PROTOCOL_CCMaintenanceServerProtocol
+ __PROTOCOL_INSTANCE_METHODS_CCMaintenanceServerProtocol
+ __PROTOCOL_METHOD_TYPES_CCMaintenanceServerProtocol
+ ___103-[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
+ ___116-[CCDonateXPCClient remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
+ ___37+[CCMaintenanceClient sharedInstance]_block_invoke
+ ___47-[CCSetsAccessDaemonDelegate prepareContainer:]_block_invoke
+ ___53+[CCSetStoreAdminXPCClient removeAllSets:completion:]_block_invoke
+ ___57-[CCSetsAccessDaemonDelegate _validateReadOnlyContainer:]_block_invoke
+ ___58-[CCMaintenanceClient performNightlyMaintenanceWithError:]_block_invoke
+ ___60-[CCXPCClient serviceThrowingRequest:completion:usingBlock:]_block_invoke
+ ___62+[CCSetStoreAdminXPCClient wrappedCompletion:retainingClient:]_block_invoke
+ ___62+[CCSetStoreAdminXPCClient wrappedCompletion:retainingClient:]_block_invoke.cold.1
+ ___62+[CCSetStoreAdminXPCClient wrappedCompletion:retainingClient:]_block_invoke.cold.2
+ ___67-[CCSetsAccessDaemonDelegate _storedLocalIDSIdentifierInContainer:]_block_invoke
+ ___70-[CCSetsAccessDaemonDelegate lastMaintenanceDateForResourceContainer:]_block_invoke
+ ___74-[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:]_block_invoke
+ ___74-[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:]_block_invoke_2
+ ___74-[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:]_block_invoke_2.cold.1
+ ___74-[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:]_block_invoke_2.cold.2
+ ___77-[CCDatabaseSetStateReader checkForPresentContent:filterByDeviceRowId:error:]_block_invoke
+ ___77-[CCDatabaseSetStateReader checkForPresentContent:filterByDeviceRowId:error:]_block_invoke.cold.1
+ ___82+[CCSetStoreAdminXPCClient performMaintenanceOnAllSets:clientId:shouldDeferBlock:]_block_invoke
+ ___82-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:usingBlock:]_block_invoke
+ ___84-[CCSetsAccessDaemonDelegate setLastMaintenanceDateForResourceContainer:date:error:]_block_invoke
+ ___92-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]_block_invoke
+ ___92-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]_block_invoke.22
+ ___92-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]_block_invoke.25
+ ___block_descriptor_32_e66_v24?0"NSObject<CCMaintenanceServerProtocol>"8?<v?"NSError">16l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e58_v24?0"NSObject<CCSetStoreAdminServiceServer>"8?<v?S>16ls32l8
+ ___block_descriptor_42_e8_32s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0S8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v16?0"NSMutableDictionary"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v16?0"NSMutableDictionary"8ls32l8s40l8r48l8
+ ___block_descriptor_60_e8_32s40s_e70_v24?0"NSObject<CCDonateService>"8?<v?Sq"CCDonateServicePriors">16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e29_v16?0"NSMutableDictionary"8ls32l8r48l8s40l8r56l8
+ ___block_descriptor_66_e8_32s40s48s56s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.197
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_getEnumTagSinglePayload
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ ___swift_storeEnumTagSinglePayload
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CascadeSets
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CascadeSets
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CascadeSets
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CascadeSets
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CascadeSets
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_CascadeSets
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CascadeSets
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _block_copy_helper
+ _block_copy_helper.39
+ _block_copy_helper.4
+ _block_descriptor
+ _block_descriptor.41
+ _block_descriptor.6
+ _block_destroy_helper
+ _block_destroy_helper.40
+ _block_destroy_helper.5
+ _dlopen
+ _dlopenHelper$BackgroundSystemTasks
+ _dlopenHelperFlag$BackgroundSystemTasks
+ _flat unique So16CCSetBookkeeping_p
+ _get_type_metadata 15Synchronization5MutexVySbG.11
+ _gotLoadHelper_x8$_OBJC_CLASS_$_BGSystemTaskScheduler
+ _malloc_size
+ _objc_allocWithZone
+ _objc_msgSend$_performNightlyMaintenanceSynchronously:completion:
+ _objc_msgSend$_remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:
+ _objc_msgSend$checkForLocalSourceDonation:error:
+ _objc_msgSend$checkForPresentContent:filterByDeviceRowId:error:
+ _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:usingBlock:
+ _objc_msgSend$enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:
+ _objc_msgSend$initWithClientId:shouldDeferBlock:
+ _objc_msgSend$initWithGuardedData:
+ _objc_msgSend$initWithQueue:setBookkeeping:
+ _objc_msgSend$initWithSetBookkeeping:
+ _objc_msgSend$performNightlyMaintenanceWithCompletionHandler:
+ _objc_msgSend$protocol
+ _objc_msgSend$register
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:
+ _objc_msgSend$resetRootDirectoryIfNecessary
+ _objc_msgSend$runWithLockAcquired:
+ _objc_msgSend$serviceThrowingRequest:completion:usingBlock:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$writeUpdatedObject:forKey:error:
+ _objc_opt_self
+ _objectdestroy.14Tm
+ _objectdestroyTm
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_deletedAsyncMethodErrorTu
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic $s11CascadeSets13ScheduledTaskP
+ _symbolic $s11CascadeSets25MaintenanceServerProtocolP
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SS
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ScTyyt______pG s5ErrorP
+ _symbolic So12BGSystemTaskC
+ _symbolic So12BGSystemTaskCSg
+ _symbolic So13BMXPCListenerC
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 11CascadeSets14ScheduledTasksC
+ _symbolic _____ 11CascadeSets17MaintenanceServerC
+ _symbolic _____ 11CascadeSets18ScheduledTaskStateC
+ _symbolic _____ 11CascadeSets19DatabaseMaintenanceO
+ _symbolic _____ 11CascadeSets19DatabaseMaintenanceO11NightlyTaskV
+ _symbolic _____ 11CascadeSets7LoggingO
+ _symbolic ______p So16CCSetBookkeepingP
+ _symbolic ______p s5ErrorP
+ _symbolic _____m 11CascadeSets19DatabaseMaintenanceO11NightlyTaskV
+ _symbolic _____ySbG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic ytIeAgHr_
+ _type_layout_string 11CascadeSets19DatabaseMaintenanceO11NightlyTaskV
- +[CCAdminXPCClient performMaintenanceOnAllSets:activity:completion:]
- +[CCAdminXPCClient removeAllSets:completion:]
- +[CCAdminXPCClient wrappedCompletion:retainingClient:]
- +[CCDaemon registerXPCActivities]
- +[CCDaemon runNightlyMaintenanceActivity:completion:]
- -[CCAdminXPCClient .cxx_destruct]
- -[CCAdminXPCClient initWithClientId:activity:]
- -[CCAdminXPCClient shouldDeferCurrentActivity:]
- -[CCDaemon initWithQueue:]
- -[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]
- -[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:].cold.1
- -[CCDataResourceReadAccess enumerateReadableSets:withOptions:itemType:usingBlock:]
- -[CCDatabaseEmptyAccess enumerateRecordResultsOfSelect:recordClass:error:usingBlock:]
- -[CCDatabaseEmptyAccess enumerateRowResultsOfSelect:error:usingBlock:]
- -[CCDatabaseEmptyAccess enumeratorForRowResultsOfSelect:error:]
- -[CCDatabaseEmptyAccess reset:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:usingBlock:].cold.1
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.7
- -[CCDatabaseUpdater registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:]
- -[CCDonateXPCClient mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]
- -[CCRemoteCRDTSetDonation mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:]
- -[CCSetDonation _mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]
- GCC_except_table149
- GCC_except_table17
- GCC_except_table44
- GCC_except_table46
- GCC_except_table50
- GCC_except_table52
- GCC_except_table54
- GCC_except_table56
- GCC_except_table62
- _CCAdminServiceResultDescription
- _OBJC_CLASS_$_BMXPCActivity
- _OBJC_CLASS_$_CCAdminXPCClient
- _OBJC_CLASS_$_CCDatabaseEmptyAccess
- _OBJC_IVAR_$_CCAdminXPCClient._activity
- _OBJC_METACLASS_$_CCAdminXPCClient
- _OBJC_METACLASS_$_CCDatabaseEmptyAccess
- _XPC_ACTIVITY_CHECK_IN
- __OBJC_$_CLASS_METHODS_CCAdminXPCClient
- __OBJC_$_INSTANCE_METHODS_CCAdminXPCClient
- __OBJC_$_INSTANCE_METHODS_CCDatabaseEmptyAccess
- __OBJC_$_INSTANCE_VARIABLES_CCAdminXPCClient
- __OBJC_$_PROP_LIST_CCDatabaseEmptyAccess
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCAdminService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCAdminServiceClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCAdminService
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCAdminServiceClient
- __OBJC_$_PROTOCOL_REFS_CCAdminServiceClient
- __OBJC_$_PROTOCOL_REFS_CCAdminServiceServer
- __OBJC_CLASS_PROTOCOLS_$_CCAdminXPCClient
- __OBJC_CLASS_PROTOCOLS_$_CCDatabaseEmptyAccess
- __OBJC_CLASS_RO_$_CCAdminXPCClient
- __OBJC_CLASS_RO_$_CCDatabaseEmptyAccess
- __OBJC_LABEL_PROTOCOL_$_CCAdminService
- __OBJC_LABEL_PROTOCOL_$_CCAdminServiceClient
- __OBJC_LABEL_PROTOCOL_$_CCAdminServiceServer
- __OBJC_METACLASS_RO_$_CCAdminXPCClient
- __OBJC_METACLASS_RO_$_CCDatabaseEmptyAccess
- __OBJC_PROTOCOL_$_CCAdminService
- __OBJC_PROTOCOL_$_CCAdminServiceClient
- __OBJC_PROTOCOL_$_CCAdminServiceServer
- __OBJC_PROTOCOL_REFERENCE_$_CCAdminServiceClient
- __OBJC_PROTOCOL_REFERENCE_$_CCAdminServiceServer
- ___33+[CCDaemon registerXPCActivities]_block_invoke
- ___33+[CCDaemon registerXPCActivities]_block_invoke.3
- ___45+[CCAdminXPCClient removeAllSets:completion:]_block_invoke
- ___53+[CCDaemon runNightlyMaintenanceActivity:completion:]_block_invoke
- ___53+[CCDaemon runNightlyMaintenanceActivity:completion:]_block_invoke.cold.1
- ___54+[CCAdminXPCClient wrappedCompletion:retainingClient:]_block_invoke
- ___54+[CCAdminXPCClient wrappedCompletion:retainingClient:]_block_invoke.cold.1
- ___54+[CCAdminXPCClient wrappedCompletion:retainingClient:]_block_invoke.cold.2
- ___68+[CCAdminXPCClient performMaintenanceOnAllSets:activity:completion:]_block_invoke
- ___69-[CCSetDonation _mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
- ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke
- ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.57
- ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.57.cold.1
- ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.cold.1
- ___76-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:usingBlock:]_block_invoke
- ___83-[CCDonateXPCClient mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
- ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke
- ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.17
- ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.20
- ___block_descriptor_40_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32s_e50_v24?0"NSObject<CCAdminServiceServer>"8?<v?S>16ls32l8
- ___block_descriptor_48_e8_32s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8
- ___block_descriptor_56_e8_32s40s48r_e36_B32?0"CCDatabaseValueRow"8^16^B24lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8s40l8s48l8
- ___block_descriptor_66_e8_32s40s_e70_v24?0"NSObject<CCDonateService>"8?<v?Sq"CCDonateServicePriors">16ls32l8s40l8
- ___block_literal_global.185
- ___block_literal_global.31
- _objc_msgSend$_enumerateReadableSets:resourceOptions:itemType:usingBlock:
- _objc_msgSend$_mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:
- _objc_msgSend$activityName
- _objc_msgSend$criterionWithColumnName:NOTEQUALSColumnValue:
- _objc_msgSend$debugDescription
- _objc_msgSend$didDefer
- _objc_msgSend$emptyResult
- _objc_msgSend$enumerateReadableSets:withOptions:itemType:usingBlock:
- _objc_msgSend$initWithActivity:activityName:
- _objc_msgSend$initWithClientId:activity:
- _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:
- _objc_msgSend$performMaintenanceOnAllSets:activity:completion:
- _objc_msgSend$runNightlyMaintenanceActivity:completion:
- _objc_msgSend$selectLocalSourceVersionInDatabase:error:
- _objc_release_x2
- _xpc_activity_get_state
- _xpc_activity_register
CStrings:
+ "%@"
+ "%@: %@"
+ "%s activated with listener: %@"
+ "%s received new connection request from %s(%d)"
+ "%s refusing connection from %{public}s, process is not biomesyncd"
+ "%s: %s: expiration handler fired"
+ "%s: cancelled"
+ "%s: done"
+ "%s: performNightlyMaintenance"
+ "%s: registering all tasks."
+ "%s: running..."
+ "%s: task failed to set retry: %@"
+ "/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks"
+ "3"
+ "@\"<CCSetBookkeeping>\""
+ "@\"CCMaintenanceServer\""
+ "@\"CCScheduledTasks\""
+ "@\"NSDate\"24@0:8@\"BMResourceContainer\"16"
+ "@\"_PASLock\""
+ "@32@0:8@16@?24"
+ "@60@0:8Q16Q24@32@40@48S56"
+ "B28@0:8S16^@20"
+ "B32@0:8^B16^@24"
+ "B40@0:8@\"BMResourceContainer\"16@\"NSDate\"24^@32"
+ "B40@0:8^B16@24^@32"
+ "B44@0:8^@16C24@28@?36"
+ "B44@0:8^@16S24@28@?36"
+ "B48@0:8@16@24B32B36^@40"
+ "B52@0:8@16C24@28@36@44"
+ "B8@?0"
+ "CCMaintenanceClient"
+ "CCMaintenanceClient performNightlyMaintenance completed"
+ "CCMaintenanceClient performNightlyMaintenance failed: %@"
+ "CCMaintenanceClient performNightlyMaintenance starting"
+ "CCMaintenanceProtocol"
+ "CCMaintenanceServer"
+ "CCMaintenanceServerProtocol"
+ "CCScheduledTaskState"
+ "CCScheduledTasks"
+ "CCSetBookkeeping"
+ "CCSetStoreAdminService"
+ "CCSetStoreAdminServiceClient"
+ "CCSetStoreAdminServiceServer"
+ "CCSetStoreAdminXPCClient"
+ "CCSetStoreAdminXPCClient shouldDeferBlock: %d"
+ "Cannot expire local device record: %@ with deviceUUID: %@. %@"
+ "Cannot request access for user-domain resource: %@ as persona: %@"
+ "CascadeSets.MaintenanceServer"
+ "CascadeSets.ScheduledTaskState"
+ "CascadeSets.ScheduledTasks"
+ "DeltaMerge"
+ "DeviceAttestation"
+ "DeviceExpiration"
+ "Enumerated %lu readable sets for internal process with result: %@"
+ "Failed to check for local source donation: %@"
+ "Failed to check for present content: %@"
+ "Failed to prepare container %@ when looking up last maintenance date"
+ "Failed to prepare container %@ when setting last maintenance date"
+ "Found no device record to expire with deviceUUID: %@. %@"
+ "Ignoring registration of relayed device site %@ matching peerDeviceUUID: %@. %@"
+ "MaintenanceServer.performNightlyMaintenance"
+ "No such set: %@ - %@"
+ "Running default maintenance"
+ "Running default maintenance as persona: %s"
+ "Select %@ returned invalid row: %@"
+ "Set contains present content - not eligible for tombstone"
+ "Set has received a local source donation - not eligible for tombstone"
+ "Set not discoverable: %@ - %@"
+ "Skipping access request: %@"
+ "T@\"<CCSetBookkeeping>\",N,R,VsetBookkeeping"
+ "T@\"BMXPCListener\",N,R,Vlistener"
+ "T@\"NSString\",N,R"
+ "TS,R,N,V_options"
+ "Unexpected peer device site %@ not matching peerDeviceUUID: %@. %@"
+ "Unsupported remote update type: %u"
+ "Vv36@0:8S16@\"NSString\"20@?<v@?S>28"
+ "Vv36@0:8S16@20@?28"
+ "Vv56@0:8S16@\"NSString\"20Q28@\"NSString\"36S44@?<v@?Sq@\"CCDonateServicePriors\">48"
+ "Vv56@0:8S16@20Q28@36S44@?48"
+ "_maintenanceServer"
+ "_performNightlyMaintenanceSynchronously:completion:"
+ "_remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
+ "_scheduledTasks"
+ "_setBookkeeping"
+ "_shouldDeferBlock"
+ "checkForLocalSourceDonation:error:"
+ "checkForPresentContent:filterByDeviceRowId:error:"
+ "com.apple.cascade.CCMaintenanceClient"
+ "com.apple.cascade.Maintenance"
+ "com.apple.cascade.database-maintenance.nightly-task"
+ "deviceUUID: %@ record already expired: %@. %@"
+ "enumerateAllSets:withOptions:setIdentifiers:usingBlock:"
+ "enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:"
+ "expireRemoteDeviceUUID:"
+ "expired"
+ "init()"
+ "initWithClientId:shouldDeferBlock:"
+ "initWithGuardedData:"
+ "initWithIdentifier:setBookkeeping:"
+ "initWithQueue:setBookkeeping:"
+ "initWithSetBookkeeping:"
+ "isExpired"
+ "lastMaintenanceDateForResourceContainer:"
+ "listener"
+ "machService"
+ "performMaintenanceOnAllSets:clientId:shouldDeferBlock:"
+ "performNightlyDatabaseMaintenance"
+ "performNightlyDatabaseMaintenanceWithCompletionHandler:"
+ "performNightlyMaintenanceWithCompletion:"
+ "performNightlyMaintenanceWithCompletionHandler:"
+ "performNightlyMaintenanceWithError:"
+ "protocol"
+ "register"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:"
+ "remoteObjectInterface"
+ "remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:"
+ "remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
+ "runWithLockAcquired:"
+ "serviceThrowingRequest:completion:usingBlock:"
+ "setBookkeeping"
+ "setExpirationHandler:"
+ "setLastMaintenanceDateForResourceContainer:date:error:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setWithArray:"
+ "sharedScheduler"
+ "start"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@?0@\"NSObject<CCMaintenanceServerProtocol>\"8@?<v@?@\"NSError\">16"
+ "v24@?0@\"NSObject<CCSetStoreAdminServiceServer>\"8@?<v@?S>16"
+ "v28@0:8B16@?20"
+ "v60@0:8@\"NSUUID\"16S24@\"CKMergeableDelta\"28@\"CCDeviceSite\"36@\"NSArray\"44@?<v@?S>52"
+ "v60@0:8@16S24@28@36@44@?52"
+ "v80@0:8S16@20Q28@36S44@48@56Q64@?72"
+ "writeUpdatedObject:forKey:error:"
- " as persona: %@"
- "#"
- "%@ nightly maintenance"
- "@\"BMXPCActivity\""
- "@64@0:8Q16Q24@32@40@48Q56"
- "B32@0:8Q16^@24"
- "B40@0:8@16B24B28^@32"
- "B40@0:8^@16C24S28@?32"
- "CCAdminService"
- "CCAdminServiceClient"
- "CCAdminServiceServer"
- "CCAdminXPCClient"
- "CCDatabaseEmptyAccess"
- "Deferred uncompleted"
- "Enumerated %lu readable sets for datavault-entitled process with result: %@"
- "Failed to select local source version for tombstone eligibility: %@"
- "Finished running activity \"com.apple.cascade.database-maintenance\""
- "Provenance table contains nonzero records - not eligible for tombstone"
- "Returning %@ for set: %@ - %@"
- "Returning empty results."
- "Running activity \"com.apple.cascade.database-maintenance\""
- "Running default maintenance%@"
- "Select %@ returned invalid row: %@, %@"
- "Skipping access request for user-domain resource: %@ as persona: %@"
- "Starting nightly maintenance"
- "TQ,R,N,V_options"
- "Vv40@0:8Q16@\"NSString\"24@?<v@?S>32"
- "Vv40@0:8Q16@24@?32"
- "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?Sq@\"CCDonateServicePriors\">52"
- "Vv60@0:8S16@20Q28@36Q44@?52"
- "_activity"
- "_enumerateReadableSets:resourceOptions:itemType:usingBlock:"
- "_mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
- "activityName"
- "com.apple.cascade.database-maintenance"
- "didDefer"
- "enumerateReadableSets:withOptions:itemType:usingBlock:"
- "initWithActivity:activityName:"
- "initWithClientId:activity:"
- "mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:"
- "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:"
- "performMaintenanceOnAllSets:activity:completion:"
- "registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:"
- "registerXPCActivities"
- "runNightlyMaintenanceActivity:completion:"
- "v24@?0@\"NSObject<CCAdminServiceServer>\"8@?<v@?S>16"
- "v48@0:8@\"CKMergeableDelta\"16@\"CCDeviceSite\"24@\"NSArray\"32@?<v@?S>40"
- "v48@0:8@16@24@32@?40"
- "v84@0:8S16@20Q28@36Q44@52@60Q68@?76"

```

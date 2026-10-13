## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-627.10.51.0.0
-  __TEXT.__text: 0x47918
+627.11.4.0.0
+  __TEXT.__text: 0x4e958
   __TEXT.__lazy_helpers: 0x5d4
-  __TEXT.__objc_methlist: 0x6840
-  __TEXT.__const: 0x252
-  __TEXT.__oslogstring: 0x6db4
-  __TEXT.__cstring: 0x3752
-  __TEXT.__gcc_except_tab: 0xb60
-  __TEXT.__unwind_info: 0x1890
+  __TEXT.__objc_methlist: 0x69e0
+  __TEXT.__const: 0x33a
+  __TEXT.__oslogstring: 0x722e
+  __TEXT.__cstring: 0x3896
+  __TEXT.__gcc_except_tab: 0xbd4
+  __TEXT.__swift5_typeref: 0xbb
+  __TEXT.__constg_swiftt: 0x88
+  __TEXT.__swift5_reflstr: 0x41
+  __TEXT.__swift5_fieldmd: 0x68
+  __TEXT.__swift5_capture: 0x74
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__swift_as_cont: 0x44
+  __TEXT.__unwind_info: 0x1ac8
+  __TEXT.__eh_frame: 0x5b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16b8
-  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__const: 0x1740
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3310
+  __DATA_CONST.__objc_selrefs: 0x3390
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x470
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x4ac0
-  __AUTH_CONST.__objc_const: 0xa208
+  __DATA_CONST.__got: 0x518
+  __AUTH_CONST.__const: 0x5b8
+  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__objc_const: 0xa4b0
   __AUTH_CONST.__lazy_load_got: 0x88
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1860
-  __DATA.__objc_ivar: 0x6a0
-  __DATA.__data: 0xa94
+  __AUTH_CONST.__auth_got: 0x680
+  __AUTH.__objc_data: 0x1a08
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x6ac
+  __DATA.__data: 0xb24
+  __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/FindMyDeviceAccessories.framework/FindMyDeviceAccessories
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote

   - /System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
+  - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2150
-  Symbols:   3741
-  CStrings:  1309
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 2267
+  Symbols:   3872
+  CStrings:  1342
 
Symbols:
+ -[TVRCDeviceQuery discoverySources]
+ -[TVRCDeviceQuery init]
+ -[TVRCDeviceQuery setDiscoverySources:]
+ -[TVRCMatchPointDeviceImpl discoverySource]
+ -[TVRCRPCompanionLinkClientWrapper _fetchAndUpdateSiriStatus]
+ -[TVRCRPCompanionLinkClientWrapper _resolveFindMyRemoteSupportForDevice:]
+ -[TVRCRPCompanionLinkClientWrapper _setFindMyRemoteSupport:]
+ -[TVRCRPCompanionLinkClientWrapper _startMonitoringSiriStatus]
+ -[TVRCRPCompanionLinkClientWrapper _stopMonitoringSiriStatus]
+ -[TVRCRPCompanionLinkClientWrapper setFindMyRemoteSupport:]
+ -[TVRCRapportDeviceImpl discoverySource]
+ -[TVRCXPCClient _beginDeviceQueryWithSources:response:]
+ -[TVRCXPCClient _startDeviceQueryRetryTimerWithEventHandler:]
+ -[TVRCXPCClient beginDeviceQueryWithSources:response:]
+ -[TVRXDevice discoverySource]
+ -[TVRXDeviceQuery _stopSearchForSources:]
+ -[TVRXDeviceQuery addDiscoverySources:]
+ -[TVRXDeviceQuery discoverySources]
+ -[TVRXDeviceQuery removeDiscoverySources:]
+ -[TVRXDeviceQuery setDiscoverySources:]
+ GCC_except_table10
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table110
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table130
+ GCC_except_table140
+ GCC_except_table147
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table32
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table8
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table97
+ _OBJC_CLASS_$_TVRCFindMyRemoteInfo
+ _OBJC_CLASS_$_TVRCFindMySupportManager
+ _OBJC_IVAR_$_TVRCDeviceQuery._discoverySources
+ _OBJC_IVAR_$_TVRCRPCompanionLinkClientWrapper._findMyRemoteSupport
+ _OBJC_IVAR_$_TVRXDeviceQuery._discoverySources
+ _OBJC_METACLASS_$_TVRCFindMyRemoteInfo
+ _OBJC_METACLASS_$_TVRCFindMySupportManager
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_TVRCFindMySupportManager
+ __CLASS_PROPERTIES_TVRCFindMySupportManager
+ __DATA_TVRCFindMyRemoteInfo
+ __DATA_TVRCFindMySupportManager
+ __INSTANCE_METHODS_TVRCFindMyRemoteInfo
+ __INSTANCE_METHODS_TVRCFindMySupportManager
+ __IVARS_TVRCFindMyRemoteInfo
+ __IVARS_TVRCFindMySupportManager
+ __METACLASS_DATA_TVRCFindMyRemoteInfo
+ __METACLASS_DATA_TVRCFindMySupportManager
+ __PROPERTIES_TVRCFindMyRemoteInfo
+ __TVRCFindMyLog
+ ___48-[TVRCRPCompanionLinkClientWrapper setDelegate:]_block_invoke
+ ___54-[TVRCXPCClient beginDeviceQueryWithSources:response:]_block_invoke
+ ___55-[TVRCXPCClient _beginDeviceQueryWithSources:response:]_block_invoke
+ ___55-[TVRCXPCClient _beginDeviceQueryWithSources:response:]_block_invoke_2
+ ___61-[TVRCRPCompanionLinkClientWrapper _fetchAndUpdateSiriStatus]_block_invoke
+ ___61-[TVRCXPCClient _startDeviceQueryRetryTimerWithEventHandler:]_block_invoke
+ ___62-[TVRCRPCompanionLinkClientWrapper _startMonitoringSiriStatus]_block_invoke
+ ___73-[TVRCRPCompanionLinkClientWrapper _resolveFindMyRemoteSupportForDevice:]_block_invoke
+ ____TVRCFindMyLog_block_invoke
+ ___block_descriptor_40_e8_32s_e28_q16?0"TVRCSiriRemoteInfo"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e42_v24?0"TVRCFindMyRemoteInfo"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10Tm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_value_buffer
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_TVRemoteCore
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _dispatch_assert_queue$V2
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _swift_allocError
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x8
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_future_wait_throwing
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SS
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ScTy___________pGSg 23FindMyDeviceAccessories22LocalFindableAccessoryV13LiveInterfaceC s5ErrorP
+ _symbolic Si
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 12TVRemoteCore16FindMyRemoteInfoC
+ _symbolic _____ 12TVRemoteCore20FindMySupportManagerC
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____SgSo7NSErrorCSgIeyByy_ 12TVRemoteCore16FindMyRemoteInfoC
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic ytIeAgHr_
- -[TVRCRPCompanionLinkClientWrapper _findMyRemoteSupportForDevice:]
- -[TVRCXPCClient _beginDeviceQueryWithResponse:]
- -[TVRCXPCClient _startDeviceQueryRetryTimerWithEventHander:]
- -[TVRCXPCClient beginDeviceQueryWithResponse:]
- -[TVRXDeviceQuery _stopSearch]
- GCC_except_table106
- GCC_except_table116
- GCC_except_table121
- GCC_except_table126
- GCC_except_table132
- GCC_except_table143
- GCC_except_table148
- GCC_except_table15
- GCC_except_table33
- GCC_except_table45
- GCC_except_table82
- GCC_except_table84
- GCC_except_table93
- GCC_except_table96
- GCC_except_table98
- ___46-[TVRCXPCClient beginDeviceQueryWithResponse:]_block_invoke
- ___47-[TVRCXPCClient _beginDeviceQueryWithResponse:]_block_invoke
- ___47-[TVRCXPCClient _beginDeviceQueryWithResponse:]_block_invoke_2
- ___60-[TVRCXPCClient _startDeviceQueryRetryTimerWithEventHander:]_block_invoke
CStrings:
+ "(unknown: 0x%lx)"
+ "-[TVRCRPCompanionLinkClientWrapper _startMonitoringSiriStatus]"
+ "-[TVRCRPCompanionLinkClientWrapper _stopMonitoringSiriStatus]"
+ "1"
+ "3"
+ "<TVRCFindMyRemoteInfo systemVersion: "
+ "<TVRXDeviceQuery %p> dropping %lu device(s) no longer covered by discovery sources %{public}@."
+ "<TVRXDeviceQuery %p> has MatchPoint enabled."
+ "<TVRXDeviceQuery %p> skipping MatchPoint discovery"
+ "<TVRXDeviceQuery %p> skipping Rapport discovery"
+ "<TVRXDeviceQuery %p> starting search with discovery sources %{public}@."
+ "<TVRXDeviceQuery %p> stopping search for discovery sources %{public}@."
+ "All"
+ "Asking tvremoted to begin device query with discovery sources %{public}@ remoteObject:%@"
+ "Companion"
+ "Connected to LocalFindableAccessory Interface"
+ "Device query already active in this process; this query's discovery sources (%{public}@) will be ignored"
+ "Failed to get paired remote for %s - %@"
+ "Find my remote for %{public}@: %@ - support: %@"
+ "Lost connection to findmydeviced, reconnecting - %{public}@"
+ "No find my remote for device: %{public}@ - error: %{public}@"
+ "Not starting device query: discovery sources %{public}@ contain no known source"
+ "Paired remote for %{public}@ is the newest remote, not offering the legacy find my experience"
+ "Received SiriStatusInfo: %@"
+ "Resolving findmy support for %@"
+ "TVRemoteCore.FindMyRemoteInfo"
+ "Updating deviceState: %@ of discovered device:%@"
+ "Using legacy find my support check for %{public}@: %@ - device capability: %{bool}d, paired remote supports find my: %{bool}d"
+ "accessories %@"
+ "init()"
+ "paired remote : %s"
+ "q16@?0@\"TVRCSiriRemoteInfo\"8"
+ "shared remote: %s"
+ "v24@?0@\"TVRCFindMyRemoteInfo\"8@\"NSError\"16"
+ "|"
- "Asking tvremoted to begin device query with remoteObject:%@"
- "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d, paired remote productID: %@"
```

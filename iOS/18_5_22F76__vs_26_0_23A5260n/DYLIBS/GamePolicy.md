## GamePolicy

> `/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy`

```diff

-2.5.2.0.0
-  __TEXT.__text: 0x169c0
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x9ac
-  __TEXT.__const: 0xdcc
-  __TEXT.__cstring: 0x1611
-  __TEXT.__oslogstring: 0x27
-  __TEXT.__swift5_typeref: 0x3df
-  __TEXT.__swift5_reflstr: 0x5db
+3.0.15.1.0
+  __TEXT.__text: 0x1eba4
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0xd64
+  __TEXT.__const: 0x121c
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__cstring: 0x1c21
+  __TEXT.__dlopen_cstrs: 0x66
+  __TEXT.__oslogstring: 0x7e
+  __TEXT.__swift5_typeref: 0x4e7
+  __TEXT.__swift5_reflstr: 0x72b
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__constg_swiftt: 0xa98
+  __TEXT.__constg_swiftt: 0xcd4
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_fieldmd: 0x774
+  __TEXT.__swift5_fieldmd: 0x8e8
   __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x88
+  __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x96f
-  __TEXT.__objc_methtype: 0x5f
-  __TEXT.__objc_stubs: 0x340
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x60
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__eh_frame: 0x38
+  __TEXT.__objc_classname: 0xac
+  __TEXT.__objc_methname: 0xed5
+  __TEXT.__objc_methtype: 0xf8
+  __TEXT.__objc_stubs: 0x740
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d0
-  __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH_CONST.__const: 0x4d8
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x17f8
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0x2140
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf88
-  __AUTH.__data: 0x2a8
-  __DATA.__data: 0x408
-  __DATA.__bss: 0xfd0
-  __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_data: 0x528
-  __DATA_DIRTY.__data: 0x470
+  __AUTH.__objc_data: 0x14c0
+  __AUTH.__data: 0x4c8
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__data: 0x5f0
+  __DATA.__bss: 0xfe0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x540
+  __DATA_DIRTY.__data: 0x4d8
   __DATA_DIRTY.__bss: 0x48
-  __DATA_DIRTY.__common: 0x100
+  __DATA_DIRTY.__common: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C05E9C73-640E-342A-8CF7-351E641CE61B
-  Functions: 897
-  Symbols:   612
-  CStrings:  278
+  UUID: DEE8207C-00C1-3C80-B8BF-F30998285F2D
+  Functions: 1254
+  Symbols:   939
+  CStrings:  402
 
Symbols:
+ +[GPGameCenterMediator launchApp]
+ +[GPGameCenterMediator launchOverlayForGameBundleId:]
+ +[GPGameLibrary library]
+ +[GPUserExperienceProxy proxy]
+ -[GPGameLibrary .cxx_destruct]
+ -[GPGameLibrary _onqueue_connectToXPCService]
+ -[GPGameLibrary appsWithBundleIdentifiers:]
+ -[GPGameLibrary appsWithStoreIdentifiers:]
+ -[GPGameLibrary dealloc]
+ -[GPGameLibrary fetchAppsWithBundleIdentifiers:completionHandler:]
+ -[GPGameLibrary fetchAppsWithStoreIdentifiers:completionHandler:]
+ -[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]
+ -[GPGameLibrary init]
+ -[GPGameLibrary installedGames]
+ -[GPGameLibrary pong]
+ -[GPGameLibrary pong].cold.1
+ -[GPGameLibraryApp .cxx_destruct]
+ -[GPGameLibraryApp adamID]
+ -[GPGameLibraryApp bundleID]
+ -[GPGameLibraryApp initWithBundleID:adamID:isGame:]
+ -[GPGameLibraryApp isGame]
+ -[GPUserExperienceProxy launchGameOverlayWithOptions:reply:]
+ -[GPUserExperienceProxy launchGameOverlay]
+ -[GPUserExperienceProxy launchGamesApp]
+ GCC_except_table1
+ GCC_except_table2
+ GCC_except_table3
+ _GameCenterFoundationLibrary
+ _GameCenterFoundationLibrary.cold.1
+ _GameCenterFoundationLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_GPGameCenterMediator
+ _OBJC_CLASS_$_GPGameLibrary
+ _OBJC_CLASS_$_GPGameLibraryApp
+ _OBJC_CLASS_$_GPUserExperienceProxy
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__TtC10GamePolicy14FrontmostGrant
+ _OBJC_CLASS_$__TtC10GamePolicy15FullScreenGrant
+ _OBJC_CLASS_$__TtC10GamePolicy15GameLibraryGame
+ _OBJC_CLASS_$__TtC10GamePolicy26GamePolicyPrivilegedAppXPC
+ _OBJC_CLASS_$__TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_GPGameLibrary._daemonConnection
+ _OBJC_IVAR_$_GPGameLibrary._invalidated
+ _OBJC_IVAR_$_GPGameLibrary._lock
+ _OBJC_IVAR_$_GPGameLibrary._queue
+ _OBJC_IVAR_$_GPGameLibraryApp._adamID
+ _OBJC_IVAR_$_GPGameLibraryApp._bundleID
+ _OBJC_IVAR_$_GPGameLibraryApp._isGame
+ _OBJC_METACLASS_$_GPGameCenterMediator
+ _OBJC_METACLASS_$_GPGameLibrary
+ _OBJC_METACLASS_$_GPGameLibraryApp
+ _OBJC_METACLASS_$_GPUserExperienceProxy
+ _OBJC_METACLASS_$__TtC10GamePolicy14FrontmostGrant
+ _OBJC_METACLASS_$__TtC10GamePolicy15FullScreenGrant
+ _OBJC_METACLASS_$__TtC10GamePolicy15GameLibraryGame
+ _OBJC_METACLASS_$__TtC10GamePolicy26GamePolicyPrivilegedAppXPC
+ _OBJC_METACLASS_$__TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_0
+ __Block_copy
+ __Block_object_dispose
+ __Block_release
+ __CLASS_METHODS__TtC10GamePolicy14FrontmostGrant
+ __CLASS_METHODS__TtC10GamePolicy15FullScreenGrant
+ __CLASS_METHODS__TtC10GamePolicy15GameLibraryGame
+ __CLASS_METHODS__TtC10GamePolicy26GamePolicyPrivilegedAppXPC
+ __CLASS_METHODS__TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge
+ __CLASS_PROPERTIES__TtC10GamePolicy14FrontmostGrant
+ __CLASS_PROPERTIES__TtC10GamePolicy15FullScreenGrant
+ __CLASS_PROPERTIES__TtC10GamePolicy15GameLibraryGame
+ __DATA__TtC10GamePolicy14FrontmostGrant
+ __DATA__TtC10GamePolicy15FullScreenGrant
+ __DATA__TtC10GamePolicy15GameLibraryGame
+ __DATA__TtC10GamePolicy26GamePolicyPrivilegedAppXPC
+ __DATA__TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy
+ __DATA__TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge
+ __INSTANCE_METHODS__TtC10GamePolicy14FrontmostGrant
+ __INSTANCE_METHODS__TtC10GamePolicy15FullScreenGrant
+ __INSTANCE_METHODS__TtC10GamePolicy15GameLibraryGame
+ __INSTANCE_METHODS__TtC10GamePolicy26GamePolicyPrivilegedAppXPC
+ __INSTANCE_METHODS__TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy
+ __INSTANCE_METHODS__TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge
+ __IVARS__TtC10GamePolicy15GameLibraryGame
+ __IVARS__TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy
+ __METACLASS_DATA__TtC10GamePolicy14FrontmostGrant
+ __METACLASS_DATA__TtC10GamePolicy15FullScreenGrant
+ __METACLASS_DATA__TtC10GamePolicy15GameLibraryGame
+ __METACLASS_DATA__TtC10GamePolicy26GamePolicyPrivilegedAppXPC
+ __METACLASS_DATA__TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy
+ __METACLASS_DATA__TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_GPGameCenterMediator
+ __OBJC_$_CLASS_METHODS_GPGameLibrary
+ __OBJC_$_CLASS_METHODS_GPUserExperienceProxy
+ __OBJC_$_INSTANCE_METHODS_GPGameLibrary
+ __OBJC_$_INSTANCE_METHODS_GPGameLibraryApp
+ __OBJC_$_INSTANCE_METHODS_GPUserExperienceProxy
+ __OBJC_$_INSTANCE_VARIABLES_GPGameLibrary
+ __OBJC_$_INSTANCE_VARIABLES_GPGameLibraryApp
+ __OBJC_$_PROP_LIST_GPGameLibraryApp
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __OBJC_CLASS_PROTOCOLS_$_GPGameLibrary
+ __OBJC_CLASS_RO_$_GPGameCenterMediator
+ __OBJC_CLASS_RO_$_GPGameLibrary
+ __OBJC_CLASS_RO_$_GPGameLibraryApp
+ __OBJC_CLASS_RO_$_GPUserExperienceProxy
+ __OBJC_LABEL_PROTOCOL_$__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __OBJC_METACLASS_RO_$_GPGameCenterMediator
+ __OBJC_METACLASS_RO_$_GPGameLibrary
+ __OBJC_METACLASS_RO_$_GPGameLibraryApp
+ __OBJC_METACLASS_RO_$_GPUserExperienceProxy
+ __OBJC_PROTOCOL_$__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __PROPERTIES__TtC10GamePolicy14FrontmostGrant
+ __PROPERTIES__TtC10GamePolicy15FullScreenGrant
+ __PROPERTIES__TtC10GamePolicy15GameLibraryGame
+ __PROTOCOLS__GamePolicyAssertion_Attribute.15
+ __PROTOCOLS__TtC10GamePolicy14GameModeStatus.11
+ __PROTOCOLS__TtC10GamePolicy15GameLibraryGame
+ __PROTOCOLS__TtC10GamePolicy15GameLibraryGame.2
+ __PROTOCOLS__TtC10GamePolicy18GameModeCCUIStatus.61
+ __PROTOCOLS__TtC10GamePolicy19GamePolicyAssertion.9
+ __PROTOCOLS__TtC10GamePolicy21GamePolicyAgentUpdate.4
+ __PROTOCOLS__TtC10GamePolicy22GameModeCCUIStatusInfo.45
+ __PROTOCOLS__TtC10GamePolicy24GameModeCCUIStatusBundle.55
+ __PROTOCOLS__TtC10GamePolicy28GameModeCCUIStatusBundleInfo.39
+ __PROTOCOLS__TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy
+ __PROTOCOLS__TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy.9
+ __PROTOCOLS__TtC10GamePolicy31ModelManagerGameAssertionStatus.11
+ __PROTOCOLS___GamePolicyAgentUpdateGameEvent.10
+ __PROTOCOL_INSTANCE_METHODS__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __PROTOCOL_INSTANCE_METHODS__TtP10GamePolicy29GamePolicyPrivilegedAppServer_
+ __PROTOCOL_METHOD_TYPES__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __PROTOCOL_METHOD_TYPES__TtP10GamePolicy29GamePolicyPrivilegedAppServer_
+ __PROTOCOL__TtP10GamePolicy29GamePolicyPrivilegedAppClient_
+ __PROTOCOL__TtP10GamePolicy29GamePolicyPrivilegedAppServer_
+ __Unwind_Resume
+ ___21-[GPGameLibrary init]_block_invoke
+ ___31-[GPGameLibrary installedGames]_block_invoke
+ ___31-[GPGameLibrary installedGames]_block_invoke_2
+ ___42-[GPGameLibrary appsWithStoreIdentifiers:]_block_invoke
+ ___42-[GPGameLibrary appsWithStoreIdentifiers:]_block_invoke_2
+ ___43-[GPGameLibrary appsWithBundleIdentifiers:]_block_invoke
+ ___43-[GPGameLibrary appsWithBundleIdentifiers:]_block_invoke_2
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.9
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.9.cold.1
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.cold.1
+ ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke
+ ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke_2
+ ___60-[GPUserExperienceProxy launchGameOverlayWithOptions:reply:]_block_invoke
+ ___65-[GPGameLibrary fetchAppsWithStoreIdentifiers:completionHandler:]_block_invoke
+ ___65-[GPGameLibrary fetchAppsWithStoreIdentifiers:completionHandler:]_block_invoke_2
+ ___66-[GPGameLibrary fetchAppsWithBundleIdentifiers:completionHandler:]_block_invoke
+ ___66-[GPGameLibrary fetchAppsWithBundleIdentifiers:completionHandler:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___GameCenterFoundationLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e11_v16?0B8B12ls32l8
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___getGKDaemonProxyClass_block_invoke
+ ___getGKDaemonProxyClass_block_invoke.cold.1
+ ___getGKLocalPlayerClass_block_invoke
+ ___getGKLocalPlayerClass_block_invoke.cold.1
+ ___objc_personality_v0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy25_8
+ __sl_dlopen
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_GamePolicy
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_GamePolicy
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_GamePolicy
+ _audit_stringGameCenterFoundation
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _dispatch_time
+ _flat unique 10GamePolicy0aB20PrivilegedToolServer_p
+ _getGKDaemonProxyClass
+ _getGKDaemonProxyClass.softClass
+ _getGKLocalPlayerClass
+ _getGKLocalPlayerClass.softClass
+ _keypath_get.10Tm
+ _keypath_get.16Tm
+ _keypath_get.20Tm
+ _keypath_get.6Tm
+ _keypath_set.11Tm
+ _keypath_set.17Tm
+ _objc_alloc
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$GamePolicyPrivilegedAppClientInterface
+ _objc_msgSend$GamePolicyPrivilegedAppServerInterface
+ _objc_msgSend$_onqueue_connectToXPCService
+ _objc_msgSend$adamID
+ _objc_msgSend$addObject:
+ _objc_msgSend$bundleID
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$initWithBundleID:adamID:isGame:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isGame
+ _objc_msgSend$launchApp
+ _objc_msgSend$launchGameOverlayWithOptions:reply:
+ _objc_msgSend$launchGamesApp
+ _objc_msgSend$launchOverlayForGameBundleId:
+ _objc_msgSend$local
+ _objc_msgSend$lock
+ _objc_msgSend$ping
+ _objc_msgSend$proxyForPlayer:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$requestInstalledGamesWithAdamIDs:withReply:
+ _objc_msgSend$requestInstalledGamesWithBundleIDs:withReply:
+ _objc_msgSend$requestInstalledGamesWithReply:
+ _objc_msgSend$requestLaunchGameOverlayWithConditional:fallbackToApp:withReply:
+ _objc_msgSend$resume
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$unlock
+ _objc_msgSend$utilityService
+ _objc_release_x25
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x9
+ _objc_storeStrong
+ _swift_allocError
+ _swift_bridgeObjectRetain_n
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_retain
+ _swift_unknownObjectRelease
+ _swift_willThrow
+ _symbolic $s10GamePolicy0aB19PrivilegedAppClientP
+ _symbolic $s10GamePolicy0aB19PrivilegedAppServerP
+ _symbolic SSSg
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic So15NSXPCConnectionC
+ _symbolic So8NSNumberCSg
+ _symbolic _____ 10GamePolicy0a7LibraryA0C
+ _symbolic _____ 10GamePolicy0a7LibraryA0C6ConfigV
+ _symbolic _____ 10GamePolicy0aB16PrivilegedAppXPCC
+ _symbolic _____ 10GamePolicy0aB21DaemonPrivilegedProxyC
+ _symbolic _____ 10GamePolicy0aB27DaemonPrivilegedProxyBridgeC
+ _symbolic _____ 10GamePolicy14FrontmostGrantC
+ _symbolic _____ 10GamePolicy15FullScreenGrantC
+ _symbolic _____AAIeyByy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____Sg 10GamePolicy0a7LibraryA0C6ConfigV
+ _symbolic _____Sg 10GamePolicy0aB11AgentUpdateC0A5EventC
+ _symbolic ______p 10GamePolicy0aB20PrivilegedToolServerP
+ _symbolic _____m 10GamePolicy0a7LibraryA0C
+ _type_layout_string 10GamePolicy0a7LibraryA0C6ConfigV
- __PROTOCOLS__GamePolicyAssertion_Attribute.13
- __PROTOCOLS__TtC10GamePolicy14GameModeStatus.8
- __PROTOCOLS__TtC10GamePolicy18GameModeCCUIStatus.26
- __PROTOCOLS__TtC10GamePolicy19GamePolicyAssertion.8
- __PROTOCOLS__TtC10GamePolicy21GamePolicyAgentUpdate.2
- __PROTOCOLS__TtC10GamePolicy22GameModeCCUIStatusInfo.12
- __PROTOCOLS__TtC10GamePolicy24GameModeCCUIStatusBundle.21
- __PROTOCOLS__TtC10GamePolicy28GameModeCCUIStatusBundleInfo.7
- __PROTOCOLS__TtC10GamePolicy31ModelManagerGameAssertionStatus.9
- __PROTOCOLS___GamePolicyAgentUpdateGameEvent.7
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_GamePolicy
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_GamePolicy
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_GamePolicy
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_GamePolicy
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_GamePolicy
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_GamePolicy
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_GamePolicy
- _objc_msgSend$compare:options:
- _objc_msgSend$sdkVersion
- _objc_retain_x27
CStrings:
+ " userFrontmostGame="
+ "%s"
+ "<FrontmostGrant>"
+ "<FullScreenGrant>"
+ "<GameLibraryGame: "
+ "@\"NSLock\""
+ "@\"NSNumber\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSString\""
+ "@\"NSXPCConnection\""
+ "@36@0:8@16@24B32"
+ "B"
+ "Class getGKDaemonProxyClass(void)_block_invoke"
+ "Class getGKLocalPlayerClass(void)_block_invoke"
+ "Daemon connection interrupted..."
+ "Daemon connection invalidated..."
+ "Error: unable to receive response from gamepolicyd"
+ "GKDaemonProxy"
+ "GKLocalPlayer"
+ "GPGameCenterMediator"
+ "GPGameCenterMediator.m"
+ "GPGameLibrary"
+ "GPGameLibrary: pong!"
+ "GPGameLibraryApp"
+ "GPUserExperienceProxy"
+ "GamePolicy.GameLibraryGame"
+ "GamePolicyPrivilegedAppClientInterface"
+ "GamePolicyPrivilegedAppServerInterface"
+ "T@\"NSNumber\",N,R,VadamID"
+ "T@\"NSNumber\",R,N,V_adamID"
+ "T@\"NSString\",R,N,V_bundleID"
+ "TB,N,R,VisGame"
+ "TB,R,N,V_isGame"
+ "Unable to find class %s"
+ "_TtC10GamePolicy14FrontmostGrant"
+ "_TtC10GamePolicy15FullScreenGrant"
+ "_TtC10GamePolicy15GameLibraryGame"
+ "_TtC10GamePolicy26GamePolicyPrivilegedAppXPC"
+ "_TtC10GamePolicy31GamePolicyDaemonPrivilegedProxy"
+ "_TtC10GamePolicy37GamePolicyDaemonPrivilegedProxyBridge"
+ "_TtP10GamePolicy29GamePolicyPrivilegedAppClient_"
+ "_TtP10GamePolicy29GamePolicyPrivilegedAppServer_"
+ "_adamID"
+ "_bundleID"
+ "_daemonConnection"
+ "_invalidated"
+ "_isGame"
+ "_lock"
+ "_onqueue_connectToXPCService"
+ "_queue"
+ "adamID"
+ "addObject:"
+ "allGameBundleIdentifiers"
+ "appsWithBundleIdentifiers:"
+ "appsWithStoreIdentifiers:"
+ "bundleID"
+ "com.apple.GPGameLibrary"
+ "com.apple.gamepolicyctl.statusChanged"
+ "com.apple.gamepolicyctl.xpc"
+ "com.apple.gamepolicyd.app.privileged"
+ "com.apple.gamepolicyd.tool.privileged"
+ "connection"
+ "currentHandler"
+ "defaultCenter"
+ "dynamicSplitterStatus"
+ "fetchAppsWithBundleIdentifiers:completionHandler:"
+ "fetchAppsWithStoreIdentifiers:completionHandler:"
+ "fetchInstalledGamesWithCompletionHandler:"
+ "gameModeStatus"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "initWithBundleID:adamID:isGame:"
+ "initWithMachServiceName:options:"
+ "installedGames"
+ "invalidate"
+ "isGame"
+ "launchApp"
+ "launchGameOverlay"
+ "launchGameOverlayWithConditional:fallbackToApp:withReply:"
+ "launchGameOverlayWithOptions:reply:"
+ "launchGamesApp"
+ "launchOverlayForGameBundleId:"
+ "library"
+ "local"
+ "modelManagerGameAssertionStatus"
+ "perfomanceGamingModeEnabled"
+ "postNotification:"
+ "previousAllGameBundleIdentifiers"
+ "proxy"
+ "proxyForPlayer:"
+ "remoteObjectProxy"
+ "requestInstalledGamesWithAdamIDs:withReply:"
+ "requestInstalledGamesWithBundleIDs:withReply:"
+ "requestInstalledGamesWithReply:"
+ "requestLaunchGameOverlayWithConditional:fallbackToApp:withReply:"
+ "requestLaunchGamesApp"
+ "resume"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setRemoteObjectInterface:"
+ "signalLowPowerModeSuggestion"
+ "sleepForTimeInterval:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation"
+ "stringWithUTF8String:"
+ "sustainedExecutionStatus"
+ "userFrontmostGame"
+ "userPowerPreferencesChangedWithEcoModeBatteryLPM:ecoModeBatteryHPM:ecoModeACPowerLPM:ecoModeACPowerHPM:"
+ "utilityService"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0B8B12"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8B16B20@?24"
+ "v32@0:8B16B20@?<v@?BB>24"
+ "v32@0:8B16B20B24B28"
+ "v32@0:8Q16@?24"
+ "void *GameCenterFoundationLibrary(void)"
- "18.0"
- "compare:options:"
- "sdkVersion"

```

## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-304.3.8.100.0
-  __TEXT.__text: 0x451bc
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0x3340
-  __TEXT.__const: 0x19e
-  __TEXT.__cstring: 0x3fce
-  __TEXT.__oslogstring: 0x3336
-  __TEXT.__gcc_except_tab: 0xec8
-  __TEXT.__unwind_info: 0x12b8
-  __TEXT.__objc_classname: 0x757
-  __TEXT.__objc_methname: 0x77ae
-  __TEXT.__objc_methtype: 0x1337
-  __TEXT.__objc_stubs: 0x5960
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x1388
-  __DATA_CONST.__objc_classlist: 0x1b0
-  __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0xb0
+304.4.11.0.0
+  __TEXT.__text: 0x5d3f4
+  __TEXT.__auth_stubs: 0x18a0
+  __TEXT.__objc_methlist: 0x38b8
+  __TEXT.__const: 0x534
+  __TEXT.__cstring: 0x46ca
+  __TEXT.__oslogstring: 0x3eae
+  __TEXT.__gcc_except_tab: 0xe84
+  __TEXT.__swift5_typeref: 0x44e
+  __TEXT.__swift5_capture: 0x26c
+  __TEXT.__constg_swiftt: 0x164
+  __TEXT.__swift5_reflstr: 0xda
+  __TEXT.__swift5_fieldmd: 0xd8
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__unwind_info: 0x1888
+  __TEXT.__eh_frame: 0xa08
+  __TEXT.__objc_classname: 0x8e7
+  __TEXT.__objc_methname: 0x88f1
+  __TEXT.__objc_methtype: 0x16d1
+  __TEXT.__objc_stubs: 0x6120
+  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__const: 0x13a8
+  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e50
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x2178
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0x210
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0x940
-  __AUTH_CONST.__cfstring: 0x3fa0
-  __AUTH_CONST.__objc_const: 0x8480
+  __DATA_CONST.__objc_arraydata: 0x218
+  __AUTH_CONST.__auth_got: 0xc60
+  __AUTH_CONST.__const: 0x1360
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x9140
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x2f4
-  __DATA.__data: 0x850
+  __AUTH.__objc_data: 0x7b8
+  __AUTH.__data: 0x138
+  __DATA.__objc_ivar: 0x2f0
+  __DATA.__data: 0xd40
   __DATA.__bss: 0xb0
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x1f0
   __DATA_DIRTY.__common: 0xc

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 47277729-DF47-3CF6-B719-EA175B278B6D
-  Functions: 1639
-  Symbols:   5727
-  CStrings:  2943
+  UUID: CF3E32EA-8F89-308A-B9B0-8228A1C82C6B
+  Functions: 2116
+  Symbols:   6331
+  CStrings:  3185
 
Symbols:
+ +[NSUserDefaults(PFUtilities) pf_clearPosterContainerBundleIdentifiers]
+ +[NSUserDefaults(PFUtilities) pf_persistPosterContainerBundleIdentifier:]
+ +[NSUserDefaults(PFUtilities) pf_persistedPosterContainerBundleIdentifiers]
+ +[NSUserDefaults(PFUtilities) pf_unpersistPosterContainerBundleIdentifier:]
+ +[PFPosterExtension extensionForProvider:error:]
+ -[PFPosterArchiver abortWithMessage:]
+ -[PFPosterArchiver processDisallowsAppleArchive]
+ GCC_except_table38
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table68
+ _CFBooleanGetTypeID
+ _CFEqual
+ _CFGetTypeID
+ _CFRelease
+ _OBJC_CLASS_$_ASDApp
+ _OBJC_CLASS_$_ASDAppLibrary
+ _OBJC_CLASS_$_ASDAppQuery
+ _OBJC_CLASS_$_ASDInstallApps
+ _OBJC_CLASS_$_ASDSystemAppMetadata
+ _OBJC_CLASS_$_LSApplicationProxy
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_LSEnumerator
+ _OBJC_CLASS_$_PFDownloadablePosterAppManager
+ _OBJC_CLASS_$_PFPosterSystemAppInstaller
+ _OBJC_METACLASS_$_PFDownloadablePosterAppManager
+ _OBJC_METACLASS_$_PFPosterSystemAppInstaller
+ _OBJC_METACLASS_$__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver
+ _OBJC_METACLASS_$__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _PFDownloadablePosterAppManagerErrorDomain
+ _PFPosterSystemAppInstallErrorDomain
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __Block_copy
+ __Block_release
+ __CATEGORY_INSTANCE_METHODS_LSEnumerator_$_PosterFoundation
+ __CATEGORY_LSEnumerator_$_PosterFoundation
+ __DATA_PFDownloadablePosterAppManager
+ __DATA_PFPosterSystemAppInstaller
+ __DATA__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver
+ __DATA__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver
+ __INSTANCE_METHODS_PFDownloadablePosterAppManager
+ __INSTANCE_METHODS_PFPosterSystemAppInstaller
+ __INSTANCE_METHODS__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver
+ __INSTANCE_METHODS__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver
+ __IVARS_PFDownloadablePosterAppManager
+ __IVARS_PFPosterSystemAppInstaller
+ __IVARS__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver
+ __IVARS__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver
+ __METACLASS_DATA_PFDownloadablePosterAppManager
+ __METACLASS_DATA_PFPosterSystemAppInstaller
+ __METACLASS_DATA__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver
+ __METACLASS_DATA__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver
+ __OBJC_$_INSTANCE_METHODS_NSUserDefaults(PFUtilities|PosterFoundation)
+ __OBJC_$_PROP_LIST_PFPosterAppPersisting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ASDAppQueryResultsObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LSApplicationWorkspaceObserverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PFPosterAppInstallObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PFPosterAppInstalling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PFPosterAppPersisting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDAppQueryResultsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSApplicationWorkspaceObserverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFPosterAppInstallObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFPosterAppInstalling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFPosterAppPersisting
+ __OBJC_$_PROTOCOL_REFS_ASDAppQueryResultsObserver
+ __OBJC_$_PROTOCOL_REFS_LSApplicationWorkspaceObserverProtocol
+ __OBJC_$_PROTOCOL_REFS_PFPosterAppInstallObserver
+ __OBJC_$_PROTOCOL_REFS_PFPosterAppInstalling
+ __OBJC_$_PROTOCOL_REFS_PFPosterAppPersisting
+ __OBJC_CLASS_PROTOCOLS_$_NSUserDefaults(PFUtilities|PosterFoundation)
+ __OBJC_LABEL_PROTOCOL_$_ASDAppQueryResultsObserver
+ __OBJC_LABEL_PROTOCOL_$_LSApplicationWorkspaceObserverProtocol
+ __OBJC_LABEL_PROTOCOL_$_PFPosterAppInstallObserver
+ __OBJC_LABEL_PROTOCOL_$_PFPosterAppInstalling
+ __OBJC_LABEL_PROTOCOL_$_PFPosterAppPersisting
+ __OBJC_PROTOCOL_$_ASDAppQueryResultsObserver
+ __OBJC_PROTOCOL_$_LSApplicationWorkspaceObserverProtocol
+ __OBJC_PROTOCOL_$_PFPosterAppInstallObserver
+ __OBJC_PROTOCOL_$_PFPosterAppInstalling
+ __OBJC_PROTOCOL_$_PFPosterAppPersisting
+ __PROPERTIES_PFDownloadablePosterAppManager
+ __PROTOCOLS_PFDownloadablePosterAppManager
+ __PROTOCOLS_PFDownloadablePosterAppManager.26
+ __PROTOCOLS_PFPosterSystemAppInstaller
+ __PROTOCOLS_PFPosterSystemAppInstaller.19
+ __PROTOCOLS__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver
+ __PROTOCOLS__TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver.15
+ __PROTOCOLS__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver
+ __PROTOCOLS__TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver.21
+ ___48+[PFPosterExtension extensionForProvider:error:]_block_invoke
+ ___57-[PFPosterArchiver _unarchiveWithHandler:manifest:error:]_block_invoke.78
+ ___block_literal_global.137
+ ___block_literal_global.147
+ ___block_literal_global.171
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy16_8
+ ___swift_memcpy4_4
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _block_copy_helper
+ _block_copy_helper.1
+ _block_copy_helper.101
+ _block_copy_helper.122
+ _block_copy_helper.17
+ _block_copy_helper.61
+ _block_copy_helper.7
+ _block_copy_helper.87
+ _block_copy_helper.95
+ _block_descriptor
+ _block_descriptor.103
+ _block_descriptor.124
+ _block_descriptor.19
+ _block_descriptor.3
+ _block_descriptor.63
+ _block_descriptor.89
+ _block_descriptor.9
+ _block_descriptor.97
+ _block_destroy_helper
+ _block_destroy_helper.102
+ _block_destroy_helper.123
+ _block_destroy_helper.18
+ _block_destroy_helper.2
+ _block_destroy_helper.62
+ _block_destroy_helper.8
+ _block_destroy_helper.88
+ _block_destroy_helper.96
+ _bzero
+ _kCFAllocatorDefault
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _keypath_get_selector_configurationDelegate
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$abortWithMessage:
+ _objc_msgSend$applicationState
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$attachToExistingInstallForBundleIdentifier:progressHandler:completion:
+ _objc_msgSend$availableAppsCache
+ _objc_msgSend$availableDownloadablePosterAppBundleIdentifiers
+ _objc_msgSend$bundleIdsWith:
+ _objc_msgSend$configurationDelegate
+ _objc_msgSend$correspondingApplicationRecord
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$executeQueryWithResultHandler:
+ _objc_msgSend$handleInstallCompletionFor:error:
+ _objc_msgSend$handleMonitoredAppStateChangeWithBundleID:app:
+ _objc_msgSend$hasConfiguredCollectionsPostersWithDelegate:
+ _objc_msgSend$hasConfiguredPosterWithDescriptorIdentifier:extensionBundleIdentifier:
+ _objc_msgSend$hasConfiguredPosterWithExtensionBundleIdentifier:
+ _objc_msgSend$hasDownloadAssertionForAppBundleIdentifier:
+ _objc_msgSend$hasParallelPlaceholder
+ _objc_msgSend$hasSystemPlaceholder:
+ _objc_msgSend$initWithAppInstaller:
+ _objc_msgSend$initWithAppInstaller:ownsInstaller:
+ _objc_msgSend$initWithAppInstaller:persistence:
+ _objc_msgSend$initWithAppInstaller:persistence:ownsInstaller:
+ _objc_msgSend$initWithBundleID:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithBundleIdentifierOfSystemPlaceholder:error:
+ _objc_msgSend$installApp:withCompletionHandler:
+ _objc_msgSend$installError
+ _objc_msgSend$installedAppsCache
+ _objc_msgSend$installedDownloadablePosterAppBundleIdentifiers
+ _objc_msgSend$installer
+ _objc_msgSend$installer:didUpdateStateForApp:isInstalled:progress:
+ _objc_msgSend$isInstalled
+ _objc_msgSend$isPlaceholder
+ _objc_msgSend$managementDomain
+ _objc_msgSend$markBundleShouldNotPersistForBundleIdentifier:
+ _objc_msgSend$markBundleShouldPersistForBundleIdentifier:
+ _objc_msgSend$notifyObserversStateChangedFor:isInstalled:progress:
+ _objc_msgSend$ownsInstaller
+ _objc_msgSend$persistedBundleIdentifiers
+ _objc_msgSend$persistence
+ _objc_msgSend$pf_persistPosterContainerBundleIdentifier:
+ _objc_msgSend$pf_persistedPosterContainerBundleIdentifiers
+ _objc_msgSend$pf_unpersistPosterContainerBundleIdentifier:
+ _objc_msgSend$pf_unprotectedUserDefaults
+ _objc_msgSend$processDisallowsAppleArchive
+ _objc_msgSend$queryForBundleIDs:
+ _objc_msgSend$releaseDownloadAssertionForAppBundleIdentifier:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$setAvailableAppsCache:
+ _objc_msgSend$setConfigurationDelegate:
+ _objc_msgSend$setInstalledAppsCache:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$shouldTakeAssertionForCollections
+ _objc_msgSend$startInstallForBundleIdentifier:progressHandler:completion:
+ _objc_msgSend$startMonitoringForBundleIdentifiers:
+ _objc_msgSend$systemPlaceholderEnumerator
+ _objc_msgSend$takeDownloadAssertionForAppBundleIdentifier:
+ _objc_msgSend$uninstallApp:requestUserConfirmation:withResultHandler:
+ _objc_msgSend$uninstallAppWithBundleIdentifier:completion:
+ _objc_msgSend$workspaceObserver
+ _objc_retain_x9
+ _objectdestroy.41Tm
+ _objectdestroy.83Tm
+ _objectdestroyTm
+ _swift_allocBox
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedAsyncMethodErrorTu
+ _swift_dynamicCast
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_endAccess
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_willThrow
+ _symbolic $s16PosterFoundation25ApplicationChangeObserver33_D6DA74298AEDBD6DA21B638912DCDBA0LLP
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SS
+ _symbolic SS3key______5valuet So26PFPosterSystemAppInstallerC16PosterFoundationE13ActiveInstall33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic SS_Sayy______pSgYbcGt s5ErrorP
+ _symbolic SS_ShySSGt
+ _symbolic SS______t So26PFPosterSystemAppInstallerC16PosterFoundationE13ActiveInstall33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic SS_ypt
+ _symbolic SaySSG
+ _symbolic SaySo6ASDAppCG
+ _symbolic SayySo10NSProgressCYbcG
+ _symbolic Sayy______pSgYbcG s5ErrorP
+ _symbolic ScA_pSg
+ _symbolic ScCySaySo6ASDAppCG______pG s5ErrorP
+ _symbolic ScCy___________pG 10Foundation4UUIDV s5ErrorP
+ _symbolic ScPSg
+ _symbolic So10NSProgressCIeghg_
+ _symbolic So10NSProgressCIeyBhy_
+ _symbolic So10NSProgressCSgIeyBy_
+ _symbolic So10NSProgressCytIeghnr_
+ _symbolic So11ASDAppQueryC
+ _symbolic So12LSEnumeratorC
+ _symbolic So26PFPosterSystemAppInstallerC
+ _symbolic So26PFPosterSystemAppInstallerCSgXw
+ _symbolic So26PFPosterSystemAppInstallerCSgXwz_Xx
+ _symbolic So30PFDownloadablePosterAppManagerCSgXw
+ _symbolic So30PFDownloadablePosterAppManagerCSgXwz_Xx
+ _symbolic So6ASDAppCSg
+ _symbolic So7NSErrorCSgIeyBhy_
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 16PosterFoundation27AppStoreDaemonQueryObserver33_D4F3B565C3E3BC45D47D520AF711D59DLLC
+ _symbolic _____ 16PosterFoundation30LSApplicationWorkspaceObserver33_D6DA74298AEDBD6DA21B638912DCDBA0LLC
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ So26PFPosterSystemAppInstallerC16PosterFoundationE09MonitoredC5State33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic _____ So26PFPosterSystemAppInstallerC16PosterFoundationE13ActiveInstall33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg So26PFPosterSystemAppInstallerC16PosterFoundationE13ActiveInstall33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSgIeghg_ s5ErrorP
+ _symbolic ______pSgXw 16PosterFoundation25ApplicationChangeObserver33_D6DA74298AEDBD6DA21B638912DCDBA0LLP
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSShySSGG s18_DictionaryStorageC
+ _symbolic _____ySS_Sayy______pSgYbcGtG s23_ContiguousArrayStorageC s5ErrorP
+ _symbolic _____ySS_ShySSGtG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC So26PFPosterSystemAppInstallerC16PosterFoundationE09MonitoredE5State33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic _____ySS_____G s18_DictionaryStorageC So26PFPosterSystemAppInstallerC16PosterFoundationE13ActiveInstall33_D4F3B565C3E3BC45D47D520AF711D59DLLV
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yySo10NSProgressCYbcG s23_ContiguousArrayStorageC
+ _symbolic _____yy______pSgYbcG s23_ContiguousArrayStorageC s5ErrorP
+ _symbolic _____yyt_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic x
+ _symbolic ySo10NSProgressCYbc
+ _symbolic ySo6ASDAppCYbc
+ _symbolic y______pSgYbc s5ErrorP
+ _symbolic ypSg
+ _symbolic ytIeAgHr_
+ _symbolic yyc
+ _type_layout_string So16os_unfair_lock_sV
+ _type_layout_string So26PFPosterSystemAppInstallerC16PosterFoundationE09MonitoredC5State33_D4F3B565C3E3BC45D47D520AF711D59DLLV
- GCC_except_table66
- _OBJC_IVAR_$_PFPosterArchiver._processHandle
- ___57-[PFPosterArchiver _unarchiveWithHandler:manifest:error:]_block_invoke.63
- ___block_literal_global.134
- ___block_literal_global.144
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithFileManager:processHandle:unarchivingContainerURL:
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "%@"
+ "%s is already installed"
+ "%s is not a deletable system app: %@"
+ "@\"<PFPosterAppInstalling>\""
+ "@\"<PFPosterAppPersisting>\""
+ "@\"_TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver\""
+ "@28@0:8@16B24"
+ "@36@0:8@16@24B32"
+ "ASDAppQueryResultsObserver"
+ "Already monitoring %s"
+ "App %s: hasConfigured=%{bool}d, hasAssertion=%{bool}d, autoRemovable=%{bool}d"
+ "App %s: hasConfiguredPosters=%{bool}d"
+ "Attaching to existing install for %s"
+ "Attempted to attach handlers for %s but no active install found - install likely already completed"
+ "Can't uninstall %s; it's not installed to begin with."
+ "Cancelling pending install for %s due to invalidation"
+ "Checking Collections posters with extension: %s, descriptors: %s"
+ "Checking auto-removable apps from %ld installed downloadable poster apps"
+ "Checking configured posters for app: %s"
+ "Checking if app can be removed: %s"
+ "Collections app has configured posters: %{bool}d"
+ "Collections extension configured but no section descriptors - skipping assertion"
+ "Detected external install for %s - creating tracking entry"
+ "Downloadable poster apps installed/uninstalled: %s"
+ "Extension %s not in hardcoded map - skipping"
+ "Failed to check configured state for %s: %@. Assuming NOT auto-removable to be safe."
+ "Failed to check configured state for %s: %@. Returning false to prevent removal."
+ "Failed to check existing install: %@"
+ "Failed to query app for uninstall %s: %s"
+ "Failed to start monitoring for %s: %s"
+ "Failed to uninstall %s. Error: %@"
+ "Fatal error"
+ "Found configured Collections poster with descriptor: %s"
+ "Found configured poster for extension %s in app %s"
+ "Install cancelled due to invalidation"
+ "Install completed for %s"
+ "Install failed for %s: %s"
+ "Install rejected - installer has been invalidated"
+ "Install started for %s with UUID: %s"
+ "Install succeeded for %s"
+ "Installing app %s"
+ "Invalidating PFDownloadablePosterAppManager"
+ "LSApplicationWorkspaceObserverProtocol"
+ "LaunchServices database rebuilt - invalidating all caches"
+ "Loquat"
+ "Marking bundleIdentifier %s as needing to persist."
+ "Marking bundleIdentifier %s as not needing to persist."
+ "No configuration delegate available to check poster state"
+ "No configurationDelegate - cannot check Collections descriptors, assuming NO"
+ "No configurationDelegate set - cannot check configured posters for %s"
+ "No configured Collections posters found"
+ "No configured posters found for app %s"
+ "No extensions mapped for app %s"
+ "PFDownloadablePosterAppManager"
+ "PFDownloadablePosterAppManager requires entitlements:\n- com.apple.private.coreservices.canmaplsdatabase\n- com.apple.security.exception.mach-lookup.global-name (com.apple.lsd.xpc)"
+ "PFDownloadablePosterAppManagerErrorDomain"
+ "PFPosterAppInstallObserver"
+ "PFPosterAppInstalling"
+ "PFPosterAppPersisting"
+ "PFPosterArchiver: Entitlement '%@' has incorrect type (expected Boolean)"
+ "PFPosterArchiver: Entitlement '%@' is explicitly set to false - remove the entitlement instead"
+ "PFPosterArchiver: Failed to create SecTask from self"
+ "PFPosterSystemAppInstallErrorDomain"
+ "PFPosterSystemAppInstaller"
+ "PersistedPosterContainerBundleIdentifiers"
+ "PosterFoundation.AppStoreDaemonQueryObserver"
+ "PosterFoundation/PFDownloadablePosterAppManager.swift"
+ "Process has disallowed AppleArchive entitlement and thus cannot archive to that format"
+ "Reconnecting to existing install for %s"
+ "Rejecting attach for %s - installer invalidated"
+ "Rejecting install for %s - installer invalidated"
+ "SkipAppAutoUninstall"
+ "Skipping monitoring - installer invalidated"
+ "Started monitoring for %s"
+ "Starting install for %s"
+ "Starting uninstall for %s"
+ "Successfully uninstalled %s."
+ "T@\"<PFPosterAppInstalling>\",N,R,Vinstaller"
+ "T@\"<PFPosterAppPersisting>\",N,R,Vpersistence"
+ "T@\"<PFPosterConfigurationQuerying>\",N,W,VconfigurationDelegate"
+ "T@\"NSArray\",N,C"
+ "T@\"NSArray\",N,R"
+ "T@\"NSSet\",N,R"
+ "T@\"_TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver\",N,R,VworkspaceObserver"
+ "TB,N,R,VownsInstaller"
+ "Taking assertion for Collections (has section descriptors)"
+ "Taking assertion for app %s (extension: %s)"
+ "Taking assertions for extensions: [%s]"
+ "Uninstall failed for %s: %s"
+ "Uninstall succeeded for %s"
+ "Uninstalling app %s"
+ "_TtC16PosterFoundationP33_D4F3B565C3E3BC45D47D520AF711D59D27AppStoreDaemonQueryObserver"
+ "_TtC16PosterFoundationP33_D6DA74298AEDBD6DA21B638912DCDBA030LSApplicationWorkspaceObserver"
+ "_createCheckedThrowingContinuation(_:)"
+ "_lock_activeInstalls"
+ "_lock_isInvalidated"
+ "_lock_monitoredApps"
+ "abortWithMessage:"
+ "appBundleIdentifierForExtension:"
+ "appQuery:resultsDidChange:"
+ "applicationIconDidChange:"
+ "applicationInstallsArePrioritized:arePaused:"
+ "applicationInstallsDidCancel:"
+ "applicationInstallsDidChange:"
+ "applicationInstallsDidPause:"
+ "applicationInstallsDidPrioritize:"
+ "applicationInstallsDidResume:"
+ "applicationInstallsDidStart:"
+ "applicationInstallsDidUpdateIcon:"
+ "applicationState"
+ "applicationStateDidChange:"
+ "applicationsDidChangePersonas:"
+ "applicationsDidFailToInstall:"
+ "applicationsDidFailToUninstall:"
+ "applicationsDidInstall:"
+ "applicationsDidUninstall:"
+ "applicationsDidUpdateMetadata:"
+ "applicationsWillInstall:"
+ "applicationsWillUninstall:"
+ "arrayForKey:"
+ "attachToExistingInstallForBundleIdentifier:progressHandler:completion:"
+ "autoRemovableAppBundleIdentifiers"
+ "availableAppsCache"
+ "availableDownloadablePosterAppBundleIdentifiers"
+ "bundleIdsWith:"
+ "canRemoveApp:"
+ "changeObserver"
+ "checkExistingInstallFor:completionHandler:"
+ "com.apple.EmojiPoster"
+ "com.apple.GradientPoster"
+ "com.apple.HelloPoster"
+ "com.apple.NanoUniverse.AegirProxyApp"
+ "com.apple.Posters"
+ "com.apple.Posters.CollectionsPosterApp"
+ "com.apple.Posters.CollectionsPosterApp.CollectionsPoster"
+ "com.apple.Posters.DownloadablePosterApp.DownloadablePoster"
+ "com.apple.Posters.KaleidoscopePosterApp"
+ "com.apple.Posters.UnityPosterApp"
+ "com.apple.Posters.WeatherPosterApp"
+ "com.apple.PridePoster"
+ "com.apple.lsd.xpc"
+ "com.apple.private.coreservices.canmaplsdatabase"
+ "com.apple.security.exception.mach-lookup.global-name"
+ "configurationDelegate"
+ "correspondingApplicationRecord"
+ "databaseWasRebuilt"
+ "defaultWorkspace"
+ "deviceManagementPolicyDidChange:"
+ "downloadablePosterManager"
+ "enumeratorWithOptions:"
+ "executeQueryWithResultHandler:"
+ "extensionForProvider:error:"
+ "handleInstallCompletionFor:error:"
+ "handleMonitoredAppStateChangeWithBundleID:app:"
+ "handleMonitoringFailureFor:error:"
+ "hasConfiguredCollectionsPostersWithDelegate:"
+ "hasConfiguredPosterWithDescriptorIdentifier:extensionBundleIdentifier:"
+ "hasConfiguredPosterWithExtensionBundleIdentifier:"
+ "hasDownloadAssertionForAppBundleIdentifier:"
+ "hasParallelPlaceholder"
+ "hasSystemPlaceholder:"
+ "helperPlaceholdersInstalled:"
+ "helperPlaceholdersUninstalled:"
+ "init()"
+ "initWithAppInstaller:"
+ "initWithAppInstaller:ownsInstaller:"
+ "initWithAppInstaller:persistence:"
+ "initWithAppInstaller:persistence:ownsInstaller:"
+ "initWithBundleID:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithBundleIdentifierOfSystemPlaceholder:error:"
+ "installApp:progressHandler:completion:"
+ "installApp:withCompletionHandler:"
+ "installError"
+ "installedAppsCache"
+ "installedDownloadablePosterAppBundleIdentifiers"
+ "installer"
+ "installer:didUpdateStateForApp:isInstalled:progress:"
+ "isInstallInProgressForBundleIdentifier:"
+ "isInstalled"
+ "isPlaceholder"
+ "isSADApp:"
+ "managementDomain"
+ "markBundleShouldNotPersistForBundleIdentifier:"
+ "markBundleShouldPersistForBundleIdentifier:"
+ "networkUsageChanged:"
+ "notifyObserversStateChangedFor:isInstalled:progress:"
+ "observeLaunchProhibitedApps"
+ "ownsInstaller"
+ "persistedBundleIdentifiers"
+ "persistence"
+ "pf_clearPosterContainerBundleIdentifiers"
+ "pf_persistPosterContainerBundleIdentifier:"
+ "pf_persistedPosterContainerBundleIdentifiers"
+ "pf_unpersistPosterContainerBundleIdentifier:"
+ "pluginsDidInstall:"
+ "pluginsDidUninstall:"
+ "pluginsWillUninstall:"
+ "processDisallowsAppleArchive"
+ "query"
+ "queryForBundleIDs:"
+ "releaseDownloadAssertionForAppBundleIdentifier:"
+ "setAvailableAppsCache:"
+ "setConfigurationDelegate:"
+ "setInstalledAppsCache:"
+ "setObserver:"
+ "setUserInitiated:"
+ "shouldTakeAssertionForCollections"
+ "startInstallForBundleIdentifier:progressHandler:completion:"
+ "startMonitoringForBundleIdentifiers:"
+ "stateChangeHandler"
+ "systemPlaceholderEnumerator"
+ "takeDownloadAssertionForAppBundleIdentifier:"
+ "takeDownloadAssertionsForExtensionBundleIdentifiers:"
+ "unable to find extension identity for %@"
+ "uninstallApp:completion:"
+ "uninstallApp:requestUserConfirmation:withResultHandler:"
+ "uninstallAppWithBundleIdentifier:completion:"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSProgress\"8"
+ "v24@0:8@\"<PFPosterAppInstallObserver>\"16"
+ "v24@0:8@\"NSArray\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
+ "v32@0:8@\"ASDAppQuery\"16@\"NSArray\"24"
+ "v32@0:8@\"NSArray\"16@\"NSArray\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSProgress\">24"
+ "v36@0:8@16B24@28"
+ "v40@0:8@\"NSString\"16@?<v@?@\"NSProgress\">24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@?24@?32"
+ "v44@0:8@\"<PFPosterAppInstalling>\"16@\"NSString\"24B32@\"NSProgress\"36"
+ "v44@0:8@16@24B32@36"
+ "workspaceObserver"
- "@\"BSProcessHandle\""
- "_processHandle"

```

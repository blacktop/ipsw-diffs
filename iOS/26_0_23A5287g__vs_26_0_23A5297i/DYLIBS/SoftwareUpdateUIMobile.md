## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-508.0.1.502.1
-  __TEXT.__text: 0x66d9c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x23b4
-  __TEXT.__cstring: 0x386e
-  __TEXT.__gcc_except_tab: 0x3b20
-  __TEXT.__oslogstring: 0x5de8
+508.0.30.0.0
+  __TEXT.__text: 0x727e0
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x2634
+  __TEXT.__cstring: 0x3d8b
+  __TEXT.__gcc_except_tab: 0x41cc
+  __TEXT.__oslogstring: 0x7625
+  __TEXT.__dlopen_cstrs: 0x126
   __TEXT.__const: 0x3a0
   __TEXT.__constg_swiftt: 0xfc
-  __TEXT.__swift5_typeref: 0x124
-  __TEXT.__swift5_reflstr: 0xce
-  __TEXT.__swift5_fieldmd: 0x94
+  __TEXT.__swift5_typeref: 0x1d0
+  __TEXT.__swift5_reflstr: 0xee
+  __TEXT.__swift5_fieldmd: 0xa0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xad0
-  __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0x5a5
-  __TEXT.__objc_methname: 0x6910
-  __TEXT.__objc_methtype: 0x18b8
-  __TEXT.__objc_stubs: 0x3b60
-  __DATA_CONST.__got: 0x808
-  __DATA_CONST.__const: 0x6e88
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__swift5_capture: 0x70
+  __TEXT.__unwind_info: 0xc90
+  __TEXT.__eh_frame: 0x1e8
+  __TEXT.__objc_classname: 0x64e
+  __TEXT.__objc_methname: 0x6fc4
+  __TEXT.__objc_methtype: 0x1a54
+  __TEXT.__objc_stubs: 0x4220
+  __DATA_CONST.__got: 0x890
+  __DATA_CONST.__const: 0x74b0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1598
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x48
-  __AUTH_CONST.__cfstring: 0x1ac0
-  __AUTH_CONST.__objc_const: 0x7118
-  __AUTH.__objc_data: 0xb28
-  __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x21c
-  __DATA.__data: 0xb38
-  __DATA.__bss: 0x300
+  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__objc_const: 0x7a98
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0xbd0
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x234
+  __DATA.__data: 0xcb0
+  __DATA.__bss: 0x360
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81681B19-23FF-3A91-A5AE-BA17BCFC45AB
-  Functions: 800
-  Symbols:   6339
-  CStrings:  1897
+  UUID: 951FF9DF-4D0A-3D41-800A-1928CB3FACEA
+  Functions: 914
+  Symbols:   6836
+  CStrings:  2074
 
Symbols:
+ +[SUUIMobileAutomationManager sharedManager]
+ +[SUUIMobileUserDefaultsBasedTestSession current]
+ -[SUUIMobileAutomationManager .cxx_destruct]
+ -[SUUIMobileAutomationManager currentSession]
+ -[SUUIMobileAutomationManager dealloc]
+ -[SUUIMobileAutomationManager descriptionDictionary]
+ -[SUUIMobileAutomationManager description]
+ -[SUUIMobileAutomationManager enabled]
+ -[SUUIMobileAutomationManager init]
+ -[SUUIMobileAutomationManager initialize]
+ -[SUUIMobileAutomationManager notifyObserversOfAutomationStateChange:]
+ -[SUUIMobileAutomationManager observeValueForKeyPath:ofObject:change:context:]
+ -[SUUIMobileAutomationManager registerAutomationObserver:]
+ -[SUUIMobileAutomationManager removeAutomationObserver:]
+ -[SUUIMobileAutomationManager resolveStoredXCUISession:]
+ -[SUUIMobileAutomationManager setupAutomationForStoredSession:]
+ -[SUUIMobileAutomationManager startObserving]
+ -[SUUIMobileAutomationManager stopObserving]
+ -[SUUIMobileAutomationManager(SoftwareUpdateServices) createSUManagerClientForAutomationSession]
+ -[SUUIMobileScanOperation dealloc]
+ -[SUUIMobileScanOperation handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:]
+ -[SUUIMobileScanOperation handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:beforePostEvent:]
+ -[SUUIMobileUpdateOperation shouldConsiderErrorAsSuccessfulCase:]
+ -[SUUIMobileUserDefaultsBasedTestSession .cxx_destruct]
+ -[SUUIMobileUserDefaultsBasedTestSession beginTestAndReturnError:]
+ -[SUUIMobileUserDefaultsBasedTestSession correlationId]
+ -[SUUIMobileUserDefaultsBasedTestSession currentExecutionResult]
+ -[SUUIMobileUserDefaultsBasedTestSession currentPhase]
+ -[SUUIMobileUserDefaultsBasedTestSession dealloc]
+ -[SUUIMobileUserDefaultsBasedTestSession endTestWithResult:error:]
+ -[SUUIMobileUserDefaultsBasedTestSession handleChangedPhase:]
+ -[SUUIMobileUserDefaultsBasedTestSession handlePhaseConfigurationSealed]
+ -[SUUIMobileUserDefaultsBasedTestSession handlePhaseFinished]
+ -[SUUIMobileUserDefaultsBasedTestSession handlePhaseRunning]
+ -[SUUIMobileUserDefaultsBasedTestSession initWithStoredSession:]
+ -[SUUIMobileUserDefaultsBasedTestSession init]
+ -[SUUIMobileUserDefaultsBasedTestSession observeValueForKeyPath:ofObject:change:context:]
+ -[SUUIMobileUserDefaultsBasedTestSession strategyClassForServiceType:]
+ -[SUUIMobileUserDefaultsBasedTestSession strategyForServiceType:]
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table37
+ GCC_except_table58
+ GCC_except_table65
+ _NSClassFromString
+ _NSKeyValueChangeNewKey
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_SUUIMobileAutomationManager
+ _OBJC_CLASS_$_SUUIMobileUserDefaultsBasedTestSession
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_SUUIMobileAutomationManager._currentSession
+ _OBJC_IVAR_$_SUUIMobileAutomationManager._lock
+ _OBJC_IVAR_$_SUUIMobileAutomationManager._observers
+ _OBJC_IVAR_$_SUUIMobileAutomationManager._observing
+ _OBJC_IVAR_$_SUUIMobileScanOperation._activity
+ _OBJC_IVAR_$_SUUIMobileUserDefaultsBasedTestSession._services
+ _OBJC_IVAR_$_SUUIMobileUserDefaultsBasedTestSession._servicesClasses
+ _OBJC_IVAR_$_SUUIMobileUserDefaultsBasedTestSession._session
+ _OBJC_METACLASS_$_SUUIMobileAutomationManager
+ _OBJC_METACLASS_$_SUUIMobileUserDefaultsBasedTestSession
+ _SoftwareUpdateSettingsMockingKitLibrary
+ _SoftwareUpdateSettingsMockingKitLibraryCore
+ _SoftwareUpdateSettingsMockingKitLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_SUUIMobileAutomationManager
+ __OBJC_$_CLASS_METHODS_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_$_CLASS_PROP_LIST_SUUIMobileAutomationManager
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileAutomationManager(SoftwareUpdateServices)
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_$_INSTANCE_METHODS__TtC22SoftwareUpdateUIMobile29SUUIMobilePlatformEnvironment(SoftwareUpdateUIMobile)
+ __OBJC_$_INSTANCE_VARIABLES_SUUIMobileAutomationManager
+ __OBJC_$_INSTANCE_VARIABLES_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_$_PROP_LIST_SUSMKTestCaseSession
+ __OBJC_$_PROP_LIST_SUUIMobileAutomationManager
+ __OBJC_$_PROP_LIST_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_$_PROTOCOL_CLASS_METHODS_SUSMKTestCaseSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUSMKTestCaseSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUSUITestAutomationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUUICustomDescribleObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUSMKTestCaseSession
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUSUITestAutomationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUUICustomDescribleObject
+ __OBJC_$_PROTOCOL_REFS_SUSMKTestCaseSession
+ __OBJC_$_PROTOCOL_REFS_SUUICustomDescribleObject
+ __OBJC_CLASS_PROTOCOLS_$_SUUIMobileAutomationManager
+ __OBJC_CLASS_PROTOCOLS_$_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_CLASS_PROTOCOLS_$__TtC22SoftwareUpdateUIMobile29SUUIMobilePlatformEnvironment(SoftwareUpdateUIMobile)
+ __OBJC_CLASS_RO_$_SUUIMobileAutomationManager
+ __OBJC_CLASS_RO_$_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_LABEL_PROTOCOL_$_SUSMKTestCaseSession
+ __OBJC_LABEL_PROTOCOL_$_SUSUITestAutomationObserver
+ __OBJC_LABEL_PROTOCOL_$_SUUICustomDescribleObject
+ __OBJC_METACLASS_RO_$_SUUIMobileAutomationManager
+ __OBJC_METACLASS_RO_$_SUUIMobileUserDefaultsBasedTestSession
+ __OBJC_PROTOCOL_$_SUSMKTestCaseSession
+ __OBJC_PROTOCOL_$_SUSUITestAutomationObserver
+ __OBJC_PROTOCOL_$_SUUICustomDescribleObject
+ __SUUIActivityCleanup
+ __SUUISignpostCreate
+ __SUUISignpostGetNanoseconds
+ ___44+[SUUIMobileAutomationManager sharedManager]_block_invoke
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.303
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.304
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.305
+ ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.334
+ ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.343
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.309
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.310
+ ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.331
+ ___60-[SUUIMobileUserDefaultsBasedTestSession handlePhaseRunning]_block_invoke
+ ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.329
+ ___61-[SUUIMobileUserDefaultsBasedTestSession handlePhaseFinished]_block_invoke
+ ___64-[SUUIMobileScanOperation action_CheckForAvailableUpdate:error:]_block_invoke.322
+ ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.415
+ ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.467
+ ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.409
+ ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.406
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.469
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.470
+ ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.399
+ ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.327
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.315
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.316
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.317
+ ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.419
+ ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.417
+ ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.468
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.324
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.325
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.395
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.397
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.398
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.333
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.335
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.337
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.339
+ ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.412
+ ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.409
+ ___SoftwareUpdateSettingsMockingKitLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_64_e8_32s40r48w_e20_v20?0B8"NSError"12lw48l8r40l8s32l8
+ ___block_descriptor_64_e8_32s40r48w_e20_v20?0B8"NSError"12lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40r48w_e32_v24?0"SUDownload"8"NSError"16lw48l8r40l8s32l8
+ ___block_descriptor_64_e8_32s40r48w_e35_v32?0B8B12"NSError"16"NSError"24lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40r48w_e5_v8?0lw48l8s32l8r40l8
+ ___block_descriptor_72_e8_32s40s48r_e35_v24?0"SUScanResults"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56w_e32_v24?0"SUDownload"8"NSError"16lw56l8s32l8s40l8s48l8
+ ___getSUSMKMockedServiceTypeUtilityClass_block_invoke
+ ___getSUSMKSUManagerClientClass_block_invoke
+ ___getSUSMKTestCaseSessionPhaseUtilityClass_block_invoke
+ ___getSUSMKUserDefaultsCodedMockedStrategyClass_block_invoke
+ ___getSUSMKUserDefaultsCodedTestCaseSessionClass_block_invoke
+ ___getSUSUIUserDefaultsKeysClass_block_invoke
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_0_2_8_0_8_0
+ ___os_log_helper_16_2_2_8_0_8_66
+ ___os_log_helper_16_2_2_8_32_8_64
+ ___os_log_helper_16_2_2_8_34_4_0
+ ___os_log_helper_16_2_2_8_66_4_2
+ ___os_log_helper_16_2_3_8_32_8_64_8_64
+ ___os_log_helper_16_2_3_8_32_8_64_8_66
+ ___os_log_helper_16_2_4_8_0_8_0_8_66_4_2
+ ___os_log_helper_16_2_4_8_32_8_64_8_64_8_64
+ ___os_log_helper_16_2_4_8_34_8_0_8_0_8_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ __dispatch_main_q
+ __os_activity_create
+ __os_activity_current
+ __os_log_debug_impl
+ __os_signpost_emit_with_name_impl
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringSoftwareUpdateSettingsMockingKit
+ _dispatch_after
+ _dispatch_once
+ _free
+ _getSUSMKMockedServiceTypeUtilityClass
+ _getSUSMKMockedServiceTypeUtilityClass.softClass
+ _getSUSMKSUManagerClientClass
+ _getSUSMKSUManagerClientClass.softClass
+ _getSUSMKTestCaseSessionPhaseUtilityClass
+ _getSUSMKTestCaseSessionPhaseUtilityClass.softClass
+ _getSUSMKUserDefaultsCodedMockedStrategyClass
+ _getSUSMKUserDefaultsCodedMockedStrategyClass.softClass
+ _getSUSMKUserDefaultsCodedTestCaseSessionClass
+ _getSUSMKUserDefaultsCodedTestCaseSessionClass.softClass
+ _getSUSUIUserDefaultsKeysClass
+ _getSUSUIUserDefaultsKeysClass.softClass
+ _get_type_metadata 26SoftwareUpdateUIFoundation20SynchronizedPropertyVySbG.23
+ _malloc_type_calloc
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_getClass
+ _objc_msgSend$SoftwareUpdateSettingsSuiteName
+ _objc_msgSend$UIUnitTestingCurrentPhase
+ _objc_msgSend$UIUnitTestingCurrentSession
+ _objc_msgSend$UIUnitTestingKeys
+ _objc_msgSend$acceptibleStrategyClassName:forType:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$allCases
+ _objc_msgSend$allOptionClasses
+ _objc_msgSend$correlationId
+ _objc_msgSend$currentExecutionResult
+ _objc_msgSend$currentPhase
+ _objc_msgSend$defaultStrategyClassHandlerForType:
+ _objc_msgSend$descriptionForObject:
+ _objc_msgSend$descriptionForPhase:
+ _objc_msgSend$descriptionForType:
+ _objc_msgSend$didEndWithResult:
+ _objc_msgSend$enabled
+ _objc_msgSend$getReturnValue:
+ _objc_msgSend$handleChangedPhase:
+ _objc_msgSend$handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:
+ _objc_msgSend$handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:beforePostEvent:
+ _objc_msgSend$handlePhaseConfigurationSealed
+ _objc_msgSend$handlePhaseFinished
+ _objc_msgSend$handlePhaseRunning
+ _objc_msgSend$initForSession:usingOptions:
+ _objc_msgSend$initWithSet:
+ _objc_msgSend$initWithStoredSession:
+ _objc_msgSend$instantiateDefaultStrategyHandlerForType:withSession:
+ _objc_msgSend$isRunning:
+ _objc_msgSend$mockedService
+ _objc_msgSend$mockedStrategyClassName
+ _objc_msgSend$mockedStrategyOptions
+ _objc_msgSend$notifyObserversOfAutomationStateChange:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$onAutomationEnabledStateChanged:
+ _objc_msgSend$postEvent:withInfo:endingActivity:
+ _objc_msgSend$processId
+ _objc_msgSend$processStartTime
+ _objc_msgSend$processStartTime:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$resolveStoredXCUISession:
+ _objc_msgSend$setUnitTestingCurrentPhase:
+ _objc_msgSend$setupAutomationForStoredSession:
+ _objc_msgSend$shouldKeepPreviousMockingKitSession
+ _objc_msgSend$shouldSkipMockingKitPIDValidation
+ _objc_msgSend$shouldSkipMockingKitPIDValidation:
+ _objc_msgSend$softwareUpdateShared
+ _objc_msgSend$startObserving
+ _objc_msgSend$stopObserving
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$unitTestingCurrentPhase
+ _objc_msgSend$unitTestingCurrentTestResult
+ _objc_msgSend$unitTestingRegisteredServicesDictionary
+ _objc_msgSend$weakObjectsHashTable
+ _objc_msgSend$willBegin
+ _objc_opt_respondsToSelector
+ _objc_release_x8
+ _objc_retain_x8
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_activity_scope_enter
+ _os_activity_scope_leave
+ _os_signpost_enabled
+ _sharedManager.onceToken
+ _sharedManager.sharedManager
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_deallocObject
+ _swift_endAccess
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_release
+ _swift_retain
+ _swift_runtimeSupportsNoncopyableTypes
+ _symbolic SayySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s5UInt8V
+ _symbolic Sb
+ _symbolic SbIegd_
+ _symbolic So8NSObjectCSg
+ _symbolic _____ s5UInt8V
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic _____ySbG 26SoftwareUpdateUIFoundation20SynchronizedPropertyV
+ _symbolic ySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztc s5UInt8V
- -[SUUIMobilePreferencesManager shouldDisableAutoInstallIOSUpdatesToggle]
- -[SUUIMobilePreferencesManager shouldDisableAutoInstallRSRToggle]
- -[SUUIMobileScanOperation handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:]
- GCC_except_table36
- GCC_except_table46
- GCC_except_table53
- GCC_except_table56
- _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_SPECIFIC
- _OBJC_IVAR_$_SUUIMobilePreferencesManager._shouldDisableAutoInstallUpdates
- _OBJC_IVAR_$_SUUIMobilePreferencesManager._shouldDisableRSR
- __INSTANCE_METHODS__TtC22SoftwareUpdateUIMobile29SUUIMobilePlatformEnvironment
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.307
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.308
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.309
- ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.326
- ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.336
- ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.312
- ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.313
- ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.334
- ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.321
- ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.409
- ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.470
- ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.412
- ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.409
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.472
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.473
- ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.393
- ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.330
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.318
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.319
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.320
- ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.413
- ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.411
- ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.471
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.327
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.328
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.389
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.391
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.392
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.336
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.338
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.340
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.342
- ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.415
- ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.403
- ___block_descriptor_48_e8_32s40s_e35_v24?0"SUScanResults"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40w_e35_v32?0B8B12"NSError"16"NSError"24lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48w_e32_v24?0"SUDownload"8"NSError"16lw48l8s32l8s40l8
- _objc_msgSend$handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:
CStrings:
+ "#24@0:8q16"
+ "%s"
+ "%s [->%{public}@]: Finished to request installation from SUS: %{public}@; error: %{public}@"
+ "%s [XCUI correlationId: %@]: Changed XCUI testing session phase into: %{public}@"
+ "%s [XCUI correlationId: %@]: Could not fetch an NSClass instance from the class name string: '%@' for type: '%@'"
+ "%s [XCUI correlationId: %@]: Could not instantiate SUSMKUserDefaultsCodedMockedStrategy for type: '%@'.\nError: %@"
+ "%s [XCUI correlationId: %@]: Creating mocked service class: %@ for service '%@'"
+ "%s [XCUI correlationId: %@]: Failed to decode the changed phase into an NSNumber. Got: %@"
+ "%s [XCUI correlationId: %@]: Registering the default implementation for service type: %@"
+ "%s [XCUI correlationId: %@]: Sending the didEnd event to service type: %@"
+ "%s [XCUI correlationId: %@]: Sending the willBegin event to service type: %@"
+ "%s [XCUI correlationId: %@]: The supplied strategy class name '%@' for type '%@' is not acceptible. Each strategy must be manually registered in the Service Type class."
+ "%s: %{public}@ exists in Production. Auto-disables."
+ "%s: Automation is enabled. Initializing session: %{public}@"
+ "%s: Could not load SUSMKManagerClient."
+ "%s: Initializing %@"
+ "%s: Manager doesn't respond to initWithSession:"
+ "%s: Property \"%{public}@\" changed to: %{public}@"
+ "%s: Start to observe for Unit Testing requests.\nNSUserDefaults Automation enabled? %{public}@"
+ "%s: Stops observing for Unit Testing requests."
+ "%{public}s: Found a UTs session stored in NSUserDefaults. However, the process '%d' isn't running anymore. As SUSkipMockingKitPIDValidation is on - we will continue to use the test plan with this, incorrect, PID."
+ "%{public}s: Found a UTs session stored in NSUserDefaults. However, the process '%d' isn't running anymore. Killing the session."
+ "%{public}s: Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %ld, %ld, different than the start time of the current process with this pid, %ld. As SUSkipMockingKitPIDValidation is on - we will continue to use the test plan with this, corrupted, PID."
+ "%{public}s: Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %ld, %ld, different than the start time of the current process with this pid, %ld. Killing the session."
+ "-[SUUIMobileAutomationManager initialize]"
+ "-[SUUIMobileAutomationManager observeValueForKeyPath:ofObject:change:context:]"
+ "-[SUUIMobileAutomationManager resolveStoredXCUISession:]"
+ "-[SUUIMobileAutomationManager setupAutomationForStoredSession:]"
+ "-[SUUIMobileAutomationManager startObserving]"
+ "-[SUUIMobileAutomationManager stopObserving]"
+ "-[SUUIMobileAutomationManager(SoftwareUpdateServices) createSUManagerClientForAutomationSession]"
+ "-[SUUIMobileScanOperation handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:beforePostEvent:]"
+ "-[SUUIMobileUserDefaultsBasedTestSession handleChangedPhase:]"
+ "-[SUUIMobileUserDefaultsBasedTestSession handlePhaseConfigurationSealed]"
+ "-[SUUIMobileUserDefaultsBasedTestSession handlePhaseFinished]_block_invoke"
+ "-[SUUIMobileUserDefaultsBasedTestSession handlePhaseRunning]_block_invoke"
+ "-[SUUIMobileUserDefaultsBasedTestSession observeValueForKeyPath:ofObject:change:context:]"
+ ">> HERE: Mobile automation state changed to %{bool}d"
+ "@\"<SUSMKMockingStrategy>\"24@0:8q16"
+ "@\"<SUSMKTestCaseSession>\"16@0:8"
+ "@\"NSHashTable\""
+ "@\"SUSMKUserDefaultsCodedTestCaseSession\""
+ "@\"SUUIMobileUserDefaultsBasedTestSession\""
+ "B24@0:8^@16"
+ "B32@0:8q16^@24"
+ "BEGIN [%lld]: CheckForAvailableUpdates Begins scanForUpdates  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "Begins scanForUpdates  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "CheckForAvailableUpdates"
+ "Could not create a SUManagerClient for Automation Session"
+ "END [%lld] %fs: CheckForAvailableUpdates "
+ "EVENT [%lld] %fs: CheckForAvailableUpdates Scan Finished ScanResults=%{public,signpost.telemetry:string1,name=ScanResults}@  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.FullScan"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.RefreshScan"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.CheckForUpdates"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ObserveConcurrentQueries"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload: checkIfAutoUpdateScheduled:withReplyHandler:"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryUpdateInfo"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForBetaPrograms:withReplyHandler:"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForMDMRestrictions:withReplyHandler:"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkIsEligibleForRollback:withReplyHandler:"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryDDMDeclaration:withReplyHandler:"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryRollbackStatus:withReplyHandler:"
+ "Failed to decode the saved automation session into an SUSMKUserDefaultsCodedTestCaseSession object. Error: %{public}@"
+ "Initialing the Mobile environment in Automation Mode"
+ "Preferred: %@; Alternate: %@"
+ "SUSMKMockedServiceTypeUtility"
+ "SUSMKSUManagerClient"
+ "SUSMKTestCaseSession"
+ "SUSMKTestCaseSessionPhaseUtility"
+ "SUSMKUserDefaultsCodedMockedStrategy"
+ "SUSMKUserDefaultsCodedTestCaseSession"
+ "SUSUITestAutomationObserver"
+ "SUSUIUserDefaultsKeys"
+ "SUUICustomDescribleObject"
+ "SUUIMobileAutomationManager"
+ "SUUIMobileUserDefaultsBasedTestSession"
+ "Scan Finished ScanResults=%{public,signpost.telemetry:string1,name=ScanResults}@  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "SoftwareUpdateServices"
+ "SoftwareUpdateSettingsSuiteName"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "T@\"NSString\",R,C,N"
+ "T@\"SUUIMobileAutomationManager\",R"
+ "T@,R,N,V_currentSession"
+ "Tq,R,N"
+ "UIUnitTestingCurrentPhase"
+ "UIUnitTestingCurrentSession"
+ "UIUnitTestingKeys"
+ "Unable to find class %s"
+ "UnsafeMutableRawBufferPointer with negative count"
+ "UnsafeRawBufferPointer with negative count"
+ "^{suui_activity_s={os_activity_scope_state_s=[2Q]}@c}"
+ "_activity"
+ "_currentSession"
+ "_isUsingAutomationServices"
+ "_observers"
+ "_observing"
+ "_services"
+ "_servicesClasses"
+ "_session"
+ "acceptibleStrategyClassName:forType:"
+ "addObserver:forKeyPath:options:context:"
+ "allCases"
+ "allOptionClasses"
+ "beginTestAndReturnError:"
+ "com.apple.SoftwareUpdateUI"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.FullScan"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.RefreshScan"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.CheckForUpdates"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ObserveConcurrentQueries"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload: checkIfAutoUpdateScheduled:withReplyHandler:"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryUpdateInfo"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForBetaPrograms:withReplyHandler:"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForMDMRestrictions:withReplyHandler:"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkIsEligibleForRollback:withReplyHandler:"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryDDMDeclaration:withReplyHandler:"
+ "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryRollbackStatus:withReplyHandler:"
+ "correlationId"
+ "createSUManagerClientForAutomationSession"
+ "current"
+ "currentExecutionResult"
+ "currentPhase"
+ "currentSession"
+ "defaultStrategyClassHandlerForType:"
+ "descriptionForObject:"
+ "descriptionForPhase:"
+ "descriptionForType:"
+ "didEndWithResult:"
+ "enabled"
+ "endTestWithResult:error:"
+ "getReturnValue:"
+ "handleChangedPhase:"
+ "handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:"
+ "handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:activity:beforePostEvent:"
+ "handlePhaseConfigurationSealed"
+ "handlePhaseFinished"
+ "handlePhaseRunning"
+ "initForSession:usingOptions:"
+ "initWithSession:"
+ "initWithSet:"
+ "initWithStoredSession:"
+ "initialize"
+ "instantiateDefaultStrategyHandlerForType:withSession:"
+ "isRunning:"
+ "mockedService"
+ "mockedStrategyClassName"
+ "mockedStrategyOptions"
+ "notifyObserversOfAutomationStateChange:"
+ "numberWithInt:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "onAutomationEnabledStateChanged:"
+ "postEvent:withInfo:endingActivity:"
+ "processId"
+ "processStartTime"
+ "processStartTime:"
+ "registerAutomationObserver:"
+ "removeAutomationObserver:"
+ "removeObserver:forKeyPath:"
+ "resolveStoredXCUISession:"
+ "setUnitTestingCurrentPhase:"
+ "setupAutomationForStoredSession:"
+ "shouldKeepPreviousMockingKitSession"
+ "shouldSkipMockingKitPIDValidation"
+ "shouldSkipMockingKitPIDValidation:"
+ "softlink:o:path:/System/Library/../../AppleInternal/Library/Frameworks/SoftwareUpdateSettingsMockingKit.framework/SoftwareUpdateSettingsMockingKit"
+ "softwareUpdateShared"
+ "startObserving"
+ "stopObserving"
+ "strategyClassForServiceType:"
+ "strategyForServiceType:"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "unitTestingCurrentPhase"
+ "unitTestingCurrentTestResult"
+ "unitTestingRegisteredServicesDictionary"
+ "v48@0:8@16@24@32^v40"
+ "v52@0:8@16@24@32B40^{suui_activity_s={os_activity_scope_state_s=[2Q]}@c}44"
+ "v60@0:8@16@24@32B40^{suui_activity_s={os_activity_scope_state_s=[2Q]}@c}44@?52"
+ "weakObjectsHashTable"
+ "willBegin"
- "-[SUUIMobileScanOperation handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:]"
- "TB,R,N,V_shouldDisableAutoInstallUpdates"
- "TB,R,N,V_shouldDisableRSR"
- "_shouldDisableAutoInstallUpdates"
- "_shouldDisableRSR"
- "handleDiscoveredScanResults:withError:usingEventInfo:isCachedResults:"
- "specific"
- "v44@0:8@16@24@32B40"

```

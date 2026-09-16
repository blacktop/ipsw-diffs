## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-511.0.0.0.0
-  __TEXT.__text: 0xbf468
-  __TEXT.__objc_methlist: 0xab1c
-  __TEXT.__const: 0x718
-  __TEXT.__cstring: 0x8da4
-  __TEXT.__oslogstring: 0x119a0
-  __TEXT.__gcc_except_tab: 0x10c4
+511.2.3.0.0
+  __TEXT.__text: 0xc119c
+  __TEXT.__objc_methlist: 0xac74
+  __TEXT.__const: 0x748
+  __TEXT.__cstring: 0x8f25
+  __TEXT.__oslogstring: 0x11d6f
+  __TEXT.__gcc_except_tab: 0x10d8
   __TEXT.__dlopen_cstrs: 0x59
-  __TEXT.__swift5_typeref: 0x294
+  __TEXT.__swift5_typeref: 0x29c
+  __TEXT.__swift5_capture: 0x160
   __TEXT.__swift5_fieldmd: 0x144
   __TEXT.__constg_swiftt: 0x264
-  __TEXT.__swift5_reflstr: 0xe6
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_capture: 0x160
+  __TEXT.__swift5_reflstr: 0xe4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_types: 0x1c
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x38e0
+  __TEXT.__unwind_info: 0x3940
   __TEXT.__eh_frame: 0x578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2728
-  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__const: 0x27f8
+  __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x150
-  __DATA_CONST.__objc_protolist: 0x3e8
+  __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e18
+  __DATA_CONST.__objc_selrefs: 0x4ec8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xf08
+  __DATA_CONST.__got: 0xf28
   __AUTH_CONST.__const: 0x1198
-  __AUTH_CONST.__cfstring: 0x7b20
-  __AUTH_CONST.__objc_const: 0x268f0
+  __AUTH_CONST.__cfstring: 0x7b60
+  __AUTH_CONST.__objc_const: 0x26b68
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x4b0
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__auth_got: 0xaf0
-  __AUTH.__objc_data: 0x8d8
+  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH.__objc_data: 0x978
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xa68
-  __DATA.__data: 0x3360
+  __DATA.__objc_ivar: 0xa80
+  __DATA.__data: 0x33c8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x36f8
   __DATA_DIRTY.__data: 0x190

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore
+  - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3951
-  Symbols:   9437
-  CStrings:  2294
+  Functions: 3984
+  Symbols:   9528
+  CStrings:  2308
 
Symbols:
+ -[DNDSAppFocusConfigurationCoordinator _acquireAuthAssertionForBundleIdentifier:completion:]
+ -[DNDSAppFocusConfigurationCoordinator _armAuthAssertionWatchdogForBundleIdentifier:]
+ -[DNDSAppFocusConfigurationCoordinator _discardAuthAssertionStateForBundleIdentifier:]
+ -[DNDSAppFocusConfigurationCoordinator _drainAuthAssertionWaitersForState:]
+ -[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]
+ -[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:]
+ -[DNDSAppFocusConfigurationCoordinator _releaseAuthAssertionToken:]
+ -[DNDSAppFocusConfigurationCoordinator assertion:didInvalidateWithError:]
+ -[DNDSAuthAssertionState .cxx_destruct]
+ -[DNDSAuthAssertionState assertion]
+ -[DNDSAuthAssertionState init]
+ -[DNDSAuthAssertionState setAssertion:]
+ -[DNDSAuthAssertionState setWatchdog:]
+ -[DNDSAuthAssertionState tokens]
+ -[DNDSAuthAssertionState waiters]
+ -[DNDSAuthAssertionState watchdog]
+ -[DNDSAuthAssertionToken .cxx_destruct]
+ -[DNDSAuthAssertionToken bundleIdentifier]
+ -[DNDSAuthAssertionToken initWithBundleIdentifier:]
+ -[DNDSModeConfigurationManager _appForegroundTriggerInTriggers:forApplicationIdentifier:]
+ -[DNDSModeConfigurationManager _modeConfigurationRecordByMigratingAppSettingsInRecord:fromApplicationIdentifier:toApplicationIdentifier:]
+ -[DNDSModeConfigurationManager migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withError:]
+ -[DNDSRemoteServiceProvider migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withRequestDetails:completionHandler:]
+ -[DNDSServer remoteServiceProvider:migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withError:]
+ GCC_except_table111
+ GCC_except_table171
+ GCC_except_table46
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_APAuthAssertion
+ _OBJC_CLASS_$_DNDSAuthAssertionState
+ _OBJC_CLASS_$_DNDSAuthAssertionToken
+ _OBJC_IVAR_$_DNDSAppFocusConfigurationCoordinator._authAssertionStatesByBundleIdentifier
+ _OBJC_IVAR_$_DNDSAuthAssertionState._assertion
+ _OBJC_IVAR_$_DNDSAuthAssertionState._tokens
+ _OBJC_IVAR_$_DNDSAuthAssertionState._waiters
+ _OBJC_IVAR_$_DNDSAuthAssertionState._watchdog
+ _OBJC_IVAR_$_DNDSAuthAssertionToken._bundleIdentifier
+ _OBJC_METACLASS_$_DNDSAuthAssertionState
+ _OBJC_METACLASS_$_DNDSAuthAssertionToken
+ __OBJC_$_CATEGORY_CLASS_METHODS_DNDModeAssertionInvalidation_$_Predicates
+ __OBJC_$_CATEGORY_CLASS_METHODS_DNDModeAssertion_$_Predicates
+ __OBJC_$_CATEGORY_DNDContact_$_Contacts
+ __OBJC_$_CATEGORY_DNDModeAssertionInvalidation_$_Predicates
+ __OBJC_$_CATEGORY_DNDModeAssertion_$_Predicates
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDateInterval_$_LifetimePhase
+ __OBJC_$_CATEGORY_NSDateInterval_$_LifetimePhase
+ __OBJC_$_CATEGORY_NSMutableDictionary_$_DNDSModeAssertionStoreRecord
+ __OBJC_$_CATEGORY_NSString_$_DNDModeAssertionReasonHelper
+ __OBJC_$_CLASS_METHODS_DNDContact(Contacts|Record|Sanitization)
+ __OBJC_$_CLASS_METHODS_DNDSModeAssertionStore(BackingRecord|BackingRecordUpgrade|DateOperations|SysdiagnoseRecord|PeaceSyncMessage|SyncMessage)
+ __OBJC_$_CLASS_METHODS_DNDSSettingsRecord(LegacySupport|BackingStore)
+ __OBJC_$_CLASS_METHODS_NSDateInterval(LifetimePhase|Schedule)
+ __OBJC_$_CLASS_METHODS_NSString(DNDModeAssertionReasonHelper|DNDModeAssertionInvalidationReasonHelper|DNDModeAssertionInvalidationReasonOverrideHelper|DNDSModeAssertionInvalidationPredicateTypeHelper|DNDModeAssertionLifetimeTypeHelper|DNDModeAssertionScheduleLifetimeBehaviorHelper)
+ __OBJC_$_INSTANCE_METHODS_DNDContact(Contacts|Record|Sanitization)
+ __OBJC_$_INSTANCE_METHODS_DNDModeAssertion(Predicates|Resolution|AssertionSyncManager)
+ __OBJC_$_INSTANCE_METHODS_DNDModeAssertionInvalidation(Predicates|Resolution|AssertionSyncManager)
+ __OBJC_$_INSTANCE_METHODS_DNDSAppSpecificSettingsManager(DNDSAppSpecificSettingsTypeAppConfigurationAction|DNDSAppSpecificSettingsTypeAppConfigurationPredicate|DNDSAppSpecificSettingsTypeAppConfigurationTargetContentIdentifierPrefix|DNDSAppSpecificSettingsTypeSystemAction)
+ __OBJC_$_INSTANCE_METHODS_DNDSAuthAssertionState
+ __OBJC_$_INSTANCE_METHODS_DNDSAuthAssertionToken
+ __OBJC_$_INSTANCE_METHODS_DNDSModeAssertionStore(BackingRecord|BackingRecordUpgrade|DateOperations|SysdiagnoseRecord|PeaceSyncMessage|SyncMessage)
+ __OBJC_$_INSTANCE_METHODS_DNDSMutableModeAssertionStore(DateOperations|DNDSModernAssertionSync)
+ __OBJC_$_INSTANCE_METHODS_DNDSServer(DNDSGlobalConfigurationManagerDelegate|DNDSAutomationManagerDataSource|DNDSAppForegroundTriggerManagerDataSource|DNDSDrivingTriggerManagerDataSource|DNDSGamingTriggerManagerDataSource|DNDSHearingTestTriggerManagerDataSource|DNDSMindfulnessTriggerManagerDataSource|DNDSSleepingTriggerManagerDataSource|DNDSSmartTriggerManagerDataSource|DNDSWorkoutTriggerManagerDataSource|DNDSImmersiveSpaceTriggerManagerDataSource)
+ __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(DNDSModeAssertionStoreRecord|DNDSBackingStoreDictionaryContext)
+ __OBJC_$_INSTANCE_METHODS_NSString(DNDModeAssertionReasonHelper|DNDModeAssertionInvalidationReasonHelper|DNDModeAssertionInvalidationReasonOverrideHelper|DNDSModeAssertionInvalidationPredicateTypeHelper|DNDModeAssertionLifetimeTypeHelper|DNDModeAssertionScheduleLifetimeBehaviorHelper)
+ __OBJC_$_INSTANCE_VARIABLES_DNDSAuthAssertionState
+ __OBJC_$_INSTANCE_VARIABLES_DNDSAuthAssertionToken
+ __OBJC_$_PROP_LIST_DNDSAuthAssertionState
+ __OBJC_$_PROP_LIST_DNDSAuthAssertionToken
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_APAuthAssertionObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_APAuthAssertionObserving
+ __OBJC_$_PROTOCOL_REFS_APAuthAssertionObserving
+ __OBJC_CLASS_PROTOCOLS_$_DNDModeAssertion(Predicates|Resolution|AssertionSyncManager)
+ __OBJC_CLASS_PROTOCOLS_$_DNDModeAssertionInvalidation(Predicates|Resolution|AssertionSyncManager)
+ __OBJC_CLASS_PROTOCOLS_$_DNDSModeAssertionStore(BackingRecord|BackingRecordUpgrade|DateOperations|SysdiagnoseRecord|PeaceSyncMessage|SyncMessage)
+ __OBJC_CLASS_PROTOCOLS_$_DNDSServer(DNDSGlobalConfigurationManagerDelegate|DNDSAutomationManagerDataSource|DNDSAppForegroundTriggerManagerDataSource|DNDSDrivingTriggerManagerDataSource|DNDSGamingTriggerManagerDataSource|DNDSHearingTestTriggerManagerDataSource|DNDSMindfulnessTriggerManagerDataSource|DNDSSleepingTriggerManagerDataSource|DNDSSmartTriggerManagerDataSource|DNDSWorkoutTriggerManagerDataSource|DNDSImmersiveSpaceTriggerManagerDataSource)
+ __OBJC_CLASS_RO_$_DNDSAuthAssertionState
+ __OBJC_CLASS_RO_$_DNDSAuthAssertionToken
+ __OBJC_LABEL_PROTOCOL_$_APAuthAssertionObserving
+ __OBJC_METACLASS_RO_$_DNDSAuthAssertionState
+ __OBJC_METACLASS_RO_$_DNDSAuthAssertionToken
+ __OBJC_PROTOCOL_$_APAuthAssertionObserving
+ ___131-[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:]_block_invoke
+ ___131-[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:]_block_invoke_2
+ ___158-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]_block_invoke
+ ___158-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]_block_invoke_2
+ ___73-[DNDSAppFocusConfigurationCoordinator assertion:didInvalidateWithError:]_block_invoke
+ ___85-[DNDSAppFocusConfigurationCoordinator _armAuthAssertionWatchdogForBundleIdentifier:]_block_invoke
+ ___89-[DNDSModeConfigurationManager _appForegroundTriggerInTriggers:forApplicationIdentifier:]_block_invoke
+ ___92-[DNDSAppFocusConfigurationCoordinator _acquireAuthAssertionForBundleIdentifier:completion:]_block_invoke
+ ___92-[DNDSAppFocusConfigurationCoordinator _acquireAuthAssertionForBundleIdentifier:completion:]_block_invoke_2
+ ___92-[DNDSAppFocusConfigurationCoordinator _acquireAuthAssertionForBundleIdentifier:completion:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e37_B16?0"DNDModeConfigurationTrigger"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e37_v24?0"APAuthAssertion"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e71_v32?0"DNDSAppFocusConfigurationTask"8"LNSuccessResult"16"NSError"24lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e30_v24?0"LNAction"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80s_e32_v16?0"DNDSAuthAssertionToken"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_DoNotDisturbServer
+ _dispatch_after
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _objc_msgSend$_acquireAuthAssertionForBundleIdentifier:completion:
+ _objc_msgSend$_appForegroundTriggerInTriggers:forApplicationIdentifier:
+ _objc_msgSend$_armAuthAssertionWatchdogForBundleIdentifier:
+ _objc_msgSend$_discardAuthAssertionStateForBundleIdentifier:
+ _objc_msgSend$_drainAuthAssertionWaitersForState:
+ _objc_msgSend$_executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:
+ _objc_msgSend$_executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:
+ _objc_msgSend$_modeConfigurationRecordByMigratingAppSettingsInRecord:fromApplicationIdentifier:toApplicationIdentifier:
+ _objc_msgSend$_releaseAuthAssertionToken:
+ _objc_msgSend$acquireForSubject:completion:
+ _objc_msgSend$applicationWithBundleIdentifier:
+ _objc_msgSend$bs_objectsOfClass:
+ _objc_msgSend$isHidden
+ _objc_msgSend$isLocked
+ _objc_msgSend$migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withError:
+ _objc_msgSend$remoteServiceProvider:migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withError:
+ _objc_msgSend$setWatchdog:
+ _objc_msgSend$subject
+ _objc_msgSend$tokens
+ _objc_msgSend$waiters
+ _objc_msgSend$watchdog
+ _symbolic _____Sg 12FindMyLocate12ClientTargetV
- GCC_except_table108
- GCC_except_table170
- __OBJC_$_CATEGORY_CLASS_METHODS_NSDateInterval_$_Schedule
- __OBJC_$_CATEGORY_DNDContact_$_Record
- __OBJC_$_CATEGORY_DNDModeAssertionInvalidation_$_Resolution
- __OBJC_$_CATEGORY_DNDModeAssertion_$_Resolution
- __OBJC_$_CATEGORY_NSDateInterval_$_Schedule
- __OBJC_$_CATEGORY_NSMutableDictionary_$_DNDSBackingStoreDictionaryContext
- __OBJC_$_CATEGORY_NSString_$_DNDModeAssertionLifetimeTypeHelper
- __OBJC_$_CLASS_METHODS_DNDContact(Record|Contacts|Sanitization)
- __OBJC_$_CLASS_METHODS_DNDModeAssertion(Resolution|AssertionSyncManager|Predicates)
- __OBJC_$_CLASS_METHODS_DNDModeAssertionInvalidation(Resolution|AssertionSyncManager|Predicates)
- __OBJC_$_CLASS_METHODS_DNDSModeAssertionStore(SyncMessage|BackingRecord|BackingRecordUpgrade|SysdiagnoseRecord|PeaceSyncMessage|DateOperations)
- __OBJC_$_CLASS_METHODS_DNDSSettingsRecord(BackingStore|LegacySupport)
- __OBJC_$_CLASS_METHODS_NSString(DNDModeAssertionLifetimeTypeHelper|DNDModeAssertionScheduleLifetimeBehaviorHelper|DNDModeAssertionReasonHelper|DNDModeAssertionInvalidationReasonHelper|DNDModeAssertionInvalidationReasonOverrideHelper|DNDSModeAssertionInvalidationPredicateTypeHelper)
- __OBJC_$_INSTANCE_METHODS_DNDContact(Record|Contacts|Sanitization)
- __OBJC_$_INSTANCE_METHODS_DNDModeAssertion(Resolution|AssertionSyncManager|Predicates)
- __OBJC_$_INSTANCE_METHODS_DNDModeAssertionInvalidation(Resolution|AssertionSyncManager|Predicates)
- __OBJC_$_INSTANCE_METHODS_DNDSAppSpecificSettingsManager(DNDSAppSpecificSettingsTypeAppConfigurationAction|DNDSAppSpecificSettingsTypeAppConfigurationTargetContentIdentifierPrefix|DNDSAppSpecificSettingsTypeSystemAction|DNDSAppSpecificSettingsTypeAppConfigurationPredicate)
- __OBJC_$_INSTANCE_METHODS_DNDSModeAssertionStore(SyncMessage|BackingRecord|BackingRecordUpgrade|SysdiagnoseRecord|PeaceSyncMessage|DateOperations)
- __OBJC_$_INSTANCE_METHODS_DNDSMutableModeAssertionStore(DNDSModernAssertionSync|DateOperations)
- __OBJC_$_INSTANCE_METHODS_DNDSServer(DNDSAutomationManagerDataSource|DNDSAppForegroundTriggerManagerDataSource|DNDSDrivingTriggerManagerDataSource|DNDSGamingTriggerManagerDataSource|DNDSHearingTestTriggerManagerDataSource|DNDSMindfulnessTriggerManagerDataSource|DNDSSleepingTriggerManagerDataSource|DNDSSmartTriggerManagerDataSource|DNDSWorkoutTriggerManagerDataSource|DNDSImmersiveSpaceTriggerManagerDataSource|DNDSGlobalConfigurationManagerDelegate)
- __OBJC_$_INSTANCE_METHODS_NSDateInterval(Schedule|LifetimePhase)
- __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(DNDSBackingStoreDictionaryContext|DNDSModeAssertionStoreRecord)
- __OBJC_$_INSTANCE_METHODS_NSString(DNDModeAssertionLifetimeTypeHelper|DNDModeAssertionScheduleLifetimeBehaviorHelper|DNDModeAssertionReasonHelper|DNDModeAssertionInvalidationReasonHelper|DNDModeAssertionInvalidationReasonOverrideHelper|DNDSModeAssertionInvalidationPredicateTypeHelper)
- __OBJC_CATEGORY_PROTOCOLS_$_DNDModeAssertionInvalidation_$_Resolution
- __OBJC_CATEGORY_PROTOCOLS_$_DNDModeAssertion_$_Resolution
- __OBJC_CLASS_PROTOCOLS_$_DNDSModeAssertionStore(SyncMessage|BackingRecord|BackingRecordUpgrade|SysdiagnoseRecord|PeaceSyncMessage|DateOperations)
- __OBJC_CLASS_PROTOCOLS_$_DNDSServer(DNDSAutomationManagerDataSource|DNDSAppForegroundTriggerManagerDataSource|DNDSDrivingTriggerManagerDataSource|DNDSGamingTriggerManagerDataSource|DNDSHearingTestTriggerManagerDataSource|DNDSMindfulnessTriggerManagerDataSource|DNDSSleepingTriggerManagerDataSource|DNDSSmartTriggerManagerDataSource|DNDSWorkoutTriggerManagerDataSource|DNDSImmersiveSpaceTriggerManagerDataSource|DNDSGlobalConfigurationManagerDelegate)
- ___107-[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:]_block_invoke
- ___107-[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48s56w_e71_v32?0"DNDSAppFocusConfigurationTask"8"LNSuccessResult"16"NSError"24lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e30_v24?0"LNAction"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$_executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Configurations/Global/DNDSGlobalConfigurationManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Configurations/Mode/DNDSModeConfigurationManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/FindMy Me Device/DNDSMeDeviceService.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Lifetime Monitors/DNDSLocationLifetimeMonitor.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Mode Assertion Manager/DNDSModeAssertionManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Placeholder Mode/DNDSPlaceholderModeManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Settings/DNDSSettingsManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Settings/Legacy Settings/DNDSLegacySettingsMigration.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Sync/Modern/DNDSModernAssertionSyncManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Sync/Sync Engines/CloudKit Sync Engine/DNDSSyncEngine.m"
+ "Acquired App Protection auth assertion for Focus filter action. bundle=%{public}@"
+ "App Protection auth assertion held past its limit; forcing release. A Focus filter action never completed. bundle=%{public}@"
+ "App Protection auth assertion invalidated externally. bundle=%{public}@; %{public}@"
+ "Cannot migrate app settings as the store is not writeable"
+ "Cannot migrate app settings as the store is not writeable; source=%{public}@; destination=%{public}@"
+ "Cannot migrate app settings with invalid bundle identifiers"
+ "Cannot migrate app settings with invalid bundle identifiers; source=%{public}@; destination=%{public}@"
+ "Failed to acquire App Protection auth assertion; action may be refused. bundle=%{public}@; %{public}@"
+ "Migrated app settings for mode configuration; modeIdentifier=%{public}@"
+ "Migrating app settings in %{public}lu mode configuration(s); source=%{public}@; destination=%{public}@"
+ "No app settings to migrate; source=%{public}@; destination=%{public}@"
+ "[%{public}@] XPC connection without any valid entitlements tried to migrate app settings, will invalidate: connection=%{public}@"
+ "v16@?0@\"DNDSAuthAssertionToken\"8"
+ "v24@?0@\"APAuthAssertion\"8@\"NSError\"16"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSGlobalConfigurationManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLegacySettingsMigration.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLocationLifetimeMonitor.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSMeDeviceService.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeAssertionManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeConfigurationManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModernAssertionSyncManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSPlaceholderModeManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSettingsManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSyncEngine.m"
```

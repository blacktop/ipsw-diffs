## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Versions/A/DoNotDisturbServer`

```diff

-511.0.0.0.0
-  __TEXT.__text: 0xc33e0
-  __TEXT.__objc_methlist: 0xa774
-  __TEXT.__const: 0x688
-  __TEXT.__cstring: 0x8784
-  __TEXT.__oslogstring: 0x10320
+511.2.3.0.0
+  __TEXT.__text: 0xc47f0
+  __TEXT.__objc_methlist: 0xa884
+  __TEXT.__const: 0x6b8
+  __TEXT.__cstring: 0x88c5
+  __TEXT.__oslogstring: 0x1055f
   __TEXT.__gcc_except_tab: 0xf00
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
-  __TEXT.__unwind_info: 0x36e8
+  __TEXT.__unwind_info: 0x3728
   __TEXT.__eh_frame: 0x578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa38
-  __DATA_CONST.__objc_classlist: 0x610
+  __DATA_CONST.__const: 0xa40
+  __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x3e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b30
+  __DATA_CONST.__objc_selrefs: 0x4ba8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3e8
   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__got: 0xe30
-  __AUTH_CONST.__const: 0x2fc8
-  __AUTH_CONST.__cfstring: 0x71a0
-  __AUTH_CONST.__objc_const: 0x257a0
+  __AUTH_CONST.__const: 0x3028
+  __AUTH_CONST.__cfstring: 0x71e0
+  __AUTH_CONST.__objc_const: 0x259f0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x4b0
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__auth_got: 0x990
-  __AUTH.__objc_data: 0x8d8
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH.__objc_data: 0x978
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xa04
-  __DATA.__data: 0x3300
+  __DATA.__objc_ivar: 0xa1c
+  __DATA.__data: 0x3308
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3658
   __DATA_DIRTY.__data: 0x198

   - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/IntentsCore.framework/Versions/A/IntentsCore
+  - /System/Library/PrivateFrameworks/LinkMetadata.framework/Versions/A/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/Versions/A/PrototypeTools

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3874
-  Symbols:   9195
-  CStrings:  2127
+  Functions: 3898
+  Symbols:   9254
+  CStrings:  2135
 
Symbols:
+ -[DNDSAppFocusConfigurationCoordinator _acquireAuthAssertionForBundleIdentifier:completion:]
+ -[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]
+ -[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:]
+ -[DNDSAppFocusConfigurationCoordinator _releaseAuthAssertionToken:]
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
+ GCC_except_table121
+ GCC_except_table178
+ GCC_except_table50
+ OBJC_IVAR_$_DNDSAppFocusConfigurationCoordinator._authAssertionStatesByBundleIdentifier
+ OBJC_IVAR_$_DNDSAuthAssertionState._assertion
+ OBJC_IVAR_$_DNDSAuthAssertionState._tokens
+ OBJC_IVAR_$_DNDSAuthAssertionState._waiters
+ OBJC_IVAR_$_DNDSAuthAssertionState._watchdog
+ OBJC_IVAR_$_DNDSAuthAssertionToken._bundleIdentifier
+ _OBJC_CLASS_$_DNDSAuthAssertionState
+ _OBJC_CLASS_$_DNDSAuthAssertionToken
+ _OBJC_METACLASS_$_DNDSAuthAssertionState
+ _OBJC_METACLASS_$_DNDSAuthAssertionToken
+ __158-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]_block_invoke_2
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
+ __OBJC_CLASS_PROTOCOLS_$_DNDModeAssertion(Predicates|Resolution|AssertionSyncManager)
+ __OBJC_CLASS_PROTOCOLS_$_DNDModeAssertionInvalidation(Predicates|Resolution|AssertionSyncManager)
+ __OBJC_CLASS_PROTOCOLS_$_DNDSModeAssertionStore(BackingRecord|BackingRecordUpgrade|DateOperations|SysdiagnoseRecord|PeaceSyncMessage|SyncMessage)
+ __OBJC_CLASS_PROTOCOLS_$_DNDSServer(DNDSGlobalConfigurationManagerDelegate|DNDSAutomationManagerDataSource|DNDSAppForegroundTriggerManagerDataSource|DNDSDrivingTriggerManagerDataSource|DNDSGamingTriggerManagerDataSource|DNDSHearingTestTriggerManagerDataSource|DNDSMindfulnessTriggerManagerDataSource|DNDSSleepingTriggerManagerDataSource|DNDSSmartTriggerManagerDataSource|DNDSWorkoutTriggerManagerDataSource|DNDSImmersiveSpaceTriggerManagerDataSource)
+ __OBJC_CLASS_RO_$_DNDSAuthAssertionState
+ __OBJC_CLASS_RO_$_DNDSAuthAssertionToken
+ __OBJC_METACLASS_RO_$_DNDSAuthAssertionState
+ __OBJC_METACLASS_RO_$_DNDSAuthAssertionToken
+ ___131-[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:]_block_invoke
+ ___131-[DNDSAppFocusConfigurationCoordinator _executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:]_block_invoke_2
+ ___158-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]_block_invoke
+ ___158-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:]_block_invoke_2
+ ___89-[DNDSModeConfigurationManager _appForegroundTriggerInTriggers:forApplicationIdentifier:]_block_invoke
+ ___block_descriptor_40_e8_32s_e37_B16?0"DNDModeConfigurationTrigger"8l
+ ___block_descriptor_72_e8_32s40s48s56s64w_e71_v32?0"DNDSAppFocusConfigurationTask"8"LNSuccessResult"16"NSError"24l
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e30_v24?0"LNAction"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s
+ ___copy_helper_block_e8_32s40s48s56s64s72s80w
+ ___copy_helper_block_e8_32s40s48s56s64w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80w
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_DoNotDisturbServer
+ _objc_msgSend$_appForegroundTriggerInTriggers:forApplicationIdentifier:
+ _objc_msgSend$_executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:assertionToken:
+ _objc_msgSend$_executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:releasingAssertionToken:
+ _objc_msgSend$_modeConfigurationRecordByMigratingAppSettingsInRecord:fromApplicationIdentifier:toApplicationIdentifier:
+ _objc_msgSend$_releaseAuthAssertionToken:
+ _objc_msgSend$bs_objectsOfClass:
+ _objc_msgSend$migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withError:
+ _objc_msgSend$remoteServiceProvider:migrateAppSettingsFromBundleIdentifier:toBundleIdentifier:withError:
+ _symbolic _____Sg 12FindMyLocate12ClientTargetV
- GCC_except_table118
- GCC_except_table177
- GCC_except_table31
- __143-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:]_block_invoke
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
- ___143-[DNDSAppFocusConfigurationCoordinator _executeAction:orActionIdentifier:withBundleIdentifier:modeIdentifier:groupIdentifier:exiting:metadata:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56w_e71_v32?0"DNDSAppFocusConfigurationTask"8"LNSuccessResult"16"NSError"24l
- ___block_descriptor_72_e8_32s40s48s56s64s_e30_v24?0"LNAction"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72w
- ___destroy_helper_block_e8_32s40s48s56s64s72w
- _objc_msgSend$_executeAction:withBundleIdentifier:modeIdentifier:groupIdentifier:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Configurations/Global/DNDSGlobalConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Configurations/Mode/DNDSModeConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/FindMy Me Device/DNDSMeDeviceService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Lifetime Monitors/DNDSLocationLifetimeMonitor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Mode Assertion Manager/DNDSModeAssertionManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Placeholder Mode/DNDSPlaceholderModeManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Settings/DNDSSettingsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Settings/Legacy Settings/DNDSLegacySettingsMigration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Sync/Modern/DNDSModernAssertionSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/Sync/Sync Engines/CloudKit Sync Engine/DNDSSyncEngine.m"
+ "Cannot migrate app settings as the store is not writeable"
+ "Cannot migrate app settings as the store is not writeable; source=%{public}@; destination=%{public}@"
+ "Cannot migrate app settings with invalid bundle identifiers"
+ "Cannot migrate app settings with invalid bundle identifiers; source=%{public}@; destination=%{public}@"
+ "Migrated app settings for mode configuration; modeIdentifier=%{public}@"
+ "Migrating app settings in %{public}lu mode configuration(s); source=%{public}@; destination=%{public}@"
+ "No app settings to migrate; source=%{public}@; destination=%{public}@"
+ "[%{public}@] XPC connection without any valid entitlements tried to migrate app settings, will invalidate: connection=%{public}@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSGlobalConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLegacySettingsMigration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSLocationLifetimeMonitor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSMeDeviceService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeAssertionManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModeConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSModernAssertionSyncManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSPlaceholderModeManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSettingsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DoNotDisturbServer/DoNotDisturbServer/DNDSSyncEngine.m"
```
